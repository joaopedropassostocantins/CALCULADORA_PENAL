import json
from pathlib import Path

path = Path('/home/ubuntu/work/CALCULADORA_PENAL/src/data/tiposPenais.json')
catalog = json.loads(path.read_text())
existing = {record['id'] for record in catalog['registros']}
SOURCE = 'https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2006/lei/l11343.htm'
CUT_OFF = catalog['dataCorte']

def make_record(id, name, device, desc, minimum, maximum, penalty, keywords):
    return {
        'id': id, 'nomeJuridico': name, 'aliases': [], 'classe': 'crime', 'jurisdicao': 'comum', 'modulo': 'Drogas',
        'norma': 'Lei nº 11.343/2006', 'dispositivo': device, 'naturezaFigura': 'basica', 'tipoPaiId': None,
        'descricaoObjetiva': desc,
        'pena': {'minimoMeses': minimum, 'maximoMeses': maximum, 'unidadePrincipal': 'meses', 'descricao': penalty, 'multa': None},
        'vigencia': {'estado': 'vigente', 'inicioVigenciaRedacao': None, 'dataConsulta': CUT_OFF, 'estadoConferencia': 'pendente', 'observacoes': 'Tipo da Lei de Drogas localizado em fonte oficial; aguarda reconciliação com jurisprudência, sanções não privativas e unidade de dias-multa.'},
        'fonteOficial': SOURCE, 'leiCriadoraOuModificadora': ['Lei nº 11.343/2006'], 'inventarioValidado': False,
        'enriquecimentoValidado': False, 'usavelNaCalculadora': False,
        'enriquecimento': {'bemJuridico': None, 'sujeitoAtivo': None, 'sujeitoPassivo': None, 'elementoSubjetivo': None, 'consumacao': None, 'tentativa': None, 'formaCulposa': None, 'acaoPenal': None, 'competencia': None, 'procedimento': None, 'rito': None, 'hediondez': None, 'qualificadoras': [], 'majorantes': [], 'minorantes': [], 'agravantesAtenuantes': [], 'extincaoPunibilidade': [], 'jurisprudenciaQualificada': [], 'controversias': []},
        'palavrasChave': keywords,
    }

new = [
 make_record('drogas-28','Porte de droga para consumo pessoal','art. 28','Adquirir, guardar, tiver em depósito, transportar ou trouxer consigo droga para consumo pessoal, sem autorização ou em desacordo com determinação legal ou regulamentar.',None,None,'Advertência sobre os efeitos das drogas, prestação de serviços à comunidade e medida educativa de comparecimento a programa ou curso educativo.',['uso pessoal','droga','consumo']),
 make_record('drogas-34','Maquinário ou instrumento para produção de drogas','art. 34','Fabricar, adquirir, utilizar, transportar, oferecer, vender, distribuir, entregar, possuir ou guardar maquinário, aparelho, instrumento ou qualquer objeto destinado à fabricação, preparação, produção ou transformação de drogas.',36,120,'Reclusão, de 3 a 10 anos, e pagamento de 1.200 a 2.000 dias-multa.',['maquinário','produção','droga']),
 make_record('drogas-36','Financiamento de crimes de drogas','art. 36','Financiar ou custear a prática de qualquer dos crimes previstos nos arts. 33, caput e § 1º, e 34 desta Lei.',36,120,'Reclusão, de 3 a 10 anos, e pagamento de 700 a 1.200 dias-multa.',['financiamento','tráfico','droga']),
 make_record('drogas-37','Colaboração como informante','art. 37','Colaborar, como informante, com grupo, organização ou associação destinados à prática de qualquer dos crimes previstos nos arts. 33, caput e § 1º, e 34 desta Lei.',24,72,'Reclusão, de 2 a 6 anos, e pagamento de 300 a 700 dias-multa.',['informante','tráfico','associação']),
 make_record('drogas-38','Prescrição ou ministração culposa de drogas','art. 38','Prescrever ou ministrar culposamente drogas, sem que delas necessite o paciente, ou fazê-lo em doses excessivas ou em desacordo com determinação legal ou regulamentar.',6,24,'Detenção, de 6 meses a 2 anos, e pagamento de 50 a 200 dias-multa.',['prescrição','culpa','droga']),
 make_record('drogas-39','Condução de embarcação ou aeronave sob efeito de drogas','art. 39','Conduzir embarcação ou aeronave após o consumo de drogas, expondo a dano potencial a incolumidade de outrem.',6,36,'Detenção, de 6 meses a 3 anos, além da apreensão do veículo, cassação da habilitação e pagamento de 200 a 400 dias-multa.',['embarcação','aeronave','droga']),
]
for item in new:
    if item['id'] not in existing:
        catalog['registros'].append(item)
path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + '\n')
print(f'added {sum(item["id"] not in existing for item in new)} drug records')
