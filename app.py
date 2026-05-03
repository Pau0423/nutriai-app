import streamlit as st

st.set_page_config(page_title="NutriAI", page_icon="🥗")

st.title("🥗 NutriAI - Generador de Menús con IA")

st.markdown("Genera menús personalizados según el tipo de dieta y tus preferencias alimentarias.")


tipo_dieta = st.selectbox("Selecciona el tipo de dieta:", [
    "Gástrica", "Astringente", "Diabética", "Vegetariana"
])

preferencias = st.text_input("Preferencias o restricciones (ej: sin pollo, sin pescado, sin arroz):")


if st.button("✨ Generar menú"):

    if not tipo_dieta:
        st.warning("Por favor selecciona un tipo de dieta.")
    else:

        preferencias_lower = preferencias.lower()

        sin_pollo = "pollo" in preferencias_lower
        sin_pescado = "pescado" in preferencias_lower
        sin_arroz = "arroz" in preferencias_lower
        vegetariano = "vegetariano" in preferencias_lower

        if tipo_dieta == "Gástrica":
            almuerzo = "Arroz blanco con pollo hervido"
            cena = "Pescado al vapor con puré de calabaza"

        elif tipo_dieta == "Astringente":
            almuerzo = "Arroz blanco con pollo a la plancha"
            cena = "Sopa de zanahoria y papa"

        elif tipo_dieta == "Diabética":
            almuerzo = "Ensalada de pollo con verduras frescas"
            cena = "Pescado con brócoli al vapor"

        elif tipo_dieta == "Vegetariana":
            almuerzo = "Ensalada de verduras con arroz integral"
            cena = "Tortilla de verduras con ensalada"

        if sin_pollo:
            almuerzo = almuerzo.replace("pollo", "verduras cocidas")

        if sin_pescado:
            cena = cena.replace("pescado", "verduras al vapor")

        if sin_arroz:
            almuerzo = almuerzo.replace("arroz blanco", "puré de calabaza")
            almuerzo = almuerzo.replace("arroz integral", "quinoa")

        if vegetariano:
            almuerzo = "Ensalada de verduras con legumbres"
            cena = "Verduras al vapor con huevo o tofu"

        st.success("Menú generado correctamente")

        st.subheader("🍽️ Menú del día")

        st.markdown(f"""
        🥗 **Almuerzo:**  
        {almuerzo}

        🌙 **Cena:**  
        {cena}
        """)


st.markdown("---")
st.subheader("ℹ️ ¿Cómo funciona?")

st.markdown("""
1. Seleccionas el tipo de dieta.
2. Escribes restricciones (por ejemplo: sin pollo, vegetariano).
3. Presionas el botón.
4. La aplicación genera un menú adaptado automáticamente.
""")

st.markdown("---")
st.caption("💡 Esta aplicación simula el comportamiento de un modelo de inteligencia artificial mediante lógica condicional.")