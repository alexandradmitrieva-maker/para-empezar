import streamlit as st
from streamlit_mic_recorder import mic_recorder
import os

# Настройка страницы
st.set_page_config(page_title="Испанский с Сашей", page_icon="🇪🇸")

# Стилизация
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { border-radius: 20px; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

st.title("Твой старт в испанском")
st.write("### Привет! Спасибо, что записались на курс!")
st.info("Попробуйте попрактиковать эти фразы. В Испании редко обращаются друг к другу на 'Вы', так что все фразы тут – на ты.")

# Обновленный список фраз с новыми именами файлов
phrases = [
    {"es": "¡Hola! ¿Qué tal?", "ru": "Привет, как дела?", "file": "Hola! Que tal.m4a"},
    {"es": "Bien, ¿y tú?", "ru": "Хорошо, а у тебя?", "file": "Bien, y tu.m4a"},
    {"es": "¿Cómo te llamas?", "ru": "Как тебя зовут?", "file": "Como te llamas.m4a"},
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
        if os.path.exists(item['file']):
            col1, col2 = st.columns([1, 1])
            with col1:
                st.write("Слушай Сашу:")
                st.audio(item['file'])
            with col2:
                st.write("Твоя очередь:")
                mic_recorder(
                    start_prompt="Нажми и говори",
                    stop_prompt="Стоп (закончить)",
                    key=f"recorder_{i}"
                )
        else:
            st.warning(f"Файл {item['file']} не найден на GitHub. Проверь название!")

st.divider()

if st.button("Я прошел все фразы!"):
    st.balloons()
    st.success("### Ого! Поздравляю, похоже, первый барьер вы преодолели! 🎉")
    st.write("Теперь ваш испанский — это не просто буквы в учебнике, а ваш собственный голос. На курсе мы превратим эти простые фразы в связную речь! Жду вас 26 мая, будем зажигать!")