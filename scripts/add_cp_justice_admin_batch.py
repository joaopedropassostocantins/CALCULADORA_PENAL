import json
from pathlib import Path

path = Path('/home/ubuntu/work/CALCULADORA_PENAL/src/data/tiposPenais.json')
catalog = json.loads(path.read_text())
existing = {record['id'] for record in catalog['registros']}
SOURCE = 'https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848.htm'
CUTOFF = catalog['dataCorte']

def make_record(id, device, name, desc, minimum, maximum, penalty, keywords, laws=None, observation=None):
    return {
        'id': id, 'nomeJuridico': name, 'aliases': [], 'classe': 'crime', 'jurisdicao': 'comum', 'modulo': 'Código Penal',
        'norma': 'Decreto-Lei nº 2.848/1940', 'dispositivo': device, 'naturezaFigura': 'basica', 'tipoPaiId': None,
        'descricaoObjetiva': desc,
        'pena': {'minimoMeses': minimum, 'maximoMeses': maximum, 'unidadePrincipal': 'meses', 'descricao': penalty, 'multa': None},
        'vigencia': {'estado': 'vigente', 'inicioVigenciaRedacao': '1940-12-07', 'dataConsulta': CUTOFF, 'estadoConferencia': 'pendente', 'observacoes': observation or 'Crime contra a Administração da Justiça localizado na fonte oficial; inventário e enriquecimento pendentes antes do cálculo.'},
        'fonteOficial': SOURCE, 'leiCriadoraOuModificadora': laws or ['Decreto-Lei nº 2.848/1940'], 'inventarioValidado': False,
        'enriquecimentoValidado': False, 'usavelNaCalculadora': False,
        'enriquecimento': {'bemJuridico': None, 'sujeitoAtivo': None, 'sujeitoPassivo': None, 'elementoSubjetivo': None, 'consumacao': None, 'tentativa': None, 'formaCulposa': None, 'acaoPenal': None, 'competencia': 'comum', 'procedimento': None, 'rito': None, 'hediondez': None, 'qualificadoras': [], 'majorantes': [], 'minorantes': [], 'agravantesAtenuantes': [], 'extincaoPunibilidade': [], 'jurisprudenciaQualificada': [], 'controversias': []},
        'palavrasChave': keywords,
    }
new = [
 make_record('cp-338','art. 338','Reingresso de estrangeiro expulso','Reingressar no território nacional o estrangeiro que dele foi expulso.',12,48,'Reclusão, de 1 a 4 anos, sem prejuízo de nova expulsão após o cumprimento da pena.',['reingresso','estrangeiro','expulsão']),
 make_record('cp-338a','art. 338-A','Descumprimento de medidas protetivas de urgência','Descumprir decisão judicial que defere medidas protetivas de urgência.',24,60,'Reclusão, de 2 a 5 anos, e multa.',['medida protetiva','descumprimento'],laws=['Decreto-Lei nº 2.848/1940','Lei nº 15.280/2025'],observation='Tipo autônomo do Código Penal, distinto do art. 24-A da Lei nº 11.340/2006; a fonte oficial mantém ambos os dispositivos em diplomas diferentes.'),
 make_record('cp-339','art. 339','Denunciação caluniosa','Dar causa à instauração de inquérito, procedimento investigatório, processo ou procedimento administrativo ou judicial contra alguém, imputando-lhe crime, infração ético-disciplinar ou ato ímprobo de que o sabe inocente.',24,96,'Reclusão, de 2 a 8 anos, e multa.',['denunciação caluniosa','inocente'],laws=['Decreto-Lei nº 2.848/1940','Lei nº 14.110/2020']),
 make_record('cp-340','art. 340','Comunicação falsa de crime ou contravenção','Provocar a ação de autoridade comunicando ocorrência de crime ou contravenção que sabe não ter ocorrido.',1,6,'Detenção, de 1 a 6 meses, ou multa.',['comunicação falsa','crime inexistente']),
 make_record('cp-341','art. 341','Autoacusação falsa','Acusar-se perante a autoridade de crime inexistente ou praticado por outrem.',3,24,'Detenção, de 3 meses a 2 anos, ou multa.',['autoacusação','crime inexistente']),
 make_record('cp-342','art. 342','Falso testemunho ou falsa perícia','Fazer afirmação falsa, negar ou calar a verdade como testemunha, perito, contador, tradutor ou intérprete em processo ou juízo arbitral.',24,48,'Reclusão, de 2 a 4 anos, e multa.',['falso testemunho','falsa perícia','processo'],laws=['Decreto-Lei nº 2.848/1940','Lei nº 12.850/2013']),
]
for item in new:
    if item['id'] not in existing:
        catalog['registros'].append(item)
path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + '\n')
print(f'added {sum(item["id"] not in existing for item in new)} justice administration records')
