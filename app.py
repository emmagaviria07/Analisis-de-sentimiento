import streamlit as st
from textblob import TextBlob
from googletrans import Translator

st.set_page_config(
    page_title="Analizador de Texto con TextBlob",
    page_icon="💬",
    layout="centered"
)

translator = Translator()


st.title("💬 Analizador de Sentimientos y Corrección de Texto")
st.markdown("""
Explora cómo **TextBlob** interpreta el tono emocional de tus palabras  
y mejora tu escritura en inglés con su sistema de corrección automática. ✨
""")


with st.sidebar:
    st.header("📘 Guía rápida")
    st.markdown("""
    **Polaridad:**  
    Indica si el sentimiento del texto es positivo, negativo o neutral.  
    Valor entre **-1 (negativo)** y **1 (positivo)**.

    **Subjetividad:**  
    Mide cuánto del texto es **opinión o emoción (1)**  
    frente a **hechos objetivos (0)**.
    """)
    st.markdown("---")
    st.info("💡 Consejo: escribe frases completas para obtener resultados más precisos.")


with st.expander("🧩 Analizar Polaridad y Subjetividad en un texto", expanded=True):
    st.markdown("Escribe un texto en español y descubre qué emoción transmite 👇")
    text1 = st.text_area("✏️ Escribe aquí tu frase:", height=150)

    if text1:
        with st.spinner("Traduciendo y analizando... 🔍"):
            translation = translator.translate(text1, src="es", dest="en")
            trans_text = translation.text
            blob = TextBlob(trans_text)
            polarity = round(blob.sentiment.polarity, 2)
            subjectivity = round(blob.sentiment.subjectivity, 2)

        # Resultados
        st.markdown("### 📈 Resultados del Análisis")
        st.write(f"**Polaridad:** {polarity}")
        st.write(f"**Subjetividad:** {subjectivity}")

        # Indicador visual del sentimiento
        if polarity >= 0.5:
            st.success("💖 Sentimiento **Positivo** 😊")
        elif polarity <= -0.5:
            st.error("💔 Sentimiento **Negativo** 😔")
        else:
            st.info("😐 Sentimiento **Neutral**")

        st.markdown("---")
        st.markdown("**Texto traducido al inglés (para el análisis):**")
        st.code(trans_text, language="markdown")


with st.expander("📝 Corrección de texto en inglés"):
    st.markdown("Escribe una oración en inglés para recibir su versión corregida automáticamente 👇")
    text2 = st.text_area("✏️ Escribe tu texto en inglés:", key="4", height=150)

    if text2:
        with st.spinner("Analizando gramática... ✍️"):
            blob2 = TextBlob(text2)
            corrected = blob2.correct()
        st.markdown("### ✅ Texto corregido:")
        st.success(corrected)


st.markdown("---")
st.caption("Hecho con ❤️ usando Streamlit, TextBlob y Googletrans.")
