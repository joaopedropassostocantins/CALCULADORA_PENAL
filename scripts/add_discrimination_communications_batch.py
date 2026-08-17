import json
from pathlib import Path

path = Path('/home/ubuntu/work/CALCULADORA_PENAL/src/data/tiposPenais.json')
catalog = json.loads(path.read_text())
existing = {record['id'] for record in catalog['registros']}
CUT_OFF = catalog['dataCorte']

def make_record(id, name, device, desc, minimum, maximum, penalty, law, source, module, keywords, note=None):
    return {
        'id': id, 'nomeJuridico': name, 'aliases': [], 'classe': 'crime', 'jurisdicao': 'comum', 'modulo': module,
        'norma': law, 'dispositivo': device, 'naturezaFigura': 'basica', 'tipoPaiId': None,
        'descricaoObjetiva': desc,
        'pena': {'minimoMeses': minimum, 'maximoMeses': maximum, 'unidadePrincipal': 'meses', 'descricao': penalty, 'multa': None},
        'vigencia': {'estado': 'vigente', 'inicioVigenciaRedacao': None, 'dataConsulta': CUT_OFF, 'estadoConferencia': 'pendente', 'observacoes': note or 'Tipo localizado em fonte oficial; cálculo bloqueado até auditoria de vigência e enriquecimento jurídico.'},
        'fonteOficial': source, 'leiCriadoraOuModificadora': [law], 'inventarioValidado': False,
        'enriquecimentoValidado': False, 'usavelNaCalculadora': False,
        'enriquecimento': {'bemJuridico': None, 'sujeitoAtivo': None, 'sujeitoPassivo': None, 'elementoSubjetivo': None, 'consumacao': None, 'tentativa': None, 'formaCulposa': None, 'acaoPenal': None, 'competencia': None, 'procedimento': None, 'rito': None, 'hediondez': None, 'qualificadoras': [], 'majorantes': [], 'minorantes': [], 'agravantesAtenuantes': [], 'extincaoPunibilidade': [], 'jurisprudenciaQualificada': [], 'controversias': []},
        'palavrasChave': keywords,
    }
HIV = 'https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2014/lei/l12984.htm'
INT = 'https://www.planalto.gov.br/ccivil_03/leis/l9296.htm'
TEL = 'https://www.planalto.gov.br/ccivil_03/leis/l9472.htm'
WORK = 'https://www.planalto.gov.br/ccivil_03/leis/l9029.htm'
new = [
 make_record('hiv-12984-1','Discriminação contra pessoa com HIV ou aids','art. 1º','Recusar, retardar, cancelar, segregar ou impedir ensino; negar emprego; exonerar ou demitir; segregar no trabalho ou escola; divulgar condição para ofender dignidade; ou recusar ou retardar atendimento de saúde por condição de HIV ou aids.',12,48,'Reclusão, de 1 a 4 anos, e multa.','Lei nº 12.984/2014',HIV,'Discriminação por HIV',['HIV','aids','discriminação']),
 make_record('interceptacao-9296-10','Interceptação ou escuta ambiental ilegal','art. 10','Realizar interceptação de comunicações telefônicas, informáticas ou telemáticas, promover escuta ambiental ou quebrar segredo da Justiça sem autorização judicial ou com objetivo não autorizado em lei.',24,48,'Reclusão, de 2 a 4 anos, e multa.','Lei nº 9.296/1996',INT,'Interceptação de comunicações',['interceptação','escuta ambiental','segredo de Justiça'],'Redação atual inclui escuta ambiental e autoridade judicial no parágrafo único, conforme Lei nº 13.869/2019.'),
 make_record('interceptacao-9296-10a','Captação ambiental ilegal','art. 10-A','Realizar captação ambiental de sinais eletromagnéticos, ópticos ou acústicos sem autorização judicial quando exigida.',24,48,'Reclusão, de 2 a 4 anos, e multa.','Lei nº 9.296/1996',INT,'Interceptação de comunicações',['captação ambiental','sinais','investigação']),
 make_record('telecom-9472-183','Desenvolvimento clandestino de atividade de telecomunicação','art. 183','Desenvolver clandestinamente atividades de telecomunicação.',24,48,'Detenção, de 2 a 4 anos, aumentada da metade se houver dano a terceiro, e multa.','Lei nº 9.472/1997',TEL,'Telecomunicações',['telecomunicação','radiofrequência','clandestino']),
 make_record('discriminacao-trabalho-9029-2','Discriminação laboral por gravidez ou esterilização','art. 2º','Exigir teste ou procedimento relativo à esterilização ou gravidez, ou adotar medidas de indução ou instigação à esterilização genética ou controle de natalidade nas hipóteses legais.',12,24,'Detenção, de 1 a 2 anos, e multa.','Lei nº 9.029/1995',WORK,'Discriminação laboral',['gravidez','esterilização','trabalho']),
]
for item in new:
    if item['id'] not in existing:
        catalog['registros'].append(item)
path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + '\n')
print(f'added {sum(item["id"] not in existing for item in new)} discrimination/communications records')
