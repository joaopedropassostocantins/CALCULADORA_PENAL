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
        'vigencia': {'estado': 'vigente', 'inicioVigenciaRedacao': None, 'dataConsulta': CUT_OFF, 'estadoConferencia': 'pendente', 'observacoes': note or 'Tipo localizado em fonte oficial; cálculo bloqueado até reconciliação de redação, vigência e unidade de multa.'},
        'fonteOficial': source, 'leiCriadoraOuModificadora': [law], 'inventarioValidado': False,
        'enriquecimentoValidado': False, 'usavelNaCalculadora': False,
        'enriquecimento': {'bemJuridico': None, 'sujeitoAtivo': None, 'sujeitoPassivo': None, 'elementoSubjetivo': None, 'consumacao': None, 'tentativa': None, 'formaCulposa': None, 'acaoPenal': None, 'competencia': None, 'procedimento': None, 'rito': None, 'hediondez': None, 'qualificadoras': [], 'majorantes': [], 'minorantes': [], 'agravantesAtenuantes': [], 'extincaoPunibilidade': [], 'jurisprudenciaQualificada': [], 'controversias': []},
        'palavrasChave': keywords,
    }
GEN = 'https://www.planalto.gov.br/ccivil_03/leis/l2889.htm'
POP = 'https://www.planalto.gov.br/ccivil_03/leis/l1521.htm'
ORD = 'https://www.planalto.gov.br/ccivil_03/leis/l8176.htm'
new = [
 make_record('genocidio-2889-1a','Genocídio por morte de membros do grupo','art. 1º, a','Matar membros de grupo nacional, étnico, racial ou religioso com intenção de destruí-lo total ou parcialmente.',144,360,'Pena do art. 121, § 2º, do Código Penal.','Lei nº 2.889/1956',GEN,'Genocídio',['genocídio','grupo nacional','grupo étnico'], 'A pena é remetida ao Código Penal e deve ser reconciliada com sua redação vigente.'),
 make_record('genocidio-2889-1b','Genocídio por lesão grave a membros do grupo','art. 1º, b','Causar lesão grave à integridade física ou mental de membros do grupo com intenção genocida.',24,96,'Pena do art. 129, § 2º, do Código Penal.','Lei nº 2.889/1956',GEN,'Genocídio',['genocídio','lesão grave'], 'A pena é remetida ao Código Penal e deve ser reconciliada com sua redação vigente.'),
 make_record('genocidio-2889-1c','Genocídio por submissão a condições destrutivas','art. 1º, c','Submeter intencionalmente o grupo a condições de existência capazes de ocasionar sua destruição física total ou parcial.',None,None,'Pena do art. 270 do Código Penal.','Lei nº 2.889/1956',GEN,'Genocídio',['genocídio','destruição física'], 'Pena por remissão legal; cálculo bloqueado até modelagem específica.'),
 make_record('genocidio-2889-1d','Genocídio por impedimento de nascimentos','art. 1º, d','Adotar medidas destinadas a impedir os nascimentos no seio do grupo com intenção genocida.',36,120,'Pena do art. 125 do Código Penal.','Lei nº 2.889/1956',GEN,'Genocídio',['genocídio','nascimentos'], 'Pena por remissão legal; cálculo bloqueado até reconciliação.'),
 make_record('genocidio-2889-1e','Genocídio por transferência forçada de crianças','art. 1º, e','Efetuar transferência forçada de crianças do grupo para outro grupo com intenção genocida.',12,36,'Pena do art. 148 do Código Penal.','Lei nº 2.889/1956',GEN,'Genocídio',['genocídio','criança','transferência forçada'], 'Pena por remissão legal; cálculo bloqueado até reconciliação.'),
 make_record('genocidio-2889-2','Associação para genocídio','art. 2º','Associarem-se mais de três pessoas para a prática dos crimes de genocídio.',None,None,'Metade da pena cominada aos crimes de genocídio.','Lei nº 2.889/1956',GEN,'Genocídio',['genocídio','associação'], 'Pena variável por remissão e fração legal.'),
 make_record('genocidio-2889-3','Incitação pública ao genocídio','art. 3º','Incitar direta e publicamente alguém a cometer crime de genocídio.',None,None,'Metade das penas dos crimes incitados; pena integral se o crime incitado se consumar.','Lei nº 2.889/1956',GEN,'Genocídio',['genocídio','incitação'], 'Pena variável por remissão e resultado.'),
 make_record('economia-popular-1521-2','Crimes contra a economia popular','art. 2º','Praticar qualquer das condutas do art. 2º, incluindo sonegação de mercadorias, fraude de pesos e medidas, venda acima de tabelas e processos fraudulentos contra o povo.',6,24,'Detenção, de 6 meses a 2 anos, e multa em unidade monetária histórica.','Lei nº 1.521/1951',POP,'Economia popular',['economia popular','mercadoria','fraude'], 'Pena pecuniária histórica pendente de normalização monetária.'),
 make_record('economia-popular-1521-3','Crimes contra a economia popular e a concorrência','art. 3º','Praticar condutas do art. 3º, incluindo destruição de produtos para alta de preços, cartel, retenção de matérias-primas e gestão fraudulenta ou temerária.',24,120,'Detenção, de 2 a 10 anos, e multa em unidade monetária histórica.','Lei nº 1.521/1951',POP,'Economia popular',['economia popular','concorrência','preços'], 'Pena pecuniária histórica pendente de normalização monetária.'),
 make_record('economia-popular-1521-4','Usura pecuniária ou real','art. 4º','Cobrar juros ou lucros usurários ou obter lucro patrimonial abusivo em situação de necessidade, inexperiência ou leviandade da outra parte.',6,24,'Detenção, de 6 meses a 2 anos, e multa.','Lei nº 1.521/1951',POP,'Economia popular',['usura','juros','economia popular'], 'Pena pecuniária histórica pendente de normalização monetária.'),
 make_record('ordem-economica-8176-1','Comércio irregular de combustíveis','art. 1º','Adquirir, distribuir ou revender derivados de petróleo, gás natural, álcool carburante ou combustíveis líquidos em desacordo com as normas legais; ou usar GLP para fins automotivos em desacordo com a lei.',12,60,'Detenção, de 1 a 5 anos.','Lei nº 8.176/1991',ORD,'Ordem econômica',['combustíveis','petróleo','GLP'], 'Redação do inciso II alterada pela Lei nº 15.348/2026; aguarda reconferência temporal.'),
 make_record('ordem-economica-8176-2','Usurpação de bens ou matéria-prima da União','art. 2º','Produzir bens ou explorar matéria-prima pertencentes à União sem autorização legal ou em desacordo com obrigações do título autorizativo, incluindo adquirir, transportar, industrializar, possuir, consumir ou comercializar os produtos.',12,60,'Detenção, de 1 a 5 anos e multa de 10 a 360 dias-multa.','Lei nº 8.176/1991',ORD,'Ordem econômica',['usurpação','matéria-prima','União'], 'Pena pecuniária em dias-multa; cálculo bloqueado até suporte específico.'),
]
for item in new:
    if item['id'] not in existing:
        catalog['registros'].append(item)
path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + '\n')
print(f'added {sum(item["id"] not in existing for item in new)} genocide/economy records')
