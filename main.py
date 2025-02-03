import streamlit as st

# Lista de músicas
tracks = [
    "4 - Amigos Pela Fé_Mais que Amigos.mp3",
    "9 - Majestosa Eucaristia _ Invade Minh'alma _ Maria E O Anjo _ Maria da Eucaristia.mp3",
    "12 - Sou Teu Anjo.mp3"
    
]

# Adicionar os elementos de áudio como HTML
audio_elements_html = ''.join([f"<audio id='audio_{i}' src='{track}'></audio>" for i, track in enumerate(tracks)])
st.markdown(f"<div id='audio-container'>{audio_elements_html}</div>", unsafe_allow_html=True)

# Exibir o player do primeiro áudio
st.audio(tracks[0], format="audio/mpeg", start_time=0, loop=False)

# Código JavaScript para tocar as músicas em sequência
st.markdown("""
<script>
    const audioElements = Array.from(document.querySelectorAll('audio'));
    let currentIndex = 0;

    function playNext() {
        if (currentIndex < audioElements.length) {
            audioElements[currentIndex].play();
            audioElements[currentIndex].addEventListener('ended', () => {
                currentIndex++;
                playNext();
            });
        }
    }

    const firstAudio = audioElements[currentIndex];
    firstAudio.addEventListener('ended', playNext);
</script>
""", unsafe_allow_html=True)

st.write("As músicas irão tocar em sequência.")
