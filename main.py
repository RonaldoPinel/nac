import streamlit as st

# Lista de músicas
tracks = [
    "4 - Amigos Pela Fé_Mais que Amigos.mp3",
    "9 - Majestosa Eucaristia _ Invade Minh'alma _ Maria E O Anjo _ Maria da Eucaristia.mp3",
    "12 - Sou Teu Anjo.mp3"
]

# Inicializar o índice da música atual
if 'current_track_index' not in st.session_state:
    st.session_state.current_track_index = 0

# Função para tocar a música atual
def play_current_track():
    track = tracks[st.session_state.current_track_index]
    st.audio(track, format="audio/mpeg", start_time=0, loop=False)

# Função para avançar para a próxima música
def next_track():
    st.session_state.current_track_index = (st.session_state.current_track_index + 1) % len(tracks)

# Exibir o nome da música atual
current_track_name = tracks[st.session_state.current_track_index]
st.markdown(f"### {current_track_name}")

# Exibir o player da música atual
play_current_track()

# Adicionar o botão para a próxima música
if st.button("Próxima Música"):
    next_track()
    st.experimental_set_query_params(index=st.session_state.current_track_index)

# Código JavaScript para tocar as músicas em sequência automaticamente
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
