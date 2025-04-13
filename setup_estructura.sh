#!/bin/bash

echo "🚧 Creando estructura del proyecto 'novela_crew'..."

mkdir -p novela_crew/{agents,context/character_sheets,chapters/cap_01,prompts,workflows,crew_config,llm_provider,utils}

touch novela_crew/context/global_state.json
touch novela_crew/chapters/cap_01/sec_01.md
touch novela_crew/prompts/prompts_base.py
touch novela_crew/workflows/flujo_narrativo.py
touch novela_crew/crew_config/agentes_config.py
touch novela_crew/crew_config/crew_definicion.py
touch novela_crew/llm_provider/openai_connector.py
touch novela_crew/llm_provider/deepseek_connector.py
touch novela_crew/utils/text_utils.py
touch novela_crew/main.py
touch novela_crew/requirements.txt

cat <<EOL > novela_crew/README.md
# Proyecto Narrativo Multiagente (CrewAI)

Este repositorio contiene el sistema narrativo basado en agentes IA usando CrewAI. La arquitectura incluye:

- Agentes narrativos especializados
- Flujos de trabajo con CrewAI
- Conexión a múltiples modelos LLM (OpenAI, DeepSeek)
- Control de contexto y estado global

Para comenzar:
\`\`\`bash
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
\`\`\`
EOL

cat <<EOL > novela_crew/requirements.txt
crewai
openai
EOL

echo "✅ Estructura creada correctamente."