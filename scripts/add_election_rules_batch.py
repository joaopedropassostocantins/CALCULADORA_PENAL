import json
from pathlib import Path

path = Path('/home/ubuntu/work/CALCULADORA_PENAL/src/data/tiposPenais.json')
catalog = json.loads(path.read_text())
existing = {record['id'] for record in catalog['registros']}
SOURCE = 'https://www.planalto.gov.br/ccivil_03/leis/l9504.htm'
CUTOFF = catalog['dataCorte']

def make_record(id, device, name, desc, minimum, maximum, penalty, keywords):
    return {
        'id': id, 'nomeJuridico': name, 'aliases': [], 'classe': 'crime', 'jurisdicao': 'eleitoral', 'modulo': 'Normas para eleições',
        'norma': 'Lei nº 9.504/1997', 'dispositivo': device, 'naturezaFigura': 'basica', 'tipoPaiId': None,
        'descricaoObjetiva': desc,
        'pena': {'minimoMeses': minimum, 'maximoMeses': maximum, 'unidadePrincipal': 'meses', 'descricao': penalty, 'multa': None},
        'vigencia': {'estado': 'vigente', 'inicioVigenciaRedacao': None, 'dataConsulta': CUTOFF, 'estadoConferencia': 'pendente', 'observacoes': 'Tipo penal localizado no texto oficial da Lei nº 9.504/1997; penas pecuniárias em UFIR ou disposições tecnológicas exigem reconciliação normativa e validação temporal antes do cálculo.'},
        'fonteOficial': SOURCE, 'leiCriadoraOuModificadora': ['Lei nº 9.504/1997'], 'inventarioValidado': False,
        'enriquecimentoValidado': False, 'usavelNaCalculadora': False,
        'enriquecimento': {'bemJuridico': None, 'sujeitoAtivo': None, 'sujeitoPassivo': None, 'elementoSubjetivo': None, 'consumacao': None, 'tentativa': None, 'formaCulposa': None, 'acaoPenal': None, 'competencia': 'eleitoral', 'procedimento': None, 'rito': None, 'hediondez': None, 'qualificadoras': [], 'majorantes': [], 'minorantes': [], 'agravantesAtenuantes': [], 'extincaoPunibilidade': [], 'jurisprudenciaQualificada': [], 'controversias': []},
        'palavrasChave': keywords,
    }
new = [
 make_record('eleicoes-9504-33-4','art. 33, § 4º','Divulgação de pesquisa eleitoral fraudulenta','Divulgar pesquisa eleitoral fraudulenta.',6,12,'Detenção, de 6 meses a 1 ano, e multa de 50.000 a 100.000 UFIR.',['pesquisa eleitoral','fraude','divulgação']),
 make_record('eleicoes-9504-34-2','art. 34, § 2º','Obstrução da fiscalização de pesquisa eleitoral','Descumprir o dever de franquear acesso ao sistema de controle de pesquisa ou retardar, impedir ou dificultar a fiscalização dos partidos.',6,12,'Detenção, de 6 meses a 1 ano, alternativa de prestação de serviços à comunidade pelo mesmo prazo, e multa de 10.000 a 20.000 UFIR.',['pesquisa eleitoral','fiscalização','obstrução']),
 make_record('eleicoes-9504-34-3','art. 34, § 3º','Irregularidade em dados de pesquisa eleitoral','Comprovar irregularidade nos dados publicados em pesquisa eleitoral.',6,12,'Penas do art. 34, § 2º: detenção, de 6 meses a 1 ano, alternativa de prestação de serviços à comunidade pelo mesmo prazo, e multa de 10.000 a 20.000 UFIR.',['pesquisa eleitoral','dados irregulares']),
 make_record('eleicoes-9504-40','art. 40','Uso de símbolos de órgãos públicos na propaganda','Usar, em propaganda eleitoral, símbolos, frases ou imagens associados ou semelhantes aos empregados por órgão de governo, empresa pública ou sociedade de economia mista.',6,12,'Detenção, de 6 meses a 1 ano, alternativa de prestação de serviços à comunidade pelo mesmo período, e multa de 10.000 a 20.000 UFIR.',['propaganda eleitoral','símbolos públicos']),
 make_record('eleicoes-9504-68-2','art. 68, § 2º','Recusa de entrega de cópia do boletim de urna','Deixar de entregar ao partido ou coligação concorrente cópia do boletim de urna requerida no prazo legal.',1,3,'Detenção, de 1 a 3 meses, alternativa de prestação de serviço à comunidade pelo mesmo período, e multa de 1.000 a 5.000 UFIR.',['boletim de urna','fiscalização eleitoral']),
 make_record('eleicoes-9504-72-i','art. 72, I','Acesso indevido a sistema eleitoral para alterar votos','Obter acesso a sistema de tratamento automático de dados usado pelo serviço eleitoral para alterar a apuração ou a contagem de votos.',60,120,'Reclusão, de 5 a 10 anos.',['sistema eleitoral','votos','acesso indevido']),
 make_record('eleicoes-9504-72-ii','art. 72, II','Introdução de comando ou programa lesivo em sistema eleitoral','Desenvolver ou introduzir comando, instrução ou programa capaz de alterar dados, instruções ou programas, ou provocar resultado diverso do esperado em sistema eleitoral.',60,120,'Reclusão, de 5 a 10 anos.',['sistema eleitoral','programa','dados']),
 make_record('eleicoes-9504-72-iii','art. 72, III','Dano físico a equipamento de votação ou totalização','Causar propositalmente dano físico a equipamento usado na votação ou na totalização de votos ou a suas partes.',60,120,'Reclusão, de 5 a 10 anos.',['urna eletrônica','equipamento eleitoral','dano']),
 make_record('eleicoes-9504-87-4','art. 87, § 4º','Obstrução da fiscalização da apuração','Descumprir disposição do art. 87 sobre a observação pelos fiscais e delegados dos partidos ou coligações durante a apuração.',1,3,'Detenção, de 1 a 3 meses, alternativa de prestação de serviços à comunidade pelo mesmo período, e multa de 1.000 a 5.000 UFIR.',['apuração eleitoral','fiscalização','boletim']),
 make_record('eleicoes-9504-91-pu','art. 91, parágrafo único','Retenção de título eleitoral','Reter título eleitoral ou comprovante de alistamento eleitoral.',1,3,'Detenção, de 1 a 3 meses, alternativa de prestação de serviços à comunidade pelo mesmo período, e multa de 5.000 a 10.000 UFIR.',['título eleitoral','alistamento','retenção']),
]
for item in new:
    if item['id'] not in existing:
        catalog['registros'].append(item)
path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + '\n')
print(f'added {sum(item["id"] not in existing for item in new)} election-rules records')
