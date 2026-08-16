export type PenaltyInputs = {
  minimumMonths: number;
  maximumMonths: number;
  baseMonths: number;
  aggravatingPercentage: number;
  mitigatingPercentage: number;
  increasePercentage: number;
  decreasePercentage: number;
};

export type PenaltyEstimate = {
  firstPhase: number;
  secondPhase: number;
  finalMonths: number;
  formattedDuration: string;
  warnings: string[];
};

const decimal = (value: number) => Math.round(value * 100) / 100;

export function formatDuration(months: number) {
  const wholeMonths = Math.max(0, Math.round(months));
  const years = Math.floor(wholeMonths / 12);
  const remainder = wholeMonths % 12;
  if (years === 0) return `${remainder} ${remainder === 1 ? "mês" : "meses"}`;
  if (remainder === 0) return `${years} ${years === 1 ? "ano" : "anos"}`;
  return `${years} ${years === 1 ? "ano" : "anos"} e ${remainder} ${remainder === 1 ? "mês" : "meses"}`;
}

/**
 * Executa somente a aritmética dos parâmetros preenchidos. Não seleciona
 * circunstâncias, percentuais ou regras jurídicas automaticamente.
 */
export function estimatePenalty(input: PenaltyInputs): PenaltyEstimate {
  const warnings: string[] = [];
  const minimum = Math.max(0, input.minimumMonths);
  const maximum = Math.max(minimum, input.maximumMonths);
  const firstPhase = Math.min(maximum, Math.max(minimum, input.baseMonths));
  if (input.baseMonths !== firstPhase) warnings.push("A pena-base foi limitada ao intervalo informado pelo usuário.");

  const secondMultiplier = 1 + (input.aggravatingPercentage - input.mitigatingPercentage) / 100;
  const secondPhase = decimal(Math.max(0, firstPhase * secondMultiplier));
  const specialMultiplier = 1 + (input.increasePercentage - input.decreasePercentage) / 100;
  const finalMonths = decimal(Math.max(0, secondPhase * specialMultiplier));
  if (finalMonths > maximum) warnings.push("O resultado excede a pena máxima informada; revise causas de aumento, concurso de crimes e limites legais aplicáveis.");

  return { firstPhase, secondPhase, finalMonths, formattedDuration: formatDuration(finalMonths), warnings };
}
