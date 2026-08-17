import json
from pathlib import Path

path = Path('/home/ubuntu/work/CALCULADORA_PENAL/src/data/tiposPenais.json')
catalog = json.loads(path.read_text())
existing = {record['id'] for record in catalog['registros']}
CUT_OFF = catalog['dataCorte']

def make_record(id, name, device, desc, minimum, maximum, penalty, law, source, module, keywords):
    return {
        'id': id, 'nomeJuridico': name, 'aliases': [], 'classe': 'crime', 'jurisdicao': 'comum', 'modulo': module,
        'norma': law, 'dispositivo': device, 'naturezaFigura': 'basica', 'tipoPaiId': None,
        'descricaoObjetiva': desc,
        'pena': {'minimoMeses': minimum, 'maximoMeses': maximum, 'unidadePrincipal': 'meses', 'descricao': penalty, 'multa': None},
        'vigencia': {'estado': 'vigente', 'inicioVigenciaRedacao': None, 'dataConsulta': CUT_OFF, 'estadoConferencia': 'pendente', 'observacoes': 'Tipo localizado em fonte oficial; cálculo bloqueado até auditoria de vigência, competência e enriquecimento jurídico.'},
        'fonteOficial': source, 'leiCriadoraOuModificadora': [law], 'inventarioValidado': False,
        'enriquecimentoValidado': False, 'usavelNaCalculadora': False,
        'enriquecimento': {'bemJuridico': None, 'sujeitoAtivo': None, 'sujeitoPassivo': None, 'elementoSubjetivo': None, 'consumacao': None, 'tentativa': None, 'formaCulposa': None, 'acaoPenal': None, 'competencia': None, 'procedimento': None, 'rito': None, 'hediondez': None, 'qualificadoras': [], 'majorantes': [], 'minorantes': [], 'agravantesAtenuantes': [], 'extincaoPunibilidade': [], 'jurisprudenciaQualificada': [], 'controversias': []},
        'palavrasChave': keywords,
    }
NUC = 'https://www.planalto.gov.br/ccivil_03/leis/l6453.htm'
IND = 'https://www.planalto.gov.br/ccivil_03/leis/l6001.htm'
new = [
 make_record('nuclear-6453-20','Uso não autorizado de material nuclear','art. 20','Produzir, processar, fornecer ou usar material nuclear sem autorização necessária ou para fim diverso do permitido em lei.',48,120,'Reclusão, de 4 a 10 anos.','Lei nº 6.453/1977',NUC,'Crimes nucleares',['material nuclear','energia nuclear']),
 make_record('nuclear-6453-21','Operação não autorizada de instalação nuclear','art. 21','Permitir o responsável pela instalação nuclear sua operação sem a necessária autorização.',24,72,'Reclusão, de 2 a 6 anos.','Lei nº 6.453/1977',NUC,'Crimes nucleares',['instalação nuclear','autorização']),
 make_record('nuclear-6453-22','Posse ou transporte não autorizado de material nuclear','art. 22','Possuir, adquirir, transferir, transportar, guardar ou trazer consigo material nuclear sem autorização necessária.',24,72,'Reclusão, de 2 a 6 anos.','Lei nº 6.453/1977',NUC,'Crimes nucleares',['material nuclear','posse','transporte']),
 make_record('nuclear-6453-23','Transmissão ilícita de informação nuclear sigilosa','art. 23','Transmitir ilicitamente informações sigilosas concernentes à energia nuclear.',48,96,'Reclusão, de 4 a 8 anos.','Lei nº 6.453/1977',NUC,'Crimes nucleares',['informação sigilosa','energia nuclear']),
 make_record('nuclear-6453-24','Extração ou comércio ilegal de minério nuclear','art. 24','Extrair, beneficiar ou comerciar ilegalmente minério nuclear.',24,72,'Reclusão, de 2 a 6 anos.','Lei nº 6.453/1977',NUC,'Crimes nucleares',['minério nuclear','extração']),
 make_record('nuclear-6453-25','Exportação ou importação não licenciada de material nuclear','art. 25','Exportar ou importar sem licença material nuclear, minérios nucleares ou materiais de interesse para energia nuclear.',24,96,'Reclusão, de 2 a 8 anos.','Lei nº 6.453/1977',NUC,'Crimes nucleares',['exportação','importação','material nuclear']),
 make_record('nuclear-6453-26','Violação de normas de segurança nuclear','art. 26','Deixar de observar normas de segurança ou proteção relativas à instalação, uso, transporte, posse ou guarda de material nuclear, expondo alguém a perigo.',24,96,'Reclusão, de 2 a 8 anos.','Lei nº 6.453/1977',NUC,'Crimes nucleares',['segurança nuclear','perigo']),
 make_record('nuclear-6453-27','Impedimento de instalação ou transporte nuclear','art. 27','Impedir ou dificultar o funcionamento de instalação nuclear ou o transporte de material nuclear.',48,120,'Reclusão, de 4 a 10 anos.','Lei nº 6.453/1977',NUC,'Crimes nucleares',['instalação nuclear','transporte']),
 make_record('indigena-6001-58-i','Ofensa ou perturbação de cultura indígena','art. 58, I','Escarnecer de cerimônia, rito, uso, costume ou tradição cultural indígena, vilipendiá-los ou perturbar sua prática.',1,3,'Detenção, de 1 a 3 meses.','Lei nº 6.001/1973',IND,'Crimes contra indígenas',['cultura indígena','cerimônia','tradição']),
 make_record('indigena-6001-58-ii','Exibição lucrativa de indígena ou comunidade','art. 58, II','Utilizar indígena ou comunidade indígena como objeto de propaganda turística ou de exibição para fins lucrativos.',2,6,'Detenção, de 2 a 6 meses.','Lei nº 6.001/1973',IND,'Crimes contra indígenas',['indígena','propaganda','exibição']),
 make_record('indigena-6001-58-iii','Fornecimento de bebidas alcoólicas a indígenas','art. 58, III','Propiciar aquisição, uso ou disseminação de bebidas alcoólicas em grupos tribais ou entre indígenas não integrados.',6,24,'Detenção, de 6 meses a 2 anos.','Lei nº 6.001/1973',IND,'Crimes contra indígenas',['indígena','bebida alcoólica','grupo tribal']),
]
for item in new:
    if item['id'] not in existing:
        catalog['registros'].append(item)
path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + '\n')
print(f'added {sum(item["id"] not in existing for item in new)} nuclear/indigenous records')
