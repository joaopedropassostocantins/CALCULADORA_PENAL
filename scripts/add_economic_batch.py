import json
from pathlib import Path

path = Path('/home/ubuntu/work/CALCULADORA_PENAL/src/data/tiposPenais.json')
catalog = json.loads(path.read_text())
existing = {record['id'] for record in catalog['registros']}
TAX = 'https://www.planalto.gov.br/ccivil_03/leis/l8137.htm'
FIN = 'https://www.planalto.gov.br/ccivil_03/leis/l7492.htm'
CUT_OFF = catalog['dataCorte']

def make_record(id, name, device, description, minimum, maximum, penalty, law, source, start, module, keywords, parent=None):
    return {
        'id': id, 'nomeJuridico': name, 'aliases': [], 'classe': 'crime', 'jurisdicao': 'comum', 'modulo': module,
        'norma': law, 'dispositivo': device, 'naturezaFigura': 'basica', 'tipoPaiId': parent,
        'descricaoObjetiva': description,
        'pena': {'minimoMeses': minimum, 'maximoMeses': maximum, 'unidadePrincipal': 'meses', 'descricao': penalty, 'multa': None},
        'vigencia': {'estado': 'vigente', 'inicioVigenciaRedacao': start, 'dataConsulta': CUT_OFF, 'estadoConferencia': 'confirmada', 'observacoes': None},
        'fonteOficial': source, 'leiCriadoraOuModificadora': [law], 'inventarioValidado': True,
        'enriquecimentoValidado': False, 'usavelNaCalculadora': True,
        'enriquecimento': {'bemJuridico': None, 'sujeitoAtivo': None, 'sujeitoPassivo': None, 'elementoSubjetivo': None, 'consumacao': None, 'tentativa': None, 'formaCulposa': None, 'acaoPenal': None, 'competencia': None, 'procedimento': None, 'rito': None, 'hediondez': None, 'qualificadoras': [], 'majorantes': [], 'minorantes': [], 'agravantesAtenuantes': [], 'extincaoPunibilidade': [], 'jurisprudenciaQualificada': [], 'controversias': []},
        'palavrasChave': keywords,
    }

new = []
# Lei 8.137/1990
new += [
 make_record('tributario-8137-1', 'Crime contra a ordem tributária por supressão ou redução de tributo', 'art. 1º', 'Suprimir ou reduzir tributo ou contribuição social e qualquer acessório mediante omissão, fraude, falsidade documental ou negativa de documento fiscal.', 24, 60, 'Reclusão, de 2 a 5 anos, e multa.', 'Lei nº 8.137/1990', TAX, '1990-12-27', 'Crimes tributários', ['sonegação fiscal', 'tributo', 'nota fiscal']),
 make_record('tributario-8137-2', 'Declaração falsa ou omissão tributária', 'art. 2º, I', 'Fazer declaração falsa ou omitir declaração sobre rendas, bens ou fatos, ou empregar fraude para eximir-se de pagamento de tributo.', 6, 24, 'Detenção, de 6 meses a 2 anos, e multa.', 'Lei nº 8.137/1990', TAX, '1990-12-27', 'Crimes tributários', ['declaração falsa', 'tributo', 'fraude fiscal']),
 make_record('tributario-8137-3-ii', 'Exigência ou recebimento de vantagem para não lançar tributo', 'art. 3º, II', 'Exigir, solicitar ou receber vantagem indevida para deixar de lançar ou cobrar tributo ou contribuição social ou cobrá-los parcialmente.', 36, 96, 'Reclusão, de 3 a 8 anos, e multa.', 'Lei nº 8.137/1990', TAX, '1990-12-27', 'Crimes tributários', ['vantagem indevida', 'tributo', 'funcionário público']),
 make_record('tributario-8137-3-iii', 'Patrocínio de interesse privado perante a administração fazendária', 'art. 3º, III', 'Patrocinar interesse privado perante a administração fazendária valendo-se da qualidade de funcionário público.', 12, 48, 'Reclusão, de 1 a 4 anos, e multa.', 'Lei nº 8.137/1990', TAX, '1990-12-27', 'Crimes tributários', ['administração fazendária', 'funcionário público', 'patrocínio']),
 make_record('tributario-8137-4-i', 'Abuso de poder econômico por ajuste ou acordo', 'art. 4º, I', 'Abusar do poder econômico dominando o mercado ou eliminando total ou parcialmente a concorrência mediante ajuste ou acordo de empresas.', 24, 60, 'Reclusão, de 2 a 5 anos, e multa.', 'Lei nº 8.137/1990', TAX, '1990-12-27', 'Crimes contra a ordem econômica', ['abuso de poder econômico', 'concorrência', 'cartel']),
 make_record('tributario-8137-7', 'Crime contra as relações de consumo', 'art. 7º', 'Praticar condutas como fraude de preços, venda de mercadoria imprópria, publicidade enganosa ou sonegação de bens nas relações de consumo.', 24, 60, 'Detenção, de 2 a 5 anos, ou multa.', 'Lei nº 8.137/1990', TAX, '1990-12-27', 'Crimes contra o consumo', ['relações de consumo', 'mercadoria imprópria', 'publicidade enganosa']),
]
# Lei 7.492/1986
financial = [
 ('2','Fabricação ou circulação não autorizada de título ou valor mobiliário','Imprimir, reproduzir, fabricar ou pôr em circulação, sem autorização, certificado ou documento representativo de título ou valor mobiliário.',24,96,'Reclusão, de 2 a 8 anos, e multa.',['título mobiliário','valor mobiliário','sistema financeiro']),
 ('3','Divulgação de informação falsa sobre instituição financeira','Divulgar informação falsa ou prejudicialmente incompleta sobre instituição financeira.',24,72,'Reclusão, de 2 a 6 anos, e multa.',['instituição financeira','informação falsa']),
 ('4','Gestão fraudulenta de instituição financeira','Gerir fraudulentamente instituição financeira.',36,144,'Reclusão, de 3 a 12 anos, e multa.',['gestão fraudulenta','instituição financeira']),
 ('4-temeraria','Gestão temerária de instituição financeira','Gerir temerariamente instituição financeira.',24,96,'Reclusão, de 2 a 8 anos, e multa.',['gestão temerária','instituição financeira']),
 ('5','Apropriação ou desvio de bem por administrador financeiro','Apropriar-se ou desviar em proveito próprio ou alheio dinheiro, título, valor ou bem móvel sob posse funcional.',24,72,'Reclusão, de 2 a 6 anos, e multa.',['apropriação','desvio','instituição financeira']),
 ('6','Indução em erro sobre operação ou situação financeira','Induzir ou manter em erro sócio, investidor ou repartição pública sobre operação ou situação financeira, sonegando informação ou prestando-a falsamente.',24,72,'Reclusão, de 2 a 6 anos, e multa.',['investidor','informação falsa','operação financeira']),
 ('7','Emissão ou negociação irregular de títulos e valores mobiliários','Emitir, oferecer ou negociar títulos ou valores mobiliários falsos, sem registro, sem lastro ou sem autorização.',24,96,'Reclusão, de 2 a 8 anos, e multa.',['títulos falsos','valores mobiliários','investimento']),
 ('8','Cobrança irregular de juros ou remuneração financeira','Exigir remuneração em desacordo com a legislação sobre operação de crédito, seguro, fundo, consórcio, corretagem ou distribuição de títulos.',12,48,'Reclusão, de 1 a 4 anos, e multa.',['juros ilegais','operação de crédito']),
 ('9','Fraude contra fiscalização ou investidor','Fraudar fiscalização ou investidor inserindo declaração falsa em documento comprobatório de investimento.',12,60,'Reclusão, de 1 a 5 anos, e multa.',['fraude contra investidor','fiscalização']),
 ('10','Falsidade em demonstrativo contábil de instituição financeira','Fazer inserir elemento falso ou omitir elemento exigido em demonstrativos contábeis de instituição financeira, seguradora ou integrante do sistema de distribuição.',12,60,'Reclusão, de 1 a 5 anos, e multa.',['demonstrativo contábil','instituição financeira']),
 ('11','Contabilidade paralela de instituição financeira','Manter ou movimentar recurso ou valor paralelamente à contabilidade exigida pela legislação.',12,60,'Reclusão, de 1 a 5 anos, e multa.',['contabilidade paralela','caixa dois','instituição financeira']),
 ('16','Funcionamento não autorizado de instituição financeira','Fazer operar, sem autorização ou com autorização obtida mediante declaração falsa, instituição financeira ou de câmbio.',12,48,'Reclusão, de 1 a 4 anos, e multa.',['instituição financeira clandestina','câmbio']),
 ('19','Financiamento obtido mediante fraude','Obter, mediante fraude, financiamento em instituição financeira.',24,72,'Reclusão, de 2 a 6 anos, e multa.',['financiamento fraudulento','fraude bancária']),
 ('21','Falsa identidade em operação de câmbio','Atribuir-se ou atribuir a terceiro falsa identidade para realizar operação de câmbio.',12,48,'Detenção, de 1 a 4 anos, e multa.',['falsa identidade','câmbio']),
 ('22','Evasão de divisas','Efetuar operação de câmbio não autorizada para promover evasão de divisas ou promover saída de moeda sem autorização.',24,72,'Reclusão, de 2 a 6 anos, e multa.',['evasão de divisas','câmbio','moeda estrangeira']),
 ('23','Omissão funcional contra o sistema financeiro','Omitir, retardar ou praticar contra a lei ato de ofício necessário ao funcionamento do sistema financeiro ou à ordem econômico-financeira.',12,48,'Reclusão, de 1 a 4 anos, e multa.',['sistema financeiro','funcionário público','omissão']),
]
for num,name,desc,minimum,maximum,penalty,keywords in financial:
    new.append(make_record(f'sfn-7492-{num}', name, f'art. {num}' if '-' not in num else f'art. {num.split("-")[0]}, parágrafo único', desc, minimum, maximum, penalty, 'Lei nº 7.492/1986', FIN, '1986-06-16', 'Crimes contra o sistema financeiro', keywords))

for item in new:
    if item['id'] not in existing:
        catalog['registros'].append(item)
path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + '\n')
print(f'added {sum(item["id"] not in existing for item in new)} records')
