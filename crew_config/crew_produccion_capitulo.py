from crewai import Crew, Task
from crew_config.agentes_config import (
    arquitecto, redactor, personajes, dialogo,
    coherencia, tematico, cientifico
)

# -------- BLOQUE A: Planificación + Redacción -------- #

planificar_capitulo = Task(
    description=(
        "Diseñar la estructura narrativa global del capítulo (cap_xx), definiendo el propósito dramático, "
        "los eventos clave, la progresión emocional del protagonista y su vínculo con el plan general de la novela. "
        "No dividas en secciones ni incluyas títulos o tonos por fragmento. La división en partes es responsabilidad técnica del Redactor."
    ),
    expected_output=(
        "Un archivo plan_cap_xx.json que contenga: objetivo narrativo del capítulo, progresión emocional general, "
        "puntos de quiebre o eventos clave, vínculo con el capítulo anterior y con el arco global definido en plan_novela.json."
    ),
    agent=arquitecto
)

redactar_capitulo = Task(
    description=(
        "Redactar el capítulo completo según el plan. Por limitaciones técnicas, divide el texto en fragmentos de ~1500 palabras "
        "pero sin romper la continuidad narrativa. Guarda cada sección como sec_yy.md y al final consolida todo en cap_xx_borrador.md."
    ),
    expected_output="Archivo borrador del capítulo completo y secciones individuales.",
    agent=redactor
)

# -------- BLOQUE B: Revisión global -------- #

revisar_coherencia = Task(
    description="Analizar el capítulo completo y validar continuidad con el Capítulo 1 y la estructura global.",
    expected_output="Informe técnico con observaciones de estilo, cronología, lógica narrativa.",
    agent=coherencia
)

revisar_personajes = Task(
    description="Evaluar consistencia y evolución emocional del protagonista.",
    expected_output="Informe psicológico sobre personajes.",
    agent=personajes
)

revisar_dialogos = Task(
    description="Analizar naturalidad y fuerza narrativa de los diálogos.",
    expected_output="Informe de evaluación de diálogos.",
    agent=dialogo
)

revisar_cientifico = Task(
    description="Verificar exactitud conceptual de los elementos técnicos.",
    expected_output="Informe de revisión científica.",
    agent=cientifico
)

revisar_tematico = Task(
    description="Detectar presencia efectiva de los temas centrales de la novela.",
    expected_output="Informe sobre elementos simbólicos y temáticos.",
    agent=tematico
)

# -------- BLOQUE C: Reescritura -------- #

reescribir_capitulo = Task(
    description="Reescribir el capítulo completo según los informes de los agentes. Dividir solo por motivos técnicos.",
    expected_output="Archivo cap_xx_propuesta.md como propuesta de versión final.",
    agent=redactor
)

crew_produccion_capitulo = Crew(
    agents=[
        arquitecto, redactor, coherencia, personajes,
        dialogo, cientifico, tematico
    ],
    tasks=[
        planificar_capitulo,
        redactar_capitulo,
        revisar_coherencia,
        revisar_personajes,
        revisar_dialogos,
        revisar_cientifico,
        revisar_tematico,
        reescribir_capitulo
    ],
    verbose=True
)