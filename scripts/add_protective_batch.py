import json
from pathlib import Path

path = Path('/home/ubuntu/work/CALCULADORA_PENAL/src/data/tiposPenais.json')
catalog = json.loads(path.read_text())
existing = {record['id'] for record in catalog['registros']}
ELDER = 'https://www.planalto.gov.br/ccivil_03/leis/2003/l10.741compilado.htm'
DISABILITY = 'https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13146.htm'
TRANSPLANT = 'https://www.planalto.gov.br/ccivil_03/leis/l9434.htm'
CUT_OFF = catalog['dataCorte']

def make_record(id, name, device, description, minimum, maximum, penalty, law, source, start, module, keywords, nature='basica', parent=None, multa=None, note=None):
    return {
        'id': id, 'nomeJuridico': name, 'aliases': [], 'classe': 'crime', 'jurisdicao': 'comum', 'modulo': module,
        'norma': law, 'dispositivo': device, 'naturezaFigura': nature, 'tipoPaiId': parent,
        'descricaoObjetiva': description,
        'pena': {'minimoMeses': minimum, 'maximoMeses': maximum, 'unidadePrincipal': 'dias-multa' if multa else 'meses', 'descricao': penalty, 'multa': multa},
        'vigencia': {'estado': 'vigente', 'inicioVigenciaRedacao': start, 'dataConsulta': CUT_OFF, 'estadoConferencia': 'confirmada', 'observacoes': note},
        'fonteOficial': source, 'leiCriadoraOuModificadora': [law], 'inventarioValidado': True,
        'enriquecimentoValidado': False, 'usavelNaCalculadora': True,
        'enriquecimento': {'bemJuridico': None, 'sujeitoAtivo': None, 'sujeitoPassivo': None, 'elementoSubjetivo': None, 'consumacao': None, 'tentativa': None, 'formaCulposa': None, 'acaoPenal': None, 'competencia': None, 'procedimento': None, 'rito': None, 'hediondez': None, 'qualificadoras': [], 'majorantes': [], 'minorantes': [], 'agravantesAtenuantes': [], 'extincaoPunibilidade': [], 'jurisprudenciaQualificada': [], 'controversias': []},
        'palavrasChave': keywords,
    }

new = []
# Estatuto da Pessoa Idosa — arts. 96 a 108
elder = [
 ('96','Discriminação contra pessoa idosa','Discriminar pessoa idosa, impedindo ou dificultando acesso a operações bancárias, transporte, contratação ou instrumento necessário à cidadania por motivo de idade.',6,12,'Reclusão, de 6 meses a 1 ano, e multa.',['pessoa idosa','discriminação','idade']),
 ('97','Omissão de assistência à pessoa idosa','Deixar de prestar assistência à pessoa idosa em iminente perigo ou recusar, retardar ou dificultar assistência à saúde sem justa causa.',6,12,'Detenção, de 6 meses a 1 ano, e multa.',['pessoa idosa','omissão de socorro','assistência à saúde']),
 ('98','Abandono de pessoa idosa','Abandonar pessoa idosa em hospital, casa de saúde, entidade de longa permanência ou congênere, ou não prover suas necessidades básicas quando obrigado.',6,36,'Detenção, de 6 meses a 3 anos, e multa.',['pessoa idosa','abandono','necessidades básicas']),
 ('99','Exposição da pessoa idosa a perigo','Expor a perigo a integridade ou a saúde física ou psíquica da pessoa idosa por condições desumanas, privação de alimentos ou cuidados ou trabalho excessivo.',24,60,'Reclusão, de 2 a 5 anos.',['pessoa idosa','maus-tratos','condições degradantes']),
 ('99-1','Exposição da pessoa idosa a perigo com lesão grave','Praticar o crime do art. 99 com resultado de lesão corporal de natureza grave.',36,84,'Reclusão, de 3 a 7 anos.',['pessoa idosa','lesão grave','maus-tratos']),
 ('99-2','Exposição da pessoa idosa a perigo com morte','Praticar o crime do art. 99 com resultado morte.',96,168,'Reclusão, de 8 a 14 anos.',['pessoa idosa','morte','maus-tratos']),
 ('100','Crimes funcionais contra direitos da pessoa idosa','Obstar acesso a cargo público, negar emprego, dificultar assistência à saúde ou frustrar ordem judicial ou dados técnicos por motivo ou em prejuízo de pessoa idosa.',6,12,'Reclusão, de 6 meses a 1 ano, e multa.',['pessoa idosa','cargo público','assistência']),
 ('101','Descumprimento de ordem judicial em favor de pessoa idosa','Deixar de cumprir, retardar ou frustrar sem justo motivo ordem judicial em ação em que pessoa idosa seja parte ou interveniente.',6,12,'Detenção, de 6 meses a 1 ano, e multa.',['pessoa idosa','ordem judicial']),
 ('102','Apropriação de bens ou rendimentos de pessoa idosa','Apropriar-se ou desviar bens, proventos, pensão ou rendimento da pessoa idosa, dando-lhes aplicação diversa da finalidade.',12,48,'Reclusão, de 1 a 4 anos, e multa.',['pessoa idosa','apropriação','pensão']),
 ('103','Negativa de acolhimento por procuração','Negar acolhimento ou permanência de pessoa idosa por recusa em outorgar procuração à entidade de atendimento.',6,12,'Detenção, de 6 meses a 1 ano, e multa.',['pessoa idosa','entidade de atendimento','procuração']),
 ('104','Retenção de cartão ou documento de pessoa idosa','Reter cartão magnético de conta de benefício, provento ou pensão ou documento para assegurar recebimento ou ressarcimento de dívida.',6,24,'Detenção, de 6 meses a 2 anos, e multa.',['pessoa idosa','cartão bancário','dívida']),
 ('105','Exibição de informação depreciativa sobre pessoa idosa','Exibir ou veicular informação ou imagem depreciativa ou injuriosa à pessoa idosa.',12,36,'Detenção, de 1 a 3 anos, e multa.',['pessoa idosa','imagem depreciativa','injúria']),
 ('106','Indução de pessoa idosa sem discernimento a outorgar procuração','Induzir pessoa idosa sem discernimento a outorgar procuração para administrar bens ou deles dispor.',24,48,'Reclusão, de 2 a 4 anos.',['pessoa idosa','procuração','discernimento']),
 ('107','Coação de pessoa idosa para ato patrimonial','Coagir pessoa idosa a doar, contratar, testar ou outorgar procuração.',24,60,'Reclusão, de 2 a 5 anos.',['pessoa idosa','coação','doação','testamento']),
 ('108','Ato notarial sem representação legal de pessoa idosa','Lavrar ato notarial envolvendo pessoa idosa sem discernimento sem a devida representação legal.',24,48,'Reclusão, de 2 a 4 anos.',['pessoa idosa','ato notarial','representação legal']),
]
for num,name,desc,minimum,maximum,penalty,keywords in elder:
    new.append(make_record(f'idosa-10741-{num}', name, f'art. {num.replace("-", ", § ")}' if '-' in num else f'art. {num}', desc, minimum, maximum, penalty, 'Lei nº 10.741/2003', ELDER, '2025-06-12' if num.startswith('99') else '2003-10-03', 'Estatuto da Pessoa Idosa', keywords, 'qualificada' if num in ('99-1','99-2') else 'basica', 'idosa-10741-99' if num in ('99-1','99-2') else None))
# Lei Brasileira de Inclusão — arts. 88 a 91
new += [
 make_record('lbi-88','Discriminação contra pessoa com deficiência','art. 88','Praticar, induzir ou incitar discriminação de pessoa em razão de sua deficiência.',12,36,'Reclusão, de 1 a 3 anos, e multa.','Lei nº 13.146/2015',DISABILITY,'2016-01-03','Pessoa com deficiência',['deficiência','discriminação']),
 make_record('lbi-88-2','Discriminação contra pessoa com deficiência por meio de comunicação','art. 88, § 2º','Praticar, induzir ou incitar discriminação de pessoa com deficiência por meio de comunicação social ou publicação.',24,60,'Reclusão, de 2 a 5 anos, e multa.','Lei nº 13.146/2015',DISABILITY,'2016-01-03','Pessoa com deficiência',['deficiência','discriminação','comunicação'],'qualificada','lbi-88'),
 make_record('lbi-89','Apropriação de rendimentos de pessoa com deficiência','art. 89','Apropriar-se ou desviar bens, proventos, pensão, benefícios, remuneração ou rendimento de pessoa com deficiência.',12,48,'Reclusão, de 1 a 4 anos, e multa.','Lei nº 13.146/2015',DISABILITY,'2016-01-03','Pessoa com deficiência',['deficiência','apropriação','benefício']),
 make_record('lbi-90','Abandono de pessoa com deficiência','art. 90','Abandonar pessoa com deficiência em hospital, casa de saúde, entidade de abrigamento ou congênere, ou deixar de prover suas necessidades básicas quando obrigado.',24,60,'Reclusão, de 2 a 5 anos, e multa.','Lei nº 13.146/2015',DISABILITY,'2025-06-12','Pessoa com deficiência',['deficiência','abandono','necessidades básicas'],note='Redação vigente consultada com alteração da Lei nº 15.163/2025.'),
 make_record('lbi-91','Retenção de cartão ou documento de pessoa com deficiência','art. 91','Reter ou utilizar cartão magnético, meio eletrônico ou documento de pessoa com deficiência destinado a benefício, remuneração ou operação financeira para obter vantagem indevida.',6,24,'Detenção, de 6 meses a 2 anos, e multa.','Lei nº 13.146/2015',DISABILITY,'2016-01-03','Pessoa com deficiência',['deficiência','cartão bancário','vantagem indevida']),
]
# Lei de Transplantes — arts. 14 a 20
new += [
 make_record('transplante-14','Remoção irregular de tecidos ou órgãos','art. 14','Remover tecidos, órgãos ou partes do corpo de pessoa ou cadáver em desacordo com a Lei de Transplantes.',24,72,'Reclusão, de 2 a 6 anos, e multa de 100 a 360 dias-multa.','Lei nº 9.434/1997',TRANSPLANT,'1997-02-05','Transplantes',['órgãos','tecidos','remoção irregular']),
 make_record('transplante-14-1','Remoção de tecidos ou órgãos mediante paga ou motivo torpe','art. 14, § 1º','Praticar remoção irregular mediante paga, promessa de recompensa ou outro motivo torpe.',36,96,'Reclusão, de 3 a 8 anos, e multa de 100 a 150 dias-multa.','Lei nº 9.434/1997',TRANSPLANT,'1997-02-05','Transplantes',['órgãos','paga','motivo torpe'],'qualificada','transplante-14'),
 make_record('transplante-14-2','Remoção irregular com lesão grave','art. 14, § 2º','Praticar remoção em pessoa viva com incapacidade superior a 30 dias, perigo de vida, debilidade permanente ou aceleração de parto.',36,120,'Reclusão, de 3 a 10 anos, e multa de 100 a 200 dias-multa.','Lei nº 9.434/1997',TRANSPLANT,'1997-02-05','Transplantes',['órgãos','lesão grave','pessoa viva'],'qualificada','transplante-14'),
 make_record('transplante-14-3','Remoção irregular com lesão gravíssima','art. 14, § 3º','Praticar remoção em pessoa viva com incapacidade para o trabalho, enfermidade incurável, perda de membro, deformidade permanente ou aborto.',48,144,'Reclusão, de 4 a 12 anos, e multa de 150 a 300 dias-multa.','Lei nº 9.434/1997',TRANSPLANT,'1997-02-05','Transplantes',['órgãos','lesão gravíssima','pessoa viva'],'qualificada','transplante-14'),
 make_record('transplante-14-4','Remoção irregular com morte','art. 14, § 4º','Praticar remoção em pessoa viva com resultado morte.',96,240,'Reclusão, de 8 a 20 anos, e multa de 200 a 360 dias-multa.','Lei nº 9.434/1997',TRANSPLANT,'1997-02-05','Transplantes',['órgãos','morte','pessoa viva'],'qualificada','transplante-14'),
 make_record('transplante-15','Compra ou venda de tecidos ou órgãos','art. 15','Comprar ou vender tecidos, órgãos ou partes do corpo humano, inclusive promover, intermediar, facilitar ou obter vantagem com a transação.',36,96,'Reclusão, de 3 a 8 anos, e multa de 200 a 360 dias-multa.','Lei nº 9.434/1997',TRANSPLANT,'1997-02-05','Transplantes',['órgãos','compra e venda','tráfico']),
 make_record('transplante-16','Transplante com material obtido ilicitamente','art. 16','Realizar transplante ou enxerto utilizando tecidos, órgãos ou partes do corpo obtidos em desacordo com a Lei.',12,72,'Reclusão, de 1 a 6 anos, e multa de 150 a 300 dias-multa.','Lei nº 9.434/1997',TRANSPLANT,'1997-02-05','Transplantes',['órgãos','transplante','material ilícito']),
 make_record('transplante-17','Transporte ou distribuição de material ilícito','art. 17','Recolher, transportar, guardar ou distribuir partes do corpo humano sabendo que foram obtidas em desacordo com a Lei.',6,24,'Reclusão, de 6 meses a 2 anos, e multa de 100 a 250 dias-multa.','Lei nº 9.434/1997',TRANSPLANT,'1997-02-05','Transplantes',['órgãos','transporte','distribuição']),
 make_record('transplante-18','Transplante em desacordo com consentimento','art. 18','Realizar transplante ou enxerto em desacordo com o consentimento do receptor e as regras legais.',6,24,'Detenção, de 6 meses a 2 anos.','Lei nº 9.434/1997',TRANSPLANT,'1997-02-05','Transplantes',['órgãos','consentimento','transplante']),
 make_record('transplante-19','Não recomposição de cadáver','art. 19','Deixar de recompor cadáver, devolvendo-lhe aspecto condigno, ou deixar de entregá-lo ou retardar sua entrega aos familiares ou interessados.',6,24,'Detenção, de 6 meses a 2 anos.','Lei nº 9.434/1997',TRANSPLANT,'1997-02-05','Transplantes',['cadáver','sepultamento','órgãos']),
 make_record('transplante-20','Anúncio ou apelo público irregular sobre transplante','art. 20','Publicar anúncio ou apelo público em desacordo com as regras legais sobre transplante.',None,None,'Multa de 100 a 200 dias-multa.','Lei nº 9.434/1997',TRANSPLANT,'1997-02-05','Transplantes',['órgãos','anúncio','apelo público'],multa={'minimoDias':100,'maximoDias':200}),
]
for item in new:
    if item['id'] not in existing:
        catalog['registros'].append(item)
path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + '\n')
print(f'added {sum(item["id"] not in existing for item in new)} records')
