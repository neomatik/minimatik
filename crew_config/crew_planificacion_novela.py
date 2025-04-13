from crewai import Crew, Task
from crew_config.agentes_config import arquitecto, personajes, dialogo, coherencia, tematico, cientifico

# Paso 0.1: Arquitecto propone la estructura general de la novela
proponer_esquema_novela = Task(
    description="Proponer la estructura narrativa completa de la novela, incluyendo actos, progresión emocional, evolución del protagonista y temas centrales. Usa como referencia el capítulo 1 ya existente.",
    expected_output="Un archivo plan_novela.json que contenga título de los actos, sinopsis de cada uno, puntos de giro clave y tono general.",
    agent=arquitecto
)

# Paso 0.2: Opiniones de los demás agentes
opinar_personajes = Task(
    description="Analizar la propuesta de estructura de novela y emitir observaciones desde el punto de vista del desarrollo psicológico y simbólico de los personajes.",
    expected_output="Informe breve indicando riesgos, oportunidades o sugerencias de ajuste en los arcos de personajes.",
    agent=personajes
)

opinar_dialogo = Task(
    description="Analizar la estructura propuesta y sugerir puntos donde los diálogos serán clave para avanzar trama, tensión o psicología.",
    expected_output="Informe sobre puntos clave donde los intercambios verbales serán narrativamente potentes.",
    agent=dialogo
)

opinar_coherencia = Task(
    description="Revisar si la propuesta tiene continuidad lógica con lo que ya se ha contado en el capítulo 1.",
    expected_output="Informe sobre posibles contradicciones, saltos temporales o incoherencias con la base narrativa.",
    agent=coherencia
)

opinar_cientifico = Task(
    description="Detectar potenciales conflictos conceptuales o científicos en la estructura general de la novela.",
    expected_output="Informe que evalúe la plausibilidad técnica o científica de los elementos clave del plan.",
    agent=cientifico
)

opinar_tematico = Task(
    description="Evaluar la fuerza de los temas centrales en la estructura global y proponer mejoras simbólicas.",
    expected_output="Informe con observaciones temáticas, símbolos, metáforas, dilemas planteados o ausentes.",
    agent=tematico
)

crew_planificacion_novela = Crew(
    agents=[arquitecto, personajes, dialogo, coherencia, cientifico, tematico],
    tasks=[
        proponer_esquema_novela,
        opinar_personajes,
        opinar_dialogo,
        opinar_coherencia,
        opinar_cientifico,
        opinar_tematico
    ],
    verbose=True
)