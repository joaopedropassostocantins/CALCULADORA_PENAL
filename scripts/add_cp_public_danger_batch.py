import json
from pathlib import Path

path = Path('/home/ubuntu/work/CALCULADORA_PENAL/src/data/tiposPenais.json')
catalog = json.loads(path.read_text())
existing = {record['id'] for record in catalog['registros']}
SOURCE = 'https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848.htm'
CUTOFF = catalog['dataCorte']

def make_record(id, device, name, desc, minimum, maximum, penalty, keywords, nature='basica', parent=None, laws=None, observation=None):
    return {
        'id': id, 'nomeJuridico': name, 'aliases': [], 'classe': 'crime', 'jurisdicao': 'comum', 'modulo': 'Código Penal',
        'norma': 'Decreto-Lei nº 2.848/1940', 'dispositivo': device, 'naturezaFigura': nature, 'tipoPaiId': parent,
        'descricaoObjetiva': desc,
        'pena': {'minimoMeses': minimum, 'maximoMeses': maximum, 'unidadePrincipal': 'meses', 'descricao': penalty, 'multa': None},
        'vigencia': {'estado': 'vigente', 'inicioVigenciaRedacao': '1940-12-07', 'dataConsulta': CUTOFF, 'estadoConferencia': 'pendente', 'observacoes': observation or 'Crime de perigo comum ou contra serviço público localizado na fonte oficial; inventário e enriquecimento pendentes antes do cálculo.'},
        'fonteOficial': SOURCE, 'leiCriadoraOuModificadora': laws or ['Decreto-Lei nº 2.848/1940'], 'inventarioValidado': False,
        'enriquecimentoValidado': False, 'usavelNaCalculadora': False,
        'enriquecimento': {'bemJuridico': None, 'sujeitoAtivo': None, 'sujeitoPassivo': None, 'elementoSubjetivo': None, 'consumacao': None, 'tentativa': None, 'formaCulposa': None, 'acaoPenal': None, 'competencia': 'comum', 'procedimento': None, 'rito': None, 'hediondez': None, 'qualificadoras': [], 'majorantes': [], 'minorantes': [], 'agravantesAtenuantes': [], 'extincaoPunibilidade': [], 'jurisprudenciaQualificada': [], 'controversias': []},
        'palavrasChave': keywords,
    }
new = [
 make_record('cp-250','art. 250, caput','Incêndio','Causar incêndio expondo a perigo a vida, a integridade física ou o patrimônio de outrem.',36,72,'Reclusão, de 3 a 6 anos, e multa.',['incêndio','perigo comum']),
 make_record('cp-250-2','art. 250, § 2º','Incêndio culposo','Causar culposamente incêndio expondo a perigo a vida, a integridade física ou o patrimônio de outrem.',6,24,'Detenção, de 6 meses a 2 anos.',['incêndio','culposo'],'culposa','cp-250'),
 make_record('cp-251','art. 251, caput','Explosão','Expor a perigo a vida, a integridade física ou o patrimônio de outrem mediante explosão, arremesso ou colocação de engenho explosivo.',36,72,'Reclusão, de 3 a 6 anos, e multa.',['explosão','engenho explosivo']),
 make_record('cp-251-1','art. 251, § 1º','Explosão com substância não equiparada a dinamite','Praticar explosão usando substância que não é dinamite ou explosivo de efeitos análogos.',12,48,'Reclusão, de 1 a 4 anos, e multa.',['explosão','substância explosiva'],'qualificada','cp-251'),
 make_record('cp-251-3a','art. 251, § 3º, primeira parte','Explosão culposa com dinamite','Causar culposamente explosão de dinamite ou substância de efeitos análogos.',6,24,'Detenção, de 6 meses a 2 anos.',['explosão','culposa','dinamite'],'culposa','cp-251'),
 make_record('cp-251-3b','art. 251, § 3º, segunda parte','Explosão culposa sem dinamite','Causar culposamente explosão nos demais casos previstos no art. 251.',3,12,'Detenção, de 3 meses a 1 ano.',['explosão','culposa'],'culposa','cp-251'),
 make_record('cp-252','art. 252','Uso de gás tóxico ou asfixiante','Expor a perigo a vida, a integridade física ou o patrimônio de outrem usando gás tóxico ou asfixiante.',12,48,'Reclusão, de 1 a 4 anos, e multa.',['gás tóxico','asfixiante']),
 make_record('cp-252-pu','art. 252, parágrafo único','Uso culposo de gás tóxico ou asfixiante','Praticar culposamente o crime de uso de gás tóxico ou asfixiante.',3,12,'Detenção, de 3 meses a 1 ano.',['gás tóxico','culposa'],'culposa','cp-252'),
 make_record('cp-253','art. 253','Fabrico, fornecimento, aquisição, posse ou transporte de explosivos ou gás tóxico','Fabricar, fornecer, adquirir, possuir ou transportar sem licença substância ou engenho explosivo, gás tóxico ou asfixiante, ou material para sua fabricação.',6,24,'Detenção, de 6 meses a 2 anos, e multa.',['explosivo','gás tóxico']),
 make_record('cp-254','art. 254, primeira parte','Inundação dolosa','Causar inundação expondo a perigo a vida, a integridade física ou o patrimônio de outrem.',36,72,'Reclusão, de 3 a 6 anos, e multa.',['inundação','perigo comum']),
 make_record('cp-254-culposa','art. 254, segunda parte','Inundação culposa','Causar culposamente inundação expondo a perigo a vida, a integridade física ou o patrimônio de outrem.',6,24,'Detenção, de 6 meses a 2 anos.',['inundação','culposa'],'culposa','cp-254'),
 make_record('cp-255','art. 255','Perigo de inundação','Remover, destruir ou inutilizar obstáculo natural ou obra destinada a impedir inundação, expondo a perigo a vida, a integridade física ou o patrimônio de outrem.',12,36,'Reclusão, de 1 a 3 anos, e multa.',['inundação','obra de contenção']),
 make_record('cp-256','art. 256, caput','Desabamento ou desmoronamento','Causar desabamento ou desmoronamento expondo a perigo a vida, a integridade física ou o patrimônio de outrem.',12,48,'Reclusão, de 1 a 4 anos, e multa.',['desabamento','desmoronamento']),
 make_record('cp-256-pu','art. 256, parágrafo único','Desabamento ou desmoronamento culposo','Causar culposamente desabamento ou desmoronamento expondo a perigo a vida, a integridade física ou o patrimônio de outrem.',6,12,'Detenção, de 6 meses a 1 ano.',['desabamento','culposa'],'culposa','cp-256'),
 make_record('cp-257','art. 257','Subtração, ocultação ou inutilização de material de salvamento','Subtrair, ocultar ou inutilizar material de combate ao perigo, socorro ou salvamento, ou impedir ou dificultar serviço dessa natureza.',24,60,'Reclusão, de 2 a 5 anos, e multa.',['material de salvamento','desastre']),
 make_record('cp-259','art. 259, caput','Difusão de doença ou praga','Difundir doença ou praga que possa causar dano a floresta, plantação ou animais de utilidade econômica.',24,60,'Reclusão, de 2 a 5 anos, e multa.',['doença','praga','floresta']),
 make_record('cp-259-pu','art. 259, parágrafo único','Difusão culposa de doença ou praga','Difundir culposamente doença ou praga que possa causar dano a floresta, plantação ou animais de utilidade econômica.',1,6,'Detenção, de 1 a 6 meses, ou multa.',['doença','praga','culposa'],'culposa','cp-259'),
 make_record('cp-260','art. 260, caput','Perigo de desastre ferroviário','Impedir ou perturbar serviço ferroviário por destruição, dano, obstáculo, falso aviso ou outro ato capaz de resultar desastre.',24,60,'Reclusão, de 2 a 5 anos, e multa.',['ferrovia','desastre ferroviário']),
 make_record('cp-260-1','art. 260, § 1º','Desastre ferroviário doloso','Se do perigo de desastre ferroviário resulta desastre.',48,144,'Reclusão, de 4 a 12 anos, e multa.',['ferrovia','desastre'],'qualificada','cp-260'),
 make_record('cp-260-2','art. 260, § 2º','Desastre ferroviário culposo','Se, por culpa, ocorre desastre ferroviário.',6,24,'Detenção, de 6 meses a 2 anos.',['ferrovia','desastre','culposa'],'culposa','cp-260'),
 make_record('cp-261','art. 261, caput','Atentado contra a segurança de transporte marítimo, fluvial ou aéreo','Expor a perigo embarcação ou aeronave, ou praticar ato tendente a impedir ou dificultar navegação marítima, fluvial ou aérea.',24,60,'Reclusão, de 2 a 5 anos.',['transporte marítimo','aeronave','navegação']),
 make_record('cp-261-1','art. 261, § 1º','Sinistro em transporte marítimo, fluvial ou aéreo','Se do atentado resulta naufrágio, submersão, encalhe, queda ou destruição de aeronave.',48,144,'Reclusão, de 4 a 12 anos.',['naufrágio','aeronave','sinistro'],'qualificada','cp-261'),
 make_record('cp-261-3','art. 261, § 3º','Sinistro culposo em transporte marítimo, fluvial ou aéreo','Se, por culpa, ocorre sinistro de transporte marítimo, fluvial ou aéreo.',6,24,'Detenção, de 6 meses a 2 anos.',['transporte','sinistro','culposa'],'culposa','cp-261'),
 make_record('cp-262','art. 262, caput','Atentado contra a segurança de outro meio de transporte','Expor a perigo outro meio de transporte público, ou impedir ou dificultar seu funcionamento.',12,24,'Detenção, de 1 a 2 anos.',['transporte público','perigo']),
 make_record('cp-262-1','art. 262, § 1º','Desastre em outro meio de transporte','Se do atentado contra outro meio de transporte resulta desastre.',24,60,'Reclusão, de 2 a 5 anos.',['transporte público','desastre'],'qualificada','cp-262'),
 make_record('cp-262-2','art. 262, § 2º','Desastre culposo em outro meio de transporte','Se, por culpa, ocorre desastre em outro meio de transporte público.',3,12,'Detenção, de 3 meses a 1 ano.',['transporte público','desastre','culposa'],'culposa','cp-262'),
 make_record('cp-264','art. 264, caput','Arremesso de projétil','Arremessar projétil contra veículo em movimento destinado ao transporte público por terra, água ou ar.',1,6,'Detenção, de 1 a 6 meses.',['projétil','transporte público']),
 make_record('cp-264-pu-lesao','art. 264, parágrafo único, lesão corporal','Arremesso de projétil com lesão corporal','Se do arremesso de projétil contra veículo resulta lesão corporal.',6,24,'Detenção, de 6 meses a 2 anos.',['projétil','lesão corporal'],'qualificada','cp-264'),
 make_record('cp-264-pu-morte','art. 264, parágrafo único, morte','Arremesso de projétil com morte','Se do arremesso de projétil contra veículo resulta morte.',None,None,'Pena do homicídio culposo, aumentada de um terço.',['projétil','morte'],'qualificada','cp-264',observation='Pena remissiva ao art. 121, § 3º, aumentada de um terço; não convertida em faixa numérica para evitar cálculo incorreto.'),
 make_record('cp-265','art. 265','Atentado contra a segurança de serviço de utilidade pública','Atentar contra a segurança ou o funcionamento de serviço de água, luz, força, calor ou outro serviço de utilidade pública.',12,60,'Reclusão, de 1 a 5 anos, e multa.',['serviço público','água','energia']),
 make_record('cp-266','art. 266','Interrupção ou perturbação de serviço telegráfico, telefônico, informático, telemático ou de informação de utilidade pública','Interromper ou perturbar serviço de comunicação ou informação de utilidade pública, ou impedir ou dificultar seu restabelecimento.',24,48,'Reclusão, de 2 a 4 anos, e multa.',['telecomunicações','serviço de informação'],laws=['Decreto-Lei nº 2.848/1940','Lei nº 12.737/2012','Lei nº 15.397/2026']),
]
for item in new:
    if item['id'] not in existing:
        catalog['registros'].append(item)
path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + '\n')
print(f'added {sum(item["id"] not in existing for item in new)} public danger records')
