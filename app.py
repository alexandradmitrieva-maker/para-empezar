import streamlit as st
from streamlit_mic_recorder import mic_recorder
import os

st.set_page_config(page_title="Испанский с Сашей", page_icon="🇪🇸")

st.title("Твой старт в испанском")
st.write("### Привет! Спасибо, что записались на курс!")
st.info("Послушайте фразу, а затем запишите свой голос, чтобы сравнить произношение.")

phrases = [
    {"es": "¡Hola! ¿Qué tal?", "ru": "Привет, как дела?", "file": "Hola! Que tal.m4a"},
    {"es": "Bien, ¿y tú?", "ru": "Хорошо, а у тебя?", "file": "Bien, y tu.m4a"},
    {"es": "¿Как тебя зовут?", "ru": "Как тебя зовут?", "file": "Como te llamas.m4a"},
    {"es": "Me llamo...", "ru": "Меня зовут...", "file": "Me llamo.m4a"},
    {"es": "Perdona, ¿me traes una caña, por favor?", "ru": "Извини, принесешь пива?", "file": "Una caña.m4a"},
    {"es": "Un café solo, por favor", "ru": "Черный кофе, пожалуйста", "file": "Cafe solo.m4a"},
    {"es": "¿Me podrías traer la carta, por favor?", "ru": "Принесешь меню?", "file": "Me podrías traer la carta.m4a"},
    {"es": "¿Me cobras, por favor?", "ru": "Посчитай меня, пожалуйста", "file": "Me cobras.m4a"},
    {"es": "Voy a pagar con tarjeta", "ru": "Я оплачу картой", "file": "Pagar con tarjeta.m4a"},
    {"es": "Voy a pagar en efectivo", "ru": "Я оплачу наличными", "file": "Pagar en efectivo.m4a"},
    {"es": "¿Cómo se dice en español...?", "ru": "Как сказать по-испански?", "file": "Como se dice.m4a"},
    {"es": "¿Podrías hablar más despacio, por favor?", "ru": "Можешь говорить медленнее?", "file": "Más despacio.m4a"},
    {"es": "Perdona, ¡no te entiendo!", "ru": "Извини, я не понимаю", "file": "Perdona, no te entiendo.m4a"},
    {"es": "¿Me podrías ayudar, por favor?", "ru": "Ты не мог бы мне помочь?", "file": "Me podrías ayudar.m4a"},
    {"es": "¿Hablas inglés?", "ru": "Ты говоришь по-английски?", "file": "Hablas inglés.m4a"}
]

for i, item in enumerate(phrases):
    with st.expander(f"{item['es']} — {item['ru']}"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("👂 **Слушай Сашу:**")
            if os.path.exists(item['file']):
                st.audio(item['file'])
            else:
                st.caption(f"⚠️ Файл {item['file']} не найден")

        with col2:
            st.write("🎤 **Твоя очередь:**")
            # Добавили принудительный формат WAV для стабильности
            audio_data = mic_recorder(
                start_prompt="Начать запись",
                stop_prompt="Сохранить",
                key=f"recorder_{i}",
                format="wav" 
            )
            
            if audio_data:
                # Четко указываем тип аудио для браузера
                st.audio(audio_data['bytes'], format="audio/wav")
                st.success("Запись готова! Нажми Play выше 👆")

st.divider()

if st.button("Я прошел все фразы!"):
    st.balloons()
    st.success("### Ого! Поздравляю, похоже, первый барьер вы преодолели! 🎉")
    st.write("Теперь ваш испанский — это не просто буквы в учебнике, а ваш собственный голос. На курсе мы превратим эти простые фразы в связную речь! Жду вас 26 мая, будем зажигать!")