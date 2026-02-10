
#import for local llm functionality
import sys
import ollama

import re

#import for file saving/text writing
from PyQt5.QtWidgets import QFileDialog

#import statement to import custom font
from PyQt5.QtGui import QFontDatabase, QFont

#import for window functions and layout
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtWidgets import (
    QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout,
    QLineEdit, QPushButton
)
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt

#this allows you to import ICO favicons
from PyQt5.QtGui import QIcon

import os, sys
from PyQt5.QtGui import QFontDatabase, QFont

#establish different visual themes
themes = [
    {
        "name": "Dark",
        "window": "#2b2b2b",
        "input": "#3c3c3c",
        "chat_bg": "#1e1e1e",
        "text": "white",
        "button": "#555"
    },
    {
         "name": "Peach Cat",
        "window": "#fff1e6",
        "input": "#ffd8b5",
        "chat_bg": "#ffe4cc",
        "text": "#4a2c1a",
        "button": "#ffb07c"
    },
    {
        "name": "Meow Mode",
        "window": "#3a2c23",
        "input": "#5a4333",
        "chat_bg": "#2b1e16",
        "text": "#f5e6d3",
        "button": "#8b5e3c"
    }
]

current_theme = 0

#create a definition for changing text and boxes
def apply_theme():
    theme = themes[current_theme]

    window.setStyleSheet(f"background-color: {theme['window']};")
    input_box.setStyleSheet(f"color: {theme['text']}; background-color: {theme['input']};")
    chat_history.setStyleSheet(f"color: {theme['text']}; background-color: {theme['chat_bg']};")
    send_button.setStyleSheet(f"background-color: {theme['button']}; color: {theme['text']};")
    theme_button.setStyleSheet(f"background-color: {theme['button']}; color: {theme['text']};")
    fish_button.setStyleSheet(f"background-color: {theme['button']}; color: {theme['text']};")
    save_button.setStyleSheet(f"background-color: {theme['button']}; color: {theme['text']};")
    box_button.setStyleSheet(f"background-color: {theme['button']}; color: {theme['text']};")
    text_label.setStyleSheet(f"{theme['text']}")



def get_llm_response(user_message):
    system_prompt = "You are a friendly, playful cat chatbot who uses cat emojis 🐱 and short replies."

    response = ollama.chat(
        model="mistral",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]
    )

    return response["message"]["content"]


app = QApplication(sys.argv)

#next four lines set the font
#font_id = QFontDatabase.addApplicationFont("InterVariable.ttf")
#font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
#app_font = QFont(font_family, 10)
#app.setFont(app_font)

#this fixes the font crash upon program run
font_id = QFontDatabase.addApplicationFont("InterVariable.ttf")
families = QFontDatabase.applicationFontFamilies(font_id)

#if families:
#    font_family = families[0]
#   app_font = QFont(font_family, 10)
#    app.setFont(app_font)
#else:
#    print("⚠ Custom font not found, using default.")


window = QWidget()
window.setWindowTitle("Cat Chat Bot")

#sets the favicon for the window
window.setWindowIcon(QIcon("catBot_multi.ico"))
#sets the background color for the window
window.setStyleSheet("background-color: #2b2b2b;")

main_layout = QVBoxLayout()
top_row = QHBoxLayout()

#help with file handling
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # PyInstaller temp folder
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# GIF label
gif_label = QLabel()
gif_label.setAlignment(Qt.AlignCenter)
#movie = QMovie("kittygiftest.gif")  # your gif file
movie = QMovie(resource_path("kittygiftest.gif"))
gif_label.setMovie(movie)
movie.start()

#fish button

fish_button = QPushButton("🐟")
fish_button.setFixedSize(40, 40)
fish_button.setStyleSheet("""
    QPushButton {
        background-color: #444;
        color: white;
        border-radius: 8px;
        font-size: 18px;
    }
    QPushButton:hover {
        background-color: #666;
    }
""")
fish_button.setToolTip("Give the cat a fish 🐟")

box_button = QPushButton("📦")
box_button.setFixedSize(40, 40)
box_button.setStyleSheet("""
    QPushButton {
        background-color: #444;
        color: white;
        border-radius: 8px;
        font-size: 18px;
    }
    QPushButton:hover {
        background-color: #666;
    }
""")

box_button.setToolTip("Give kitty a box 📦")

#creates a save button
save_button = QPushButton("💾")
save_button.setFixedSize(40, 40)
save_button.setStyleSheet("""
    QPushButton {
        background-color: #444;
        color: white;
        border-radius: 8px;
        font-size: 18px;
    }
    QPushButton:hover {
        background-color: #666;
    }
""")

#theme button
theme_button = QPushButton("🎨")
theme_button.setFixedSize(40, 40)
theme_button.setStyleSheet("""
    QPushButton {
        background-color: #444;
        color: white;
        border-radius: 8px;
        font-size: 16px;
    }
    QPushButton:hover {
        background-color: #666;
    }
""")

# Text label under the GIF
text_label = QLabel("Hello! I'm your Cat Chat Bot 🐱🤖")
text_label.setAlignment(Qt.AlignCenter)

## this will be the holder for the typed text
text_label2 = QLabel("...")
text_label2.setAlignment(Qt.AlignCenter)

#this sets the font for the title
#title_font = QFont(font_family, 14, QFont.Bold)
#text_label.setFont(title_font)

# Input row (text box + button)
top_row = QVBoxLayout()
input_box = QLineEdit()
input_box.setPlaceholderText("Type your message...")

#sets text of enter button, and font type
send_button = QPushButton("Enter")
#send_button.setFont(title_font)

#sets the color for the text
text_label.setStyleSheet("color: white; font-size: 14px;")
input_box.setStyleSheet("color: white; background-color: #3c3c3c;")
send_button.setStyleSheet("background-color: #555; color: white;")


#chat history
chat_history = QTextEdit()
chat_history.setReadOnly(True)

#set chat font
#chat_font = QFont(font_family, 10)
#chat_history.setFont(title_font)

top_row.addWidget(gif_label)

button_row = QHBoxLayout()
button_row.setAlignment(Qt.AlignCenter)

button_row.addWidget(fish_button)
button_row.addWidget(box_button)
button_row.addWidget(theme_button)
button_row.addWidget(save_button)

main_layout.addLayout(top_row)
main_layout.addLayout(button_row)
main_layout.addWidget(text_label)
main_layout.addWidget(chat_history)
main_layout.addWidget(input_box)
main_layout.addWidget(send_button)

main_layout.addLayout(top_row)
window.setLayout(main_layout)

#when fish button is clicked
def give_fish():
    chat_history.setStyleSheet("color: white; background-color: #1e1e1e;")
    chat_history.append("You: 🐟")
    chat_history.append("Cat Bot: *nom nom nom* 😻🐟 Thank you, human!")

    if sound_on:
        mew_sound.stop()
        mew_sound.play()

fish_button.clicked.connect(give_fish)

#when box button is clicked
def give_box():
    chat_history.setStyleSheet("color: white; background-color: #1e1e1e;")
    chat_history.append("You: 📦")
    chat_history.append("Cat Bot: I fits, I sits 😼📦 This box is PERFECT.")
    if sound_on:
        mew_sound.stop()
        mew_sound.play()

box_button.clicked.connect(give_box)

#when save button is clicked
def save_chat():
    chat_history.setStyleSheet("color: white; background-color: #1e1e1e;")
    chat_history.append("You: 💾")
    chat_history.append("Chat history has been saved")

save_button.clicked.connect(save_chat)


def save_chat_history():
    text = chat_history.toPlainText()
    if not text.strip():
        return

    file_path, _ = QFileDialog.getSaveFileName(
        window,
        "Save Chat History",
        "cat_chat.txt",
        "Text Files (*.txt)"
    )

    if file_path:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text)


save_button.clicked.connect(save_chat_history)

window.setLayout(main_layout)
window.resize(300, 450)
window.show()

def send_message():
    #layout.insertWidget(2, chat_history)
    user_text = input_box.text()
    if user_text:
        chat_history.setStyleSheet("color: white; background-color: #1e1e1e;")
        text_label2.setText(f"You said: {user_text} ")
        input_box.clear()
        text_label.setText("Thinking... 🐾")

        try:
            reply = get_llm_response(user_text)
            chat_history.append(f"Cat Bot: {reply}")
            text_label.setText("I am your friendly Cat Chat Bot 😺")
        except Exception as e:
            chat_history.append("Cat Bot: My brain is napping 😿")
            print(e)

#change the theme on button click
def cycle_theme():
    global current_theme
    current_theme = (current_theme + 1) % len(themes)
    apply_theme()

theme_button.clicked.connect(cycle_theme)
apply_theme()  # call once on startup

send_button.clicked.connect(send_message)
input_box.returnPressed.connect(send_message)

=======
#import for local llm functionality
import sys
import ollama

import re

#import for file saving/text writing
from PyQt5.QtWidgets import QFileDialog

#import statement to import custom font
from PyQt5.QtGui import QFontDatabase, QFont

#import for window functions and layout
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtWidgets import (
    QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout,
    QLineEdit, QPushButton
)
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt

#this allows you to import ICO favicons
from PyQt5.QtGui import QIcon

import os, sys
from PyQt5.QtGui import QFontDatabase, QFont

#establish different visual themes
themes = [
    {
        "name": "Dark",
        "window": "#2b2b2b",
        "input": "#3c3c3c",
        "chat_bg": "#1e1e1e",
        "text": "white",
        "button": "#555"
    },
    {
         "name": "Peach Cat",
        "window": "#fff1e6",
        "input": "#ffd8b5",
        "chat_bg": "#ffe4cc",
        "text": "#4a2c1a",
        "button": "#ffb07c"
    },
    {
        "name": "Meow Mode",
        "window": "#3a2c23",
        "input": "#5a4333",
        "chat_bg": "#2b1e16",
        "text": "#f5e6d3",
        "button": "#8b5e3c"
    }
]

current_theme = 0

#create a definition for changing text and boxes
def apply_theme():
    theme = themes[current_theme]

    window.setStyleSheet(f"background-color: {theme['window']};")
    input_box.setStyleSheet(f"color: {theme['text']}; background-color: {theme['input']};")
    chat_history.setStyleSheet(f"color: {theme['text']}; background-color: {theme['chat_bg']};")
    send_button.setStyleSheet(f"background-color: {theme['button']}; color: {theme['text']};")
    theme_button.setStyleSheet(f"background-color: {theme['button']}; color: {theme['text']};")
    fish_button.setStyleSheet(f"background-color: {theme['button']}; color: {theme['text']};")
    save_button.setStyleSheet(f"background-color: {theme['button']}; color: {theme['text']};")
    box_button.setStyleSheet(f"background-color: {theme['button']}; color: {theme['text']};")
    text_label.setStyleSheet(f"{theme['text']}")



def get_llm_response(user_message):
    system_prompt = "You are a friendly, playful cat chatbot who uses cat emojis 🐱 and short replies."

    response = ollama.chat(
        model="mistral",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]
    )

    return response["message"]["content"]


app = QApplication(sys.argv)

#next four lines set the font
#font_id = QFontDatabase.addApplicationFont("InterVariable.ttf")
#font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
#app_font = QFont(font_family, 10)
#app.setFont(app_font)

#this fixes the font crash upon program run
font_id = QFontDatabase.addApplicationFont("InterVariable.ttf")
families = QFontDatabase.applicationFontFamilies(font_id)

#if families:
#    font_family = families[0]
#   app_font = QFont(font_family, 10)
#    app.setFont(app_font)
#else:
#    print("⚠ Custom font not found, using default.")


window = QWidget()
window.setWindowTitle("Cat Chat Bot")

#sets the favicon for the window
window.setWindowIcon(QIcon("catBot_multi.ico"))
#sets the background color for the window
window.setStyleSheet("background-color: #2b2b2b;")

main_layout = QVBoxLayout()
top_row = QHBoxLayout()

#help with file handling
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # PyInstaller temp folder
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# GIF label
gif_label = QLabel()
gif_label.setAlignment(Qt.AlignCenter)
#movie = QMovie("kittygiftest.gif")  # your gif file
movie = QMovie(resource_path("kittygiftest.gif"))
gif_label.setMovie(movie)
movie.start()

#fish button

fish_button = QPushButton("🐟")
fish_button.setFixedSize(40, 40)
fish_button.setStyleSheet("""
    QPushButton {
        background-color: #444;
        color: white;
        border-radius: 8px;
        font-size: 18px;
    }
    QPushButton:hover {
        background-color: #666;
    }
""")
fish_button.setToolTip("Give the cat a fish 🐟")

box_button = QPushButton("📦")
box_button.setFixedSize(40, 40)
box_button.setStyleSheet("""
    QPushButton {
        background-color: #444;
        color: white;
        border-radius: 8px;
        font-size: 18px;
    }
    QPushButton:hover {
        background-color: #666;
    }
""")

box_button.setToolTip("Give kitty a box 📦")

#creates a save button
save_button = QPushButton("💾")
save_button.setFixedSize(40, 40)
save_button.setStyleSheet("""
    QPushButton {
        background-color: #444;
        color: white;
        border-radius: 8px;
        font-size: 18px;
    }
    QPushButton:hover {
        background-color: #666;
    }
""")

#theme button
theme_button = QPushButton("🎨")
theme_button.setFixedSize(40, 40)
theme_button.setStyleSheet("""
    QPushButton {
        background-color: #444;
        color: white;
        border-radius: 8px;
        font-size: 16px;
    }
    QPushButton:hover {
        background-color: #666;
    }
""")

# Text label under the GIF
text_label = QLabel("Hello! I'm your Cat Chat Bot 🐱🤖")
text_label.setAlignment(Qt.AlignCenter)

## this will be the holder for the typed text
text_label2 = QLabel("...")
text_label2.setAlignment(Qt.AlignCenter)

#this sets the font for the title
#title_font = QFont(font_family, 14, QFont.Bold)
#text_label.setFont(title_font)

# Input row (text box + button)
top_row = QVBoxLayout()
input_box = QLineEdit()
input_box.setPlaceholderText("Type your message...")

#sets text of enter button, and font type
send_button = QPushButton("Enter")
#send_button.setFont(title_font)

#sets the color for the text
text_label.setStyleSheet("color: white; font-size: 14px;")
input_box.setStyleSheet("color: white; background-color: #3c3c3c;")
send_button.setStyleSheet("background-color: #555; color: white;")


#chat history
chat_history = QTextEdit()
chat_history.setReadOnly(True)

#set chat font
#chat_font = QFont(font_family, 10)
#chat_history.setFont(title_font)

top_row.addWidget(gif_label)

button_row = QHBoxLayout()
button_row.setAlignment(Qt.AlignCenter)

button_row.addWidget(fish_button)
button_row.addWidget(box_button)
button_row.addWidget(theme_button)
button_row.addWidget(save_button)

main_layout.addLayout(top_row)
main_layout.addLayout(button_row)
main_layout.addWidget(text_label)
main_layout.addWidget(chat_history)
main_layout.addWidget(input_box)
main_layout.addWidget(send_button)

main_layout.addLayout(top_row)
window.setLayout(main_layout)

#when fish button is clicked
def give_fish():
    chat_history.setStyleSheet("color: white; background-color: #1e1e1e;")
    chat_history.append("You: 🐟")
    chat_history.append("Cat Bot: *nom nom nom* 😻🐟 Thank you, human!")

    if sound_on:
        mew_sound.stop()
        mew_sound.play()

fish_button.clicked.connect(give_fish)

#when box button is clicked
def give_box():
    chat_history.setStyleSheet("color: white; background-color: #1e1e1e;")
    chat_history.append("You: 📦")
    chat_history.append("Cat Bot: I fits, I sits 😼📦 This box is PERFECT.")
    if sound_on:
        mew_sound.stop()
        mew_sound.play()

box_button.clicked.connect(give_box)

#when save button is clicked
def save_chat():
    chat_history.setStyleSheet("color: white; background-color: #1e1e1e;")
    chat_history.append("You: 💾")
    chat_history.append("Chat history has been saved")

save_button.clicked.connect(save_chat)


def save_chat_history():
    text = chat_history.toPlainText()
    if not text.strip():
        return

    file_path, _ = QFileDialog.getSaveFileName(
        window,
        "Save Chat History",
        "cat_chat.txt",
        "Text Files (*.txt)"
    )

    if file_path:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text)


save_button.clicked.connect(save_chat_history)

window.setLayout(main_layout)
window.resize(300, 450)
window.show()

def send_message():
    #layout.insertWidget(2, chat_history)
    user_text = input_box.text()
    if user_text:
        chat_history.setStyleSheet("color: white; background-color: #1e1e1e;")
        text_label2.setText(f"You said: {user_text} ")
        input_box.clear()
        text_label.setText("Thinking... 🐾")

        try:
            reply = get_llm_response(user_text)
            chat_history.append(f"Cat Bot: {reply}")
            text_label.setText("I am your friendly Cat Chat Bot 😺")
        except Exception as e:
            chat_history.append("Cat Bot: My brain is napping 😿")
            print(e)

#change the theme on button click
def cycle_theme():
    global current_theme
    current_theme = (current_theme + 1) % len(themes)
    apply_theme()

theme_button.clicked.connect(cycle_theme)
apply_theme()  # call once on startup

send_button.clicked.connect(send_message)
input_box.returnPressed.connect(send_message)

>>>>>>> ecd40400c76e210e986a0e489a9ec030de886afd
sys.exit(app.exec_())