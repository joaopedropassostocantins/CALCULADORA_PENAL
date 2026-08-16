export type ConsultationPack = {
  id: "avulsa" | "cinco" | "dez";
  name: string;
  consultations: number;
  price: number;
  description: string;
  featured?: boolean;
};

/** Valores apenas ilustrativos e centralizados para atualização comercial. */
export const consultationPacks: ConsultationPack[] = [
  {
    id: "avulsa",
    name: "Consulta avulsa",
    consultations: 1,
    price: 3.99,
    description: "Para calcular uma simulação pontual.",
  },
  {
    id: "cinco",
    name: "Pacote 5 consultas",
    consultations: 5,
    price: 17.95,
    description: "Para analisar cenários de uma mesma peça com calma.",
    featured: true,
  },
  {
    id: "dez",
    name: "Pacote 10 consultas",
    consultations: 10,
    price: 31.9,
    description: "Para estudos e comparações de múltiplos cenários.",
  },
];

export function getPack(id: string) {
  return consultationPacks.find(pack => pack.id === id);
}

export function formatBRL(value: number) {
  return new Intl.NumberFormat("pt-BR", { style: "currency", currency: "BRL" }).format(value);
}
