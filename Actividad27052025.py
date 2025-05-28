import streamlit as st  # type: ignore
import pandas as pd  # type: ignore
import matplotlib.pyplot as plt  # type: ignore
import plotly.express as px  # type: ignore
import numpy as np  # type: ignore
import altair as alt  # type: ignore
from datetime import datetime, time as dt_time
import time  # para time.sleep()

# Configuración de la página
st.set_page_config(page_title="Series, Películas y Música", layout="centered")

# Estilos personalizados
st.markdown("""
<style>
    .main {
        background-color: #F5F5F5;
        font-family: 'sans-serif';
    }
    .block-style {
        background-color: #DDE3F0;
        padding: 20px;
        margin-bottom: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.15);
    }
    h1, h2, h3, h4, h5 {
        color: #004AAD;
    }
    .stButton>button {
        background-color: #004AAD;
        color: #ffffff;
        border-radius: 10px;
        padding: 0.5em 1em;
        border: none;
    }
</style>
""", unsafe_allow_html=True)

# Función para crear secciones colapsables decoradas
def collapsible_block(label):
    return st.expander(label, expanded=False)

with collapsible_block("👋 Presentación"):
    st.markdown('''<h1>🎬🎶 Dashboard de Series, Películas y Música</h1><h3>Andrea Galindo Yáñez - A01368483</h3>''', unsafe_allow_html=True)
    st.subheader("Este es tu primer dashboard con Streamlit.")
    st.subheader("Lo voy a usar como base para mi reto :)")
    st.write("A01368483")
    st.write("TITULO 1")
    st.write("TITULO 2")
    st.write("SERIES QUE LE RECOMIENDO PROFE")

with collapsible_block("🔘 App con botones"):
    if st.button('Presiona aquí - Botón 1'):
        st.write('Cobra Kai')
    else:
        st.write('Botón 1: Adiós')

    if st.button('Presiona aquí - Botón 2'):
        st.write('The Bear')
    else:
        st.write('Botón 2: Adiós')

    if st.button('Presiona aquí - Botón 3'):
        st.write('Mr. Robot')
    else:
        st.write('Botón 3: Adiós')

with collapsible_block("📊 Datos y visualización"):
    data = pd.DataFrame({ 'Nombre': ['A', 'B', 'C'], 'Valor': [10, 20, 30] })
    st.dataframe(data)
    fig, ax = plt.subplots()
    ax.bar(data['Nombre'], data['Valor'])
    st.pyplot(fig)
    fig2 = px.bar(data, x='Nombre', y='Valor', title='Ejemplo con Plotly')
    st.plotly_chart(fig2)

with collapsible_block("📋 Interacción con Sliders"):
    st.subheader('¿Cuál es tu época favorita de música?')
    epoca_musical = st.select_slider('Selecciona una época', options=['60s', '70s', '80s', '90s', '2000s', '2010s', '2020s'], value='2000s')
    st.write("Tu época favorita es:", epoca_musical)
    st.subheader('¿Qué tanto te gustó Harry Potter?')
    st.write('Tu nivel de satisfacción con Harry Potter es:', st.slider('Nivel de satisfacción', 0, 100, 85))
    st.subheader('Selecciona tu horario para ver series')
    st.write("Tu horario seleccionado es:", st.slider("¿A qué hora ves series normalmente?", value=(dt_time(20, 0), dt_time(23, 0))))
    st.subheader('¿Cuándo planeas maratonear Star Wars?')
    st.write("Tienes agendado el maratón para:", st.slider("Fecha y hora del maratón", value=datetime(2025, 6, 15, 18, 0), format="MM/DD/YY - hh:mm"))

with collapsible_block("📈 Gráficos de línea"):
    dias = pd.date_range("2025-01-01", periods=20)
    temp_df = pd.DataFrame({
        'Monterrey': np.random.normal(28, 2, size=20),
        'CDMX': np.random.normal(22, 1.5, size=20),
        'Cancún': np.random.normal(30, 2.5, size=20)
    }, index=dias)
    st.line_chart(temp_df)

with collapsible_block("📝 Encuesta con Selectbox"):
    st.write('Temporada Favorita de Stranger Things:', st.selectbox('Temporada Favorita de Stranger Things', ('T1', 'T2', 'T3', 'T4')))
    st.write('Película de Disney estrenada en el año 2003:', st.selectbox('Película de Disney estrenada en el año 2003', ('Tierra de Osos', 'Lilo y Stitch', 'Lluvia de Hamburguesas', 'Mean Girls', 'Herbie a toda marcha')))
    st.write('¿Qué canciones no son de Guns N Roses?', st.selectbox('¿Qué canciones no son de Guns N Roses?', ('Sweet Child O´Mine', 'So Fine', 'Nightrain', 'Rocket Queen')))
    st.write('Personas que NO son de The Office:', st.selectbox('Personas que NO son de The Office', ('Michel Scott', 'Pam', 'Jim', 'Kelly', 'Miguel')))
    st.write('¿Cuál es tu personaje favorito de Harry Potter?', st.selectbox('¿Cuál es tu personaje favorito de Harry Potter?', ('Harry', 'Hermione', 'Ron', 'Dumbledore', 'Snape')))

with collapsible_block("✅ Selección múltiple"):
    st.write('Series seleccionadas: ' + ', '.join(st.multiselect('¿Cuáles son tus series favoritas?', ['Stranger Things', 'Breaking Bad', 'Dark', 'The Office', 'The Mandalorian'], default=['Stranger Things', 'The Office'])))
    st.write('Géneros musicales seleccionados: ' + ', '.join(st.multiselect('¿Qué géneros de música te gustan?', ['Rock en español', 'Rock', 'Hip Hop', 'Rap', 'Pop'], default=['Rap', 'Pop'])))
    st.write('Plataformas seleccionadas: ' + ', '.join(st.multiselect('¿Qué plataformas de streaming usas?', ['Netflix', 'Disney+', 'Prime Video', 'HBO Max', 'Star+'], default=['Netflix', 'Prime Video'])))
    st.write('Sagas seleccionadas: ' + ', '.join(st.multiselect('¿Qué saga maratoneas más?', ['Harry Potter', 'Star Wars', 'El Señor de los Anillos', 'Marvel', 'DC'], default=['Harry Potter', 'Marvel'])))
    st.write('Series por ver: ' + ', '.join(st.multiselect('¿Qué series te gustaría ver?', ['Cobra Kai', 'You', 'The Bear', 'Malcolm', 'Friends'], default=['Malcolm', 'Friends'])))

with collapsible_block("📌 Acciones del día"):
    st.write("¿Qué tipo de contenido quieres incluir en tu maratón?")
    if st.checkbox('Películas'):
        st.write("Agregaste películas a tu maratón.")
    if st.checkbox('Series'):
        st.write("Series añadidas a tu lista.")
    if st.checkbox('Documentales'):
        st.write("Documentales seleccionados. ¡A aprender algo nuevo!")
    if st.checkbox('Anime'):
        st.write("Anime incluido. ¡Hora de los subtítulos!")
    if st.checkbox('Reality Shows'):
        st.write("Reality shows agregados. ¡Diversión sin culpa!")

with collapsible_block("📂 Carga de archivos CSV"):
    st.subheader("Sube tu primer archivo CSV")
    archivo_1 = st.file_uploader("Archivo 1", type="csv", key="csv1")
    if archivo_1 is not None:
        df1 = pd.read_csv(archivo_1)
        st.subheader("Contenido del archivo 1")
        st.write(df1)
        st.subheader("Estadísticas descriptivas del archivo 1")
        st.write(df1.describe())
    else:
        st.info("Sube el primer archivo CSV")

    st.subheader("Sube tu segundo archivo CSV")
    archivo_2 = st.file_uploader("Archivo 2", type="csv", key="csv2")
    if archivo_2 is not None:
        df2 = pd.read_csv(archivo_2)
        st.subheader("Contenido del archivo 2")
        st.write(df2)
        st.subheader("Estadísticas descriptivas del archivo 2")
        st.write(df2.describe())
    else:
        st.info("Sube el segundo archivo CSV")

with collapsible_block("📦 Cargas Simuladas con st.progress"):
    st.write("Carga 1 (rápida)")
    bar1 = st.progress(0)
    for i in range(100):
        time.sleep(0.005)
        bar1.progress(i + 1)

    st.write("Carga 2 (media)")
    bar2 = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        bar2.progress(i + 1)

    st.write("Carga 3 (lenta)")
    bar3 = st.progress(0)
    for i in range(100):
        time.sleep(0.02)
        bar3.progress(i + 1)

    st.success("Todas las cargas han terminado ✅")
    st.balloons()

with collapsible_block("🧾 Encuesta: Tus gustos en entretenimiento"):
    st.header("Encuesta de Preferencias")

    with st.form("form_entretenimiento"):
        st.subheader("Completa la siguiente encuesta:")

        q1 = st.selectbox("1. ¿Cuál es tu género de películas favorito?", ["Acción", "Comedia", "Drama", "Terror", "Ciencia ficción"])
        q2 = st.selectbox("2. ¿Qué plataforma usas más para ver series?", ["Netflix", "HBO Max", "Disney+", "Amazon Prime", "Otra"])
        q3 = st.slider("3. ¿Cuántas horas a la semana ves series?", 0, 40, 10)
        q4 = st.radio("4. ¿Ves películas en cine o en casa?", ["Cine", "Casa"])
        q5 = st.selectbox("5. ¿Qué saga prefieres?", ["Harry Potter", "Star Wars", "El Señor de los Anillos", "Marvel", "DC"])
        q6 = st.multiselect("6. ¿Qué géneros musicales disfrutas?", ["Pop", "Rock", "Reggaetón", "Clásica", "Jazz"])
        q7 = st.select_slider("7. Nivel de fanatismo por las series", ["Bajo", "Medio", "Alto", "Extremo"])
        q8 = st.selectbox("8. ¿Tienes suscripción activa?", ["Sí", "No"])
        q9 = st.radio("9. ¿Con quién ves películas/series principalmente?", ["Solo/a", "Familia", "Amigos", "Pareja"])
        q10 = st.text_input("10. ¿Serie o película favorita del último año?")

        enviado = st.form_submit_button("Enviar Encuesta")

        if enviado:
            st.success("¡Gracias por completar la encuesta! 🎉")
            st.markdown(f"""
            #### Resumen de tus respuestas:
            - 🎬 Género favorito: **{q1}**
            - 📺 Plataforma principal: **{q2}**
            - ⏰ Horas semanales viendo series: **{q3}**
            - 🏠 Lugar de visualización: **{q4}**
            - 🧙 Saga favorita: **{q5}**
            - 🎵 Géneros musicales: **{', '.join(q6)}**
            - 🔥 Nivel de fanatismo: **{q7}**
            - 💳 Suscripción activa: **{q8}**
            - 👥 Compañía al ver contenido: **{q9}**
            - 🌟 Favorita reciente: **{q10}**
            """)
        else:
            st.info("Por favor completa y envía la encuesta.")

        # 👇 Videos añadidos al final del formulario
        st.markdown("### 🎥 Videos relacionados al entretenimiento")
        st.video("https://www.youtube.com/watch?v=gWcb7eugjTo")
        st.caption("Historia y evolución de las plataformas de streaming")

        st.video("https://www.youtube.com/watch?v=WBlIUsFEnsw")
        st.caption("La influencia del cine en la cultura popular")
