import json
from pathlib import Path

path = Path('/home/ubuntu/work/CALCULADORA_PENAL/src/data/tiposPenais.json')
catalog = json.loads(path.read_text())
existing = {record['id'] for record in catalog['registros']}
SOURCE = 'https://www.planalto.gov.br/ccivil_03/leis/l6766.htm'
CUT_OFF = catalog['dataCorte']

def make_record(id, name, device, desc, minimum, maximum, penalty, keywords):
    return {
        'id': id, 'nomeJuridico': name, 'aliases': [], 'classe': 'crime', 'jurisdicao': 'comum', 'modulo': 'Parcelamento do solo urbano',
        'norma': 'Lei nº 6.766/1979', 'dispositivo': device, 'naturezaFigura': 'basica', 'tipoPaiId': None,
        'descricaoObjetiva': desc,
        'pena': {'minimoMeses': minimum, 'maximoMeses': maximum, 'unidadePrincipal': 'meses', 'descricao': penalty, 'multa': None},
        'vigencia': {'estado': 'vigente', 'inicioVigenciaRedacao': None, 'dataConsulta': CUT_OFF, 'estadoConferencia': 'pendente', 'observacoes': 'Crime localizado em texto compilado oficial; multa calculada em múltiplos de salário mínimo e participação acessória exigem modelagem específica.'},
        'fonteOficial': SOURCE, 'leiCriadoraOuModificadora': ['Lei nº 6.766/1979'], 'inventarioValidado': False,
        'enriquecimentoValidado': False, 'usavelNaCalculadora': False,
        'enriquecimento': {'bemJuridico': None, 'sujeitoAtivo': None, 'sujeitoPassivo': None, 'elementoSubjetivo': None, 'consumacao': None, 'tentativa': None, 'formaCulposa': None, 'acaoPenal': None, 'competencia': None, 'procedimento': None, 'rito': None, 'hediondez': None, 'qualificadoras': [], 'majorantes': [], 'minorantes': [], 'agravantesAtenuantes': [], 'extincaoPunibilidade': [], 'jurisprudenciaQualificada': [], 'controversias': []},
        'palavrasChave': keywords,
    }
new = [
 make_record('parcelamento-6766-50','Parcelamento urbano ilegal','art. 50','Dar início ou efetuar loteamento ou desmembramento urbano sem autorização, em desacordo com a lei ou licença, ou fazer afirmação falsa sobre sua legalidade.',12,48,'Reclusão, de 1 a 4 anos, e multa de 5 a 50 vezes o maior salário mínimo vigente.',['loteamento','desmembramento','solo urbano']),
 make_record('parcelamento-6766-51','Concurso para parcelamento urbano ilegal','art. 51','Concorrer para a prática dos crimes do art. 50, especialmente como mandatário de loteador, diretor ou gerente de sociedade.',12,48,'Penas cominadas ao art. 50, conforme a participação.',['loteamento','concurso','parcelamento']),
 make_record('parcelamento-6766-52','Registro irregular de parcelamento urbano','art. 52','Registrar loteamento ou desmembramento não aprovado, registrar compromisso ou cessão relativa a parcelamento não registrado ou efetuar registro de contrato de venda irregular.',12,24,'Detenção, de 1 a 2 anos, e multa de 5 a 50 vezes o maior salário mínimo vigente.',['registro','loteamento','desmembramento']),
]
for item in new:
    if item['id'] not in existing:
        catalog['registros'].append(item)
path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + '\n')
print(f'added {sum(item["id"] not in existing for item in new)} land-subdivision records')
