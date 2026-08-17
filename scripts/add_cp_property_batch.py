import json
from pathlib import Path

path = Path('/home/ubuntu/work/CALCULADORA_PENAL/src/data/tiposPenais.json')
catalog = json.loads(path.read_text())
existing = {record['id'] for record in catalog['registros']}
SOURCE = 'https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848.htm'
CUTOFF = catalog['dataCorte']

def make_record(id, device, name, desc, minimum, maximum, penalty, keywords, nature='basica', parent=None, unit='meses', laws=None, observation=None):
    return {
        'id': id, 'nomeJuridico': name, 'aliases': [], 'classe': 'crime', 'jurisdicao': 'comum', 'modulo': 'Código Penal',
        'norma': 'Decreto-Lei nº 2.848/1940', 'dispositivo': device, 'naturezaFigura': nature, 'tipoPaiId': parent,
        'descricaoObjetiva': desc,
        'pena': {'minimoMeses': minimum, 'maximoMeses': maximum, 'unidadePrincipal': unit, 'descricao': penalty, 'multa': None},
        'vigencia': {'estado': 'vigente', 'inicioVigenciaRedacao': '1940-12-07', 'dataConsulta': CUTOFF, 'estadoConferencia': 'pendente', 'observacoes': observation or 'Figura patrimonial do Código Penal localizada no texto oficial; inventário e enriquecimento pendentes antes do cálculo.'},
        'fonteOficial': SOURCE, 'leiCriadoraOuModificadora': laws or ['Decreto-Lei nº 2.848/1940'], 'inventarioValidado': False,
        'enriquecimentoValidado': False, 'usavelNaCalculadora': False,
        'enriquecimento': {'bemJuridico': None, 'sujeitoAtivo': None, 'sujeitoPassivo': None, 'elementoSubjetivo': None, 'consumacao': None, 'tentativa': None, 'formaCulposa': None, 'acaoPenal': None, 'competencia': 'comum', 'procedimento': None, 'rito': None, 'hediondez': None, 'qualificadoras': [], 'majorantes': [], 'minorantes': [], 'agravantesAtenuantes': [], 'extincaoPunibilidade': [], 'jurisprudenciaQualificada': [], 'controversias': []},
        'palavrasChave': keywords,
    }
new = [
 make_record('cp-159','art. 159, caput','Extorsão mediante sequestro','Sequestrar pessoa com o fim de obter vantagem como condição ou preço do resgate.',96,180,'Reclusão, de 8 a 15 anos.',['extorsão mediante sequestro','resgate'],laws=['Decreto-Lei nº 2.848/1940','Lei nº 8.072/1990']),
 make_record('cp-159-1','art. 159, § 1º','Extorsão mediante sequestro qualificada por duração, vítima ou concurso','Se o sequestro dura mais de 24 horas, a vítima é menor de 18 ou maior de 60 anos, ou o crime é cometido em concurso.',144,240,'Reclusão, de 12 a 20 anos.',['sequestro','vítima vulnerável'],'qualificada','cp-159',laws=['Decreto-Lei nº 2.848/1940','Lei nº 8.072/1990','Lei nº 10.741/2003']),
 make_record('cp-159-2','art. 159, § 2º','Extorsão mediante sequestro com lesão grave','Se da extorsão mediante sequestro resulta lesão corporal de natureza grave.',192,288,'Reclusão, de 16 a 24 anos.',['sequestro','lesão grave'],'qualificada','cp-159',laws=['Decreto-Lei nº 2.848/1940','Lei nº 8.072/1990']),
 make_record('cp-159-3','art. 159, § 3º','Extorsão mediante sequestro com morte','Se da extorsão mediante sequestro resulta morte.',288,360,'Reclusão, de 24 a 30 anos.',['sequestro','morte'],'qualificada','cp-159',laws=['Decreto-Lei nº 2.848/1940','Lei nº 8.072/1990']),
 make_record('cp-160','art. 160','Extorsão indireta','Exigir ou receber, como garantia de dívida, abusando da situação de alguém, documento que possa dar causa a procedimento criminal contra a vítima ou terceiro.',12,36,'Reclusão, de 1 a 3 anos, e multa.',['extorsão indireta','garantia de dívida']),
 make_record('cp-161','art. 161','Alteração de limites','Suprimir ou deslocar tapume, marco ou outro sinal indicativo de linha divisória para apropriar-se de coisa imóvel alheia.',0.5,6,'Detenção, de 1 a 6 meses, e multa.',['alteração de limites','imóvel']),
 make_record('cp-162','art. 162','Supressão ou alteração de marca em animais','Suprimir ou alterar indevidamente, em gado ou rebanho alheio, marca ou sinal indicativo de propriedade.',6,36,'Detenção, de 6 meses a 3 anos, e multa.',['marca de animais','gado']),
 make_record('cp-163','art. 163','Dano','Destruir, inutilizar ou deteriorar coisa alheia.',1,6,'Detenção, de 1 a 6 meses, ou multa.',['dano','patrimônio']),
 make_record('cp-163-pu','art. 163, parágrafo único','Dano qualificado','Praticar dano com violência ou grave ameaça, substância inflamável ou explosiva, contra patrimônio público especificado em lei, ou por motivo egoístico ou com prejuízo considerável para a vítima.',6,36,'Detenção, de 6 meses a 3 anos, e multa, além da pena correspondente à violência.',['dano qualificado','patrimônio público'],'qualificada','cp-163'),
 make_record('cp-164','art. 164','Introdução ou abandono de animais em propriedade alheia','Introduzir ou deixar animais em propriedade alheia sem consentimento, desde que o fato resulte prejuízo.',0.5,6,'Detenção, de 15 dias a 6 meses, ou multa.',['animais','propriedade alheia']),
 make_record('cp-165','art. 165','Dano em coisa de valor artístico, arqueológico ou histórico','Destruir, inutilizar ou deteriorar coisa tombada por autoridade competente por seu valor artístico, arqueológico ou histórico.',6,24,'Detenção, de 6 meses a 2 anos, e multa.',['patrimônio histórico','dano']),
 make_record('cp-166','art. 166','Alteração de local especialmente protegido','Alterar, sem licença da autoridade competente, o aspecto de local especialmente protegido por lei.',1,12,'Detenção, de 1 mês a 1 ano, ou multa.',['local protegido','patrimônio cultural']),
 make_record('cp-168a','art. 168-A','Apropriação indébita previdenciária','Deixar de repassar à previdência social as contribuições recolhidas dos contribuintes no prazo e forma legal ou convencional.',24,60,'Reclusão, de 2 a 5 anos, e multa.',['previdência social','contribuição','apropriação indébita'],'omissiva',laws=['Decreto-Lei nº 2.848/1940','Lei nº 9.983/2000']),
 make_record('cp-169','art. 169','Apropriação de coisa havida por erro, caso fortuito ou força da natureza','Apropriar-se de coisa alheia vinda ao poder do agente por erro, caso fortuito ou força da natureza.',1,12,'Detenção, de 1 mês a 1 ano, ou multa.',['apropriação','erro','coisa achada']),
 make_record('cp-172','art. 172','Duplicata simulada','Emitir fatura, duplicata ou nota de venda que não corresponda à mercadoria vendida ou ao serviço prestado.',24,48,'Detenção, de 2 a 4 anos, e multa.',['duplicata simulada','fatura']),
 make_record('cp-173','art. 173','Abuso de incapazes','Abusar, em proveito próprio ou alheio, de necessidade, paixão, inexperiência, alienação ou debilidade mental de outrem, induzindo-o a ato de efeito jurídico prejudicial.',24,72,'Reclusão, de 2 a 6 anos, e multa.',['abuso de incapazes','fraude']),
 make_record('cp-174','art. 174','Induzimento à especulação','Abusar da inexperiência, simplicidade ou inferioridade mental de outrem, induzindo-o a jogo, aposta ou especulação ruinosa.',12,36,'Reclusão, de 1 a 3 anos, e multa.',['induzimento à especulação','jogo']),
 make_record('cp-175','art. 175','Fraude no comércio','Enganar, no exercício de atividade comercial, o adquirente ou consumidor vendendo mercadoria falsificada ou deteriorada ou entregando uma mercadoria por outra.',6,24,'Detenção, de 6 meses a 2 anos, ou multa.',['fraude no comércio','consumidor']),
 make_record('cp-175-1','art. 175, § 1º','Fraude no comércio qualificada','Alterar em obra encomendada a qualidade ou peso de metal, substituir pedra verdadeira ou vender como precioso metal de outra qualidade.',12,60,'Reclusão, de 1 a 5 anos, e multa.',['fraude no comércio','metais','pedras'],'qualificada','cp-175'),
 make_record('cp-176','art. 176','Outras fraudes','Tomar refeição em restaurante, alojar-se em hotel ou utilizar meio de transporte sem recursos para efetuar o pagamento.',0.5,2,'Detenção, de 15 dias a 2 meses, ou multa.',['outras fraudes','restaurante','hotel']),
 make_record('cp-177','art. 177','Fraudes e abusos na fundação ou administração de sociedade por ações','Promover a fundação de sociedade por ações com afirmação falsa ou ocultação fraudulenta de fato relativo à constituição da sociedade.',12,48,'Reclusão, de 1 a 4 anos, e multa, se o fato não constituir crime contra a economia popular.',['sociedade por ações','fraude societária']),
 make_record('cp-177-2','art. 177, § 2º','Negociação fraudulenta de voto societário','Acionista que, para obter vantagem, negocia o voto nas deliberações de assembleia geral.',6,24,'Detenção, de 6 meses a 2 anos, e multa.',['sociedade por ações','voto','fraude'],'qualificada','cp-177'),
 make_record('cp-178','art. 178','Emissão irregular de conhecimento de depósito ou warrant','Emitir conhecimento de depósito ou warrant em desacordo com disposição legal.',12,48,'Reclusão, de 1 a 4 anos, e multa.',['warrant','conhecimento de depósito']),
 make_record('cp-179','art. 179','Fraude à execução','Fraudar execução alienando, desviando, destruindo ou danificando bens, ou simulando dívidas.',6,24,'Detenção, de 6 meses a 2 anos, ou multa.',['fraude à execução','bens']),
 make_record('cp-180-1','art. 180, § 1º','Receptação qualificada','Adquirir, receber, transportar, conduzir, ocultar, ter em depósito, desmontar, montar, vender, expor à venda ou utilizar, em atividade comercial ou industrial, coisa que deve saber ser produto de crime.',36,96,'Reclusão, de 3 a 8 anos, e multa.',['receptação qualificada','atividade comercial'],'qualificada','cp-180',laws=['Decreto-Lei nº 2.848/1940','Lei nº 9.426/1996']),
 make_record('cp-180-3','art. 180, § 3º','Receptação culposa','Adquirir ou receber coisa que, por sua natureza, desproporção entre valor e preço ou condição de quem oferece, deve presumir-se obtida por meio criminoso.',1,12,'Detenção, de 1 mês a 1 ano, ou multa, ou ambas as penas.',['receptação culposa','coisa produto de crime'],'culposa','cp-180',laws=['Decreto-Lei nº 2.848/1940','Lei nº 9.426/1996']),
 make_record('cp-180a','art. 180-A','Receptação de animal','Adquirir, receber, transportar, conduzir, ocultar, ter em depósito ou vender animal que sabe ou deve saber ser produto de crime, com finalidade de produção ou comercialização.',36,96,'Reclusão, de 3 a 8 anos, e multa.',['receptação de animal','semovente'],laws=['Decreto-Lei nº 2.848/1940','Lei nº 13.330/2016','Lei nº 15.397/2026']),
]
for item in new:
    if item['id'] not in existing:
        catalog['registros'].append(item)
path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + '\n')
print(f'added {sum(item["id"] not in existing for item in new)} Código Penal property records')
