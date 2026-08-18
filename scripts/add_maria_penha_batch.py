import json
from pathlib import Path

path = Path('/home/ubuntu/work/CALCULADORA_PENAL/src/data/tiposPenais.json')
catalog = json.loads(path.read_text())
existing = {record['id'] for record in catalog['registros']}
SOURCE = 'https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2006/lei/l11340.htm'
CUTOFF = catalog['dataCorte']
record = {
    'id': 'maria-penha-11340-24a',
    'nomeJuridico': 'Descumprimento de medidas protetivas de urgência',
    'aliases': ['crime do art. 24-A da Lei Maria da Penha'],
    'classe': 'crime',
    'jurisdicao': 'comum',
    'modulo': 'Lei Maria da Penha',
    'norma': 'Lei nº 11.340/2006',
    'dispositivo': 'art. 24-A',
    'naturezaFigura': 'basica',
    'tipoPaiId': None,
    'descricaoObjetiva': 'Descumprir decisão judicial que defere medidas protetivas de urgência previstas na Lei Maria da Penha.',
    'pena': {'minimoMeses': 24, 'maximoMeses': 60, 'unidadePrincipal': 'meses', 'descricao': 'Reclusão, de 2 a 5 anos, e multa.', 'multa': None},
    'vigencia': {'estado': 'vigente', 'inicioVigenciaRedacao': '2024-10-10', 'dataConsulta': CUTOFF, 'estadoConferencia': 'pendente', 'observacoes': 'Pena vigente conferida no texto oficial com redação dada pela Lei nº 14.994/2024; a majorante do § 4º, incluída pela Lei nº 15.383/2026, deve ser modelada no enriquecimento e não como tipo autônomo.'},
    'fonteOficial': SOURCE,
    'leiCriadoraOuModificadora': ['Lei nº 11.340/2006', 'Lei nº 13.641/2018', 'Lei nº 14.994/2024', 'Lei nº 15.383/2026'],
    'inventarioValidado': False,
    'enriquecimentoValidado': False,
    'usavelNaCalculadora': False,
    'enriquecimento': {'bemJuridico': None, 'sujeitoAtivo': None, 'sujeitoPassivo': None, 'elementoSubjetivo': None, 'consumacao': None, 'tentativa': None, 'formaCulposa': None, 'acaoPenal': None, 'competencia': 'comum', 'procedimento': None, 'rito': None, 'hediondez': None, 'qualificadoras': [], 'majorantes': [], 'minorantes': [], 'agravantesAtenuantes': [], 'extincaoPunibilidade': [], 'jurisprudenciaQualificada': [], 'controversias': []},
    'palavrasChave': ['violência doméstica', 'medida protetiva', 'descumprimento', 'Lei Maria da Penha'],
}
if record['id'] not in existing:
    catalog['registros'].append(record)
    path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + '\n')
    print('added maria-penha-11340-24a')
else:
    print('already present')
