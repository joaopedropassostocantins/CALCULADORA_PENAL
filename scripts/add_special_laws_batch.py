import json
from pathlib import Path

path = Path('/home/ubuntu/work/CALCULADORA_PENAL/src/data/tiposPenais.json')
catalog = json.loads(path.read_text())
existing = {record['id'] for record in catalog['registros']}
ABUSE = 'https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2019/lei/l13869.htm'
AML = 'https://www.planalto.gov.br/ccivil_03/leis/l9613compilado.htm'
CUT_OFF = catalog['dataCorte']

def make_record(id, name, device, description, minimum, maximum, penalty, law, source, start, module, keywords, parent=None, note=None):
    return {
        'id': id,
        'nomeJuridico': name,
        'aliases': [],
        'classe': 'crime',
        'jurisdicao': 'comum',
        'modulo': module,
        'norma': law,
        'dispositivo': device,
        'naturezaFigura': 'basica',
        'tipoPaiId': parent,
        'descricaoObjetiva': description,
        'pena': {'minimoMeses': minimum, 'maximoMeses': maximum, 'unidadePrincipal': 'meses', 'descricao': penalty, 'multa': None},
        'vigencia': {'estado': 'vigente', 'inicioVigenciaRedacao': start, 'dataConsulta': CUT_OFF, 'estadoConferencia': 'confirmada', 'observacoes': note},
        'fonteOficial': source,
        'leiCriadoraOuModificadora': [law],
        'inventarioValidado': True,
        'enriquecimentoValidado': False,
        'usavelNaCalculadora': True,
        'enriquecimento': {
            'bemJuridico': None, 'sujeitoAtivo': None, 'sujeitoPassivo': None, 'elementoSubjetivo': None,
            'consumacao': None, 'tentativa': None, 'formaCulposa': None, 'acaoPenal': None,
            'competencia': None, 'procedimento': None, 'rito': None, 'hediondez': None,
            'qualificadoras': [], 'majorantes': [], 'minorantes': [], 'agravantesAtenuantes': [],
            'extincaoPunibilidade': [], 'jurisprudenciaQualificada': [], 'controversias': [],
        },
        'palavrasChave': keywords,
    }

abuse_rows = [
 ('9','Privação de liberdade em desconformidade legal','Decretar medida de privação da liberdade em manifesta desconformidade com as hipóteses legais.',12,48,'Detenção, de 1 a 4 anos, e multa',['prisão ilegal','privação de liberdade']),
 ('10','Condução coercitiva manifestamente descabida','Decretar condução coercitiva de testemunha ou investigado manifestamente descabida ou sem prévia intimação.',12,48,'Detenção, de 1 a 4 anos, e multa',['condução coercitiva','testemunha']),
 ('12','Omissões na comunicação de prisão','Deixar injustificadamente de comunicar prisão em flagrante à autoridade judiciária no prazo legal.',6,24,'Detenção, de 6 meses a 2 anos, e multa',['comunicação de prisão','flagrante']),
 ('13','Constrangimento de preso ou detento','Constranger preso ou detento, mediante violência, grave ameaça ou redução de sua capacidade de resistência, a exibir-se, submeter-se a situação vexatória ou produzir prova contra si ou terceiro.',12,48,'Detenção, de 1 a 4 anos, e multa, sem prejuízo da pena da violência.',['preso','prova contra si','constrangimento']),
 ('15','Constrangimento de pessoa obrigada a guardar sigilo','Constranger a depor, sob ameaça de prisão, pessoa que deva guardar segredo ou resguardar sigilo.',12,48,'Detenção, de 1 a 4 anos, e multa.',['sigilo','interrogatório','direito ao silêncio']),
 ('15a','Violência institucional','Submeter vítima de infração penal ou testemunha de crime violento a procedimentos desnecessários, repetitivos ou invasivos que provoquem revitimização.',3,12,'Detenção, de 3 meses a 1 ano, e multa.',['violência institucional','revitimização']),
 ('16','Falsa identificação ao preso','Deixar de identificar-se ou identificar-se falsamente ao preso durante captura, detenção, prisão ou interrogatório.',6,24,'Detenção, de 6 meses a 2 anos, e multa.',['falsa identidade','prisão']),
 ('18','Interrogatório durante repouso noturno','Submeter preso a interrogatório policial durante o repouso noturno fora das exceções legais.',6,24,'Detenção, de 6 meses a 2 anos, e multa.',['interrogatório noturno','preso']),
 ('19','Impedimento de pleito de preso','Impedir ou retardar injustificadamente o envio de pleito de preso à autoridade judiciária competente.',12,48,'Detenção, de 1 a 4 anos, e multa.',['pleito de preso','custódia']),
 ('20','Impedimento de entrevista reservada com advogado','Impedir sem justa causa a entrevista pessoal e reservada do preso, réu solto ou investigado com advogado ou defensor.',6,24,'Detenção, de 6 meses a 2 anos, e multa.',['advogado','entrevista reservada','defensor']),
 ('21','Manutenção irregular de presos em cela','Manter presos de sexos diferentes na mesma cela ou manter criança ou adolescente com maior de idade em ambiente inadequado.',12,48,'Detenção, de 1 a 4 anos, e multa.',['cela','preso','criança']),
 ('22','Invasão de imóvel por agente público','Invadir ou adentrar imóvel alheio clandestina ou astuciosamente, sem determinação judicial ou fora das condições legais.',12,48,'Detenção, de 1 a 4 anos, e multa.',['invasão de domicílio','busca e apreensão']),
 ('23','Inovação artificiosa em diligência ou investigação','Inovar artificiosamente no curso de diligência, investigação ou processo para eximir ou atribuir responsabilidade ou agravar situação.',12,48,'Detenção, de 1 a 4 anos, e multa.',['fraude processual','investigação']),
 ('24','Constrangimento de instituição hospitalar','Constranger funcionário de instituição hospitalar a admitir pessoa falecida para alterar local ou momento de crime.',12,48,'Detenção, de 1 a 4 anos, e multa, além da pena da violência.',['hospital','alteração de local de crime']),
 ('25','Obtenção ilícita de prova','Proceder à obtenção de prova em procedimento de investigação ou fiscalização por meio manifestamente ilícito.',12,48,'Detenção, de 1 a 4 anos, e multa.',['prova ilícita','investigação']),
 ('27','Investigação sem indício','Requisitar ou instaurar procedimento investigatório contra alguém sem indício da prática de crime, ilícito funcional ou infração administrativa.',6,24,'Detenção, de 6 meses a 2 anos, e multa.',['investigação sem justa causa','procedimento investigatório']),
 ('28','Divulgação indevida de gravação','Divulgar gravação ou trecho sem relação com a prova pretendida, expondo intimidade, vida privada, honra ou imagem.',12,48,'Detenção, de 1 a 4 anos, e multa.',['gravação','intimidade','vida privada']),
 ('29','Informação falsa sobre procedimento','Prestar informação falsa sobre procedimento judicial, policial, fiscal ou administrativo para prejudicar interesse de investigado.',6,24,'Detenção, de 6 meses a 2 anos, e multa.',['informação falsa','investigado']),
 ('30','Persecução sem justa causa contra inocente','Dar início ou proceder à persecução penal, civil ou administrativa sem justa causa fundamentada ou contra quem sabe inocente.',12,48,'Detenção, de 1 a 4 anos, e multa.',['persecução sem justa causa','inocente']),
 ('31','Procrastinação de investigação','Estender injustificadamente a investigação, procrastinando-a em prejuízo do investigado ou fiscalizado.',6,24,'Detenção, de 6 meses a 2 anos, e multa.',['investigação prolongada','procrastinação']),
 ('32','Negativa de acesso aos autos','Negar acesso do interessado, defensor ou advogado aos autos de investigação ou impedir obtenção de cópias fora das exceções legais.',6,24,'Detenção, de 6 meses a 2 anos, e multa.',['acesso aos autos','cópias','defesa']),
 ('33','Exigência sem amparo legal','Exigir informação ou cumprimento de obrigação sem expresso amparo legal, ou invocar cargo para obter vantagem ou privilégio indevido.',6,24,'Detenção, de 6 meses a 2 anos, e multa.',['exigência ilegal','vantagem indevida']),
 ('36','Indisponibilidade excessiva de ativos','Decretar indisponibilidade de ativos financeiros em quantia exacerbadamente superior à dívida e deixar de corrigi-la.',12,48,'Detenção, de 1 a 4 anos, e multa.',['indisponibilidade de ativos','excesso judicial']),
 ('37','Vista procrastinatória em órgão colegiado','Demorar demasiada e injustificadamente no exame de processo com vista para procrastinar seu andamento ou retardar julgamento.',6,24,'Detenção, de 6 meses a 2 anos, e multa.',['vista','procrastinação processual']),
 ('38','Antecipação de culpa em investigação','Antecipar por comunicação, inclusive rede social, atribuição de culpa antes de concluídas as apurações e formalizada a acusação.',6,24,'Detenção, de 6 meses a 2 anos, e multa.',['presunção de inocência','antecipação de culpa']),
]
new=[]
for num,name,desc,minimum,maximum,penalty,keywords in abuse_rows:
    new.append(make_record(f'abuso-autoridade-{num}', name, f'art. {num}' if num != '15a' else 'art. 15-A', desc, minimum, maximum, penalty, 'Lei nº 13.869/2019', ABUSE, '2020-01-03', 'Abuso de autoridade', keywords))
new.append(make_record('lavagem-1', 'Lavagem ou ocultação de bens, direitos e valores', 'art. 1º, caput', 'Ocultar ou dissimular a natureza, origem, localização, disposição, movimentação ou propriedade de bens, direitos ou valores provenientes direta ou indiretamente de infração penal.', 36, 120, 'Reclusão, de 3 a 10 anos, e multa.', 'Lei nº 9.613/1998', AML, '2012-07-10', 'Lavagem de dinheiro', ['lavagem de dinheiro','ocultação de bens','dissimulação de valores']))

for item in new:
    if item['id'] not in existing:
        catalog['registros'].append(item)
path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + '\n')
print(f'added {sum(item["id"] not in existing for item in new)} records')
