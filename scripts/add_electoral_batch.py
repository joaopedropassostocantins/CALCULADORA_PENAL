import json
from pathlib import Path

path = Path('/home/ubuntu/work/CALCULADORA_PENAL/src/data/tiposPenais.json')
catalog = json.loads(path.read_text())
existing = {record['id'] for record in catalog['registros']}
SOURCE = 'https://www.planalto.gov.br/ccivil_03/leis/l4737compilado.htm'
CUT_OFF = catalog['dataCorte']

def make_record(num, name, desc, minimum, maximum, penalty, keywords):
    return {
        'id': f'eleitoral-4737-{num.lower().replace("º", "").replace("§", "par").replace(" ", "-").replace(".", "").replace(",", "-")}',
        'nomeJuridico': name, 'aliases': [], 'classe': 'crime', 'jurisdicao': 'eleitoral', 'modulo': 'Crimes eleitorais',
        'norma': 'Lei nº 4.737/1965', 'dispositivo': f'art. {num}', 'naturezaFigura': 'basica', 'tipoPaiId': None,
        'descricaoObjetiva': desc,
        'pena': {'minimoMeses': minimum, 'maximoMeses': maximum, 'unidadePrincipal': 'meses', 'descricao': penalty, 'multa': None},
        'vigencia': {'estado': 'vigente', 'inicioVigenciaRedacao': None, 'dataConsulta': CUT_OFF, 'estadoConferencia': 'pendente', 'observacoes': 'Crime eleitoral localizado no texto compilado oficial; cálculo bloqueado até suporte a dias-multa, penas máximas e reconciliação com leis eleitorais especiais.'},
        'fonteOficial': SOURCE, 'leiCriadoraOuModificadora': ['Lei nº 4.737/1965'], 'inventarioValidado': False,
        'enriquecimentoValidado': False, 'usavelNaCalculadora': False,
        'enriquecimento': {'bemJuridico': None, 'sujeitoAtivo': None, 'sujeitoPassivo': None, 'elementoSubjetivo': None, 'consumacao': None, 'tentativa': None, 'formaCulposa': None, 'acaoPenal': None, 'competencia': None, 'procedimento': None, 'rito': None, 'hediondez': None, 'qualificadoras': [], 'majorantes': [], 'minorantes': [], 'agravantesAtenuantes': [], 'extincaoPunibilidade': [], 'jurisprudenciaQualificada': [], 'controversias': []},
        'palavrasChave': keywords,
    }

rows = [
 ('289','Inscrição fraudulenta de eleitor','Inscrever-se fraudulentamente eleitor.',0,60,'Reclusão até 5 anos e pagamento de 5 a 15 dias-multa.',['alistamento','fraude']),
 ('290','Indução à inscrição eleitoral irregular','Induzir alguém a inscrever-se eleitor com infração de dispositivo do Código Eleitoral.',0,24,'Reclusão até 2 anos e pagamento de 15 a 30 dias-multa.',['alistamento','indução']),
 ('291','Inscrição fraudulenta por juiz','Efetuar o juiz, fraudulentamente, a inscrição de alistando.',0,60,'Reclusão até 5 anos e pagamento de 5 a 15 dias-multa.',['juiz eleitoral','alistamento']),
 ('292','Negativa ou retardamento ilegal de inscrição','Negar ou retardar autoridade judiciária, sem fundamento legal, a inscrição requerida.',None,None,'Pagamento de 30 a 60 dias-multa.',['alistamento','autoridade judiciária']),
 ('293','Perturbação ou impedimento do alistamento','Perturbar ou impedir de qualquer forma o alistamento.',0.5,6,'Detenção de 15 dias a 6 meses ou pagamento de 30 a 60 dias-multa.',['alistamento','perturbação']),
 ('295','Retenção de título eleitoral','Reter título eleitoral contra a vontade do eleitor.',0,2,'Detenção até 2 meses ou pagamento de 30 a 60 dias-multa.',['título eleitoral']),
 ('296','Desordem nos trabalhos eleitorais','Promover desordem que prejudique os trabalhos eleitorais.',0,2,'Detenção até 2 meses e pagamento de 60 a 90 dias-multa.',['desordem','eleição']),
 ('297','Impedimento do exercício do sufrágio','Impedir ou embaraçar o exercício do sufrágio.',0,6,'Detenção até 6 meses e pagamento de 60 a 100 dias-multa.',['sufrágio','eleição']),
 ('298','Prisão ou detenção eleitoral ilegal','Prender ou deter eleitor, membro de mesa, fiscal, delegado ou candidato com violação do art. 236.',0,48,'Reclusão até 4 anos.',['prisão','eleitor']),
 ('299','Corrupção eleitoral','Dar, oferecer, prometer, solicitar ou receber vantagem para obter ou dar voto ou conseguir ou prometer abstenção.',0,48,'Reclusão até 4 anos e pagamento de 5 a 15 dias-multa.',['corrupção eleitoral','voto']),
 ('300','Coação eleitoral por servidor público','Valer-se servidor público da autoridade para coagir alguém a votar ou não votar em candidato ou partido.',0,6,'Detenção até 6 meses e pagamento de 60 a 100 dias-multa.',['coação','servidor público','voto']),
 ('301','Coação eleitoral com violência ou grave ameaça','Usar violência ou grave ameaça para coagir alguém a votar ou não votar em candidato ou partido.',0,48,'Reclusão até 4 anos e pagamento de 5 a 15 dias-multa.',['violência','grave ameaça','voto']),
 ('302','Concentração fraudulenta de eleitores','Promover no dia da eleição concentração de eleitores para impedir, embaraçar ou fraudar o exercício do voto.',48,72,'Reclusão de 4 a 6 anos e pagamento de 200 a 300 dias-multa.',['transporte de eleitores','concentração','fraude']),
 ('303','Majoração de preços eleitorais','Majorar preços de utilidades e serviços necessários à realização das eleições.',None,None,'Pagamento de 250 a 300 dias-multa.',['preços','eleição']),
 ('304','Omissão ou exclusividade de utilidades eleitorais','Ocultar, sonegar, açambarcar ou recusar no dia da eleição fornecimento de utilidades, alimentação ou transporte, ou concedê-los com exclusividade.',None,None,'Pagamento de 250 a 300 dias-multa.',['transporte','alimentação','eleição']),
 ('305','Intervenção estranha na mesa receptora','Intervir autoridade estranha à mesa receptora no seu funcionamento.',0,6,'Detenção até 6 meses e pagamento de 60 a 90 dias-multa.',['mesa receptora','eleição']),
 ('306','Desrespeito à ordem de votação','Não observar a ordem em que os eleitores devem ser chamados a votar.',None,None,'Pagamento de 15 a 30 dias-multa.',['votação','mesa receptora']),
 ('307','Fornecimento de cédula oficial marcada','Fornecer ao eleitor cédula oficial já assinalada ou marcada.',0,60,'Reclusão até 5 anos e pagamento de 5 a 15 dias-multa.',['cédula','voto']),
 ('308','Rubrica ou entrega irregular de cédula','Rubricar e fornecer a cédula oficial em oportunidade diversa da entrega ao eleitor.',0,60,'Reclusão até 5 anos e pagamento de 60 a 90 dias-multa.',['cédula','mesa receptora']),
 ('309','Voto múltiplo ou em lugar de outrem','Votar ou tentar votar mais de uma vez ou em lugar de outrem.',0,36,'Reclusão até 3 anos.',['voto','fraude']),
 ('310','Irregularidade que anula votação','Praticar ou permitir na mesa receptora irregularidade que determine a anulação da votação.',0,6,'Detenção até 6 meses ou pagamento de 90 a 120 dias-multa.',['mesa receptora','anulação']),
 ('311','Voto fora da seção eleitoral','Votar em seção em que não está inscrito ou permitir que o voto seja admitido.',0,1,'Detenção até 1 mês ou pagamento de multa conforme a função.',['seção eleitoral','voto']),
 ('312','Violação do sigilo do voto','Violar ou tentar violar o sigilo do voto.',0,24,'Detenção até 2 anos.',['sigilo','voto']),
 ('317','Violação do sigilo da urna','Violar ou tentar violar o sigilo da urna ou dos invólucros.',36,60,'Reclusão de 3 a 5 anos.',['urna','sigilo']),
 ('320','Inscrição simultânea em partidos','Inscrever-se eleitor simultaneamente em dois ou mais partidos.',None,None,'Pagamento de 10 a 20 dias-multa.',['partido','alistamento']),
 ('321','Assinatura em múltiplas fichas partidárias','Colher a assinatura do eleitor em mais de uma ficha de registro de partido.',0,2,'Detenção até 2 meses ou pagamento de 20 a 40 dias-multa.',['partido','assinatura']),
 ('323','Divulgação de fato inverídico em propaganda','Divulgar na propaganda ou campanha eleitoral fato que sabe inverídico sobre partido ou candidato e capaz de influenciar o eleitorado.',2,12,'Detenção de 2 meses a 1 ano ou pagamento de 120 a 150 dias-multa.',['propaganda','fato inverídico']),
 ('324','Calúnia eleitoral','Caluniar alguém na propaganda eleitoral ou visando a fins de propaganda, imputando fato definido como crime.',6,24,'Detenção de 6 meses a 2 anos e pagamento de 10 a 40 dias-multa.',['calúnia','propaganda']),
 ('325','Difamação eleitoral','Difamar alguém na propaganda eleitoral ou visando a fins de propaganda, imputando fato ofensivo à reputação.',3,12,'Detenção de 3 meses a 1 ano e pagamento de 5 a 30 dias-multa.',['difamação','propaganda']),
 ('326','Injúria eleitoral','Injuriar alguém na propaganda eleitoral ou visando a fins de propaganda, ofendendo sua dignidade ou decoro.',0,6,'Detenção até 6 meses ou pagamento de 30 a 60 dias-multa.',['injúria','propaganda']),
 ('326-A','Denunciação caluniosa eleitoral','Dar causa à instauração de investigação ou processo atribuindo a alguém crime ou ato infracional que sabe inocente, com finalidade eleitoral.',24,96,'Reclusão de 2 a 8 anos e multa.',['denunciação caluniosa','investigação','eleição']),
 ('326-B','Violência política contra a mulher','Assediar, constranger, humilhar, perseguir ou ameaçar candidata ou detentora de mandato por menosprezo ou discriminação à condição de mulher ou cor, raça ou etnia.',12,48,'Reclusão de 1 a 4 anos e multa.',['violência política','mulher','eleição']),
 ('331','Perturbação de meio de propaganda','Inutilizar, alterar ou perturbar meio de propaganda devidamente empregado.',0,6,'Detenção até 6 meses ou pagamento de 90 a 120 dias-multa.',['propaganda','eleição']),
 ('332','Impedimento do exercício de propaganda','Impedir o exercício de propaganda.',0,6,'Detenção até 6 meses e pagamento de 30 a 60 dias-multa.',['propaganda','eleição']),
 ('334','Uso de organização comercial para propaganda ou aliciamento','Utilizar organização comercial de vendas, distribuição de mercadorias, prêmios e sorteios para propaganda ou aliciamento de eleitores.',6,12,'Detenção de 6 meses a 1 ano e cassação do registro se o responsável for candidato.',['propaganda','aliciamento']),
 ('335','Propaganda em língua estrangeira','Fazer propaganda eleitoral em língua estrangeira.',3,6,'Detenção de 3 a 6 meses e pagamento de 30 a 60 dias-multa.',['propaganda','língua estrangeira']),
 ('338','Omissão de prioridade postal eleitoral','Não assegurar funcionário postal a prioridade legal para remessa eleitoral.',None,None,'Pagamento de 30 a 60 dias-multa.',['serviço postal','eleição']),
 ('339','Destruição ou ocultação de urna ou documentos eleitorais','Destruir, suprimir ou ocultar urna contendo votos ou documentos relativos à eleição.',24,72,'Reclusão de 2 a 6 anos e pagamento de 5 a 15 dias-multa.',['urna','documentos','eleição']),
 ('340','Fabricação ou guarda de material eleitoral exclusivo','Fabricar, adquirir, fornecer, subtrair ou guardar urnas, mapas, cédulas ou papéis de uso exclusivo da Justiça Eleitoral.',0,36,'Reclusão até 3 anos e pagamento de 3 a 15 dias-multa.',['urna','cédula','Justiça Eleitoral']),
]
for row in rows:
    record = make_record(*row)
    if record['id'] not in existing:
        catalog['registros'].append(record)
path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + '\n')
print(f'added {sum(make_record(*row)["id"] not in existing for row in rows)} electoral records')
