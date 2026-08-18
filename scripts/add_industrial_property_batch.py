import json
from pathlib import Path

path = Path('/home/ubuntu/work/CALCULADORA_PENAL/src/data/tiposPenais.json')
catalog = json.loads(path.read_text())
existing = {record['id'] for record in catalog['registros']}
SOURCE = 'https://www.planalto.gov.br/ccivil_03/leis/l9279.htm'
CUT_OFF = catalog['dataCorte']

def make_record(id, name, device, desc, minimum, maximum, penalty, keywords):
    return {
        'id': id, 'nomeJuridico': name, 'aliases': [], 'classe': 'crime', 'jurisdicao': 'comum', 'modulo': 'Propriedade industrial',
        'norma': 'Lei nº 9.279/1996', 'dispositivo': device, 'naturezaFigura': 'basica', 'tipoPaiId': None,
        'descricaoObjetiva': desc,
        'pena': {'minimoMeses': minimum, 'maximoMeses': maximum, 'unidadePrincipal': 'meses', 'descricao': penalty, 'multa': None},
        'vigencia': {'estado': 'vigente', 'inicioVigenciaRedacao': None, 'dataConsulta': CUT_OFF, 'estadoConferencia': 'pendente', 'observacoes': 'Crime localizado no capítulo penal da fonte oficial compilada; cálculo bloqueado até auditoria de elementos, tentativa, ação penal e multa.'},
        'fonteOficial': SOURCE, 'leiCriadoraOuModificadora': ['Lei nº 9.279/1996'], 'inventarioValidado': False,
        'enriquecimentoValidado': False, 'usavelNaCalculadora': False,
        'enriquecimento': {'bemJuridico': None, 'sujeitoAtivo': None, 'sujeitoPassivo': None, 'elementoSubjetivo': None, 'consumacao': None, 'tentativa': None, 'formaCulposa': None, 'acaoPenal': None, 'competencia': None, 'procedimento': None, 'rito': None, 'hediondez': None, 'qualificadoras': [], 'majorantes': [], 'minorantes': [], 'agravantesAtenuantes': [], 'extincaoPunibilidade': [], 'jurisprudenciaQualificada': [], 'controversias': []},
        'palavrasChave': keywords,
    }
P = 'detenção, de 3 meses a 1 ano, ou multa.'
P_SHORT = 'Detenção, de 1 a 3 meses, ou multa.'
new = [
 make_record('propriedade-industrial-9279-183','Violação de patente por fabricação ou uso','art. 183','Fabricar produto objeto de patente de invenção ou modelo de utilidade, ou usar meio ou processo patenteado, sem autorização do titular.',3,12,'Detenção, de 3 meses a 1 ano, ou multa.',['patente','invenção','modelo de utilidade']),
 make_record('propriedade-industrial-9279-184','Comércio ou importação de produto patenteado','art. 184','Exportar, vender, oferecer, manter em estoque, ocultar, receber ou importar produto fabricado ou obtido com violação de patente para fins econômicos.',1,3,P_SHORT,['patente','importação','comércio']),
 make_record('propriedade-industrial-9279-185','Fornecimento de componente para processo patenteado','art. 185','Fornecer componente, material ou equipamento cuja aplicação final necessariamente induza à exploração de objeto de patente.',1,3,P_SHORT,['patente','componente','processo']),
 make_record('propriedade-industrial-9279-187','Fabricação de produto com desenho industrial ilícito','art. 187','Fabricar, sem autorização do titular, produto que incorpore desenho industrial registrado ou imitação substancial capaz de induzir erro ou confusão.',3,12,P,['desenho industrial','imitação']),
 make_record('propriedade-industrial-9279-188','Comércio ou importação de produto com desenho industrial ilícito','art. 188','Exportar, vender, oferecer, manter em estoque, ocultar, receber ou importar objeto que incorpore ilicitamente desenho industrial ou imitação substancial.',1,3,P_SHORT,['desenho industrial','importação','comércio']),
 make_record('propriedade-industrial-9279-189','Reprodução ou alteração de marca registrada','art. 189','Reproduzir ou imitar marca registrada sem autorização, ou alterar marca registrada de outrem já aposta em produto colocado no mercado.',3,12,P,['marca','reprodução','imitação']),
 make_record('propriedade-industrial-9279-190','Comércio de produto com marca ilícita','art. 190','Importar, exportar, vender, oferecer, expor, ocultar ou manter em estoque produto com marca ilicitamente reproduzida ou embalagem com marca legítima de outrem.',1,3,P_SHORT,['marca','importação','comércio']),
 make_record('propriedade-industrial-9279-191','Uso indevido de símbolos oficiais em marca','art. 191','Reproduzir ou imitar armas, brasões ou distintivos oficiais em marca, nome comercial, insígnia ou propaganda, ou vender produto assim assinalado.',1,3,P_SHORT,['marca','símbolo oficial','propaganda']),
 make_record('propriedade-industrial-9279-192','Falsa indicação geográfica','art. 192','Fabricar, importar, exportar, vender, expor, oferecer ou manter em estoque produto com falsa indicação geográfica.',1,3,P_SHORT,['indicação geográfica','produto']),
 make_record('propriedade-industrial-9279-193','Uso de indicação geográfica falsa ou retificativa','art. 193','Usar termos retificativos que não ressalvem a verdadeira procedência do produto.',1,3,P_SHORT,['indicação geográfica','procedência']),
 make_record('propriedade-industrial-9279-194','Indicação falsa de procedência','art. 194','Usar marca, nome comercial, título de estabelecimento, insígnia ou sinal que indique procedência diversa da verdadeira, ou vender produto com esses sinais.',1,3,P_SHORT,['procedência','marca','nome comercial']),
 make_record('propriedade-industrial-9279-195','Concorrência desleal','art. 195','Publicar falsa afirmação, desviar clientela por fraude, usar sinais alheios, corromper empregado de concorrente, violar segredo empresarial ou divulgar dados de testes não divulgados, entre outras condutas legais.',3,12,P,['concorrência desleal','segredo empresarial','clientela']),
]
for item in new:
    if item['id'] not in existing:
        catalog['registros'].append(item)
path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + '\n')
print(f'added {sum(item["id"] not in existing for item in new)} industrial-property records')
