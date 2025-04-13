import os
from llm_provider.openai_connector import chat_completion_openai
from llm_provider.deepseek_connector import chat_completion_deepseek
from llm_provider.claude_connector import chat_completion_claude

def chat_completion(prompt: str, system_prompt: str = "", provider: str = None) -> str:
    provider = provider or os.getenv("DEFAULT_LLM", "openai")

    if provider == "openai":
        return chat_completion_openai(prompt, system_prompt)
    elif provider == "deepseek":
        return chat_completion_deepseek(prompt, system_prompt)
    elif provider == "claude":
        return chat_completion_claude(prompt, system_prompt)
    else:
        raise ValueError(f"Proveedor LLM no reconocido: {provider}")