import json
from pathlib import Path

path = Path('/home/ubuntu/work/CALCULADORA_PENAL/src/data/tiposPenais.json')
catalog = json.loads(path.read_text())
existing = {record['id'] for record in catalog['registros']}
ECA = 'https://www.planalto.gov.br/ccivil_03/leis/l8069.htm'
HENRY = 'https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2022/lei/l14344.htm'
RACE = 'https://www.planalto.gov.br/ccivil_03/leis/l7716.htm'
CUT_OFF = catalog['dataCorte']

def make_record(id, name, device, description, minimum, maximum, penalty, law, source, module, keywords, nature='basica', parent=None, note=None):
    return {
        'id': id, 'nomeJuridico': name, 'aliases': [], 'classe': 'crime', 'jurisdicao': 'comum', 'modulo': module,
        'norma': law, 'dispositivo': device, 'naturezaFigura': nature, 'tipoPaiId': parent,
        'descricaoObjetiva': description,
        'pena': {'minimoMeses': minimum, 'maximoMeses': maximum, 'unidadePrincipal': 'meses', 'descricao': penalty, 'multa': None},
        'vigencia': {'estado': 'vigente', 'inicioVigenciaRedacao': None, 'dataConsulta': CUT_OFF, 'estadoConferencia': 'confirmada', 'observacoes': note},
        'fonteOficial': source, 'leiCriadoraOuModificadora': [law], 'inventarioValidado': True,
        'enriquecimentoValidado': False, 'usavelNaCalculadora': True,
        'enriquecimento': {'bemJuridico': None, 'sujeitoAtivo': None, 'sujeitoPassivo': None, 'elementoSubjetivo': None, 'consumacao': None, 'tentativa': None, 'formaCulposa': None, 'acaoPenal': None, 'competencia': None, 'procedimento': None, 'rito': None, 'hediondez': None, 'qualificadoras': [], 'majorantes': [], 'minorantes': [], 'agravantesAtenuantes': [], 'extincaoPunibilidade': [], 'jurisprudenciaQualificada': [], 'controversias': []},
        'palavrasChave': keywords,
    }

new = []
# ECA — crimes dos arts. 228 a 244-C, apenas redações vigentes
new += [
 make_record('eca-228','Omissão de registro ou declaração de nascimento','art. 228','Deixar encarregado de serviço ou dirigente de estabelecimento de saúde de gestante de manter registros ou fornecer declaração de nascimento.',6,24,'Detenção, de 6 meses a 2 anos.','Lei nº 8.069/1990',ECA,'ECA',['criança','nascimento','registro']),
 make_record('eca-228-culposa','Omissão culposa de registro ou declaração de nascimento','art. 228, parágrafo único','Praticar culposamente a omissão prevista no art. 228.',2,6,'Detenção, de 2 a 6 meses, ou multa.','Lei nº 8.069/1990',ECA,'ECA',['criança','nascimento','culpa'],'culposa','eca-228'),
 make_record('eca-229','Omissão de identificação ou exames do neonato','art. 229','Deixar profissional ou dirigente de estabelecimento de saúde de identificar corretamente neonato e parturiente ou de proceder aos exames legais.',6,24,'Detenção, de 6 meses a 2 anos.','Lei nº 8.069/1990',ECA,'ECA',['neonato','parturiente','saúde']),
 make_record('eca-229-culposa','Omissão culposa de identificação ou exames','art. 229, parágrafo único','Praticar culposamente a omissão prevista no art. 229.',2,6,'Detenção, de 2 a 6 meses, ou multa.','Lei nº 8.069/1990',ECA,'ECA',['neonato','culpa'],'culposa','eca-229'),
 make_record('eca-230','Privação ilegal de liberdade de criança ou adolescente','art. 230','Privar criança ou adolescente de liberdade mediante apreensão sem flagrante de ato infracional ou ordem judicial escrita.',6,24,'Detenção, de 6 meses a 2 anos.','Lei nº 8.069/1990',ECA,'ECA',['apreensão ilegal','criança','adolescente']),
 make_record('eca-231','Omissão de comunicação de apreensão','art. 231','Deixar autoridade policial de comunicar imediatamente apreensão de criança ou adolescente à autoridade judicial e à família.',6,24,'Detenção, de 6 meses a 2 anos.','Lei nº 8.069/1990',ECA,'ECA',['apreensão','comunicação','autoridade policial']),
 make_record('eca-232','Submissão a vexame ou constrangimento','art. 232','Submeter criança ou adolescente sob autoridade, guarda ou vigilância a vexame ou constrangimento.',6,24,'Detenção, de 6 meses a 2 anos.','Lei nº 8.069/1990',ECA,'ECA',['vexame','constrangimento','criança']),
 make_record('eca-234','Omissão de liberação de criança ou adolescente','art. 234','Deixar autoridade competente, sem justa causa, de ordenar imediata liberação de criança ou adolescente após conhecimento da ilegalidade da apreensão.',6,24,'Detenção, de 6 meses a 2 anos.','Lei nº 8.069/1990',ECA,'ECA',['liberação','apreensão ilegal']),
 make_record('eca-235','Descumprimento de prazo em favor de adolescente privado de liberdade','art. 235','Descumprir injustificadamente prazo fixado no ECA em benefício de adolescente privado de liberdade.',6,24,'Detenção, de 6 meses a 2 anos.','Lei nº 8.069/1990',ECA,'ECA',['adolescente','privação de liberdade','prazo']),
 make_record('eca-236','Obstrução da atuação de autoridade de proteção','art. 236','Impedir ou embaraçar ação de autoridade judiciária, Conselho Tutelar ou Ministério Público no exercício de função prevista no ECA.',6,24,'Detenção, de 6 meses a 2 anos.','Lei nº 8.069/1990',ECA,'ECA',['Conselho Tutelar','Ministério Público','obstrução']),
 make_record('eca-237','Subtração de criança ou adolescente para colocação em lar substituto','art. 237','Subtrair criança ou adolescente ao poder de quem o tem sob guarda legal ou judicial com fim de colocação em lar substituto.',24,72,'Reclusão, de 2 a 6 anos, e multa.','Lei nº 8.069/1990',ECA,'ECA',['guarda','lar substituto','subtração']),
 make_record('eca-238','Entrega mediante paga ou recompensa','art. 238','Prometer ou efetivar entrega de filho ou pupilo a terceiro mediante paga ou recompensa, ou oferecer ou efetivar a paga.',12,48,'Reclusão, de 1 a 4 anos, e multa.','Lei nº 8.069/1990',ECA,'ECA',['adoção ilegal','paga','recompensa']),
 make_record('eca-239','Envio irregular de criança ou adolescente ao exterior','art. 239','Promover ou auxiliar ato destinado ao envio de criança ou adolescente ao exterior em desacordo com formalidades ou com finalidade de lucro.',48,72,'Reclusão, de 4 a 6 anos, e multa.','Lei nº 8.069/1990',ECA,'ECA',['envio ao exterior','criança','lucro']),
 make_record('eca-239-violencia','Envio ao exterior com violência, grave ameaça ou fraude','art. 239, parágrafo único','Praticar o crime do art. 239 com violência, grave ameaça ou fraude.',72,96,'Reclusão, de 6 a 8 anos, além da pena correspondente à violência.','Lei nº 8.069/1990',ECA,'ECA',['envio ao exterior','violência','fraude'],'qualificada','eca-239'),
 make_record('eca-240','Produção de conteúdo de violência sexual contra criança ou adolescente','art. 240','Produzir, reproduzir, dirigir, fotografar, filmar ou registrar conteúdo de violência sexual contra criança ou adolescente.',48,120,'Reclusão, de 4 a 10 anos, e multa.','Lei nº 8.069/1990',ECA,'ECA',['violência sexual','conteúdo digital','criança'],note='Redação vigente consultada com alteração da Lei nº 15.487/2026.'),
 make_record('eca-241','Venda ou exposição à venda de conteúdo de violência sexual','art. 241','Vender ou expor à venda fotografia, vídeo ou registro que contenha violência sexual contra criança ou adolescente.',48,120,'Reclusão, de 4 a 10 anos, e multa.','Lei nº 8.069/1990',ECA,'ECA',['violência sexual','venda','criança'],note='Redação vigente consultada com alteração da Lei nº 15.487/2026.'),
 make_record('eca-241a','Distribuição ou divulgação de conteúdo de violência sexual','art. 241-A','Oferecer, trocar, disponibilizar, transmitir, distribuir, publicar ou divulgar registro de violência sexual contra criança ou adolescente.',48,120,'Reclusão, de 4 a 10 anos, e multa.','Lei nº 8.069/1990',ECA,'ECA',['violência sexual','internet','divulgação'],note='Redação vigente consultada com alteração da Lei nº 15.487/2026.'),
 make_record('eca-241b','Aquisição, posse ou armazenamento de conteúdo de violência sexual','art. 241-B','Adquirir, possuir, armazenar ou solicitar registro de violência sexual contra criança ou adolescente.',36,72,'Reclusão, de 3 a 6 anos, e multa.','Lei nº 8.069/1990',ECA,'ECA',['violência sexual','posse','armazenamento'],note='Redação vigente consultada com alteração da Lei nº 15.487/2026.'),
 make_record('eca-241c','Simulação digital de violência sexual contra criança ou adolescente','art. 241-C','Simular conteúdo de violência sexual envolvendo criança ou adolescente por adulteração, montagem ou modificação, inclusive com inteligência artificial.',36,60,'Reclusão, de 3 a 5 anos, e multa.','Lei nº 8.069/1990',ECA,'ECA',['violência sexual','deepfake','inteligência artificial'],note='Redação vigente consultada com alteração da Lei nº 15.487/2026.'),
 make_record('eca-241d','Aliciamento de menor de 14 anos para ato libidinoso','art. 241-D','Aliciar, assediar, convidar, instigar ou constranger menor de 14 anos por qualquer meio para praticar ato libidinoso.',36,60,'Reclusão, de 3 a 5 anos, e multa, se o fato não constituir crime mais grave.','Lei nº 8.069/1990',ECA,'ECA',['aliciamento','menor de 14 anos','ato libidinoso'],note='Redação vigente consultada com alteração da Lei nº 15.487/2026.'),
 make_record('eca-242','Fornecimento de arma a criança ou adolescente','art. 242','Vender, fornecer ou entregar a criança ou adolescente arma, munição ou explosivo.',36,72,'Reclusão, de 3 a 6 anos.','Lei nº 8.069/1990',ECA,'ECA',['arma','munição','adolescente']),
 make_record('eca-243','Fornecimento de bebida alcoólica ou produto capaz de causar dependência','art. 243','Vender, fornecer, servir, ministrar ou entregar a criança ou adolescente bebida alcoólica ou produto capaz de causar dependência, se o fato não for mais grave.',24,48,'Detenção, de 2 a 4 anos, e multa, se o fato não constitui crime mais grave.','Lei nº 8.069/1990',ECA,'ECA',['bebida alcoólica','dependência','adolescente']),
 make_record('eca-244','Fornecimento de fogos de estampido ou artifício','art. 244','Vender, fornecer ou entregar a criança ou adolescente fogos de estampido ou de artifício com potencial de dano físico.',6,24,'Detenção, de 6 meses a 2 anos, e multa.','Lei nº 8.069/1990',ECA,'ECA',['fogos de artifício','criança']),
 make_record('eca-244a','Exploração sexual de criança ou adolescente','art. 244-A','Submeter criança ou adolescente à exploração sexual, se o fato não constituir crime mais grave.',48,120,'Reclusão, de 4 a 10 anos e multa.','Lei nº 8.069/1990',ECA,'ECA',['exploração sexual','criança','adolescente'],note='Redação vigente consultada com alteração da Lei nº 15.487/2026.'),
 make_record('eca-244b','Corrupção de menor','art. 244-B','Corromper ou facilitar a corrupção de menor de 18 anos praticando com ele infração penal ou induzindo-o a praticá-la.',12,48,'Reclusão, de 1 a 4 anos.','Lei nº 8.069/1990',ECA,'ECA',['corrupção de menor','adolescente']),
 make_record('eca-244c','Omissão dolosa de comunicação de desaparecimento','art. 244-C','Deixar pai, mãe ou responsável legal de comunicar dolosamente à autoridade pública o desaparecimento de criança ou adolescente.',24,48,'Reclusão, de 2 a 4 anos, e multa.','Lei nº 8.069/1990',ECA,'ECA',['desaparecimento','criança','responsável legal']),
]
# Lei Henry Borel — arts. 25 e 26
new += [
 make_record('henry-borel-25','Descumprimento de medida protetiva de urgência contra criança ou adolescente','art. 25','Descumprir decisão judicial que defere medida protetiva de urgência prevista na Lei Henry Borel.',3,24,'Detenção, de 3 meses a 2 anos.','Lei nº 14.344/2022',HENRY,'Lei Henry Borel',['medida protetiva','violência doméstica','criança']),
 make_record('henry-borel-26','Omissão de comunicação de violência contra criança ou adolescente','art. 26','Deixar de comunicar à autoridade pública violência, tratamento cruel ou degradante, formas violentas de educação, correção ou disciplina contra criança ou adolescente ou abandono de incapaz.',6,36,'Detenção, de 6 meses a 3 anos.','Lei nº 14.344/2022',HENRY,'Lei Henry Borel',['omissão de comunicação','violência doméstica','abandono']),
]
# Lei 7.716/1989 — artigos penais vigentes
race_rows = [
 ('2a','Injúria racial','art. 2º-A','Injuriar alguém, ofendendo-lhe a dignidade ou o decoro em razão de raça, cor, etnia ou procedência nacional.',24,60,'Reclusão, de 2 a 5 anos, e multa.',[]),
 ('3','Discriminação no acesso a cargo público','art. 3º','Impedir ou obstar acesso de pessoa habilitada a cargo da Administração Pública ou de concessionária por discriminação.',24,60,'Reclusão, de 2 a 5 anos.',[]),
 ('4','Discriminação no emprego privado','art. 4º','Negar ou obstar emprego em empresa privada por discriminação ou preconceito.',24,60,'Reclusão, de 2 a 5 anos.',[]),
 ('5','Discriminação em estabelecimento comercial','art. 5º','Recusar ou impedir acesso a estabelecimento comercial, negando servir, atender ou receber cliente ou comprador.',12,36,'Reclusão, de 1 a 3 anos.',[]),
 ('6','Discriminação em estabelecimento de ensino','art. 6º','Recusar, negar ou impedir inscrição ou ingresso de aluno em estabelecimento de ensino.',36,60,'Reclusão, de 3 a 5 anos.',[]),
 ('7','Discriminação em hospedagem','art. 7º','Impedir acesso ou recusar hospedagem em hotel, pensão, estalagem ou estabelecimento similar.',36,60,'Reclusão, de 3 a 5 anos.',[]),
 ('8','Discriminação em restaurante ou bar','art. 8º','Impedir acesso ou recusar atendimento em restaurante, bar, confeitaria ou local semelhante aberto ao público.',12,36,'Reclusão, de 1 a 3 anos.',[]),
 ('9','Discriminação em estabelecimento esportivo ou de diversão','art. 9º','Impedir acesso ou recusar atendimento em estabelecimento esportivo, casa de diversões ou clube social aberto ao público.',12,36,'Reclusão, de 1 a 3 anos.',[]),
 ('10','Discriminação em salão ou estabelecimento similar','art. 10','Impedir acesso ou recusar atendimento em salão de cabeleireiro, barbearia, termas, casa de massagem ou similar.',12,36,'Reclusão, de 1 a 3 anos.',[]),
 ('11','Discriminação em edifício ou elevador','art. 11','Impedir acesso a entradas sociais, elevadores ou escadas de edifícios públicos ou residenciais.',12,36,'Reclusão, de 1 a 3 anos.',[]),
 ('12','Discriminação em transporte público','art. 12','Impedir acesso ou uso de transporte público concedido por discriminação.',12,36,'Reclusão, de 1 a 3 anos.',[]),
 ('13','Discriminação no acesso às Forças Armadas','art. 13','Impedir ou obstar acesso de alguém a serviço em qualquer ramo das Forças Armadas.',24,48,'Reclusão, de 2 a 4 anos.',[]),
 ('14','Discriminação contra casamento ou convivência','art. 14','Impedir ou obstar por qualquer meio casamento ou convivência familiar e social.',24,48,'Reclusão, de 2 a 4 anos.',[]),
 ('20','Discriminação ou preconceito','art. 20','Praticar, induzir ou incitar discriminação ou preconceito de raça, cor, etnia, religião ou procedência nacional.',12,36,'Reclusão, de 1 a 3 anos e multa.',[]),
 ('20-1','Propaganda nazista','art. 20, § 1º','Fabricar, comercializar, distribuir ou veicular símbolos ou propaganda com cruz suástica ou gamada para divulgação do nazismo.',24,60,'Reclusão, de 2 a 5 anos e multa.',[],'qualificada','race-20'),
 ('20-2','Discriminação por meio de comunicação','art. 20, § 2º','Praticar os crimes do art. 20 por meio de comunicação social, redes sociais, internet ou publicação.',24,60,'Reclusão, de 2 a 5 anos e multa.',[],'qualificada','race-20'),
 ('20-2a','Discriminação em atividades públicas específicas','art. 20, § 2º-A','Praticar os crimes do art. 20 em contexto de atividades esportivas, religiosas, artísticas ou culturais destinadas ao público.',24,60,'Reclusão, de 2 a 5 anos e proibição de frequência a locais públicos específicos.',[],'qualificada','race-20'),
 ('20-2b','Violência ou obstrução de manifestação religiosa','art. 20, § 2º-B','Obstar, impedir ou empregar violência contra manifestações ou práticas religiosas, sem prejuízo da pena correspondente à violência.',24,60,'Reclusão, de 2 a 5 anos e multa, sem prejuízo da pena da violência.',[],'qualificada','race-20'),
]
for num,name,device,desc,minimum,maximum,penalty,keywords,*tail in race_rows:
    nature = tail[0] if tail else 'basica'
    parent = tail[1] if len(tail) > 1 else None
    new.append(make_record(f'raciais-7716-{num}', name, device, desc, minimum, maximum, penalty, 'Lei nº 7.716/1989', RACE, 'Crimes raciais', ['racismo','discriminação','preconceito'] + keywords, nature, parent))

for item in new:
    if item['id'] not in existing:
        catalog['registros'].append(item)
path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + '\n')
print(f'added {sum(item["id"] not in existing for item in new)} records')
