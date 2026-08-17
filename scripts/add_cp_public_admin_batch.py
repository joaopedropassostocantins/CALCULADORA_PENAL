import json
from pathlib import Path

path = Path('/home/ubuntu/work/CALCULADORA_PENAL/src/data/tiposPenais.json')
catalog = json.loads(path.read_text())
existing = {record['id'] for record in catalog['registros']}
SOURCE = 'https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848.htm'
CUTOFF = catalog['dataCorte']

def make_record(id, device, name, desc, minimum, maximum, penalty, keywords, nature='basica', parent=None, laws=None, observation=None):
    return {
        'id': id, 'nomeJuridico': name, 'aliases': [], 'classe': 'crime', 'jurisdicao': 'comum', 'modulo': 'Código Penal',
        'norma': 'Decreto-Lei nº 2.848/1940', 'dispositivo': device, 'naturezaFigura': nature, 'tipoPaiId': parent,
        'descricaoObjetiva': desc,
        'pena': {'minimoMeses': minimum, 'maximoMeses': maximum, 'unidadePrincipal': 'meses', 'descricao': penalty, 'multa': None},
        'vigencia': {'estado': 'vigente', 'inicioVigenciaRedacao': '1940-12-07', 'dataConsulta': CUTOFF, 'estadoConferencia': 'pendente', 'observacoes': observation or 'Figura funcional do Código Penal localizada no texto oficial; inventário e enriquecimento pendentes antes do cálculo.'},
        'fonteOficial': SOURCE, 'leiCriadoraOuModificadora': laws or ['Decreto-Lei nº 2.848/1940'], 'inventarioValidado': False,
        'enriquecimentoValidado': False, 'usavelNaCalculadora': False,
        'enriquecimento': {'bemJuridico': None, 'sujeitoAtivo': 'funcionário público', 'sujeitoPassivo': None, 'elementoSubjetivo': None, 'consumacao': None, 'tentativa': None, 'formaCulposa': None, 'acaoPenal': None, 'competencia': 'comum', 'procedimento': None, 'rito': None, 'hediondez': None, 'qualificadoras': [], 'majorantes': [], 'minorantes': [], 'agravantesAtenuantes': [], 'extincaoPunibilidade': [], 'jurisprudenciaQualificada': [], 'controversias': []},
        'palavrasChave': keywords,
    }
new = [
 make_record('cp-311a','art. 311-A, caput','Fraudes em certames de interesse público','Utilizar ou divulgar indevidamente, com fim de beneficiar alguém ou comprometer a credibilidade do certame, conteúdo sigiloso de concurso, avaliação, exame ou processo seletivo previsto em lei.',12,48,'Reclusão, de 1 a 4 anos, e multa.',['fraude em concurso','certame público'],laws=['Decreto-Lei nº 2.848/1940','Lei nº 12.550/2011']),
 make_record('cp-311a-2','art. 311-A, § 2º','Fraude em certame com dano à Administração Pública','Se da ação ou omissão relativa a certame de interesse público resulta dano à Administração Pública.',24,72,'Reclusão, de 2 a 6 anos, e multa.',['fraude em concurso','dano à Administração Pública'],'qualificada','cp-311a',laws=['Decreto-Lei nº 2.848/1940','Lei nº 12.550/2011']),
 make_record('cp-312-2','art. 312, § 2º','Peculato culposo','Se o funcionário concorre culposamente para o crime de outrem.',3,12,'Detenção, de 3 meses a 1 ano.',['peculato culposo','funcionário público'],'culposa','cp-312'),
 make_record('cp-313','art. 313','Peculato mediante erro de outrem','Apropriar-se de dinheiro ou utilidade que, no exercício do cargo, recebeu por erro de outrem.',12,48,'Reclusão, de 1 a 4 anos, e multa.',['peculato mediante erro','funcionário público']),
 make_record('cp-313a','art. 313-A','Inserção de dados falsos em sistema de informações','Inserir ou facilitar a inserção de dados falsos, ou alterar ou excluir indevidamente dados corretos em sistemas informatizados ou bancos de dados da Administração Pública, para vantagem indevida ou dano.',24,144,'Reclusão, de 2 a 12 anos, e multa.',['dados falsos','sistema de informações','Administração Pública'],laws=['Decreto-Lei nº 2.848/1940','Lei nº 9.983/2000']),
 make_record('cp-313b','art. 313-B','Modificação ou alteração não autorizada de sistema de informações','Modificar ou alterar sistema de informações ou programa de informática sem autorização ou solicitação de autoridade competente.',3,24,'Detenção, de 3 meses a 2 anos, e multa.',['sistema de informações','alteração não autorizada'],laws=['Decreto-Lei nº 2.848/1940','Lei nº 9.983/2000']),
 make_record('cp-314','art. 314','Extravio, sonegação ou inutilização de livro ou documento','Extraviar, sonegar ou inutilizar, total ou parcialmente, livro oficial ou documento sob guarda em razão do cargo.',12,48,'Reclusão, de 1 a 4 anos, se o fato não constitui crime mais grave.',['documento público','extravio','sonegação']),
 make_record('cp-315','art. 315','Emprego irregular de verbas ou rendas públicas','Dar às verbas ou rendas públicas aplicação diversa da estabelecida em lei.',0.5,3,'Detenção, de 1 a 3 meses, ou multa.',['verba pública','emprego irregular']),
 make_record('cp-316-1','art. 316, § 1º','Excesso de exação','Exigir tributo ou contribuição social que sabe ou deveria saber indevido, ou empregar na cobrança meio vexatório ou gravoso não autorizado.',36,96,'Reclusão, de 3 a 8 anos, e multa.',['excesso de exação','tributo'],'qualificada','cp-316',laws=['Decreto-Lei nº 2.848/1940','Lei nº 8.137/1990']),
 make_record('cp-316-2','art. 316, § 2º','Desvio de excesso de exação','Desviar, em proveito próprio ou de outrem, o que recebeu indevidamente para recolher aos cofres públicos.',24,144,'Reclusão, de 2 a 12 anos, e multa.',['excesso de exação','desvio'],'qualificada','cp-316'),
 make_record('cp-317-2','art. 317, § 2º','Corrupção passiva privilegiada','Praticar, deixar de praticar ou retardar ato de ofício, com infração de dever funcional, cedendo a pedido ou influência de outrem.',0.5,12,'Detenção, de 3 meses a 1 ano, ou multa.',['corrupção passiva','influência'],'privilegiada','cp-317'),
 make_record('cp-318','art. 318','Facilitação de contrabando ou descaminho','Facilitar, com infração de dever funcional, a prática de contrabando ou descaminho.',36,96,'Reclusão, de 3 a 8 anos, e multa.',['contrabando','descaminho','funcionário público'],laws=['Decreto-Lei nº 2.848/1940','Lei nº 8.137/1990']),
 make_record('cp-319','art. 319','Prevaricação','Retardar ou deixar de praticar indevidamente ato de ofício, ou praticá-lo contra disposição expressa de lei, para satisfazer interesse ou sentimento pessoal.',3,12,'Detenção, de 3 meses a 1 ano, e multa.',['prevaricação','ato de ofício']),
 make_record('cp-319a','art. 319-A','Omissão na vedação de acesso a aparelho de comunicação por preso','Deixar diretor de penitenciária ou agente público de cumprir o dever de vedar ao preso acesso a aparelho telefônico, rádio ou similar que permita comunicação.',3,12,'Detenção, de 3 meses a 1 ano.',['presídio','aparelho telefônico','omissão'],'omissiva',laws=['Decreto-Lei nº 2.848/1940','Lei nº 11.466/2007']),
 make_record('cp-320','art. 320','Condescendência criminosa','Deixar o funcionário, por indulgência, de responsabilizar subordinado que cometeu infração no exercício do cargo ou de comunicar o fato à autoridade competente.',0.5,1,'Detenção, de 15 dias a 1 mês, ou multa.',['condescendência criminosa','subordinado']),
 make_record('cp-321','art. 321','Advocacia administrativa','Patrocinar, direta ou indiretamente, interesse privado perante a Administração Pública valendo-se da qualidade de funcionário.',1,3,'Detenção, de 1 a 3 meses, ou multa.',['advocacia administrativa','interesse privado']),
 make_record('cp-321-pu','art. 321, parágrafo único','Advocacia administrativa com interesse ilegítimo','Se o interesse patrocinado perante a Administração Pública é ilegítimo.',3,12,'Detenção, de 3 meses a 1 ano, além da multa.',['advocacia administrativa','interesse ilegítimo'],'qualificada','cp-321'),
 make_record('cp-322','art. 322','Violência arbitrária','Praticar violência no exercício de função ou a pretexto de exercê-la.',6,36,'Detenção, de 6 meses a 3 anos, além da pena correspondente à violência.',['violência arbitrária','função pública']),
 make_record('cp-323','art. 323','Abandono de função','Abandonar cargo público fora dos casos permitidos em lei.',0.5,1,'Detenção, de 15 dias a 1 mês, ou multa.',['abandono de função','cargo público']),
 make_record('cp-323-1','art. 323, § 1º','Abandono de função com prejuízo público','Se do abandono de função resulta prejuízo público.',3,12,'Detenção, de 3 meses a 1 ano, e multa.',['abandono de função','prejuízo público'],'qualificada','cp-323'),
 make_record('cp-323-2','art. 323, § 2º','Abandono de função em faixa de fronteira','Se o abandono de função ocorre em lugar compreendido na faixa de fronteira.',12,36,'Detenção, de 1 a 3 anos, e multa.',['abandono de função','faixa de fronteira'],'qualificada','cp-323'),
 make_record('cp-324','art. 324','Exercício funcional ilegalmente antecipado ou prolongado','Entrar no exercício de função pública antes das exigências legais ou continuar a exercê-la sem autorização após exoneração, remoção, substituição ou suspensão.',0.5,1,'Detenção, de 15 dias a 1 mês, ou multa.',['função pública','exercício ilegal']),
 make_record('cp-325','art. 325','Violação de sigilo funcional','Revelar fato conhecido em razão do cargo que deva permanecer em segredo ou facilitar sua revelação, se o fato não constitui crime mais grave.',6,24,'Detenção, de 6 meses a 2 anos, ou multa.',['sigilo funcional','funcionário público']),
 make_record('cp-325-2','art. 325, § 2º','Violação de sigilo funcional com dano','Se da ação ou omissão de violação de sigilo funcional resulta dano à Administração Pública ou a outrem.',24,72,'Reclusão, de 2 a 6 anos, e multa.',['sigilo funcional','dano'],'qualificada','cp-325',laws=['Decreto-Lei nº 2.848/1940','Lei nº 9.983/2000']),
 make_record('cp-326','art. 326','Violação do sigilo de proposta de concorrência','Devassar o sigilo de proposta de concorrência pública ou proporcionar a terceiro o ensejo de devassá-lo.',3,12,'Detenção, de 3 meses a 1 ano, e multa.',['concorrência pública','sigilo de proposta']),
]
for item in new:
    if item['id'] not in existing:
        catalog['registros'].append(item)
path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + '\n')
print(f'added {sum(item["id"] not in existing for item in new)} Código Penal public-administration records')
