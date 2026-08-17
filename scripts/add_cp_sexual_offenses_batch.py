import json
from pathlib import Path

path = Path('/home/ubuntu/work/CALCULADORA_PENAL/src/data/tiposPenais.json')
catalog = json.loads(path.read_text())
existing = {record['id'] for record in catalog['registros']}
SOURCE = 'https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848.htm'
CUTOFF = catalog['dataCorte']

def make_record(id, device, name, desc, minimum, maximum, penalty, keywords, laws):
    return {
        'id': id, 'nomeJuridico': name, 'aliases': [], 'classe': 'crime', 'jurisdicao': 'comum', 'modulo': 'Código Penal',
        'norma': 'Decreto-Lei nº 2.848/1940', 'dispositivo': device, 'naturezaFigura': 'basica', 'tipoPaiId': None,
        'descricaoObjetiva': desc,
        'pena': {'minimoMeses': minimum, 'maximoMeses': maximum, 'unidadePrincipal': 'meses', 'descricao': penalty, 'multa': None},
        'vigencia': {'estado': 'vigente', 'inicioVigenciaRedacao': '1940-12-07', 'dataConsulta': CUTOFF, 'estadoConferencia': 'pendente', 'observacoes': 'Tipo sexual autônomo do Código Penal localizado na fonte oficial; inventário e enriquecimento pendentes antes do cálculo.'},
        'fonteOficial': SOURCE, 'leiCriadoraOuModificadora': laws, 'inventarioValidado': False,
        'enriquecimentoValidado': False, 'usavelNaCalculadora': False,
        'enriquecimento': {'bemJuridico': None, 'sujeitoAtivo': None, 'sujeitoPassivo': None, 'elementoSubjetivo': None, 'consumacao': None, 'tentativa': None, 'formaCulposa': None, 'acaoPenal': None, 'competencia': 'comum', 'procedimento': None, 'rito': None, 'hediondez': None, 'qualificadoras': [], 'majorantes': [], 'minorantes': [], 'agravantesAtenuantes': [], 'extincaoPunibilidade': [], 'jurisprudenciaQualificada': [], 'controversias': []},
        'palavrasChave': keywords,
    }
new = [
 make_record('cp-215','art. 215','Violação sexual mediante fraude','Ter conjunção carnal ou praticar outro ato libidinoso com alguém mediante fraude ou outro meio que impeça ou dificulte a livre manifestação de vontade da vítima.',24,72,'Reclusão, de 2 a 6 anos.',['violação sexual','fraude','ato libidinoso'],['Decreto-Lei nº 2.848/1940','Lei nº 12.015/2009']),
 make_record('cp-215a','art. 215-A','Importunação sexual','Praticar contra alguém e sem sua anuência ato libidinoso com objetivo de satisfazer a própria lascívia ou a de terceiro.',12,60,'Reclusão, de 1 a 5 anos, se o ato não constitui crime mais grave.',['importunação sexual','ato libidinoso'],['Decreto-Lei nº 2.848/1940','Lei nº 13.718/2018']),
 make_record('cp-216a','art. 216-A','Assédio sexual','Constranger alguém com intuito de obter vantagem ou favorecimento sexual, prevalecendo-se de condição de superior hierárquico ou ascendência inerente a emprego, cargo ou função.',1,24,'Detenção, de 1 a 2 anos.',['assédio sexual','superior hierárquico'],['Decreto-Lei nº 2.848/1940','Lei nº 10.224/2001']),
 make_record('cp-216b','art. 216-B','Registro não autorizado da intimidade sexual','Produzir, fotografar, filmar ou registrar conteúdo com cena de nudez ou ato sexual ou libidinoso íntimo e privado sem autorização dos participantes.',0.5,12,'Detenção, de 6 meses a 1 ano, e multa.',['intimidade sexual','nudez','registro não autorizado'],['Decreto-Lei nº 2.848/1940','Lei nº 13.772/2018']),
 make_record('cp-218','art. 218','Induzimento à satisfação da lascívia de outrem','Induzir alguém menor de 14 anos a satisfazer a lascívia de outrem.',72,168,'Reclusão, de 6 a 14 anos, e multa.',['lascívia','menor de 14 anos'],['Decreto-Lei nº 2.848/1940','Lei nº 12.015/2009','Lei nº 15.280/2025']),
 make_record('cp-218a','art. 218-A','Satisfação de lascívia mediante presença de criança ou adolescente','Praticar na presença de menor de 14 anos, ou induzi-lo a presenciar, conjunção carnal ou outro ato libidinoso para satisfazer lascívia própria ou alheia.',60,144,'Reclusão, de 5 a 12 anos, e multa.',['lascívia','criança','presença'],['Decreto-Lei nº 2.848/1940','Lei nº 12.015/2009','Lei nº 15.280/2025']),
 make_record('cp-218b','art. 218-B','Favorecimento da exploração sexual de vulnerável','Submeter, induzir ou atrair à prostituição ou outra forma de exploração sexual pessoa menor de 18 anos ou sem discernimento necessário, facilitar a exploração ou impedir que a abandone.',84,192,'Reclusão, de 7 a 16 anos, e multa.',['exploração sexual','vulnerável','prostituição'],['Decreto-Lei nº 2.848/1940','Lei nº 12.015/2009','Lei nº 12.978/2014','Lei nº 15.280/2025']),
 make_record('cp-218c','art. 218-C','Divulgação de cena de estupro, sexo, nudez ou pornografia','Oferecer, disponibilizar, transmitir, vender, distribuir, publicar ou divulgar registro audiovisual de estupro, apologia ou indução à sua prática, ou cena de sexo, nudez ou pornografia sem consentimento da vítima.',48,120,'Reclusão, de 4 a 10 anos, e multa, se o fato não constitui crime mais grave.',['divulgação de cena','pornografia','nudez','estupro'],['Decreto-Lei nº 2.848/1940','Lei nº 13.718/2018','Lei nº 15.280/2025']),
]
for item in new:
    if item['id'] not in existing:
        catalog['registros'].append(item)
path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + '\n')
print(f'added {sum(item["id"] not in existing for item in new)} sexual offenses')
