import json
from pathlib import Path

path = Path('/home/ubuntu/work/CALCULADORA_PENAL/src/data/tiposPenais.json')
catalog = json.loads(path.read_text())
existing = {record['id'] for record in catalog['registros']}
CUT_OFF = catalog['dataCorte']

def make_record(id, name, device, desc, minimum, maximum, penalty, law, source, module, keywords, note=None, nature='basica', parent=None):
    return {
        'id': id, 'nomeJuridico': name, 'aliases': [], 'classe': 'crime', 'jurisdicao': 'comum', 'modulo': module,
        'norma': law, 'dispositivo': device, 'naturezaFigura': nature, 'tipoPaiId': parent,
        'descricaoObjetiva': desc,
        'pena': {'minimoMeses': minimum, 'maximoMeses': maximum, 'unidadePrincipal': 'meses', 'descricao': penalty, 'multa': None},
        'vigencia': {'estado': 'vigente', 'inicioVigenciaRedacao': None, 'dataConsulta': CUT_OFF, 'estadoConferencia': 'pendente', 'observacoes': note or 'Tipo penal localizado em fonte oficial compilada; cálculo bloqueado até auditoria temporal, jurídica e de unidades de multa.'},
        'fonteOficial': source, 'leiCriadoraOuModificadora': [law], 'inventarioValidado': False,
        'enriquecimentoValidado': False, 'usavelNaCalculadora': False,
        'enriquecimento': {'bemJuridico': None, 'sujeitoAtivo': None, 'sujeitoPassivo': None, 'elementoSubjetivo': None, 'consumacao': None, 'tentativa': None, 'formaCulposa': None, 'acaoPenal': None, 'competencia': None, 'procedimento': None, 'rito': None, 'hediondez': None, 'qualificadoras': [], 'majorantes': [], 'minorantes': [], 'agravantesAtenuantes': [], 'extincaoPunibilidade': [], 'jurisprudenciaQualificada': [], 'controversias': []},
        'palavrasChave': keywords,
    }

CDC = 'https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm'
BANK = 'https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2005/lei/l11101.htm'
PROC = 'https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/l14133.htm'
new = []
for num,name,desc,minimum,maximum,penalty in [
 ('63','Omissão de alerta sobre nocividade ou periculosidade','Omitir dizeres ou sinais ostensivos sobre nocividade ou periculosidade de produtos, embalagens ou publicidade.',6,24,'Detenção, de 6 meses a 2 anos, e multa.'),
 ('64','Omissão de comunicação de nocividade','Deixar de comunicar à autoridade competente e aos consumidores a nocividade ou periculosidade posterior à colocação do produto no mercado.',6,24,'Detenção, de 6 meses a 2 anos, e multa.'),
 ('65','Execução de serviço de alta periculosidade contra determinação','Executar serviço de alto grau de periculosidade contrariando determinação de autoridade competente.',6,24,'Detenção, de 6 meses a 2 anos, e multa.'),
 ('66','Afirmação falsa ou enganosa sobre produto ou serviço','Fazer afirmação falsa ou enganosa ou omitir informação relevante sobre produto ou serviço.',3,12,'Detenção, de 3 meses a 1 ano, e multa.'),
 ('67','Publicidade enganosa ou abusiva','Fazer ou promover publicidade que sabe ou deveria saber enganosa ou abusiva.',3,12,'Detenção, de 3 meses a 1 ano, e multa.'),
 ('68','Publicidade perigosa à saúde ou segurança','Fazer ou promover publicidade capaz de induzir consumidor a comportamento prejudicial ou perigoso à saúde ou segurança.',6,24,'Detenção, de 6 meses a 2 anos, e multa.'),
 ('69','Omissão de dados da publicidade','Deixar de organizar dados fáticos, técnicos e científicos que dão base à publicidade.',1,6,'Detenção, de 1 a 6 meses ou multa.'),
 ('70','Uso de peça usada sem autorização','Empregar na reparação de produtos peça ou componente usado sem autorização do consumidor.',3,12,'Detenção, de 3 meses a 1 ano, e multa.'),
 ('71','Cobrança abusiva de dívida','Utilizar na cobrança de dívidas ameaça, coação, constrangimento, afirmação falsa ou procedimento que exponha consumidor a ridículo ou interfira em seu trabalho, descanso ou lazer.',3,12,'Detenção, de 3 meses a 1 ano, e multa.'),
 ('72','Impedimento de acesso a cadastro do consumidor','Impedir ou dificultar acesso do consumidor a informações em cadastros, bancos de dados, fichas ou registros.',6,12,'Detenção, de 6 meses a 1 ano ou multa.'),
 ('73','Omissão de correção de cadastro inexato','Deixar de corrigir imediatamente informação inexata sobre consumidor em cadastro, banco de dados, ficha ou registro.',1,6,'Detenção, de 1 a 6 meses ou multa.'),
 ('74','Omissão de termo de garantia','Deixar de entregar ao consumidor termo de garantia adequadamente preenchido e com conteúdo claro.',1,6,'Detenção, de 1 a 6 meses ou multa.'),
]:
    new.append(make_record(f'consumo-8078-{num}',name,f'art. {num}',desc,minimum,maximum,penalty,'Lei nº 8.078/1990',CDC,'Crimes contra relações de consumo',['consumidor','relações de consumo',name.lower()]))
for num,name,desc,minimum,maximum,penalty in [
 ('168','Fraude contra credores em falência ou recuperação','Praticar ato fraudulento antes ou depois da falência, recuperação judicial ou extrajudicial com prejuízo a credores e vantagem indevida.',36,72,'Reclusão, de 3 a 6 anos, e multa.'),
 ('169','Violação de sigilo empresarial em recuperação ou falência','Violar, explorar ou divulgar sem justa causa sigilo empresarial ou dados confidenciais contribuindo para inviabilidade econômica ou financeira.',24,48,'Reclusão, de 2 a 4 anos, e multa.'),
 ('170','Divulgação de informação falsa sobre devedor','Divulgar informação falsa sobre devedor em recuperação judicial para levá-lo à falência ou obter vantagem.',24,48,'Reclusão, de 2 a 4 anos, e multa.'),
 ('171','Indução a erro no processo falimentar','Sonegar, omitir ou prestar informação falsa em processo de falência ou recuperação para induzir autoridades, credores ou administrador judicial em erro.',24,48,'Reclusão, de 2 a 4 anos, e multa.'),
 ('172','Favorecimento de credores','Praticar ato patrimonial ou gerador de obrigação para favorecer credor em prejuízo dos demais.',24,60,'Reclusão, de 2 a 5 anos, e multa.'),
 ('173','Desvio, ocultação ou apropriação de bens','Apropriar-se, desviar ou ocultar bens de devedor em recuperação ou massa falida, inclusive por interposta pessoa.',24,48,'Reclusão, de 2 a 4 anos, e multa.'),
 ('174','Aquisição ou uso ilegal de bens da massa','Adquirir, receber ou usar ilicitamente bem que sabe pertencer à massa falida ou influir para que terceiro o faça.',24,48,'Reclusão, de 2 a 4 anos, e multa.'),
 ('175','Habilitação ilegal de crédito','Apresentar relação ou habilitação de crédito falsa ou título falso ou simulado em falência ou recuperação.',24,48,'Reclusão, de 2 a 4 anos, e multa.'),
 ('176','Exercício ilegal de atividade após inabilitação','Exercer atividade para a qual foi inabilitado ou incapacitado por decisão judicial nos termos da Lei de Falências.',12,48,'Reclusão, de 1 a 4 anos, e multa.'),
 ('177','Violação de impedimento no processo falimentar','Adquirir ou especular com bens da massa ou de devedor em recuperação por agente que atuou no respectivo processo.',24,48,'Reclusão, de 2 a 4 anos, e multa.'),
 ('178','Omissão de documentos contábeis obrigatórios','Deixar de elaborar, escriturar ou autenticar documentos contábeis obrigatórios antes ou depois da falência ou recuperação.',12,24,'Detenção, de 1 a 2 anos, e multa, se o fato não constitui crime mais grave.'),
]:
    new.append(make_record(f'falimentar-11101-{num}',name,f'art. {num}',desc,minimum,maximum,penalty,'Lei nº 11.101/2005',BANK,'Crimes falimentares',['falência','recuperação judicial',name.lower()]))
for num,name,desc,minimum,maximum,penalty in [
 ('337-E','Contratação direta ilegal','Admitir, possibilitar ou dar causa a contratação direta fora das hipóteses previstas em lei.',48,96,'Reclusão, de 4 a 8 anos, e multa.'),
 ('337-F','Frustração do caráter competitivo de licitação','Frustrar ou fraudar o caráter competitivo de processo licitatório com intuito de obter vantagem da adjudicação.',48,96,'Reclusão, de 4 a 8 anos, e multa.'),
 ('337-G','Patrocínio de contratação indevida','Patrocinar interesse privado perante a Administração dando causa a licitação ou contrato cuja invalidação seja decretada judicialmente.',6,36,'Reclusão, de 6 meses a 3 anos, e multa.'),
 ('337-H','Modificação ou pagamento irregular em contrato administrativo','Dar causa a modificação ou vantagem irregular em contrato administrativo ou pagar fatura preterindo ordem cronológica.',48,96,'Reclusão, de 4 a 8 anos, e multa.'),
 ('337-I','Perturbação de processo licitatório','Impedir, perturbar ou fraudar realização de ato de processo licitatório.',6,36,'Detenção, de 6 meses a 3 anos, e multa.'),
 ('337-J','Violação de sigilo em licitação','Devassar sigilo de proposta ou proporcionar a terceiro oportunidade de devassá-lo.',24,36,'Detenção, de 2 a 3 anos, e multa.'),
 ('337-K','Afastamento de licitante','Afastar ou tentar afastar licitante por violência, grave ameaça, fraude ou vantagem.',36,60,'Reclusão, de 3 a 5 anos, e multa, além da pena da violência.'),
 ('337-L','Fraude em licitação ou contrato','Fraudar licitação ou contrato em prejuízo da Administração mediante entrega diversa, falsificação, troca ou outro meio fraudulento.',48,96,'Reclusão, de 4 a 8 anos, e multa.'),
 ('337-M','Contratação de empresa inidônea','Admitir em licitação empresa ou profissional declarado inidôneo.',12,36,'Reclusão, de 1 a 3 anos, e multa.'),
 ('337-M-1','Celebração de contrato com inidôneo','Celebrar contrato com empresa ou profissional declarado inidôneo.',36,72,'Reclusão, de 3 a 6 anos, e multa.'),
 ('337-N','Impedimento indevido de inscrição cadastral','Obstar ou dificultar injustamente inscrição em registro cadastral ou alterar, suspender ou cancelar registro indevidamente.',6,24,'Reclusão, de 6 meses a 2 anos, e multa.'),
 ('337-O','Omissão grave de dado por projetista','Omitir, modificar ou entregar dado cadastral ou condição de contorno em dissonância relevante com a realidade em contratação de projeto.',6,36,'Reclusão, de 6 meses a 3 anos, e multa.'),
]:
    new.append(make_record(f'licitacao-14133-{num.lower()}',name,f'art. {num}',desc,minimum,maximum,penalty,'Lei nº 14.133/2021',PROC,'Crimes em licitações e contratos administrativos',['licitação','contrato administrativo',name.lower()]))
for item in new:
    if item['id'] not in existing:
        catalog['registros'].append(item)
path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + '\n')
print(f'added {sum(item["id"] not in existing for item in new)} economic records')
