import json
from pathlib import Path

path = Path('/home/ubuntu/work/CALCULADORA_PENAL/src/data/tiposPenais.json')
catalog = json.loads(path.read_text())
existing = {record['id'] for record in catalog['registros']}
SOURCE = 'https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2005/lei/l11105.htm'
CUTOFF = catalog['dataCorte']

def make_record(id, device, name, desc, minimum, maximum, penalty, keywords, observations='Tipo penal da Lei de Biossegurança localizado em fonte oficial; inventário e enriquecimento ainda serão auditados antes de liberar o cálculo.'):
    return {
        'id': id, 'nomeJuridico': name, 'aliases': [], 'classe': 'crime', 'jurisdicao': 'comum', 'modulo': 'Biossegurança',
        'norma': 'Lei nº 11.105/2005', 'dispositivo': device, 'naturezaFigura': 'basica', 'tipoPaiId': None,
        'descricaoObjetiva': desc,
        'pena': {'minimoMeses': minimum, 'maximoMeses': maximum, 'unidadePrincipal': 'meses', 'descricao': penalty, 'multa': None},
        'vigencia': {'estado': 'vigente', 'inicioVigenciaRedacao': '2005-03-24', 'dataConsulta': CUTOFF, 'estadoConferencia': 'pendente', 'observacoes': observations},
        'fonteOficial': SOURCE, 'leiCriadoraOuModificadora': ['Lei nº 11.105/2005'], 'inventarioValidado': False,
        'enriquecimentoValidado': False, 'usavelNaCalculadora': False,
        'enriquecimento': {'bemJuridico': None, 'sujeitoAtivo': None, 'sujeitoPassivo': None, 'elementoSubjetivo': None, 'consumacao': None, 'tentativa': None, 'formaCulposa': None, 'acaoPenal': None, 'competencia': 'comum', 'procedimento': None, 'rito': None, 'hediondez': None, 'qualificadoras': [], 'majorantes': [], 'minorantes': [], 'agravantesAtenuantes': [], 'extincaoPunibilidade': [], 'jurisprudenciaQualificada': [], 'controversias': []},
        'palavrasChave': keywords,
    }
new = [
 make_record('biosseguranca-11105-24','art. 24','Uso irregular de embrião humano','Utilizar embrião humano em desacordo com o disposto no art. 5º da Lei nº 11.105/2005.',1,3,'Detenção, de 1 a 3 anos, e multa.',['biossegurança','embrião humano','células-tronco']),
 make_record('biosseguranca-11105-25','art. 25','Engenharia genética em célula germinal humana','Praticar engenharia genética em célula germinal humana, zigoto humano ou embrião humano.',12,48,'Reclusão, de 1 a 4 anos, e multa.',['biossegurança','engenharia genética','célula germinal']),
 make_record('biosseguranca-11105-26','art. 26','Clonagem humana','Realizar clonagem humana.',24,60,'Reclusão, de 2 a 5 anos, e multa.',['biossegurança','clonagem humana']),
 make_record('biosseguranca-11105-27','art. 27','Liberação ou descarte irregular de OGM','Liberar ou descartar organismo geneticamente modificado ou seus derivados no meio ambiente em desacordo com as normas legais e regulamentares.',12,48,'Reclusão, de 1 a 4 anos, e multa.',['biossegurança','OGM','meio ambiente'], 'O art. 27, § 2º prevê majorantes por resultado, que devem permanecer no campo de enriquecimento e não como tipos autônomos.'),
 make_record('biosseguranca-11105-28','art. 28','Uso de tecnologia genética de restrição','Utilizar, comercializar, registrar, patentear ou licenciar tecnologias genéticas de restrição do uso.',24,60,'Reclusão, de 2 a 5 anos, e multa.',['biossegurança','tecnologia genética','restrição de uso']),
 make_record('biosseguranca-11105-29','art. 29','Produção ou comércio irregular de OGM','Produzir, armazenar, transportar, comercializar, importar ou exportar organismo geneticamente modificado ou seus derivados sem autorização ou em desacordo com as normas legais e regulamentares.',12,24,'Reclusão, de 1 a 2 anos, e multa.',['biossegurança','OGM','produção','importação','exportação']),
]
for item in new:
    if item['id'] not in existing:
        catalog['registros'].append(item)
path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + '\n')
print(f'added {sum(item["id"] not in existing for item in new)} biosafety records')
