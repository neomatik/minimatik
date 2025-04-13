import os
import requests

def chat_completion_deepseek(prompt: str, system_prompt: str = "") -> str:
    api_url = "https://api-inference.huggingface.co/models/deepseek-ai/deepseek-coder-6.7b-instruct"
    headers = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_TOKEN')}"}

    payload = {
        "inputs": f"<|system|>\n{system_prompt}\n<|user|>\n{prompt}",
        "parameters": {"temperature": 0.7}
    }

    response = requests.post(api_url, headers=headers, json=payload)
    data = response.json()
    return data[0]["generated_text"] if isinstance(data, list) else data.get("generated_text", "")