export type LegalNorm = {
  block: string;
  norm: string;
  subject: string;
  nature: string;
  officialUrl: string;
};

export type LegalStatement = {
  enunciado: string;
  teor: string;
  incidencia: string;
};

export type LegalCatalog = {
  norms: LegalNorm[];
  bindingStatements: LegalStatement[];
  courtStatements: LegalStatement[];
  precedents: LegalStatement[];
  importedAt: string;
};
