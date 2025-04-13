from llm_provider.llm_router import chat_completion
from utils.context_manager import get_contexto_para_agente
from utils.prompts_utils import get_prompt_para_agente

def ejecutar_agente(nombre_agente: str, prompt_usuario: str, capitulo_actual: str = "cap_02"):
    contexto = get_contexto_para_agente(nombre_agente, capitulo_actual)
    contexto_base = contexto.get("capitulos_previos", "")
    prompt_agente = get_prompt_para_agente(nombre_agente)

    system_prompt = f"{prompt_agente}\n\n[Contexto relevante]\n{contexto_base}"
    return chat_completion(prompt=prompt_usuario, system_prompt=system_prompt)