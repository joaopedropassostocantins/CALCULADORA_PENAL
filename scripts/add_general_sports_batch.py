import json
from pathlib import Path

path = Path('/home/ubuntu/work/CALCULADORA_PENAL/src/data/tiposPenais.json')
catalog = json.loads(path.read_text())
existing = {record['id'] for record in catalog['registros']}
SOURCE = 'https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14597.htm'
CUT_OFF = catalog['dataCorte']

def make_record(id, name, device, desc, minimum, maximum, penalty, keywords):
    return {
        'id': id, 'nomeJuridico': name, 'aliases': [], 'classe': 'crime', 'jurisdicao': 'comum', 'modulo': 'Lei Geral do Esporte',
        'norma': 'Lei nº 14.597/2023', 'dispositivo': device, 'naturezaFigura': 'basica', 'tipoPaiId': None,
        'descricaoObjetiva': desc,
        'pena': {'minimoMeses': minimum, 'maximoMeses': maximum, 'unidadePrincipal': 'meses', 'descricao': penalty, 'multa': None},
        'vigencia': {'estado': 'vigente', 'inicioVigenciaRedacao': None, 'dataConsulta': CUT_OFF, 'estadoConferencia': 'pendente', 'observacoes': 'Crime localizado na Lei Geral do Esporte vigente; cálculo bloqueado até auditoria de majorantes, competência, ação penal e sanção impeditiva de comparecimento.'},
        'fonteOficial': SOURCE, 'leiCriadoraOuModificadora': ['Lei nº 14.597/2023'], 'inventarioValidado': False,
        'enriquecimentoValidado': False, 'usavelNaCalculadora': False,
        'enriquecimento': {'bemJuridico': None, 'sujeitoAtivo': None, 'sujeitoPassivo': None, 'elementoSubjetivo': None, 'consumacao': None, 'tentativa': None, 'formaCulposa': None, 'acaoPenal': None, 'competencia': None, 'procedimento': None, 'rito': None, 'hediondez': None, 'qualificadoras': [], 'majorantes': [], 'minorantes': [], 'agravantesAtenuantes': [], 'extincaoPunibilidade': [], 'jurisprudenciaQualificada': [], 'controversias': []},
        'palavrasChave': keywords,
    }
new = [
 make_record('esporte-14597-198','Solicitação ou aceitação de vantagem para manipulação esportiva','art. 198','Solicitar ou aceitar vantagem ou promessa para ato ou omissão destinado a alterar ou falsear resultado de competição esportiva ou evento associado.',24,72,'Reclusão, de 2 a 6 anos, e multa.',['manipulação de resultado','vantagem','competição esportiva']),
 make_record('esporte-14597-199','Oferta de vantagem para manipulação esportiva','art. 199','Dar ou prometer vantagem patrimonial ou não patrimonial para alterar ou falsear resultado de competição esportiva ou evento associado.',24,72,'Reclusão, de 2 a 6 anos, e multa.',['manipulação de resultado','vantagem','esporte']),
 make_record('esporte-14597-200','Fraude de resultado de competição esportiva','art. 200','Fraudar ou contribuir para fraudar de qualquer forma o resultado de competição esportiva ou evento associado.',24,72,'Reclusão, de 2 a 6 anos, e multa.',['fraude esportiva','resultado','competição']),
 make_record('esporte-14597-201','Tumulto, violência ou invasão em evento esportivo','art. 201','Promover tumulto, praticar ou incitar violência ou invadir local restrito a competidores ou árbitros em evento esportivo, incluindo condutas de torcedores nas hipóteses legais.',12,24,'Reclusão, de 1 a 2 anos, e multa, com majorantes e sanções impeditivas específicas.',['violência esportiva','tumulto','torcedor']),
]
for item in new:
    if item['id'] not in existing:
        catalog['registros'].append(item)
path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + '\n')
print(f'added {sum(item["id"] not in existing for item in new)} general-sports records')
