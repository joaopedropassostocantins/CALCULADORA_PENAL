import json
from pathlib import Path

path = Path('/home/ubuntu/work/CALCULADORA_PENAL/src/data/tiposPenais.json')
catalog = json.loads(path.read_text())
existing = {record['id'] for record in catalog['registros']}
SOURCE = 'https://www.planalto.gov.br/ccivil_03/decreto-lei/del3688.htm'
CUT_OFF = catalog['dataCorte']

def make_record(num, name, desc, minimum, maximum, penalty, keywords, unit='meses'):
    return {
        'id': f'contravencao-3688-{num.lower().replace("º", "").replace("§", "par").replace(" ", "-").replace(".", "").replace(",", "-")}',
        'nomeJuridico': name, 'aliases': [], 'classe': 'contravencao', 'jurisdicao': 'comum', 'modulo': 'Contravenções',
        'norma': 'Decreto-Lei nº 3.688/1941', 'dispositivo': f'art. {num}', 'naturezaFigura': 'basica', 'tipoPaiId': None,
        'descricaoObjetiva': desc,
        'pena': {'minimoMeses': minimum, 'maximoMeses': maximum, 'unidadePrincipal': unit, 'descricao': penalty, 'multa': None},
        'vigencia': {'estado': 'vigente', 'inicioVigenciaRedacao': None, 'dataConsulta': CUT_OFF, 'estadoConferencia': 'pendente', 'observacoes': 'Contravenção vigente consultada em texto oficial; inventário permanece pendente até normalização das penas históricas, prisão simples e multas.'},
        'fonteOficial': SOURCE, 'leiCriadoraOuModificadora': ['Decreto-Lei nº 3.688/1941'], 'inventarioValidado': False,
        'enriquecimentoValidado': False, 'usavelNaCalculadora': False,
        'enriquecimento': {'bemJuridico': None, 'sujeitoAtivo': None, 'sujeitoPassivo': None, 'elementoSubjetivo': None, 'consumacao': None, 'tentativa': None, 'formaCulposa': None, 'acaoPenal': None, 'competencia': None, 'procedimento': None, 'rito': None, 'hediondez': None, 'qualificadoras': [], 'majorantes': [], 'minorantes': [], 'agravantesAtenuantes': [], 'extincaoPunibilidade': [], 'jurisprudenciaQualificada': [], 'controversias': []},
        'palavrasChave': keywords,
    }

rows = [
 ('18','Fabrico, comércio ou detenção irregular de arma ou munição','Fabricar, importar, exportar, ter em depósito ou vender, sem permissão, arma ou munição.',3,12,'Prisão simples, de 3 meses a 1 ano, ou multa, ou ambas.',['arma','munição']),
 ('19','Porte de arma','Trazer consigo arma fora de casa ou dependência, sem licença da autoridade.',0.5,6,'Prisão simples, de 15 dias a 6 meses, ou multa, ou ambas.',['porte de arma']),
 ('20','Anúncio de meio abortivo','Anunciar processo, substância ou objeto destinado a provocar aborto.',None,None,'Multa.',['aborto','anúncio'],'sem-pena-privativa'),
 ('21','Vias de fato','Praticar vias de fato contra alguém, se o fato não constitui crime.',0.5,3,'Prisão simples, de 15 dias a 3 meses, ou multa.',['vias de fato']),
 ('22','Internação irregular em estabelecimento psiquiátrico','Receber e internar pessoa apresentada como doente mental sem formalidades legais.',None,None,'Multa; formas específicas podem ter prisão simples e multa.',['internação psiquiátrica']),
 ('23','Custódia indevida de doente mental','Receber e ter sob custódia doente mental fora do caso legal, sem autorização.',0.5,3,'Prisão simples, de 15 dias a 3 meses, ou multa.',['doente mental','custódia']),
 ('24','Fabricação ou comércio de gazua','Fabricar, ceder ou vender gazua ou instrumento usualmente empregado em furto.',6,24,'Prisão simples, de 6 meses a 2 anos, e multa.',['gazua','furto']),
 ('25','Posse não justificada de instrumento de furto','Ter em poder gazuas, chaves falsas ou instrumentos de furto nas condições legais, sem destinação legítima.',2,12,'Prisão simples, de 2 meses a 1 ano, e multa.',['chave falsa','furto']),
 ('26','Violação de lugar ou objeto por serralheiro','Abrir fechadura ou aparelho de defesa de lugar ou objeto sem certificar-se da legitimidade do solicitante.',0.5,3,'Prisão simples, de 15 dias a 3 meses, ou multa.',['serralheiro','fechadura']),
 ('28','Disparo de arma de fogo','Disparar arma de fogo em lugar habitado, via pública ou direção desta.',1,6,'Prisão simples, de 1 a 6 meses, ou multa.',['disparo','arma de fogo']),
 ('29','Desabamento de construção','Provocar desabamento de construção ou causá-lo por erro de projeto ou execução, se não for crime.',None,None,'Multa.',['desabamento','construção'],'sem-pena-privativa'),
 ('30','Perigo de desabamento','Omitir providência reclamada pelo estado ruinoso de construção sob responsabilidade.',None,None,'Multa.',['desabamento','omissão'],'sem-pena-privativa'),
 ('31','Omissão de cautela na guarda ou condução de animais','Deixar animal perigoso em liberdade, confiá-lo a pessoa inexperiente ou não guardá-lo com cautela.',10/30,2,'Prisão simples, de 10 dias a 2 meses, ou multa.',['animal perigoso','cautela']),
 ('32','Falta de habilitação para dirigir veículo','Dirigir sem habilitação veículo em via pública ou embarcação a motor em águas públicas.',None,None,'Multa.',['habilitação','veículo'],'sem-pena-privativa'),
 ('33','Direção não licenciada de aeronave','Dirigir aeronave sem estar devidamente licenciado.',0.5,3,'Prisão simples, de 15 dias a 3 meses, e multa.',['aeronave','licença']),
 ('34','Direção perigosa','Dirigir veículo ou embarcação em via ou águas públicas pondo em perigo a segurança alheia.',0.5,3,'Prisão simples, de 15 dias a 3 meses, ou multa.',['direção perigosa','segurança']),
 ('35','Abuso na prática da aviação','Praticar acrobacias ou voos baixos fora da zona permitida ou pousar aeronave fora de local destinado.',0.5,3,'Prisão simples, de 15 dias a 3 meses, ou multa.',['aviação','voo baixo']),
 ('36','Omissão de sinal de perigo','Deixar de colocar na via pública sinal ou obstáculo legalmente destinado a evitar perigo.',10/30,2,'Prisão simples, de 10 dias a 2 meses, ou multa.',['sinal de perigo','via pública']),
 ('37','Arremesso ou colocação perigosa','Arremessar ou derramar coisa em via pública ou local de uso comum capaz de ofender, sujar ou molestar.',None,None,'Multa.',['via pública','perigo'],'sem-pena-privativa'),
 ('38','Emissão abusiva de fumaça, vapor ou gás','Provocar abusivamente emissão de fumaça, vapor ou gás capaz de ofender ou molestar.',None,None,'Multa.',['fumaça','gás','emissão'],'sem-pena-privativa'),
 ('40','Provocação de tumulto ou conduta inconveniente','Provocar tumulto ou portar-se inconvenientemente em solenidade, ato oficial, assembleia ou espetáculo público.',0.5,6,'Prisão simples, de 15 dias a 6 meses, ou multa.',['tumulto','conduta inconveniente']),
 ('41','Falso alarme','Provocar alarme anunciando desastre ou perigo inexistente ou praticar ato capaz de produzir pânico.',0.5,6,'Prisão simples, de 15 dias a 6 meses, ou multa.',['alarme falso','pânico']),
 ('42','Perturbação do trabalho ou sossego','Perturbar trabalho ou sossego alheios por gritaria, profissão ruidosa, instrumento sonoro ou barulho de animal.',0.5,3,'Prisão simples, de 15 dias a 3 meses, ou multa.',['sossego','barulho','ruído']),
 ('43','Recusa de moeda de curso legal','Recusar receber moeda de curso legal pelo seu valor.',None,None,'Multa.',['moeda','curso legal'],'sem-pena-privativa'),
 ('44','Imitação de moeda para propaganda','Usar como propaganda impresso ou objeto confundível com moeda por pessoa inexperiente.',None,None,'Multa.',['moeda','propaganda'],'sem-pena-privativa'),
 ('45','Simulação da qualidade de funcionário','Fingir-se funcionário público.',1,3,'Prisão simples, de 1 a 3 meses, ou multa.',['funcionário público','falsa qualidade']),
 ('46','Uso ilegítimo de uniforme ou distintivo','Usar publicamente uniforme ou distintivo de função pública que não exerce ou sinal regulado por lei indevidamente.',None,None,'Multa.',['uniforme','distintivo'],'sem-pena-privativa'),
 ('47','Exercício ilegal de profissão ou atividade','Exercer profissão ou atividade econômica sem preencher condições legais ou anunciar que a exerce.',0.5,3,'Prisão simples, de 15 dias a 3 meses, ou multa.',['profissão','atividade econômica']),
 ('48','Exercício ilegal de comércio de antiguidades','Exercer comércio de antiguidades, obras de arte ou manuscritos antigos sem observância legal.',1,6,'Prisão simples, de 1 a 6 meses, ou multa.',['antiguidades','obras de arte']),
 ('49','Falta de matrícula ou escrituração de atividade','Infringir determinação legal relativa à matrícula ou escrituração de indústria, comércio ou atividade.',None,None,'Multa.',['escrituração','atividade'],'sem-pena-privativa'),
 ('50','Jogo de azar','Estabelecer ou explorar jogo de azar em lugar público ou acessível ao público.',3,12,'Prisão simples, de 3 meses a 1 ano, e multa.',['jogo de azar','aposta']),
 ('51','Loteria não autorizada','Promover ou fazer extrair loteria sem autorização legal ou guardar, vender ou expor bilhete não autorizado.',6,24,'Prisão simples, de 6 meses a 2 anos, e multa.',['loteria','aposta']),
 ('52','Loteria estrangeira','Introduzir no país para comércio bilhete de loteria, rifa ou tômbola estrangeiras.',4/3,12,'Prisão simples, de 4 meses a 1 ano, e multa.',['loteria estrangeira']),
 ('53','Loteria estadual irregular','Introduzir para comércio bilhete de loteria estadual em território onde não possa circular.',2/3,6,'Prisão simples, de 2 a 6 meses, e multa.',['loteria estadual']),
 ('54','Exibição ou guarda de lista de sorteio','Exibir ou ter sob guarda lista de sorteio de loteria estrangeira ou estadual irregular.',1/3,3,'Prisão simples, de 1 a 3 meses, e multa.',['lista de sorteio','loteria']),
 ('55','Impressão irregular de bilhetes ou anúncios','Imprimir ou executar serviço de bilhetes, listas, avisos ou cartazes de loteria em local onde não possa circular.',1,6,'Prisão simples, de 1 a 6 meses, e multa.',['bilhete','loteria']),
 ('56','Distribuição ou transporte de listas de loteria','Distribuir ou transportar cartazes, listas de sorteio ou avisos de loteria onde não possa circular.',1/3,3,'Prisão simples, de 1 a 3 meses, e multa.',['loteria','transporte']),
 ('57','Publicidade de sorteio irregular','Divulgar anúncio, aviso ou resultado de extração de loteria onde a circulação não seja legal.',None,None,'Multa.',['loteria','publicidade'],'sem-pena-privativa'),
 ('58','Jogo do bicho','Explorar ou realizar loteria denominada jogo do bicho ou praticar ato relativo à exploração.',4/3,12,'Prisão simples, de 4 meses a 1 ano, e multa.',['jogo do bicho','loteria']),
 ('59','Vadiagem','Entregar-se habitualmente à ociosidade sendo válido para o trabalho e sem renda suficiente ou ocupação lícita.',0.5,3,'Prisão simples, de 15 dias a 3 meses.',['vadiagem']),
 ('62','Embriaguez pública perigosa','Apresentar-se publicamente embriagado causando escândalo ou perigo à própria segurança ou alheia.',0.5,3,'Prisão simples, de 15 dias a 3 meses, ou multa.',['embriaguez']),
 ('63','Servir bebida alcoólica em hipóteses proibidas','Servir bebida alcoólica a pessoa embriagada, com faculdades mentais afetadas ou judicialmente proibida.',2,12,'Prisão simples, de 2 meses a 1 ano, ou multa.',['bebida alcoólica','embriaguez']),
 ('64','Crueldade contra animais','Tratar animal com crueldade ou submetê-lo a trabalho excessivo, inclusive experiência cruel em animal vivo.',10/30,1,'Prisão simples, de 10 dias a 1 mês, ou multa.',['animal','crueldade']),
 ('66','Omissão de comunicação de crime','Deixar de comunicar crime de ação pública conhecido no exercício de função pública ou profissão sanitária nas hipóteses legais.',None,None,'Multa.',['omissão','comunicação de crime'],'sem-pena-privativa'),
 ('67','Inumação ou exumação irregular','Inumar ou exumar cadáver em infração às disposições legais.',1,12,'Prisão simples, de 1 mês a 1 ano, ou multa.',['cadáver','inumação']),
 ('68','Recusa de dados sobre identidade','Recusar à autoridade dados justificadamente solicitados sobre identidade, estado, profissão, domicílio ou residência.',None,None,'Multa; forma de declaração inverídica pode ter prisão simples e multa.',['identidade','autoridade'],'sem-pena-privativa'),
 ('70','Violação do monopólio postal','Praticar ato que importe violação do monopólio postal da União.',3,12,'Prisão simples, de 3 meses a 1 ano, ou multa, ou ambas.',['serviço postal','monopólio postal']),
]
for row in rows:
    num,name,desc,minimum,maximum,penalty,keywords,*rest = row
    unit = rest[0] if rest else 'meses'
    record = make_record(num,name,desc,minimum,maximum,penalty,keywords,unit)
    if record['id'] not in existing:
        catalog['registros'].append(record)
path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + '\n')
print(f'added {sum(make_record(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7] if len(row) > 7 else "meses")["id"] not in existing for row in rows)} records')
