import json
from pathlib import Path

path = Path('/home/ubuntu/work/CALCULADORA_PENAL/src/data/tiposPenais.json')
catalog = json.loads(path.read_text())
existing = {record['id'] for record in catalog['registros']}
SOURCE = 'https://www.planalto.gov.br/ccivil_03/decreto-lei/del0201.htm'
CUT_OFF = catalog['dataCorte']

def make_record(id, device, name, desc, minimum, maximum, penalty):
    return {
        'id': id, 'nomeJuridico': name, 'aliases': [], 'classe': 'crime', 'jurisdicao': 'comum', 'modulo': 'Crimes de responsabilidade municipal',
        'norma': 'Decreto-Lei nº 201/1967', 'dispositivo': device, 'naturezaFigura': 'basica', 'tipoPaiId': None,
        'descricaoObjetiva': desc,
        'pena': {'minimoMeses': minimum, 'maximoMeses': maximum, 'unidadePrincipal': 'meses', 'descricao': penalty, 'multa': None},
        'vigencia': {'estado': 'vigente', 'inicioVigenciaRedacao': None, 'dataConsulta': CUT_OFF, 'estadoConferencia': 'pendente', 'observacoes': 'Crime judicial de responsabilidade municipal localizado em fonte oficial; cálculo bloqueado até auditoria de leis modificadoras, sujeito ativo, competência e sanções acessórias.'},
        'fonteOficial': SOURCE, 'leiCriadoraOuModificadora': ['Decreto-Lei nº 201/1967'], 'inventarioValidado': False,
        'enriquecimentoValidado': False, 'usavelNaCalculadora': False,
        'enriquecimento': {'bemJuridico': None, 'sujeitoAtivo': 'Prefeito municipal', 'sujeitoPassivo': None, 'elementoSubjetivo': None, 'consumacao': None, 'tentativa': None, 'formaCulposa': None, 'acaoPenal': 'pública', 'competencia': None, 'procedimento': None, 'rito': None, 'hediondez': None, 'qualificadoras': [], 'majorantes': [], 'minorantes': [], 'agravantesAtenuantes': [], 'extincaoPunibilidade': [], 'jurisprudenciaQualificada': [], 'controversias': []},
        'palavrasChave': ['prefeito', 'crime de responsabilidade', 'município'],
    }
R = 'Reclusão, de 2 a 12 anos.'
D = 'Detenção, de 3 meses a 3 anos.'
new = [
 make_record('prefeito-201-1-i','art. 1º, I','Apropriação ou desvio de bens e rendas públicas','Apropriar-se de bens ou rendas públicas ou desviá-los em proveito próprio ou alheio.',24,144,R),
 make_record('prefeito-201-1-ii','art. 1º, II','Uso indevido de bens, rendas ou serviços públicos','Utilizar-se indevidamente, em proveito próprio ou alheio, de bens, rendas ou serviços públicos.',24,144,R),
 make_record('prefeito-201-1-iii','art. 1º, III','Desvio ou aplicação indevida de verbas públicas','Desviar ou aplicar indevidamente rendas ou verbas públicas.',3,36,D),
 make_record('prefeito-201-1-iv','art. 1º, IV','Emprego irregular de subvenções e recursos','Empregar subvenções, auxílios, empréstimos ou recursos em desacordo com planos ou programas.',3,36,D),
 make_record('prefeito-201-1-v','art. 1º, V','Despesa pública não autorizada','Ordenar ou efetuar despesas não autorizadas por lei ou em desacordo com normas financeiras.',3,36,D),
 make_record('prefeito-201-1-vi','art. 1º, VI','Omissão de contas anuais municipais','Deixar de prestar contas anuais da administração financeira do Município à Câmara ou órgão competente.',3,36,D),
 make_record('prefeito-201-1-vii','art. 1º, VII','Omissão de contas de recursos recebidos','Deixar de prestar contas no tempo devido da aplicação de recursos, empréstimos, subvenções ou auxílios recebidos.',3,36,D),
 make_record('prefeito-201-1-viii','art. 1º, VIII','Empréstimo ou título municipal sem autorização','Contrair empréstimo, emitir apólices ou obrigar o Município por títulos sem autorização da Câmara ou em desacordo com a lei.',3,36,D),
 make_record('prefeito-201-1-ix','art. 1º, IX','Concessão irregular de empréstimo ou subvenção','Conceder empréstimos, auxílios ou subvenções sem autorização da Câmara ou em desacordo com a lei.',3,36,D),
 make_record('prefeito-201-1-x','art. 1º, X','Alienação ou oneração irregular de bens municipais','Alienar ou onerar bens imóveis ou rendas municipais sem autorização da Câmara ou em desacordo com a lei.',3,36,D),
 make_record('prefeito-201-1-xi','art. 1º, XI','Contratação pública sem concorrência exigida','Adquirir bens ou realizar serviços e obras sem concorrência ou coleta de preços nos casos exigidos.',3,36,D),
 make_record('prefeito-201-1-xii','art. 1º, XII','Inversão indevida da ordem de pagamentos','Antecipar ou inverter a ordem de pagamento a credores do Município sem vantagem para o erário.',3,36,D),
 make_record('prefeito-201-1-xiii','art. 1º, XIII','Nomeação irregular de servidor','Nomear, admitir ou designar servidor contra expressa disposição de lei.',3,36,D),
 make_record('prefeito-201-1-xiv','art. 1º, XIV','Descumprimento injustificado de lei ou ordem judicial','Negar execução a lei federal, estadual ou municipal ou deixar de cumprir ordem judicial sem justificar a recusa ou impossibilidade por escrito.',3,36,D),
 make_record('prefeito-201-1-xv','art. 1º, XV','Omissão de certidão de ato ou contrato municipal','Deixar de fornecer certidões de atos ou contratos municipais dentro do prazo legal.',3,36,D),
 make_record('prefeito-201-1-xvi','art. 1º, XVI','Omissão na redução da dívida consolidada','Deixar de ordenar redução da dívida consolidada quando ultrapassado o limite máximo fixado pelo Senado.',3,36,D),
 make_record('prefeito-201-1-xvii','art. 1º, XVII','Abertura irregular de crédito público','Ordenar ou autorizar abertura de crédito em desacordo com limites do Senado, sem fundamento orçamentário ou com inobservância legal.',3,36,D),
 make_record('prefeito-201-1-xviii','art. 1º, XVIII','Omissão de cancelamento ou reserva de operação de crédito','Deixar de promover cancelamento, amortização ou reserva para anular efeitos de operação de crédito irregular.',3,36,D),
 make_record('prefeito-201-1-xix','art. 1º, XIX','Omissão na liquidação de antecipação de receita','Deixar de promover liquidação integral de operação de crédito por antecipação de receita até o encerramento do exercício.',3,36,D),
 make_record('prefeito-201-1-xx','art. 1º, XX','Operação de crédito irregular entre entes federativos','Ordenar ou autorizar operação de crédito ilegal com outro ente da Federação ou entidade da administração indireta.',3,36,D),
 make_record('prefeito-201-1-xxi','art. 1º, XXI','Antecipação de receita tributária futura','Captar recursos a título de antecipação de receita de tributo ou contribuição cujo fato gerador ainda não ocorreu.',3,36,D),
 make_record('prefeito-201-1-xxii','art. 1º, XXII','Desvio de recursos de emissão de títulos','Ordenar ou autorizar destinação de recursos provenientes de títulos para finalidade diversa da prevista na lei autorizadora.',3,36,D),
 make_record('prefeito-201-1-xxiii','art. 1º, XXIII','Transferência voluntária irregular','Realizar ou receber transferência voluntária em desacordo com limite ou condição legal.',3,36,D),
]
for item in new:
    if item['id'] not in existing:
        catalog['registros'].append(item)
path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + '\n')
print(f'added {sum(item["id"] not in existing for item in new)} municipal-responsibility records')
