import json
from pathlib import Path
catalog = json.loads(Path('/home/ubuntu/work/CALCULADORA_PENAL/src/data/tiposPenais.json').read_text())
records = [r for r in catalog['registros'] if r.get('modulo') == 'Código Penal']
for r in records:
    print(f"{r['id']}\t{r['dispositivo']}\t{r['nomeJuridico']}")
print(f'TOTAL {len(records)}')
