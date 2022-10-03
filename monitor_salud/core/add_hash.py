from typing import Dict, Any
import hashlib
import json

def generate_hash(req_json: Dict[str, Any], codigo_seguridad):
    codigo_hash = hashlib.md5()
    json_ecoded= json.dumps(req_json, sort_keys=True).encode()
    codigo_seguridad_encoded = codigo_seguridad.encode()
    codigo_hash.update(json_ecoded)
    codigo_hash.update(codigo_seguridad_encoded)
    return codigo_hash.hexdigest()