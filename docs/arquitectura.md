# 🧠 Arquitectura del Sistema Narrativo CrewAI

## Estructura de Carpetas

```
novela_crew/
├── agents/                # Agentes definidos
├── chapters/              # Capítulos divididos en secciones
├── context/               # Estado global, personajes y planes
├── crew_config/           # Definición de crews y tareas
├── llm_provider/          # OpenAI, DeepSeek, Claude
├── prompts/               # Prompts personalizados
├── utils/                 # Funciones de guardado y contexto
├── workflows/             # Flujo de trabajo principal
└── main.py                # Lanzador del sistema
```

## Agentes del Sistema

| Agente        | Rol                           |
|---------------|--------------------------------|
| Arquitecto    | Planificación estructural     |
| Redactor      | Redacción del capítulo        |
| Coherencia    | Verificación de continuidad   |
| Personajes    | Evolución psicológica         |
| Diálogo       | Tensión y naturalidad verbal  |
| Temático      | Profundidad simbólica         |
| Científico    | Precisión conceptual          |

## Flujo Narrativo (Resumen)

1. **Planificación global** de la novela (una vez)
2. **Planificación del capítulo** por el Arquitecto
3. **Redacción completa** por el Redactor (secciones técnicas)
4. **Revisión de agentes** sobre el capítulo consolidado
5. **Informe integrado** y validación
6. **Reescritura** del capítulo según sugerencias
7. **Versión final** y actualización del estado global

## Modelos LLM Integrados

| Proveedor  | Estado   |
|------------|----------|
| OpenAI     | ✅ Activo  |
| DeepSeek   | 💤 Preparado |
| Claude     | 💤 Preparado |