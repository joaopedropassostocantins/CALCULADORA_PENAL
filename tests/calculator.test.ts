import { describe, expect, it } from "vitest";
import { estimatePenalty, formatDuration } from "../src/lib/calculator";
import { consultationPacks, getPack } from "../src/data/pricing";

describe("calculadora de parâmetros", () => {
  it("aplica apenas a aritmética dos percentuais informados", () => {
    const estimate = estimatePenalty({ minimumMonths: 12, maximumMonths: 60, baseMonths: 24, aggravatingPercentage: 10, mitigatingPercentage: 0, increasePercentage: 50, decreasePercentage: 0 });
    expect(estimate.firstPhase).toBe(24);
    expect(estimate.secondPhase).toBe(26.4);
    expect(estimate.finalMonths).toBe(39.6);
  });

  it("formata duração em anos e meses", () => {
    expect(formatDuration(30)).toBe("2 anos e 6 meses");
  });
});

describe("pacotes de consulta", () => {
  it("mantém a consulta avulsa de R$ 3,99 e pacotes por quantidade", () => {
    expect(getPack("avulsa")).toMatchObject({ consultations: 1, price: 3.99 });
    expect(consultationPacks.every(pack => pack.consultations > 0)).toBe(true);
  });
});
