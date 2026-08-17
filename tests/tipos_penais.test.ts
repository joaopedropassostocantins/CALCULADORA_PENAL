import { execFileSync } from "node:child_process";
import { createHash } from "node:crypto";
import fs from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";

const root = process.cwd();
const canonicalPath = path.join(root, "src/data/tiposPenais.json");
const publicPath = path.join(root, "sites/calculadora-penal/data/tiposPenais.public.json");
const csvPath = path.join(root, "src/data/tiposPenais.csv");

type RecordItem = {
  id: string;
  dispositivo: string;
  pena: { minimoMeses: number | null; maximoMeses: number | null };
  inventarioValidado: boolean;
  usavelNaCalculadora: boolean;
  tipoPaiId: string | null;
  validationState?: string;
  canCalculate?: boolean;
};

function loadCanonical() {
  return JSON.parse(fs.readFileSync(canonicalPath, "utf8")) as { registros: RecordItem[]; registrosPendentes: number; estadoGeral: string; quantidadeTotalAtiva: number };
}

function digest(filePath: string) {
  return createHash("sha256").update(fs.readFileSync(filePath)).digest("hex");
}

describe("catálogo canônico de tipos penais", () => {
  it("mantém IDs, dispositivos, pais e penas consistentes", () => {
    const catalog = loadCanonical();
    const ids = new Set(catalog.registros.map((record) => record.id));
    const devices = new Set(catalog.registros.map((record) => `${record.id}:${record.dispositivo}`));

    expect(ids.size).toBe(catalog.registros.length);
    expect(devices.size).toBe(catalog.registros.length);
    expect(catalog.quantidadeTotalAtiva).toBe(catalog.registros.length);
    for (const record of catalog.registros) {
      expect(record.pena.minimoMeses == null || record.pena.maximoMeses == null || record.pena.minimoMeses <= record.pena.maximoMeses).toBe(true);
      expect(record.tipoPaiId === null || ids.has(record.tipoPaiId)).toBe(true);
      expect(record.usavelNaCalculadora).toBe(record.inventarioValidado);
    }
  });

  it("preserva as regressões legislativas solicitadas", () => {
    const byId = new Map(loadCanonical().registros.map((record) => [record.id, record]));
    const expected: Record<string, [number, number]> = {
      "cp-133": [6, 36],
      "cp-121-2d": [240, 480],
      "cp-121a": [240, 480],
      "cp-121b": [240, 480],
      "cp-129-9": [24, 60],
      "cp-147c": [12, 36],
      "cp-217a": [120, 216],
      "cp-217a-3": [144, 288],
      "cp-217a-4": [240, 480],
      "cp-157": [72, 120],
      "cp-157-3-ii": [288, 360],
      "cp-359p": [36, 72],
    };
    for (const [id, [minimum, maximum]] of Object.entries(expected)) {
      const record = byId.get(id);
      expect(record, `registro ausente: ${id}`).toBeDefined();
      expect(record?.pena.minimoMeses).toBe(minimum);
      expect(record?.pena.maximoMeses).toBe(maximum);
    }
  });

  it("não expõe pendências para o cálculo nem marca o catálogo como completo", () => {
    const catalog = loadCanonical();
    const publicCatalog = JSON.parse(fs.readFileSync(publicPath, "utf8")) as { estadoGeral: string; registros: RecordItem[] };
    expect(catalog.estadoGeral).toBe("incompleto");
    expect(catalog.registrosPendentes).toBeGreaterThan(0);
    expect(publicCatalog.estadoGeral).toBe("incompleto");
    expect(publicCatalog.registros.every((record) => record.validationState === "confirmada" || record.validationState === "pendente")).toBe(true);
    expect(publicCatalog.registros.filter((record) => record.canCalculate).length).toBe(catalog.registros.filter((record) => record.inventarioValidado).length);
    expect(publicCatalog.registros.filter((record) => !record.canCalculate).length).toBe(catalog.registrosPendentes);
    expect(publicCatalog.registros.length).toBe(catalog.registros.length);
  });

  it("gera JSON e CSV determinísticos", () => {
    const files = [canonicalPath, csvPath, path.join(root, "src/data/fontesPenais.json"), publicPath];
    const before = files.map(digest);
    execFileSync("node", ["scripts/generate_tipos_penais.mjs"], { cwd: root, stdio: "pipe" });
    const after = files.map(digest);
    expect(after).toEqual(before);
    expect(fs.readFileSync(csvPath, "utf8").trim().split("\n")).toHaveLength(loadCanonical().registros.length + 1);
  });
});
