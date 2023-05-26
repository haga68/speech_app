from gtts import gTTS
import win32com.client as wincl
import streamlit as st
def main():
    st.title('Text2Speech')
    selected = st.radio('Audio type',
                        ['Microsoft','Google'])
    text = st.text_input(label='Message',
                         value='Hello World')
    if st.button('Speak'):
        audio = 'speech.mp3'
        if selected == 'Google':
            tts = gTTS(text=text, lang='ja')
            tts.save(audio)
        elif selected == 'Microsoft':
            sapi = wincl.Dispatch('SAPI.SpVoice')
            fs = wincl.Dispatch('SAPI.SpFileStream')
            fs.Open(audio,3)
            sapi.AudioOutputStream = fs
            sapi.Speak(text)
            fs.Close()
        st.audio(audio)

if __name__ == '__main__':
    main()