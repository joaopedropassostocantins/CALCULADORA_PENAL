import json
from pathlib import Path

path = Path('/home/ubuntu/work/CALCULADORA_PENAL/src/data/tiposPenais.json')
catalog = json.loads(path.read_text())
remove_ids = {
    'desarmamento-10826-12', 'desarmamento-10826-13', 'desarmamento-10826-14',
    'desarmamento-10826-15', 'desarmamento-10826-16', 'desarmamento-10826-17',
    'desarmamento-10826-18',
}
original = len(catalog['registros'])
catalog['registros'] = [record for record in catalog['registros'] if record['id'] not in remove_ids]
for record in catalog['registros']:
    if record['id'] == 'desarmamento-10826-16-2':
        record['modulo'] = 'Armas'
        record['tipoPaiId'] = 'armas-16'
        record['leiCriadoraOuModificadora'] = ['Lei nº 10.826/2003', 'Lei nº 13.964/2019']
path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + '\n')
print(f'removed {original - len(catalog["registros"])} duplicate disarmament records; kept qualified record')
