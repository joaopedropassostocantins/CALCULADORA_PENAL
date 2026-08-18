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
        'vigencia': {'estado': 'vigente', 'inicioVigenciaRedacao': None, 'dataConsulta': CUT_OFF, 'estadoConferencia': 'pendente', 'observacoes': note or 'Tipo localizado em fonte oficial; cálculo bloqueado até auditoria da redação vigente e enriquecimento jurídico.'},
        'fonteOficial': source, 'leiCriadoraOuModificadora': [law], 'inventarioValidado': False,
        'enriquecimentoValidado': False, 'usavelNaCalculadora': False,
        'enriquecimento': {'bemJuridico': None, 'sujeitoAtivo': None, 'sujeitoPassivo': None, 'elementoSubjetivo': None, 'consumacao': None, 'tentativa': None, 'formaCulposa': None, 'acaoPenal': None, 'competencia': None, 'procedimento': None, 'rito': None, 'hediondez': None, 'qualificadoras': [], 'majorantes': [], 'minorantes': [], 'agravantesAtenuantes': [], 'extincaoPunibilidade': [], 'jurisprudenciaQualificada': [], 'controversias': []},
        'palavrasChave': keywords,
    }
PWD = 'https://www.planalto.gov.br/ccivil_03/leis/l7853.htm'
FAM = 'https://www.planalto.gov.br/ccivil_03/leis/l9263.htm'
new = [
 make_record('deficiencia-7853-8','Discriminação contra pessoa com deficiência','art. 8º','Recusar, cobrar valor adicional, suspender, procrastinar ou cancelar matrícula; obstar concurso ou emprego público; negar emprego ou promoção; recusar assistência de saúde; descumprir ordem judicial; ou omitir dados técnicos por motivo de deficiência.',24,60,'Reclusão, de 2 a 5 anos, e multa.','Lei nº 7.853/1989',PWD,'Crimes contra pessoas com deficiência',['deficiência','discriminação','educação','trabalho'],'A redação vigente foi alterada pela Lei nº 13.146/2015 e a lei recebeu atualização terminológica em 2025.'),
 make_record('planejamento-familiar-9263-15','Esterilização cirúrgica irregular','art. 15','Realizar esterilização cirúrgica em desacordo com o art. 10 da Lei de Planejamento Familiar.',24,96,'Reclusão, de 2 a 8 anos, e multa.','Lei nº 9.263/1996',FAM,'Planejamento familiar',['esterilização','planejamento familiar']),
 make_record('planejamento-familiar-9263-16','Omissão de notificação de esterilização','art. 16','Deixar o médico de notificar à autoridade sanitária as esterilizações cirúrgicas realizadas.',6,24,'Detenção, de 6 meses a 2 anos, e multa.','Lei nº 9.263/1996',FAM,'Planejamento familiar',['esterilização','notificação sanitária']),
 make_record('planejamento-familiar-9263-17','Indução ou instigação de esterilização','art. 17','Induzir ou instigar dolosamente a prática de esterilização cirúrgica.',12,24,'Reclusão, de 1 a 2 anos.','Lei nº 9.263/1996',FAM,'Planejamento familiar',['esterilização','indução','instigação']),
 make_record('planejamento-familiar-9263-18','Exigência de atestado de esterilização','art. 18','Exigir atestado de esterilização para qualquer fim.',12,24,'Reclusão, de 1 a 2 anos, e multa.','Lei nº 9.263/1996',FAM,'Planejamento familiar',['esterilização','atestado']),
]
for item in new:
    if item['id'] not in existing:
        catalog['registros'].append(item)
path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + '\n')
print(f'added {sum(item["id"] not in existing for item in new)} disability/family-planning records')
