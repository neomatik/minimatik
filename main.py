from crew_config.crew_definicion import crew_planificacion_novela, crew_produccion_capitulo

if __name__ == "__main__":
    print("🚀 Ejecutando Paso 0: Planificación global de la novela...")
    crew_planificacion_novela.kickoff()

    print("\n✍️ Ejecutando Paso 1: Producción de capítulo...")
    crew_produccion_capitulo.kickoff()