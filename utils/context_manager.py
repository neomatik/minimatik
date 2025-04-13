import os
import json

def cargar_texto(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def cargar_json(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def get_contexto_para_agente(agente: str, capitulo_actual: str):
    context = {}

    # Capítulos previos
    capitulos_dir = f"chapters"
    capitulos = sorted([
        os.path.join(dp, f) for dp, dn, filenames in os.walk(capitulos_dir)
        for f in filenames if f.startswith("cap_") and f.endswith(".md") and capitulo_actual not in f
    ])
    context["capitulos_previos"] = "

".join([cargar_texto(f) for f in capitulos])

    # Personajes
    personajes_path = "context/character_sheets/personajes.json"
    if os.path.exists(personajes_path):
        context["personajes"] = cargar_json(personajes_path)

    # Estado global
    estado_path = "context/global_state.json"
    if os.path.exists(estado_path):
        context["estado_global"] = cargar_json(estado_path)

    return context