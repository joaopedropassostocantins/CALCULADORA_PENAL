import json
from pathlib import Path

path = Path('/home/ubuntu/work/CALCULADORA_PENAL/src/data/tiposPenais.json')
catalog = json.loads(path.read_text())
existing = {record['id'] for record in catalog['registros']}
SOURCE = 'https://www.planalto.gov.br/ccivil_03/decreto-lei/del1001.htm'
CUT_OFF = catalog['dataCorte']

def make_record(id, name, device, description, minimum, maximum, penalty, keywords, note=None):
    return {
        'id': id, 'nomeJuridico': name, 'aliases': [], 'classe': 'crime', 'jurisdicao': 'militar', 'modulo': 'Código Penal Militar',
        'norma': 'Decreto-Lei nº 1.001/1969', 'dispositivo': device, 'naturezaFigura': 'basica', 'tipoPaiId': None,
        'descricaoObjetiva': description,
        'pena': {'minimoMeses': minimum, 'maximoMeses': maximum, 'unidadePrincipal': 'meses', 'descricao': penalty, 'multa': None},
        'vigencia': {'estado': 'vigente', 'inicioVigenciaRedacao': None, 'dataConsulta': CUT_OFF, 'estadoConferencia': 'pendente', 'observacoes': note or 'Tipo penal militar localizado no texto compilado oficial; aguarda auditoria integral de vigência, competência militar e sobreposição com a legislação comum.'},
        'fonteOficial': SOURCE, 'leiCriadoraOuModificadora': ['Decreto-Lei nº 1.001/1969', 'Lei nº 14.688/2023'], 'inventarioValidado': False,
        'enriquecimentoValidado': False, 'usavelNaCalculadora': False,
        'enriquecimento': {'bemJuridico': None, 'sujeitoAtivo': None, 'sujeitoPassivo': None, 'elementoSubjetivo': None, 'consumacao': None, 'tentativa': None, 'formaCulposa': None, 'acaoPenal': None, 'competencia': None, 'procedimento': None, 'rito': None, 'hediondez': None, 'qualificadoras': [], 'majorantes': [], 'minorantes': [], 'agravantesAtenuantes': [], 'extincaoPunibilidade': [], 'jurisprudenciaQualificada': [], 'controversias': []},
        'palavrasChave': keywords,
    }

rows = [
 make_record('cpm-136','Hostilidade contra país estrangeiro','art. 136','Praticar o militar ato de hostilidade contra país estrangeiro, expondo o Brasil a perigo de guerra.',96,180,'Reclusão, de 8 a 15 anos.',['país estrangeiro','hostilidade','guerra']),
 make_record('cpm-149','Reunião de militares contra ordem ou disciplina','art. 149','Reunirem-se militares agindo contra ordem recebida de superior, recusando obediência ou praticando violência, nas hipóteses legais.',None,None,'Pena conforme as hipóteses e parágrafos do art. 149.',['disciplina militar','ordem superior','reunião']),
 make_record('cpm-205','Homicídio simples militar','art. 205','Matar alguém no âmbito da lei penal militar.',72,240,'Reclusão, de 6 a 20 anos.',['homicídio','militar']),
 make_record('cpm-240','Furto simples militar','art. 240','Subtrair, para si ou para outrem, coisa alheia móvel.',None,72,'Reclusão, até 6 anos.',['furto','patrimônio militar']),
 make_record('cpm-251','Estelionato militar','art. 251','Obter, para si ou para outrem, vantagem ilícita, em prejuízo alheio, induzindo ou mantendo alguém em erro por meio fraudulento.',24,84,'Reclusão, de 2 a 7 anos.',['estelionato','fraude','patrimônio']),
 make_record('cpm-290','Tráfico, posse ou uso de entorpecente em lugar sujeito à administração militar','art. 290','Receber, preparar, produzir, vender, fornecer, ter em depósito, transportar, trazer consigo, guardar, ministrar ou entregar a consumo substância entorpecente em lugar sujeito à administração militar, sem autorização ou em desacordo com determinação legal ou regulamentar.',None,60,'Reclusão, até 5 anos.',['entorpecente','droga','administração militar']),
 make_record('cpm-303','Peculato militar','art. 303','Apropriar-se ou desviar dinheiro, valor ou bem móvel público ou particular de que tenha posse ou detenção em razão do cargo ou comissão.',36,180,'Reclusão, de 3 a 15 anos.',['peculato','administração militar']),
 make_record('cpm-308','Corrupção passiva militar','art. 308','Solicitar ou receber vantagem indevida, ou aceitar promessa de tal vantagem, em razão da função.',24,144,'Reclusão, de 2 a 12 anos.',['corrupção passiva','vantagem indevida','função militar'],note='Redação e pena consultadas após alteração da Lei nº 14.688/2023.'),
]
for item in rows:
    if item['id'] not in existing:
        catalog['registros'].append(item)
path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + '\n')
print(f'added {sum(item["id"] not in existing for item in rows)} military records')
