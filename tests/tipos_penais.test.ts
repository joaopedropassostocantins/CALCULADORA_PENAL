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
  modulo: string;
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
    expect(catalog.registros.filter((record) => record.modulo === "Trânsito")).toHaveLength(15);
    expect(catalog.registros.filter((record) => record.modulo === "Crimes ambientais")).toHaveLength(39);
    expect(catalog.registros.filter((record) => record.modulo === "Abuso de autoridade")).toHaveLength(25);
    expect(catalog.registros.filter((record) => record.modulo === "Lavagem de dinheiro")).toHaveLength(1);
    expect(catalog.registros.filter((record) => record.modulo === "Crimes tributários")).toHaveLength(4);
    expect(catalog.registros.filter((record) => record.modulo === "Crimes contra a ordem econômica")).toHaveLength(1);
    expect(catalog.registros.filter((record) => record.modulo === "Crimes contra o consumo")).toHaveLength(1);
    expect(catalog.registros.filter((record) => record.modulo === "Crimes contra o sistema financeiro")).toHaveLength(16);
    expect(catalog.registros.filter((record) => record.modulo === "Estatuto da Pessoa Idosa")).toHaveLength(15);
    expect(catalog.registros.filter((record) => record.modulo === "Pessoa com deficiência")).toHaveLength(5);
    expect(catalog.registros.filter((record) => record.modulo === "Transplantes")).toHaveLength(11);
    expect(catalog.registros.filter((record) => record.modulo === "ECA")).toHaveLength(26);
    expect(catalog.registros.filter((record) => record.modulo === "Lei Henry Borel")).toHaveLength(2);
    expect(catalog.registros.filter((record) => record.modulo === "Crimes raciais")).toHaveLength(18);
    expect(catalog.registros.filter((record) => record.modulo === "Contravenções")).toHaveLength(47);
    expect(catalog.registros.filter((record) => record.modulo === "Contravenções").every((record) => !record.inventarioValidado && !record.usavelNaCalculadora)).toBe(true);
    expect(catalog.registros.filter((record) => record.modulo === "Código Penal Militar")).toHaveLength(8);
    expect(catalog.registros.filter((record) => record.modulo === "Código Penal Militar").every((record) => !record.inventarioValidado && !record.usavelNaCalculadora)).toBe(true);
    expect(catalog.registros.filter((record) => record.modulo === "Crimes eleitorais")).toHaveLength(39);
    expect(catalog.registros.filter((record) => record.modulo === "Crimes eleitorais").every((record) => !record.inventarioValidado && !record.usavelNaCalculadora)).toBe(true);
    expect(catalog.registros.filter((record) => record.modulo === "Crimes de tortura")).toHaveLength(4);
    expect(catalog.registros.filter((record) => record.modulo === "Terrorismo")).toHaveLength(4);
    expect(catalog.registros.filter((record) => record.modulo === "Estado Democrático de Direito")).toHaveLength(9);
    expect(catalog.registros.filter((record) => ["Crimes de tortura", "Terrorismo", "Estado Democrático de Direito"].includes(record.modulo)).every((record) => !record.inventarioValidado && !record.usavelNaCalculadora)).toBe(true);
    expect(catalog.registros.filter((record) => record.modulo === "Crimes contra relações de consumo")).toHaveLength(12);
    expect(catalog.registros.filter((record) => record.modulo === "Crimes falimentares")).toHaveLength(11);
    expect(catalog.registros.filter((record) => record.modulo === "Crimes em licitações e contratos administrativos")).toHaveLength(12);
    expect(catalog.registros.filter((record) => record.modulo === "Drogas")).toHaveLength(8);
    expect(catalog.registros.filter((record) => record.modulo === "Drogas").every((record) => !record.inventarioValidado && !record.usavelNaCalculadora || record.dispositivo === "art. 33, caput" || record.dispositivo === "art. 35")).toBe(true);
    expect(catalog.registros.filter((record) => record.modulo === "Organização criminosa")).toHaveLength(7);
    expect(catalog.registros.filter((record) => record.modulo === "Organização criminosa").every((record) => !record.inventarioValidado && !record.usavelNaCalculadora || record.dispositivo === "art. 2º, caput")).toBe(true);
    for (const record of catalog.registros) {
      expect(record.pena.minimoMeses == null || record.pena.maximoMeses == null || record.pena.minimoMeses <= record.pena.maximoMeses).toBe(true);
      expect(record.tipoPaiId === null || ids.has(record.tipoPaiId)).toBe(true);
      expect(record.usavelNaCalculadora).toBe(record.inventarioValidado);
    }
  });

  it("preserva as regressões legislativas solicitadas", () => {
    const byId = new Map(loadCanonical().registros.map((record) => [record.id, record]));
    const expected: Record<string, [number | null, number | null]> = {
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
      "ctb-302": [24, 48],
      "ctb-303": [6, 24],
      "ctb-306": [6, 36],
      "ctb-308-2": [60, 120],
      "ctb-309": [6, 12],
      "ambiental-32-1a": [24, 60],
      "ambiental-35": [12, 60],
      "ambiental-40": [12, 60],
      "ambiental-41": [24, 48],
      "ambiental-54": [12, 48],
      "ambiental-54-2": [12, 60],
      "ambiental-60": [6, 24],
      "ambiental-69a": [36, 72],
      "abuso-autoridade-9": [12, 48],
      "abuso-autoridade-15a": [3, 12],
      "abuso-autoridade-22": [12, 48],
      "abuso-autoridade-38": [6, 24],
      "lavagem-1": [36, 120],
      "tributario-8137-1": [24, 60],
      "tributario-8137-3-ii": [36, 96],
      "tributario-8137-7": [24, 60],
      "sfn-7492-4": [36, 144],
      "sfn-7492-4-temeraria": [24, 96],
      "sfn-7492-16": [12, 48],
      "sfn-7492-22": [24, 72],
      "idosa-10741-96": [6, 12],
      "idosa-10741-99": [24, 60],
      "idosa-10741-99-2": [96, 168],
      "idosa-10741-102": [12, 48],
      "lbi-88": [12, 36],
      "lbi-90": [24, 60],
      "transplante-14": [24, 72],
      "transplante-14-4": [96, 240],
      "transplante-15": [36, 96],
      "transplante-20": [null, null],
      "eca-240": [48, 120],
      "eca-243": [24, 48],
      "eca-244b": [12, 48],
      "eca-244c": [24, 48],
      "henry-borel-25": [3, 24],
      "raciais-7716-2a": [24, 60],
      "raciais-7716-20": [12, 36],
      "raciais-7716-20-1": [24, 60],
      "cpm-205": [72, 240],
      "cpm-251": [24, 84],
      "cpm-303": [36, 180],
      "cpm-308": [24, 144],
      "eleitoral-4737-302": [48, 72],
      "eleitoral-4737-323": [2, 12],
      "eleitoral-4737-326": [0, 6],
      "eleitoral-4737-326-a": [24, 96],
      "eleitoral-4737-326-b": [12, 48],
      "eleitoral-4737-339": [24, 72],
      "tortura-1": [24, 96],
      "tortura-1-2": [12, 48],
      "tortura-1-3": [48, 120],
      "tortura-1-3-morte": [96, 192],
      "terrorismo-2": [144, 360],
      "terrorismo-3": [60, 96],
      "terrorismo-5": [null, 360],
      "terrorismo-6": [180, 360],
      "estado-democratico-359i": [36, 96],
      "estado-democratico-359k-2": [72, 180],
      "estado-democratico-359n": [36, 72],
      "estado-democratico-359r": [24, 96],
      "consumo-8078-63": [6, 24],
      "consumo-8078-66": [3, 12],
      "consumo-8078-71": [3, 12],
      "consumo-8078-74": [1, 6],
      "falimentar-11101-168": [36, 72],
      "falimentar-11101-172": [24, 60],
      "falimentar-11101-178": [12, 24],
      "licitacao-14133-337-e": [48, 96],
      "licitacao-14133-337-m-1": [36, 72],
      "licitacao-14133-337-o": [6, 36],
      "drogas-28": [null, null],
      "drogas-34": [36, 120],
      "drogas-36": [36, 120],
      "drogas-37": [24, 72],
      "drogas-38": [6, 24],
      "drogas-39": [6, 36],
      "orgcrime-12850-18": [12, 36],
      "orgcrime-12850-19": [12, 48],
      "orgcrime-12850-20": [12, 48],
      "orgcrime-12850-21": [6, 24],
      "orgcrime-12850-21a": [48, 144],
      "orgcrime-12850-21b": [48, 144],
    };
    for (const [id, [minimum, maximum]] of Object.entries(expected)) {
      const record = byId.get(id);
      expect(record, `registro ausente: ${id}`).toBeDefined();
      expect(record?.pena.minimoMeses).toBe(minimum);
      expect(record?.pena.maximoMeses).toBe(maximum);
    }
    expect(byId.get("transplante-20")?.usavelNaCalculadora).toBe(false);
    expect(byId.get("transplante-20")?.inventarioValidado).toBe(false);
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
