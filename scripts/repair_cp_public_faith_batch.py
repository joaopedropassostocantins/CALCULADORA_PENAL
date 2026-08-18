import json
from pathlib import Path

path = Path('/home/ubuntu/work/CALCULADORA_PENAL/src/data/tiposPenais.json')
catalog = json.loads(path.read_text())
for record in catalog['registros']:
    if record['id'] == 'cp-296-pu':
        record['naturezaFigura'] = 'qualificada'
        record['vigencia']['observacoes'] = 'Figura do art. 296, § 1º, III, com conduta própria e mesma pena do tipo-base; natureza normalizada para enumeração aceita pelo schema.'
path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + '\n')
print('normalized cp-296-pu naturezaFigura to qualificada')
