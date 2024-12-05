import streamlit as st
import random
import time

def generar_mensaje_cumpleanos():
    mensajes_emojis = [
        "🌻 Hoy no es solo un cumpleaños, es un gran dia porque se trata de ti 🌻",
        "🌻 Diecinueve años de pura magia, creatividad y potencial sin límites. Que sigan los sueños! 🌻",
        "🌻 Creces como una flor única, desafiando lo ordinario y celebrando lo extraordinario. ¡Feliz día! 🌻",
        "🌻 Cada año es un nuevo acto en el teatro de tu vida. ¡Que este sea el más espectacular! 🌻"
        "🌻 Feliz cumpleaños a la mejor persona que pude haber conocido🌻🌻"
        "🌻 Gracias por ser tu, única y especial 🌻🌻"
    ]

    frases_divertidas = [
        "Alerta: Cumpleañera Precaución: Felicidad extrema incoming! 🚨",
        "Sistema de celebración Jazmyn: Iniciando secuencia de diversión máxima en 3, 2, 1... ¡Despegue! 🛸",
        "Jazmyn: Cargando actualizaciones de vida. Por favor, no interrumpir la magia en progreso. 🔄"
    ]

    efectos_visuales = [
        "🎉 BOOM! Otro año increíble recién comenzado. ¡Felicidades, Jazmyn! 🎊",
        "💥 ¡EXPLOSIÓN DE FELICIDAD DETECTADA! Nivel: Jazmyn 🌈",
        "✨ Cargando: Año más increíble. Por favor, espere... ¡COMPLETADO! 🚀"
    ]

    mensaje_final = random.choice(mensajes_emojis + frases_divertidas + efectos_visuales)
    return mensaje_final

def aplicacion_cumpleanos():
    st.set_page_config(page_title="Cumpleaños Jazmyn", page_icon="🎂")
    
    # Título animado
    st.markdown("""
    <h1 style='text-align: center; color: #FF69B4; 
    text-shadow: 2px 2px 4px #FF1493;
    font-size: 4em;
    animation: bounce 2s infinite;'>
    🎂 ¡Feliz Cumpleaños Jazmyn! 🎂
    </h1>
    
    <style>
    @keyframes bounce {
        0%, 20%, 50%, 80%, 100% {transform: translateY(0);}
        40% {transform: translateY(-20px);}
        60% {transform: translateY(-10px);}
    }
    </style>
    """, unsafe_allow_html=True)

    # Fondo colorido
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #FF6B6B, #4ECDC4, #FFD93D);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
    }
    @keyframes gradient {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }
    </style>
    """, unsafe_allow_html=True)

    # Botón de generación con estilo
    col1, col2, col3 = st.columns([1,2,1])
    
    with col2:
        if st.button("🎈 Generar Mensaje Mágico 🎈", use_container_width=True):
            with st.spinner('Preparando algo especial...'):
                time.sleep(1)
                felicitacion = generar_mensaje_cumpleanos()
                st.balloons()
                st.snow()
                st.success(felicitacion)

def main():
    aplicacion_cumpleanos()

if __name__ == "__main__":
    main()
