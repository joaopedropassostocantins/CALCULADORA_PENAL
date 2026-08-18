import json
from pathlib import Path

path = Path('/home/ubuntu/work/CALCULADORA_PENAL/src/data/tiposPenais.json')
catalog = json.loads(path.read_text())
existing = {record['id'] for record in catalog['registros']}
SOURCE = 'https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848.htm'
CUTOFF = catalog['dataCorte']

def make_record(id, device, name, desc, minimum, maximum, penalty, keywords, nature='basica', parent=None, laws=None):
    return {
        'id': id, 'nomeJuridico': name, 'aliases': [], 'classe': 'crime', 'jurisdicao': 'comum', 'modulo': 'Código Penal',
        'norma': 'Decreto-Lei nº 2.848/1940', 'dispositivo': device, 'naturezaFigura': nature, 'tipoPaiId': parent,
        'descricaoObjetiva': desc,
        'pena': {'minimoMeses': minimum, 'maximoMeses': maximum, 'unidadePrincipal': 'meses', 'descricao': penalty, 'multa': None},
        'vigencia': {'estado': 'vigente', 'inicioVigenciaRedacao': '1940-12-07', 'dataConsulta': CUTOFF, 'estadoConferencia': 'pendente', 'observacoes': 'Crime contra a Administração da Justiça localizado na fonte oficial; inventário e enriquecimento pendentes antes do cálculo.'},
        'fonteOficial': SOURCE, 'leiCriadoraOuModificadora': laws or ['Decreto-Lei nº 2.848/1940'], 'inventarioValidado': False,
        'enriquecimentoValidado': False, 'usavelNaCalculadora': False,
        'enriquecimento': {'bemJuridico': None, 'sujeitoAtivo': None, 'sujeitoPassivo': None, 'elementoSubjetivo': None, 'consumacao': None, 'tentativa': None, 'formaCulposa': None, 'acaoPenal': None, 'competencia': 'comum', 'procedimento': None, 'rito': None, 'hediondez': None, 'qualificadoras': [], 'majorantes': [], 'minorantes': [], 'agravantesAtenuantes': [], 'extincaoPunibilidade': [], 'jurisprudenciaQualificada': [], 'controversias': []},
        'palavrasChave': keywords,
    }
new = [
 make_record('cp-343','art. 343','Corrupção ativa de testemunha ou perito','Dar, oferecer ou prometer dinheiro ou vantagem a testemunha, perito, contador, tradutor ou intérprete para fazer afirmação falsa, negar ou calar a verdade.',36,48,'Reclusão, de 3 a 4 anos, e multa.',['corrupção de testemunha','perícia','processo'],laws=['Decreto-Lei nº 2.848/1940','Lei nº 10.268/2001']),
 make_record('cp-344','art. 344','Coação no curso do processo','Usar violência ou grave ameaça para favorecer interesse próprio ou alheio contra pessoa que funciona ou é chamada a intervir em processo.',12,48,'Reclusão, de 1 a 4 anos, e multa, além da pena correspondente à violência.',['coação processual','processo judicial'],laws=['Decreto-Lei nº 2.848/1940','Lei nº 14.245/2021']),
 make_record('cp-345','art. 345','Exercício arbitrário das próprias razões','Fazer justiça pelas próprias mãos para satisfazer pretensão, embora legítima, salvo quando a lei o permite.',0.5,1,'Detenção, de 15 dias a 1 mês, ou multa, além da pena correspondente à violência.',['justiça pelas próprias mãos','pretensão']),
 make_record('cp-346','art. 346','Subtração ou dano de coisa própria em poder de terceiro','Tirar, suprimir, destruir ou danificar coisa própria que se acha em poder de terceiro por determinação judicial ou convenção.',6,24,'Detenção, de 6 meses a 2 anos, e multa.',['coisa própria','determinação judicial']),
 make_record('cp-347','art. 347','Fraude processual','Inovar artificiosamente, na pendência de processo civil ou administrativo, o estado de lugar, coisa ou pessoa para induzir juiz ou perito a erro.',3,24,'Detenção, de 3 meses a 2 anos, e multa.',['fraude processual','processo']),
 make_record('cp-348','art. 348','Favorecimento pessoal','Auxiliar a subtrair-se à ação de autoridade pública autor de crime punido com reclusão.',1,6,'Detenção, de 1 a 6 meses, e multa.',['favorecimento pessoal','fuga']),
 make_record('cp-348-1','art. 348, § 1º','Favorecimento pessoal de crime sem reclusão','Auxiliar a subtrair-se à ação de autoridade pública autor de crime que não tenha pena de reclusão.',0.5,3,'Detenção, de 15 dias a 3 meses, e multa.',['favorecimento pessoal','crime sem reclusão'],'qualificada','cp-348'),
 make_record('cp-349','art. 349','Favorecimento real','Prestar a criminoso, fora dos casos de coautoria ou receptação, auxílio destinado a tornar seguro o proveito do crime.',1,6,'Detenção, de 1 a 6 meses, e multa.',['favorecimento real','proveito do crime']),
 make_record('cp-349a','art. 349-A','Entrada de aparelho de comunicação em estabelecimento prisional','Ingressar, promover, intermediar, auxiliar ou facilitar a entrada, sem autorização legal, de aparelho telefônico móvel, rádio ou similar em estabelecimento prisional.',3,12,'Detenção, de 3 meses a 1 ano.',['estabelecimento prisional','aparelho telefônico'],laws=['Decreto-Lei nº 2.848/1940','Lei nº 12.012/2009']),
]
for item in new:
    if item['id'] not in existing:
        catalog['registros'].append(item)
path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + '\n')
print(f'added {sum(item["id"] not in existing for item in new)} procedural justice records')
