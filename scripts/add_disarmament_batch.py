import json
from pathlib import Path

path = Path('/home/ubuntu/work/CALCULADORA_PENAL/src/data/tiposPenais.json')
catalog = json.loads(path.read_text())
existing = {record['id'] for record in catalog['registros']}
SOURCE = 'https://www.planalto.gov.br/ccivil_03/leis/2003/l10.826compilado.htm'
CUTOFF = catalog['dataCorte']

def make_record(id, device, name, desc, minimum, maximum, penalty, keywords, nature='basica', parent=None, observations='Tipo penal do capítulo de crimes do Estatuto do Desarmamento conferido na fonte oficial; inventário e enriquecimento permanecem pendentes antes do cálculo.'):
    return {
        'id': id, 'nomeJuridico': name, 'aliases': [], 'classe': 'crime', 'jurisdicao': 'comum', 'modulo': 'Estatuto do Desarmamento',
        'norma': 'Lei nº 10.826/2003', 'dispositivo': device, 'naturezaFigura': nature, 'tipoPaiId': parent,
        'descricaoObjetiva': desc,
        'pena': {'minimoMeses': minimum, 'maximoMeses': maximum, 'unidadePrincipal': 'meses', 'descricao': penalty, 'multa': None},
        'vigencia': {'estado': 'vigente', 'inicioVigenciaRedacao': '2003-12-22', 'dataConsulta': CUTOFF, 'estadoConferencia': 'pendente', 'observacoes': observations},
        'fonteOficial': SOURCE, 'leiCriadoraOuModificadora': ['Lei nº 10.826/2003', 'Lei nº 13.964/2019', 'Lei nº 15.358/2026'], 'inventarioValidado': False,
        'enriquecimentoValidado': False, 'usavelNaCalculadora': False,
        'enriquecimento': {'bemJuridico': None, 'sujeitoAtivo': None, 'sujeitoPassivo': None, 'elementoSubjetivo': None, 'consumacao': None, 'tentativa': None, 'formaCulposa': None, 'acaoPenal': None, 'competencia': 'comum', 'procedimento': None, 'rito': None, 'hediondez': None, 'qualificadoras': [], 'majorantes': [], 'minorantes': [], 'agravantesAtenuantes': [], 'extincaoPunibilidade': [], 'jurisprudenciaQualificada': [], 'controversias': []},
        'palavrasChave': keywords,
    }
new = [
 make_record('desarmamento-10826-12','art. 12','Posse irregular de arma de fogo de uso permitido','Possuir ou manter sob sua guarda arma de fogo, acessório ou munição de uso permitido em desacordo com determinação legal ou regulamentar no interior da residência ou local de trabalho previsto em lei.',1,3,'Detenção, de 1 a 3 anos, e multa.',['arma de fogo','posse irregular','uso permitido']),
 make_record('desarmamento-10826-13','art. 13','Omissão de cautela','Deixar de observar as cautelas necessárias para impedir que menor de 18 anos ou pessoa com deficiência mental se apodere de arma de fogo sob posse ou propriedade do agente.',1,2,'Detenção, de 1 a 2 anos, e multa.',['arma de fogo','omissão de cautela','menor']),
 make_record('desarmamento-10826-14','art. 14','Porte ilegal de arma de fogo de uso permitido','Portar, deter, adquirir, fornecer, receber, ter em depósito, transportar, ceder, emprestar, remeter, empregar, manter sob guarda ou ocultar arma de fogo, acessório ou munição de uso permitido sem autorização e em desacordo com determinação legal ou regulamentar.',24,48,'Reclusão, de 2 a 4 anos, e multa.',['arma de fogo','porte ilegal','uso permitido']),
 make_record('desarmamento-10826-15','art. 15','Disparo de arma de fogo','Disparar arma de fogo ou acionar munição em lugar habitado, em suas adjacências, em via pública ou em direção a ela, quando a conduta não tiver como finalidade a prática de outro crime.',24,48,'Reclusão, de 2 a 4 anos, e multa.',['arma de fogo','disparo','via pública']),
 make_record('desarmamento-10826-16','art. 16','Posse ou porte ilegal de arma de fogo de uso restrito','Possuir, deter, portar, adquirir, fornecer, receber, ter em depósito, transportar, ceder, emprestar, remeter, empregar, manter sob guarda ou ocultar arma de fogo, acessório ou munição de uso restrito sem autorização e em desacordo com determinação legal ou regulamentar.',36,72,'Reclusão, de 3 a 6 anos, e multa.',['arma de fogo','uso restrito','posse ilegal','porte ilegal']),
 make_record('desarmamento-10826-16-2','art. 16, § 2º','Posse ou porte de arma de fogo de uso proibido','Praticar as condutas do art. 16, caput ou § 1º, envolvendo arma de fogo de uso proibido.',48,144,'Reclusão, de 4 a 12 anos, e multa.',['arma de fogo','uso proibido','qualificadora'], 'qualificada', 'desarmamento-10826-16', 'Qualificadora autônoma do art. 16, § 2º, com pena própria; as condutas do § 1º que mantêm a mesma pena do caput não foram duplicadas.'),
 make_record('desarmamento-10826-17','art. 17','Comércio ilegal de arma de fogo','Adquirir, alugar, receber, transportar, conduzir, ocultar, ter em depósito, desmontar, montar, remontar, adulterar, vender, expor à venda ou utilizar arma de fogo, acessório ou munição, em proveito próprio ou alheio, no exercício de atividade comercial ou industrial, sem autorização ou em desacordo com determinação legal ou regulamentar.',72,144,'Reclusão, de 6 a 12 anos, e multa.',['arma de fogo','comércio ilegal','munição']),
 make_record('desarmamento-10826-18','art. 18','Tráfico internacional de arma de fogo','Importar, exportar ou favorecer a entrada ou saída do território nacional, a qualquer título, de arma de fogo, acessório ou munição sem autorização da autoridade competente.',96,192,'Reclusão, de 8 a 16 anos, e multa.',['arma de fogo','tráfico internacional','importação','exportação']),
]
for item in new:
    if item['id'] not in existing:
        catalog['registros'].append(item)
path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + '\n')
print(f'added {sum(item["id"] not in existing for item in new)} disarmament records')
