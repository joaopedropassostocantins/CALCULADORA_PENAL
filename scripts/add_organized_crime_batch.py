import json
from pathlib import Path

path = Path('/home/ubuntu/work/CALCULADORA_PENAL/src/data/tiposPenais.json')
catalog = json.loads(path.read_text())
existing = {record['id'] for record in catalog['registros']}
SOURCE = 'https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2013/lei/l12850.htm'
CUT_OFF = catalog['dataCorte']

def make_record(id, name, device, desc, minimum, maximum, penalty, keywords, note=None):
    return {
        'id': id, 'nomeJuridico': name, 'aliases': [], 'classe': 'crime', 'jurisdicao': 'comum', 'modulo': 'Organização criminosa',
        'norma': 'Lei nº 12.850/2013', 'dispositivo': device, 'naturezaFigura': 'basica', 'tipoPaiId': None,
        'descricaoObjetiva': desc,
        'pena': {'minimoMeses': minimum, 'maximoMeses': maximum, 'unidadePrincipal': 'meses', 'descricao': penalty, 'multa': None},
        'vigencia': {'estado': 'vigente', 'inicioVigenciaRedacao': None, 'dataConsulta': CUT_OFF, 'estadoConferencia': 'pendente', 'observacoes': note or 'Infração penal correlata localizada em fonte oficial compilada; cálculo bloqueado até reconferência das alterações legislativas recentes e do enriquecimento jurídico.'},
        'fonteOficial': SOURCE, 'leiCriadoraOuModificadora': ['Lei nº 12.850/2013'], 'inventarioValidado': False,
        'enriquecimentoValidado': False, 'usavelNaCalculadora': False,
        'enriquecimento': {'bemJuridico': None, 'sujeitoAtivo': None, 'sujeitoPassivo': None, 'elementoSubjetivo': None, 'consumacao': None, 'tentativa': None, 'formaCulposa': None, 'acaoPenal': None, 'competencia': None, 'procedimento': None, 'rito': None, 'hediondez': None, 'qualificadoras': [], 'majorantes': [], 'minorantes': [], 'agravantesAtenuantes': [], 'extincaoPunibilidade': [], 'jurisprudenciaQualificada': [], 'controversias': []},
        'palavrasChave': keywords,
    }

new = [
 make_record('orgcrime-12850-18','Revelação indevida da identidade de colaborador','art. 18','Revelar a identidade, fotografar ou filmar colaborador sem prévia autorização por escrito.',12,36,'Reclusão, de 1 a 3 anos, e multa.',['colaborador','identidade','sigilo']),
 make_record('orgcrime-12850-19','Imputação falsa em colaboração com a Justiça','art. 19','Imputar falsamente infração penal a pessoa inocente sob pretexto de colaboração ou revelar informação inverídica sobre estrutura de organização criminosa.',12,48,'Reclusão, de 1 a 4 anos, e multa.',['colaboração','imputação falsa','organização criminosa']),
 make_record('orgcrime-12850-20','Violação de sigilo de investigação de organização criminosa','art. 20','Descumprir determinação de sigilo de investigação que envolva ação controlada ou infiltração de agentes.',12,48,'Reclusão, de 1 a 4 anos, e multa.',['sigilo','ação controlada','infiltração']),
 make_record('orgcrime-12850-21','Omissão ou uso indevido de dados requisitados','art. 21','Recusar ou omitir dados cadastrais, registros, documentos ou informações requisitados no curso de investigação ou processo, ou apropriar-se, divulgar ou usar indevidamente esses dados.',6,24,'Reclusão, de 6 meses a 2 anos, e multa.',['dados cadastrais','investigação','sigilo']),
 make_record('orgcrime-12850-21a','Obstrução de ações contra o crime organizado','art. 21-A','Solicitar ou ordenar violência ou grave ameaça contra agente público, advogado, defensor, jurado, testemunha, colaborador ou perito para impedir, embaraçar ou retaliar processo ou investigação de crime organizado.',48,144,'Reclusão, de 4 a 12 anos, e multa.',['obstrução','violência','crime organizado'],'Incluído pela Lei nº 15.245/2025; requer conferência temporal específica.'),
 make_record('orgcrime-12850-21b','Ajuste para violência contra agente ou colaborador','art. 21-B','Ajustarem-se duas ou mais pessoas para praticar violência ou grave ameaça contra pessoas protegidas com finalidade de impedir, embaraçar ou retaliar processo ou investigação de crime organizado.',48,144,'Reclusão, de 4 a 12 anos, e multa.',['ajuste','violência','crime organizado'],'Incluído pela Lei nº 15.245/2025; requer conferência temporal específica.'),
]
for item in new:
    if item['id'] not in existing:
        catalog['registros'].append(item)
path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + '\n')
print(f'added {sum(item["id"] not in existing for item in new)} organized-crime records')
