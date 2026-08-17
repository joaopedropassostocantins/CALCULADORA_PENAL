import json
from pathlib import Path

path = Path('/home/ubuntu/work/CALCULADORA_PENAL/src/data/tiposPenais.json')
catalog = json.loads(path.read_text())
existing = {record['id'] for record in catalog['registros']}
SOURCE = 'https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848.htm'
CUTOFF = catalog['dataCorte']

def make_record(id, device, name, desc, minimum, maximum, penalty, keywords, nature='basica', parent=None, unit='meses', laws=None, observation=None):
    return {
        'id': id, 'nomeJuridico': name, 'aliases': [], 'classe': 'crime', 'jurisdicao': 'comum', 'modulo': 'Código Penal',
        'norma': 'Decreto-Lei nº 2.848/1940', 'dispositivo': device, 'naturezaFigura': nature, 'tipoPaiId': parent,
        'descricaoObjetiva': desc,
        'pena': {'minimoMeses': minimum, 'maximoMeses': maximum, 'unidadePrincipal': unit, 'descricao': penalty, 'multa': None},
        'vigencia': {'estado': 'vigente', 'inicioVigenciaRedacao': '1940-12-07', 'dataConsulta': CUTOFF, 'estadoConferencia': 'pendente', 'observacoes': observation or 'Figura do Código Penal localizada no texto oficial; inventário e enriquecimento pendentes antes do cálculo.'},
        'fonteOficial': SOURCE, 'leiCriadoraOuModificadora': laws or ['Decreto-Lei nº 2.848/1940'], 'inventarioValidado': False,
        'enriquecimentoValidado': False, 'usavelNaCalculadora': False,
        'enriquecimento': {'bemJuridico': None, 'sujeitoAtivo': None, 'sujeitoPassivo': None, 'elementoSubjetivo': None, 'consumacao': None, 'tentativa': None, 'formaCulposa': None, 'acaoPenal': None, 'competencia': 'comum', 'procedimento': None, 'rito': None, 'hediondez': None, 'qualificadoras': [], 'majorantes': [], 'minorantes': [], 'agravantesAtenuantes': [], 'extincaoPunibilidade': [], 'jurisprudenciaQualificada': [], 'controversias': []},
        'palavrasChave': keywords,
    }
new = [
 make_record('cp-134','art. 134','Exposição ou abandono de recém-nascido','Expor ou abandonar recém-nascido para ocultar desonra própria.',6,24,'Detenção, de 6 meses a 2 anos.',['recém-nascido','abandono']),
 make_record('cp-134-1','art. 134, § 1º','Exposição ou abandono de recém-nascido com lesão grave','Se da exposição ou abandono de recém-nascido resulta lesão corporal de natureza grave.',12,36,'Detenção, de 1 a 3 anos.',['recém-nascido','lesão grave'],'qualificada','cp-134'),
 make_record('cp-134-2','art. 134, § 2º','Exposição ou abandono de recém-nascido com morte','Se da exposição ou abandono de recém-nascido resulta morte.',24,72,'Detenção, de 2 a 6 anos.',['recém-nascido','morte'],'qualificada','cp-134'),
 make_record('cp-135','art. 135','Omissão de socorro','Deixar de prestar assistência, quando possível sem risco pessoal, a pessoa nas situações de desamparo ou grave e iminente perigo, ou não pedir socorro da autoridade pública.',1,6,'Detenção, de 1 a 6 meses, ou multa.',['omissão de socorro']),
 make_record('cp-135a','art. 135-A','Condicionamento de atendimento médico-hospitalar emergencial','Exigir cheque-caução, nota promissória, garantia ou preenchimento prévio de formulários como condição para atendimento médico-hospitalar emergencial.',3,12,'Detenção, de 3 meses a 1 ano, e multa.',['atendimento médico','cheque-caução'],laws=['Decreto-Lei nº 2.848/1940','Lei nº 12.653/2012']),
 make_record('cp-136','art. 136','Maus-tratos','Expor a perigo a vida ou a saúde de pessoa sob autoridade, guarda ou vigilância para educação, ensino, tratamento ou custódia, mediante privação de alimentação ou cuidados, trabalho excessivo ou abuso de correção.',24,60,'Reclusão, de 2 a 5 anos.',['maus-tratos','criança'],laws=['Decreto-Lei nº 2.848/1940','Lei nº 15.163/2025']),
 make_record('cp-136-1','art. 136, § 1º','Maus-tratos com lesão grave','Se dos maus-tratos resulta lesão corporal de natureza grave.',36,84,'Reclusão, de 3 a 7 anos.',['maus-tratos','lesão grave'],'qualificada','cp-136',laws=['Decreto-Lei nº 2.848/1940','Lei nº 15.163/2025']),
 make_record('cp-136-2','art. 136, § 2º','Maus-tratos com morte','Se dos maus-tratos resulta morte.',96,168,'Reclusão, de 8 a 14 anos.',['maus-tratos','morte'],'qualificada','cp-136',laws=['Decreto-Lei nº 2.848/1940','Lei nº 15.163/2025']),
 make_record('cp-137','art. 137','Rixa','Participar de rixa, salvo para separar os contendores.',0.5,2,'Detenção, de 15 dias a 2 meses, ou multa.',['rixa']),
 make_record('cp-137-pu','art. 137, parágrafo único','Rixa com morte ou lesão grave','Se ocorre morte ou lesão corporal de natureza grave na rixa.',6,24,'Detenção, de 6 meses a 2 anos.',['rixa','lesão grave','morte'],'qualificada','cp-137'),
 make_record('cp-138','art. 138','Calúnia','Caluniar alguém, imputando-lhe falsamente fato definido como crime.',6,24,'Detenção, de 6 meses a 2 anos, e multa.',['calúnia','honra']),
 make_record('cp-139','art. 139','Difamação','Difamar alguém, imputando-lhe fato ofensivo à sua reputação.',3,12,'Detenção, de 3 meses a 1 ano, e multa.',['difamação','honra']),
 make_record('cp-140','art. 140','Injúria','Injuriar alguém, ofendendo-lhe a dignidade ou o decoro.',1,6,'Detenção, de 1 a 6 meses, ou multa.',['injúria','honra']),
 make_record('cp-140-2','art. 140, § 2º','Injúria real','Se a injúria consiste em violência ou vias de fato aviltantes.',3,12,'Detenção, de 3 meses a 1 ano, e multa, além da pena correspondente à violência.',['injúria real','violência'],'qualificada','cp-140'),
 make_record('cp-140-3','art. 140, § 3º','Injúria qualificada por religião, idade ou deficiência','Se a injúria consiste na utilização de elementos referentes à religião ou à condição de pessoa idosa ou com deficiência.',12,36,'Reclusão, de 1 a 3 anos, e multa.',['injúria qualificada','religião','pessoa idosa','deficiência'],'qualificada','cp-140',laws=['Decreto-Lei nº 2.848/1940','Lei nº 14.532/2023']),
 make_record('cp-146','art. 146','Constrangimento ilegal','Constranger alguém, mediante violência ou grave ameaça, ou reduzindo sua capacidade de resistência, a não fazer o que a lei permite ou a fazer o que ela não manda.',0.5,12,'Detenção, de 3 meses a 1 ano, ou multa.',['constrangimento ilegal']),
 make_record('cp-146a','art. 146-A','Intimidação sistemática (bullying)','Intimidar sistematicamente, individualmente ou em grupo, mediante violência física ou psicológica, de modo intencional e repetitivo, por atos de intimidação, humilhação, discriminação ou ações previstas no tipo.',None,None,'Multa, se a conduta não constituir crime mais grave.',['bullying','intimidação sistemática'],unit='sem-pena-privativa',laws=['Decreto-Lei nº 2.848/1940','Lei nº 14.811/2024']),
 make_record('cp-146a-pu','art. 146-A, parágrafo único','Intimidação sistemática virtual (cyberbullying)','Se a intimidação sistemática é realizada por rede de computadores, rede social, aplicativo, jogo on-line ou outro meio ou ambiente digital.',24,48,'Reclusão, de 2 a 4 anos, e multa, se a conduta não constituir crime mais grave.',['cyberbullying','ambiente digital'],'qualificada','cp-146a',laws=['Decreto-Lei nº 2.848/1940','Lei nº 14.811/2024']),
 make_record('cp-147a','art. 147-A','Perseguição','Perseguir alguém reiteradamente por qualquer meio, ameaçando sua integridade, restringindo sua locomoção ou perturbando sua liberdade ou privacidade.',6,24,'Reclusão, de 6 meses a 2 anos, e multa.',['perseguição','stalking'],laws=['Decreto-Lei nº 2.848/1940','Lei nº 14.132/2021']),
 make_record('cp-150','art. 150','Violação de domicílio','Entrar ou permanecer clandestina ou astuciosamente, ou contra a vontade de quem de direito, em casa alheia ou dependências.',1,3,'Detenção, de 1 a 3 meses, ou multa.',['violação de domicílio','casa']),
 make_record('cp-150-1','art. 150, § 1º','Violação de domicílio qualificada','Se a violação de domicílio é cometida durante a noite, em lugar ermo, com violência ou arma, ou por duas ou mais pessoas.',6,24,'Detenção, de 6 meses a 2 anos, além da pena correspondente à violência.',['violação de domicílio','arma'],'qualificada','cp-150'),
 make_record('cp-151','art. 151','Violação de correspondência','Devassar indevidamente o conteúdo de correspondência fechada dirigida a outrem.',1,6,'Detenção, de 1 a 6 meses, ou multa.',['correspondência','comunicação']),
 make_record('cp-151-3','art. 151, § 3º','Violação de correspondência com abuso de função','Cometer crime de violação de correspondência com abuso de função em serviço postal, telegráfico, radioelétrico ou telefônico.',12,36,'Detenção, de 1 a 3 anos.',['correspondência','abuso de função'],'qualificada','cp-151'),
 make_record('cp-152','art. 152','Correspondência comercial','Abusar da condição de sócio ou empregado de estabelecimento comercial ou industrial para desviar, sonegar, subtrair ou suprimir correspondência, ou revelar a estranho seu conteúdo.',3,24,'Detenção, de 3 meses a 2 anos.',['correspondência comercial']),
 make_record('cp-153','art. 153','Divulgação de segredo','Divulgar sem justa causa conteúdo de documento particular ou de correspondência confidencial cuja divulgação possa produzir dano a outrem.',0.5,6,'Detenção, de 1 a 6 meses, ou multa histórica prevista no texto legal.',['divulgação de segredo','documento particular'],observation='A fonte oficial mantém referência a multa histórica em réis, com remissão à Lei nº 7.209/1984; registro pendente e não calculável até normalização segura da sanção pecuniária.'),
 make_record('cp-153-1a','art. 153, § 1º-A','Divulgação de informação sigilosa da Administração Pública','Divulgar sem justa causa informações sigilosas ou reservadas, definidas em lei, contidas ou não em sistemas de informações ou banco de dados da Administração Pública.',12,48,'Detenção, de 1 a 4 anos, e multa.',['informação sigilosa','Administração Pública'],'qualificada','cp-153',laws=['Decreto-Lei nº 2.848/1940','Lei nº 9.983/2000']),
 make_record('cp-154','art. 154','Violação de segredo profissional','Revelar sem justa causa segredo conhecido em razão de função, ministério, ofício ou profissão, cuja revelação possa produzir dano a outrem.',3,12,'Detenção, de 3 meses a 1 ano, ou multa histórica prevista no texto legal.',['segredo profissional','confidencialidade'],observation='A fonte oficial mantém referência a multa histórica em conto de réis, com remissão à Lei nº 7.209/1984; registro pendente e não calculável até normalização segura da sanção pecuniária.'),
]
for item in new:
    if item['id'] not in existing:
        catalog['registros'].append(item)
path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + '\n')
print(f'added {sum(item["id"] not in existing for item in new)} Código Penal personal-rights records')
