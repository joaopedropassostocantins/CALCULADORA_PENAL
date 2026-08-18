import json
from pathlib import Path

path = Path('/home/ubuntu/work/CALCULADORA_PENAL/src/data/tiposPenais.json')
catalog = json.loads(path.read_text())
count = 0
for record in catalog['registros']:
    if record['classe'] == 'contravencao':
        record['inventarioValidado'] = False
        record['usavelNaCalculadora'] = False
        record['vigencia']['estadoConferencia'] = 'pendente'
        record['vigencia']['observacoes'] = 'Contravenção vigente consultada em texto oficial; inventário permanece pendente até normalização das penas históricas, prisão simples e multas.'
        count += 1
path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + '\n')
print(f'fixed {count} contraventions as pending/non-calculable')
