from crewai import Agent
from utils.prompts_utils import get_prompt_para_agente

arquitecto = Agent(
    name="Arquitecto Narrativo",
    role="Diseñador de estructura narrativa global",
    goal="Planificar la novela y cada capítulo con visión estructural, emocional y dramática.",
    backstory=get_prompt_para_agente("arquitecto"),
    verbose=True
)

redactor = Agent(
    name="Redactor Literario",
    role="Narrador principal en voz de Elías Navarro",
    goal="Redactar el capítulo completo con voz sobria, precisa e introspectiva.",
    backstory=get_prompt_para_agente("redactor"),
    verbose=True
)

coherencia = Agent(
    name="Supervisor de Coherencia",
    role="Inspector de continuidad narrativa",
    goal="Detectar inconsistencias entre capítulos, en estilo, cronología o lógica narrativa.",
    backstory=get_prompt_para_agente("coherencia"),
    verbose=True
)

personajes = Agent(
    name="Analista de Personajes",
    role="Psicólogo narrativo",
    goal="Evaluar la consistencia psicológica y simbólica de los personajes en cada capítulo.",
    backstory=get_prompt_para_agente("personajes"),
    verbose=True
)

dialogo = Agent(
    name="Editor de Diálogos",
    role="Especialista en intercambios verbales",
    goal="Asegurar que los diálogos sean naturales, cargados de tensión o significación.",
    backstory=get_prompt_para_agente("dialogo"),
    verbose=True
)

tematico = Agent(
    name="Analista Temático",
    role="Guardían del significado profundo",
    goal="Detectar símbolos, dilemas y temas centrales.",
    backstory=get_prompt_para_agente("tematico"),
    verbose=True
)

cientifico = Agent(
    name="Consultor Científico",
    role="Validador técnico del contenido narrativo",
    goal="Verificar la plausibilidad y corrección de todo contenido técnico o científico.",
    backstory=get_prompt_para_agente("cientifico"),
    verbose=True
)

agentes_narrativos = [
    arquitecto, redactor, coherencia, personajes,
    dialogo, tematico, cientifico
]