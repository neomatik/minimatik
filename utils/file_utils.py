import os
import json
from datetime import datetime

# Asegura que el directorio existe antes de guardar
def ensure_dir(path: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)

# Guardar texto plano
def guardar_texto(path: str, contenido: str):
    ensure_dir(path)
    with open(path, "w", encoding="utf-8") as f:
        f.write(contenido)

# Guardar en JSON
def guardar_json(path: str, data: dict):
    ensure_dir(path)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

# Guardar sección individual
def guardar_seccion(capitulo: str, seccion_num: int, contenido: str):
    path = f"chapters/{capitulo}/sec_{seccion_num:02d}.md"
    guardar_texto(path, contenido)

# Consolidar varias secciones en un archivo
def consolidar_capitulo(capitulo: str, secciones: list[str], nombre: str = "borrador"):
    path = f"chapters/{capitulo}/cap_{capitulo}_{nombre}.md"
    contenido = "\n\n".join(secciones)
    guardar_texto(path, contenido)

# Guardar planificación de capítulo
def guardar_plan_capitulo(capitulo: str, plan: dict):
    path = f"context/plan_cap_{capitulo}.json"
    guardar_json(path, plan)

# Guardar informe de revisiones
def guardar_revisiones(capitulo: str, contenido: str):
    path = f"context/revisiones_cap_{capitulo}.md"
    guardar_texto(path, contenido)

# Opción extra: guardar con timestamp (para logs)
def guardar_version_temporal(nombre_base: str, contenido: str, extension="txt"):
    fecha = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = f"versiones/{nombre_base}_{fecha}.{extension}"
    guardar_texto(path, contenido)