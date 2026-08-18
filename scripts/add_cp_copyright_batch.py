import json
from pathlib import Path

path = Path('/home/ubuntu/work/CALCULADORA_PENAL/src/data/tiposPenais.json')
catalog = json.loads(path.read_text())
existing = {record['id'] for record in catalog['registros']}
SOURCE = 'https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848.htm'
CUTOFF = catalog['dataCorte']

def make_record(id, device, name, desc, minimum, maximum, penalty, keywords, nature='basica', parent=None):
    return {
        'id': id, 'nomeJuridico': name, 'aliases': [], 'classe': 'crime', 'jurisdicao': 'comum', 'modulo': 'Código Penal',
        'norma': 'Decreto-Lei nº 2.848/1940', 'dispositivo': device, 'naturezaFigura': nature, 'tipoPaiId': parent,
        'descricaoObjetiva': desc,
        'pena': {'minimoMeses': minimum, 'maximoMeses': maximum, 'unidadePrincipal': 'meses', 'descricao': penalty, 'multa': None},
        'vigencia': {'estado': 'vigente', 'inicioVigenciaRedacao': '1940-12-07', 'dataConsulta': CUTOFF, 'estadoConferencia': 'pendente', 'observacoes': 'Figura do art. 184 do Código Penal localizada no texto oficial; inventário e enriquecimento pendentes antes do cálculo.'},
        'fonteOficial': SOURCE, 'leiCriadoraOuModificadora': ['Decreto-Lei nº 2.848/1940', 'Lei nº 10.695/2003'], 'inventarioValidado': False,
        'enriquecimentoValidado': False, 'usavelNaCalculadora': False,
        'enriquecimento': {'bemJuridico': None, 'sujeitoAtivo': None, 'sujeitoPassivo': None, 'elementoSubjetivo': None, 'consumacao': None, 'tentativa': None, 'formaCulposa': None, 'acaoPenal': None, 'competencia': 'comum', 'procedimento': None, 'rito': None, 'hediondez': None, 'qualificadoras': [], 'majorantes': [], 'minorantes': [], 'agravantesAtenuantes': [], 'extincaoPunibilidade': [], 'jurisprudenciaQualificada': [], 'controversias': []},
        'palavrasChave': keywords,
    }
new = [
 make_record('cp-184','art. 184, caput','Violação de direitos autorais e conexos','Violar direitos de autor e os que lhe são conexos.',0.5,12,'Detenção, de 3 meses a 1 ano, ou multa.',['direito autoral','obra intelectual','fonograma']),
 make_record('cp-184-1','art. 184, § 1º','Reprodução não autorizada com intuito de lucro','Reproduzir total ou parcialmente obra intelectual, interpretação, execução ou fonograma, com intuito de lucro direto ou indireto, sem autorização dos titulares.',24,48,'Reclusão, de 2 a 4 anos, e multa.',['direito autoral','reprodução','lucro'],'qualificada','cp-184'),
 make_record('cp-184-2','art. 184, § 2º','Distribuição ou comercialização ilícita de obra autoral','Distribuir, vender, expor à venda, alugar, introduzir no País, adquirir, ocultar ou ter em depósito, com intuito de lucro, obra, fonograma ou cópia produzida com violação de direito autoral.',24,48,'Reclusão, de 2 a 4 anos, e multa.',['direito autoral','distribuição','comércio'],'qualificada','cp-184'),
 make_record('cp-184-3','art. 184, § 3º','Oferta pública não autorizada de obra autoral','Oferecer ao público, mediante cabo, fibra ótica, satélite, ondas ou outro sistema de seleção de obra para recebimento em tempo e lugar determinados, com intuito de lucro, sem autorização.',24,48,'Reclusão, de 2 a 4 anos, e multa.',['direito autoral','oferta pública','streaming'],'qualificada','cp-184'),
]
for item in new:
    if item['id'] not in existing:
        catalog['registros'].append(item)
path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + '\n')
print(f'added {sum(item["id"] not in existing for item in new)} copyright records')
