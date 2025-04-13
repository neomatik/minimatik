from prompts.prompts_base import PROMPTS

def get_prompt_para_agente(nombre_agente: str) -> str:
    return PROMPTS.get(nombre_agente, "")