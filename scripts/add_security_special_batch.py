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
        'vigencia': {'estado': 'vigente', 'inicioVigenciaRedacao': None, 'dataConsulta': CUT_OFF, 'estadoConferencia': 'pendente', 'observacoes': note},
        'fonteOficial': source, 'leiCriadoraOuModificadora': [law], 'inventarioValidado': False,
        'enriquecimentoValidado': False, 'usavelNaCalculadora': False,
        'enriquecimento': {'bemJuridico': None, 'sujeitoAtivo': None, 'sujeitoPassivo': None, 'elementoSubjetivo': None, 'consumacao': None, 'tentativa': None, 'formaCulposa': None, 'acaoPenal': None, 'competencia': None, 'procedimento': None, 'rito': None, 'hediondez': None, 'qualificadoras': [], 'majorantes': [], 'minorantes': [], 'agravantesAtenuantes': [], 'extincaoPunibilidade': [], 'jurisprudenciaQualificada': [], 'controversias': []},
        'palavrasChave': keywords,
    }

TORTURE = 'https://www.planalto.gov.br/ccivil_03/leis/l9455.htm'
TERROR = 'https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2016/lei/l13260.htm'
STATE = 'https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/l14197.htm'
new = [
 make_record('tortura-1','Tortura','art. 1º, caput e incisos I a III','Constranger alguém com violência ou grave ameaça causando sofrimento físico ou mental para obter informação, provocar ato criminoso ou por discriminação; submeter pessoa sob guarda, poder ou autoridade a intenso sofrimento como castigo; ou submeter mulher reiteradamente a intenso sofrimento no contexto de violência doméstica.',24,96,'Reclusão, de 2 a 8 anos.','Lei nº 9.455/1997',TORTURE,'Crimes de tortura',['tortura','sofrimento físico','violência doméstica'],'Redação do inciso III consultada com alteração da Lei nº 15.410/2026; aguarda conferência temporal detalhada.'),
 make_record('tortura-1-2','Omissão diante de tortura','art. 1º, § 2º','Omitir-se diante de condutas de tortura quando tinha o dever de evitá-las ou apurá-las.',12,48,'Detenção, de 1 a 4 anos.','Lei nº 9.455/1997',TORTURE,'Crimes de tortura',['tortura','omissão','dever de apuração'],'Tipo autônomo consultado na fonte oficial.'),
 make_record('tortura-1-3','Tortura com lesão grave ou gravíssima','art. 1º, § 3º, primeira parte','Praticar tortura da qual resulta lesão corporal de natureza grave ou gravíssima.',48,120,'Reclusão, de 4 a 10 anos.','Lei nº 9.455/1997',TORTURE,'Crimes de tortura',['tortura','lesão grave'],'Resultado qualificativo pendente de reconciliação com a figura-base.'),
 make_record('tortura-1-3-morte','Tortura com resultado morte','art. 1º, § 3º, segunda parte','Praticar tortura da qual resulta morte.',96,192,'Reclusão, de 8 a 16 anos.','Lei nº 9.455/1997',TORTURE,'Crimes de tortura',['tortura','morte'],'Resultado qualificativo pendente de reconciliação com a figura-base.'),
 make_record('terrorismo-2','Terrorismo','art. 2º, caput e § 1º','Praticar atos de terrorismo por razões de xenofobia, discriminação ou preconceito com finalidade de provocar terror social ou generalizado.',144,360,'Reclusão, de 12 a 30 anos, além das sanções correspondentes à ameaça ou violência.','Lei nº 13.260/2016',TERROR,'Terrorismo',['terrorismo','terror social','explosivo'],'Tipo-base consultado na fonte oficial.'),
 make_record('terrorismo-3','Organização terrorista','art. 3º','Promover, constituir, integrar ou prestar auxílio, pessoalmente ou por interposta pessoa, a organização terrorista.',60,96,'Reclusão, de 5 a 8 anos, e multa.','Lei nº 13.260/2016',TERROR,'Terrorismo',['organização terrorista','terrorismo'],'Tipo autônomo consultado na fonte oficial.'),
 make_record('terrorismo-5','Atos preparatórios de terrorismo','art. 5º','Realizar atos preparatórios de terrorismo com propósito inequívoco de consumar o delito, incluindo recrutamento, transporte, municiamento ou treinamento nas hipóteses legais.',None,360,'Pena correspondente ao delito consumado, diminuída de fração legal.','Lei nº 13.260/2016',TERROR,'Terrorismo',['terrorismo','atos preparatórios','treinamento'],'Pena variável por remissão e redução legal; bloqueado até modelagem específica.'),
 make_record('terrorismo-6','Financiamento do terrorismo','art. 6º','Receber, prover, oferecer, obter, guardar, manter em depósito, solicitar ou investir recursos para planejamento, preparação ou execução de crimes de terrorismo.',180,360,'Reclusão, de 15 a 30 anos.','Lei nº 13.260/2016',TERROR,'Terrorismo',['financiamento','terrorismo','recursos']),
 make_record('estado-democratico-359i','Atentado à soberania','art. 359-I','Negociar com governo ou grupo estrangeiro para provocar guerra contra o país ou invadi-lo.',36,96,'Reclusão, de 3 a 8 anos.','Lei nº 14.197/2021',STATE,'Estado Democrático de Direito',['soberania','guerra']),
 make_record('estado-democratico-359j','Atentado à integridade nacional','art. 359-J','Praticar violência ou grave ameaça para desmembrar parte do território nacional e constituir país independente.',24,72,'Reclusão, de 2 a 6 anos, além da pena da violência.','Lei nº 14.197/2021',STATE,'Estado Democrático de Direito',['integridade nacional','território']),
 make_record('estado-democratico-359k','Espionagem','art. 359-K, caput','Entregar a governo estrangeiro, agentes ou organização criminosa estrangeira documento ou informação secretos ou ultrassecretos cuja revelação possa colocar em perigo a ordem constitucional ou a soberania.',36,144,'Reclusão, de 3 a 12 anos.','Lei nº 14.197/2021',STATE,'Estado Democrático de Direito',['espionagem','segredo','soberania']),
 make_record('estado-democratico-359k-2','Espionagem com violação de sigilo','art. 359-K, § 2º','Transmitir ou revelar documento, dado ou informação secretos ou ultrassecretos com violação do dever de sigilo.',72,180,'Reclusão, de 6 a 15 anos.','Lei nº 14.197/2021',STATE,'Estado Democrático de Direito',['espionagem','sigilo']),
 make_record('estado-democratico-359k-3','Facilitação de espionagem por acesso','art. 359-K, § 3º','Facilitar espionagem mediante fornecimento ou empréstimo de senha ou forma de acesso a sistemas de informações a pessoas não autorizadas.',12,48,'Detenção, de 1 a 4 anos.','Lei nº 14.197/2021',STATE,'Estado Democrático de Direito',['espionagem','senha','sistema']),
 make_record('estado-democratico-359l','Abolição violenta do Estado Democrático de Direito','art. 359-L','Tentar, com violência ou grave ameaça, abolir o Estado Democrático de Direito impedindo ou restringindo o exercício dos poderes constitucionais.',48,96,'Reclusão, de 4 a 8 anos, além da pena da violência.','Lei nº 14.197/2021',STATE,'Estado Democrático de Direito',['Estado Democrático','violência','poderes constitucionais']),
 make_record('estado-democratico-359m','Golpe de Estado','art. 359-M','Tentar depor por violência ou grave ameaça o governo legitimamente constituído.',48,144,'Reclusão, de 4 a 12 anos, além da pena da violência.','Lei nº 14.197/2021',STATE,'Estado Democrático de Direito',['golpe de Estado','governo']),
 make_record('estado-democratico-359n','Interrupção do processo eleitoral','art. 359-N','Impedir ou perturbar eleição ou aferição de resultado mediante violação indevida de mecanismos de segurança do sistema eletrônico de votação.',36,72,'Reclusão, de 3 a 6 anos, e multa.','Lei nº 14.197/2021',STATE,'Estado Democrático de Direito',['eleição','urna eletrônica','segurança']),
 make_record('estado-democratico-359r','Sabotagem','art. 359-R','Destruir ou inutilizar meios de comunicação, instalações ou serviços destinados à defesa nacional com fim de abolir o Estado Democrático de Direito.',24,96,'Reclusão, de 2 a 8 anos.','Lei nº 14.197/2021',STATE,'Estado Democrático de Direito',['sabotagem','defesa nacional']),
]
for item in new:
    if item['id'] not in existing:
        catalog['registros'].append(item)
path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + '\n')
print(f'added {sum(item["id"] not in existing for item in new)} special-security records')
