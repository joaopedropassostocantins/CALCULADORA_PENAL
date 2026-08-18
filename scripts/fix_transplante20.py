import json
from pathlib import Path

path = Path('/home/ubuntu/work/CALCULADORA_PENAL/src/data/tiposPenais.json')
catalog = json.loads(path.read_text())
for record in catalog['registros']:
    if record['id'] == 'transplante-20':
        record['inventarioValidado'] = False
        record['usavelNaCalculadora'] = False
        record['vigencia']['estadoConferencia'] = 'pendente'
        record['vigencia']['observacoes'] = 'Pena exclusivamente pecuniária em dias-multa; manter bloqueado até a calculadora suportar esta unidade sem conversão indevida.'
        break
else:
    raise SystemExit('transplante-20 não encontrado')
path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + '\n')
print('fixed transplante-20 as pending/non-calculable')
