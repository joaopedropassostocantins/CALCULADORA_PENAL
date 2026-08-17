import json
from pathlib import Path

path = Path('/home/ubuntu/work/CALCULADORA_PENAL/src/data/tiposPenais.json')
catalog = json.loads(path.read_text())
for record in catalog['registros']:
    if record['id'].startswith('raciais-7716-20-'):
        record['tipoPaiId'] = 'raciais-7716-20'
path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + '\n')
print('fixed racial qualified parent references')
