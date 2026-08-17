import json
from pathlib import Path

path = Path('/home/ubuntu/work/CALCULADORA_PENAL/src/data/tiposPenais.json')
catalog = json.loads(path.read_text())
existing = {record['id'] for record in catalog['registros']}
SOURCE = 'https://www.planalto.gov.br/ccivil_03/leis/l6091.htm'
CUT_OFF = catalog['dataCorte']

def make_record(id, device, name, desc, minimum, maximum, penalty, keywords):
    return {
        'id': id, 'nomeJuridico': name, 'aliases': [], 'classe': 'crime', 'jurisdicao': 'eleitoral', 'modulo': 'Transporte eleitoral',
        'norma': 'Lei nº 6.091/1974', 'dispositivo': device, 'naturezaFigura': 'basica', 'tipoPaiId': None,
        'descricaoObjetiva': desc,
        'pena': {'minimoMeses': minimum, 'maximoMeses': maximum, 'unidadePrincipal': 'meses', 'descricao': penalty, 'multa': None},
        'vigencia': {'estado': 'vigente', 'inicioVigenciaRedacao': None, 'dataConsulta': CUT_OFF, 'estadoConferencia': 'pendente', 'observacoes': 'Crime eleitoral localizado em fonte oficial; cálculo bloqueado até suporte a dias-multa, reconciliação com o Código Eleitoral e análise da sanção de cancelamento de registro.'},
        'fonteOficial': SOURCE, 'leiCriadoraOuModificadora': ['Lei nº 6.091/1974'], 'inventarioValidado': False,
        'enriquecimentoValidado': False, 'usavelNaCalculadora': False,
        'enriquecimento': {'bemJuridico': None, 'sujeitoAtivo': None, 'sujeitoPassivo': None, 'elementoSubjetivo': None, 'consumacao': None, 'tentativa': None, 'formaCulposa': None, 'acaoPenal': None, 'competencia': 'eleitoral', 'procedimento': None, 'rito': None, 'hediondez': None, 'qualificadoras': [], 'majorantes': [], 'minorantes': [], 'agravantesAtenuantes': [], 'extincaoPunibilidade': [], 'jurisprudenciaQualificada': [], 'controversias': []},
        'palavrasChave': keywords,
    }
new = [
 make_record('transporte-eleitoral-6091-11-i','art. 11, I','Omissão ou informação inexata sobre veículos eleitorais','Descumprir dever de informar veículos ou prestar informação inexata para elidir a contribuição legal ao transporte eleitoral.',0.5,6,'Detenção, de 15 dias a 6 meses, e 60 a 100 dias-multa.',['transporte eleitoral','informação','veículos']),
 make_record('transporte-eleitoral-6091-11-ii','art. 11, II','Desatendimento de requisição de transporte eleitoral','Desatender requisição judicial eleitoral de veículos ou embarcações para transporte de eleitores.',None,None,'Pagamento de 200 a 300 dias-multa e apreensão do veículo.',['transporte eleitoral','requisição','dias-multa']),
 make_record('transporte-eleitoral-6091-11-iii','art. 11, III','Transporte ou alimentação eleitoral proibidos','Descumprir proibições legais de transporte ou alimentação de eleitores em período eleitoral.',48,72,'Reclusão, de 4 a 6 anos, e 200 a 300 dias-multa.',['transporte eleitoral','alimentação','eleição']),
 make_record('transporte-eleitoral-6091-11-iv','art. 11, IV','Obstrução de serviço eleitoral de transporte ou alimentação','Obstar a prestação dos serviços de transporte ou alimentação de eleitores atribuídos à Justiça Eleitoral.',24,48,'Reclusão, de 2 a 4 anos.',['transporte eleitoral','obstrução','Justiça Eleitoral']),
 make_record('transporte-eleitoral-6091-11-pu','art. 11, parágrafo único','Responsabilidade do guardião de veículo eleitoral','Responsável pela guarda de veículo ou embarcação utilizado em infração do art. 11.',0.5,6,'Detenção, de 15 dias a 6 meses, e 60 a 100 dias-multa.',['transporte eleitoral','guarda de veículo']),
]
for item in new:
    if item['id'] not in existing:
        catalog['registros'].append(item)
path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + '\n')
print(f'added {sum(item["id"] not in existing for item in new)} electoral-transport records')
