import json
from pathlib import Path

path = Path('/home/ubuntu/work/CALCULADORA_PENAL/src/data/tiposPenais.json')
catalog = json.loads(path.read_text())
existing = {record['id'] for record in catalog['registros']}
SOURCE = 'https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14785.htm'
CUT_OFF = catalog['dataCorte']

def make_record(id, name, device, desc, minimum, maximum, penalty, keywords):
    return {
        'id': id, 'nomeJuridico': name, 'aliases': [], 'classe': 'crime', 'jurisdicao': 'comum', 'modulo': 'Agrotóxicos e produtos de controle ambiental',
        'norma': 'Lei nº 14.785/2023', 'dispositivo': device, 'naturezaFigura': 'basica', 'tipoPaiId': None,
        'descricaoObjetiva': desc,
        'pena': {'minimoMeses': minimum, 'maximoMeses': maximum, 'unidadePrincipal': 'meses', 'descricao': penalty, 'multa': None},
        'vigencia': {'estado': 'vigente', 'inicioVigenciaRedacao': None, 'dataConsulta': CUT_OFF, 'estadoConferencia': 'pendente', 'observacoes': 'Crime localizado na lei vigente de agrotóxicos; cálculo bloqueado até auditoria das majorantes, regulamentação e enriquecimento jurídico.'},
        'fonteOficial': SOURCE, 'leiCriadoraOuModificadora': ['Lei nº 14.785/2023'], 'inventarioValidado': False,
        'enriquecimentoValidado': False, 'usavelNaCalculadora': False,
        'enriquecimento': {'bemJuridico': None, 'sujeitoAtivo': None, 'sujeitoPassivo': None, 'elementoSubjetivo': None, 'consumacao': None, 'tentativa': None, 'formaCulposa': None, 'acaoPenal': None, 'competencia': None, 'procedimento': None, 'rito': None, 'hediondez': None, 'qualificadoras': [], 'majorantes': [], 'minorantes': [], 'agravantesAtenuantes': [], 'extincaoPunibilidade': [], 'jurisprudenciaQualificada': [], 'controversias': []},
        'palavrasChave': keywords,
    }
new = [
 make_record('agrotoxicos-14785-56','Produção ou comércio não autorizado de agrotóxicos','art. 56','Produzir, armazenar, transportar, importar, utilizar ou comercializar agrotóxicos, produtos de controle ambiental ou afins não registrados ou não autorizados.',36,108,'Reclusão, de 3 a 9 anos, e multa, com majorantes por dano patrimonial ou ambiental.',['agrotóxicos','registro','produto de controle ambiental']),
 make_record('agrotoxicos-14785-57','Destinação irregular de resíduos de agrotóxicos','art. 57','Produzir, importar, comercializar ou dar destinação a resíduos e embalagens vazias de agrotóxicos, produtos de controle ambiental ou afins em desacordo com a lei.',24,48,'Reclusão, de 2 a 4 anos, e multa.',['agrotóxicos','resíduos','embalagens']),
]
for item in new:
    if item['id'] not in existing:
        catalog['registros'].append(item)
path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + '\n')
print(f'added {sum(item["id"] not in existing for item in new)} pesticide records')
