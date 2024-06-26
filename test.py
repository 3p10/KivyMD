from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDButton
from kivy.uix.image import Image

# KV string for layout
kv_string = """
ScreenManager:
    MainScreen:
    SecondScreen:
    ThirdScreen:
    FourthScreen:

<MainScreen>:
    name: 'main'
    BoxLayout:
        orientation: 'vertical'
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1
            Rectangle:
                size: self.size
                pos: self.pos
        Image:
            source: 'image1.png'
            size_hint_y: None
            height: '200dp'
        MDLabel:
            markup: True
            text: ' [b]Exam Information:[/b] \\n' +\
                ' [u]Course: CT30A2803 User Interfaces and Usability - Monimuoto-opetus 8.1.2024-19.4.2024[/u] \\n' +\
                ' Exam type: Final Exam \\n Language: English \\n Recommended tools: Paper, pen and camera \\n' +\
                ' General information about the exam: \\n' +\
                '  • Questions in total: 6 \\n  • Maximum points: 20 \\n  • 4 right/wrong type questions (8 points/ 40%) \\n' +\
                '  • 2 Text/Essay type questions (12 points/ 60%) \\n' +\
                ' Attempts: 1 \\n Duration: 30 min[/size]'
            halign: 'left'  # Align text to the left
            theme_text_color: 'Primary'
        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: dp(38)
            padding: dp(8)
            spacing: dp(8)
            MDCheckbox:
                id: accept_checkbox
            MDLabel:
                text: 'I have read und understood the assignment.'
                theme_text_color: 'Primary'
        Button:
            text: 'Start Exam'
            size_hint: None, None
            size: 150, 50
            pos_hint: {'right': 1, 'bottom': 1}
            theme_text_color: 'Custom'
            on_release: root.manager.current = 'second'
            background_color: (0, 0, 0, 1)

<SecondScreen>:
    name: 'second'
    BoxLayout:
        orientation: 'vertical'
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1
            Rectangle:
                size: self.size
                pos: self.pos
        Image:
            source: 'image1.png'
            size_hint_y: None
            height: '200dp'
        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: dp(40)
            padding: dp(10), dp(5)
            MDLabel:
                text: 'Question 1 and 2:'
                halign: 'left'
            # Box containing "Time: 30:00"
            BoxLayout:
                size_hint_y: None
                height: dp(38)
                padding: dp(8)
                spacing: dp(8)
                padding: dp(250), dp(5)
                MDLabel:
                    text: "Time: 30:00"
                    theme_text_color: 'Primary'
                    halign: 'center'
                    valign: 'middle'
                    size_hint_x: None
                    width: 150
                    canvas.before:
                        Color:
                            rgba: 0.5, 0.5, 0.5, 1
                        Rectangle:
                            size: self.size
                            pos: self.pos
        MDBoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: dp(130)
            padding: dp(13), dp(1)
            md_bg_color: 0.7, 0.7, 0.7, 1
            MDLabel:
                text: "UX design is concerned only with how a product looks, not how it functions?"
                valign: 'center'
            MDBoxLayout:
                orientation: 'horizontal'
                size_hint_y: None
                height: dp(30)
                padding: dp(5)
                spacing: dp(3)
                MDCheckbox:
                    id: true_checkbox1
                MDLabel:
                    text: "True"
            MDBoxLayout:
                orientation: 'horizontal'
                size_hint_y: None
                height: dp(30)
                padding: dp(5)
                spacing: dp(3)
                MDCheckbox:
                    id: false_checkbox1
                MDLabel:
                    text: "False"
                # Square with the text "2 points"
                BoxLayout:
                    size_hint_y: None
                    height: dp(68)
                    padding: dp(250), dp(5)
                    MDBoxLayout:
                        orientation: 'horizontal'
                        size_hint_x: None
                        width: dp(100)
                        padding: dp(4), 0
                        spacing: dp(8)
                        canvas.before:
                            Color:
                                rgba: 1, 1, 1, 1
                            Rectangle:
                                size: self.size
                                pos: self.pos
                        MDLabel:
                            text: "Question 1 \\n2 points"
                            theme_text_color: 'Primary'
                            halign: 'center'
                            valign: 'center'
        # Space between question boxes
        MDBoxLayout:
            size_hint_y: None
            height: dp(20)  
        MDBoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: dp(130)
            padding: dp(13), dp(1)
            md_bg_color: 0.7, 0.7, 0.7, 1
            MDLabel:
                text: "A good UX designer prioritizes accessibility to ensure all users, including those with disabilities, can use the product effectively?"
                valign: 'center'
            MDBoxLayout:
                orientation: 'horizontal'
                size_hint_y: None
                height: dp(30)
                padding: dp(5)
                spacing: dp(3)
                MDCheckbox:
                    id: true_checkbox2
                MDLabel:
                    text: "True"
            MDBoxLayout:
                orientation: 'horizontal'
                size_hint_y: None
                height: dp(30)
                padding: dp(5)
                spacing: dp(3)
                MDCheckbox:
                    id: false_checkbox2
                MDLabel:
                    text: "False"
                # Square with the text "2 points"
                BoxLayout:
                    size_hint_y: None
                    height: dp(68)
                    padding: dp(250), dp(5)
                    MDBoxLayout:
                        orientation: 'horizontal'
                        size_hint_x: None
                        width: dp(100)
                        padding: dp(4), 0
                        spacing: dp(8)
                        canvas.before:
                            Color:
                                rgba: 1, 1, 1, 1
                            Rectangle:
                                size: self.size
                                pos: self.pos
                        MDLabel:
                            text: "Question 2 \\n2 points"
                            theme_text_color: 'Primary'
                            halign: 'center'
                            valign: 'center'
        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: dp(50)
            padding: dp(8)
            spacing: dp(8)
            Button:
                size_hint: None, None
                size: 200, 50
                text: 'Main Page'
                on_release: root.manager.current = 'main'
                background_color: (0, 0, 0, 1)
            Widget:
            Button:
                size_hint: None, None
                size: 200, 50
                text: 'Next Question'
                on_release: root.manager.current = 'third'
                background_color: (0, 0, 0, 1)

        # Add gray boxes
        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: dp(28)
            padding: dp(10), dp(5), dp(10), dp(5)
            spacing: dp(5)
            MDLabel:
                size_hint_x: None
                width: dp(95)
                canvas.before:
                    Color:
                        rgba: 0.5, 0.5, 0.5, 1
                    Rectangle:
                        size: self.size
                        pos: self.pos
            MDLabel:
                size_hint_x: None
                width: dp(95)
                canvas.before:
                    Color:
                        rgba: 0.5, 0.5, 0.5, 1
                    Rectangle:
                        size: self.size
                        pos: self.pos
            MDLabel:
                size_hint_x: None
                width: dp(95)
                canvas.before:
                    Color:
                        rgba: 0.5, 0.5, 0.5, 1
                    Rectangle:
                        size: self.size
                        pos: self.pos
            MDLabel:
                size_hint_x: None
                width: dp(95)
                canvas.before:
                    Color:
                        rgba: 0.5, 0.5, 0.5, 1
                    Rectangle:
                        size: self.size
                        pos: self.pos
            MDLabel:
                size_hint_x: None
                width: dp(190)
                canvas.before:
                    Color:
                        rgba: 0.5, 0.5, 0.5, 1
                    Rectangle:
                        size: self.size
                        pos: self.pos
            MDLabel:
                size_hint_x: None
                width: dp(190)
                canvas.before:
                    Color:
                        rgba: 0.5, 0.5, 0.5, 1
                    Rectangle:
                        size: self.size
                        pos: self.pos
            
<ThirdScreen>:
    name: 'third'
    BoxLayout:
        orientation: 'vertical'
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1
            Rectangle:
                size: self.size
                pos: self.pos
        Image:
            source: 'image1.png'
            size_hint_y: None
            height: '200dp'
        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: dp(40)
            padding: dp(10), dp(5)
            MDLabel:
                text: 'Question 3 and 4:'
                halign: 'left'
            # Box containing "Time: 26:20"
            BoxLayout:
                size_hint_y: None
                height: dp(38)
                padding: dp(8)
                spacing: dp(8)
                padding: dp(250), dp(5)
                MDLabel:
                    text: "Time: 26:20"
                    theme_text_color: 'Primary'
                    halign: 'center'
                    valign: 'middle'
                    size_hint_x: None
                    width: 150
                    canvas.before:
                        Color:
                            rgba: 0.5, 0.5, 0.5, 1
                        Rectangle:
                            size: self.size
                            pos: self.pos
        MDBoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: dp(130)
            padding: dp(13), dp(1)
            md_bg_color: 0.7, 0.7, 0.7, 1
            MDLabel:
                text: "Good UI design focuses solely on making things look visually appealing?"
                valign: 'center'
            MDBoxLayout:
                orientation: 'horizontal'
                size_hint_y: None
                height: dp(30)
                padding: dp(5)
                spacing: dp(3)
                MDCheckbox:
                    id: true_checkbox1
                MDLabel:
                    text: "True"
            MDBoxLayout:
                orientation: 'horizontal'
                size_hint_y: None
                height: dp(30)
                padding: dp(5)
                spacing: dp(3)
                MDCheckbox:
                    id: false_checkbox1
                MDLabel:
                    text: "False"
                # Square with the text "2 points"
                BoxLayout:
                    size_hint_y: None
                    height: dp(68)
                    padding: dp(250), dp(5)
                    MDBoxLayout:
                        orientation: 'horizontal'
                        size_hint_x: None
                        width: dp(100)
                        padding: dp(4), 0
                        spacing: dp(8)
                        canvas.before:
                            Color:
                                rgba: 1, 1, 1, 1
                            Rectangle:
                                size: self.size
                                pos: self.pos
                        MDLabel:
                            text: "Question 3 \\n2 points"
                            theme_text_color: 'Primary'
                            halign: 'center'
                            valign: 'center'
        # Space between boxes
        MDBoxLayout:
            size_hint_y: None
            height: dp(20)
        MDBoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: dp(130)
            padding: dp(13), dp(1)
            md_bg_color: 0.7, 0.7, 0.7, 1
            MDLabel:
                text: "Consistency in UI design helps users predict how elements will behave across an application."
                valign: 'center'
            MDBoxLayout:
                orientation: 'horizontal'
                size_hint_y: None
                height: dp(30)
                padding: dp(5)
                spacing: dp(3)
                MDCheckbox:
                    id: true_checkbox2
                MDLabel:
                    text: "True"
            MDBoxLayout:
                orientation: 'horizontal'
                size_hint_y: None
                height: dp(30)
                padding: dp(5)
                spacing: dp(3)
                MDCheckbox:
                    id: false_checkbox2
                MDLabel:
                    text: "False"
                # Square with the text "2 points"
                BoxLayout:
                    size_hint_y: None
                    height: dp(68)
                    padding: dp(250), dp(5)
                    MDBoxLayout:
                        orientation: 'horizontal'
                        size_hint_x: None
                        width: dp(100)
                        padding: dp(4), 0
                        spacing: dp(8)
                        canvas.before:
                            Color:
                                rgba: 1, 1, 1, 1
                            Rectangle:
                                size: self.size
                                pos: self.pos
                        MDLabel:
                            text: "Question 4 \\n2 points"
                            theme_text_color: 'Primary'
                            halign: 'center'
                            valign: 'center'
        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: dp(50)
            padding: dp(8)
            spacing: dp(8)
            Button:
                size_hint: None, None
                size: 200, 50
                text: 'Previous Question'
                on_release: root.manager.current = 'second'
                background_color: (0, 0, 0, 1)
            Widget:
            Button:
                size_hint: None, None
                size: 200, 50
                text: 'Next Question'
                on_release: root.manager.current = 'fourth'
                background_color: (0, 0, 0, 1)

        # Add gray and green boxes
        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: dp(28)
            padding: dp(10), dp(5), dp(10), dp(5)
            spacing: dp(5)
            MDLabel:
                size_hint_x: None
                width: dp(95)
                canvas.before:
                    Color:
                        rgba: 0, 1, 0, 1 #Green
                    Rectangle:
                        size: self.size
                        pos: self.pos
            MDLabel:
                size_hint_x: None
                width: dp(95)
                canvas.before:
                    Color:
                        rgba: 0, 1, 0, 1 #Green
                    Rectangle:
                        size: self.size
                        pos: self.pos
            MDLabel:
                size_hint_x: None
                width: dp(95)
                canvas.before:
                    Color:
                        rgba: 0.5, 0.5, 0.5, 1
                    Rectangle:
                        size: self.size
                        pos: self.pos
            MDLabel:
                size_hint_x: None
                width: dp(95)
                canvas.before:
                    Color:
                        rgba: 0.5, 0.5, 0.5, 1
                    Rectangle:
                        size: self.size
                        pos: self.pos
            MDLabel:
                size_hint_x: None
                width: dp(190)
                canvas.before:
                    Color:
                        rgba: 0.5, 0.5, 0.5, 1
                    Rectangle:
                        size: self.size
                        pos: self.pos
            MDLabel:
                size_hint_x: None
                width: dp(190)
                canvas.before:
                    Color:
                        rgba: 0.5, 0.5, 0.5, 1
                    Rectangle:
                        size: self.size
                        pos: self.pos
                        


<FourthScreen>:
    name: 'fourth'
    BoxLayout:
        orientation: 'vertical'
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1
            Rectangle:
                size: self.size
                pos: self.pos
        Image:
            source: 'image1.png'
            size_hint_y: None
            height: '200dp'
        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: dp(40)
            padding: dp(10), dp(5)
            MDLabel:
                text: 'Question 5:'
                halign: 'left'
            # Box containing "Time: 22:17"
            BoxLayout:
                size_hint_y: None
                height: dp(38)
                padding: dp(8)
                spacing: dp(8)
                padding: dp(250), dp(5)
                MDLabel:
                    text: "Time: 22:17"
                    theme_text_color: 'Primary'
                    halign: 'center'
                    valign: 'middle'
                    size_hint_x: None
                    width: 150
                    canvas.before:
                        Color:
                            rgba: 0.5, 0.5, 0.5, 1
                        Rectangle:
                            size: self.size
                            pos: self.pos

        MDBoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: dp(285)
            padding: dp(13), dp(1)
            md_bg_color: 0.7, 0.7, 0.7, 1
            MDLabel:
                text: "Explain the importance of user interface (UI) consistency in enhancing the overall user experience. Provide examples to support your explanation."
                valign: 'center'
            BoxLayout:
                size_hint_y: None
                height: dp(200)
                padding: dp(13), dp(5)
                canvas.before:
                    Color:
                        rgba: 1, 1, 1, 1
                    Rectangle:
                        size: self.size
                        pos: self.pos
                TextInput:
                    hint_text: "Type your answer here"
                    multiline: True
                    background_color: 1, 1, 1, 1  # White background
                    foreground_color: 0, 0, 0, 1  # Black text color

                        
        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: dp(50)
            padding: dp(8)
            spacing: dp(8)
            Button:
                size_hint: None, None
                size: 200, 50
                text: 'Previous Question'
                on_release: root.manager.current = 'third'
                background_color: (0, 0, 0, 1)
            Widget:
            Button:
                size_hint: None, None
                size: 200, 50
                text: 'Next Question'
                on_release: root.manager.current = 'fifth'
                background_color: (0, 0, 0, 1)

        # Add gray, greean and yellow boxes
        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: dp(28)
            padding: dp(10), dp(5), dp(10), dp(5)
            spacing: dp(5)
            MDLabel:
                size_hint_x: None
                width: dp(95)
                canvas.before:
                    Color:
                        rgba: 0, 1, 0, 1  # Green
                    Rectangle:
                        size: self.size
                        pos: self.pos
            MDLabel:
                size_hint_x: None
                width: dp(95)
                canvas.before:
                    Color:
                        rgba: 0, 1, 0, 1 # Green
                    Rectangle:
                        size: self.size
                        pos: self.pos
            MDLabel:
                size_hint_x: None
                width: dp(95)
                canvas.before:
                    Color:
                        rgba: 1, 1, 0, 1 # Yellow
                    Rectangle:
                        size: self.size
                        pos: self.pos
            MDLabel:
                size_hint_x: None
                width: dp(95)
                canvas.before:
                    Color:
                        rgba: 0, 1, 0, 1 # Green
                    Rectangle:
                        size: self.size
                        pos: self.pos
            MDLabel:
                size_hint_x: None
                width: dp(190)
                canvas.before:
                    Color:
                        rgba: 0.5, 0.5, 0.5, 1
                    Rectangle:
                        size: self.size
                        pos: self.pos
            MDLabel:
                size_hint_x: None
                width: dp(190)
                canvas.before:
                    Color:
                        rgba: 0.5, 0.5, 0.5, 1
                    Rectangle:
                        size: self.size
                        pos: self.pos

<FifthScreen>:
    name: 'fifth'
    BoxLayout:
        orientation: 'vertical'
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1
            Rectangle:
                size: self.size
                pos: self.pos
        Image:
            source: 'image1.png'
            size_hint_y: None
            height: '200dp'
        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: dp(40)
            padding: dp(10), dp(5)
            MDLabel:
                text: 'Question 6:'
                halign: 'left'
            # Box containing "Time: 04:20"
            BoxLayout:
                size_hint_y: None
                height: dp(38)
                padding: dp(8)
                spacing: dp(8)
                padding: dp(250), dp(5)
                MDLabel:
                    text: "Time: 04:20"
                    theme_text_color: 'Primary'
                    halign: 'center'
                    valign: 'middle'
                    size_hint_x: None
                    width: 150
                    canvas.before:
                        Color:
                            rgba: 1, 0, 0, 1
                        Rectangle:
                            size: self.size
                            pos: self.pos

        MDBoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: dp(285)
            padding: dp(13), dp(1)
            md_bg_color: 0.7, 0.7, 0.7, 1
            MDLabel:
                text: "Explain the importance of user interface (UI) consistency in enhancing the overall user experience. Provide examples to support your explanation."
                valign: 'center'
            BoxLayout:
                size_hint_y: None
                height: dp(200)
                padding: dp(13), dp(5)
                canvas.before:
                    Color:
                        rgba: 1, 1, 1, 1
                    Rectangle:
                        size: self.size
                        pos: self.pos
                TextInput:
                    hint_text: "Type your answer here"
                    multiline: True
                    background_color: 1, 1, 1, 1  # White background
                    foreground_color: 0, 0, 0, 1  # Black text color

                        
        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: dp(50)
            padding: dp(8)
            spacing: dp(8)
            Button:
                size_hint: None, None
                size: 200, 50
                text: 'Previous Question'
                on_release: root.manager.current = 'fourth'
                background_color: (0, 0, 0, 1)
            Widget:
            Button:
                size_hint: None, None
                size: 200, 50
                text: 'Exam Overview'
                on_release: root.manager.current = 'sixth'
                background_color: (0, 0, 0, 1)

        # Add gray, green and yellow boxes
        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: dp(28)
            padding: dp(10), dp(5), dp(10), dp(5)
            spacing: dp(5)
            MDLabel:
                size_hint_x: None
                width: dp(95)
                canvas.before:
                    Color:
                        rgba: 0, 1, 0, 1  # Green
                    Rectangle:
                        size: self.size
                        pos: self.pos
            MDLabel:
                size_hint_x: None
                width: dp(95)
                canvas.before:
                    Color:
                        rgba: 0, 1, 0, 1 # Green
                    Rectangle:
                        size: self.size
                        pos: self.pos
            MDLabel:
                size_hint_x: None
                width: dp(95)
                canvas.before:
                    Color:
                        rgba: 1, 1, 0, 1 # Yellow
                    Rectangle:
                        size: self.size
                        pos: self.pos
            MDLabel:
                size_hint_x: None
                width: dp(95)
                canvas.before:
                    Color:
                        rgba: 0, 1, 0, 1 # Green
                    Rectangle:
                        size: self.size
                        pos: self.pos
            MDLabel:
                size_hint_x: None
                width: dp(190)
                canvas.before:
                    Color:
                        rgba: 0, 1, 0, 1 # Green
                    Rectangle:
                        size: self.size
                        pos: self.pos
            MDLabel:
                size_hint_x: None
                width: dp(190)
                canvas.before:
                    Color:
                        rgba: 0.5, 0.5, 0.5, 1
                    Rectangle:
                        size: self.size
                        pos: self.pos

<SixthScreen>:
    name: 'sixth'
    BoxLayout:
        orientation: 'vertical'
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1
            Rectangle:
                size: self.size
                pos: self.pos
        Image:
            source: 'image1.png'
            size_hint_y: None
            height: '200dp'
        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: dp(40)
            padding: dp(10), dp(5)
            MDLabel:
                text: 'Exam Overview'
                halign: 'left'
            # Box containing "Time: 03:00"
            BoxLayout:
                size_hint_y: None
                height: dp(38)
                padding: dp(8)
                spacing: dp(8)
                padding: dp(250), dp(5)
                MDLabel:
                    text: "Time: 03:00"
                    theme_text_color: 'Primary'
                    halign: 'center'
                    valign: 'middle'
                    size_hint_x: None
                    width: 150
                    canvas.before:
                        Color:
                            rgba: 1, 0, 0, 1
                        Rectangle:
                            size: self.size
                            pos: self.pos
        MDBoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: dp(60)
            valign: 'center'
            padding: dp(13), dp(1)
            md_bg_color: 0.7, 0.7, 0.7, 1
            pos_hint: {'center_x': 0.5}
            size_hint_x: None
            width: dp(200)
            MDLabel:
                text: "4/6 questions answered"
                height: dp(40)
                halign: 'center'
        MDBoxLayout:
            size_hint_y: None
            height: dp(35)
        MDBoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: dp(60)
            valign: 'center'
            padding: dp(13), dp(1)
            md_bg_color: 0.7, 0.7, 0.7, 1
            pos_hint: {'center_x': 0.5}
            size_hint_x: None  # Remove automatic width calculation based on children
            width: dp(400)
            MDLabel:
                text: "Question 6 Not answered (Essay)"
                height: dp(40)
                halign: 'center'
        MDBoxLayout:
            size_hint_y: None
            height: dp(35)
        MDBoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: dp(60)
            valign: 'center'
            padding: dp(13), dp(1)
            md_bg_color: 0.7, 0.7, 0.7, 1
            pos_hint: {'center_x': 0.5}
            size_hint_x: None  # Remove automatic width calculation based on children
            width: dp(400)
            MDLabel:
                text: "Question 3 Not answered (True/False)"
                height: dp(40)
                halign: 'center'

        MDLabel:
            halign: 'left'
        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: dp(50)
            padding: dp(8)
            spacing: dp(8)
            Button:
                size_hint: None, None
                size: 200, 50
                pos_hint: {'left': 1, 'bottom': 1}
                text: 'Previous Question'
                on_release: root.manager.current = 'fifth'
                background_color: (0, 0, 0, 1)
            Widget:
            Button:
                size_hint: None, None
                size: 200, 50
                text: 'Return Exam'
                background_color: (0, 0, 0, 1)
        # Add gray, green and yellow boxes
        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: dp(28)
            padding: dp(10), dp(5), dp(10), dp(5)
            spacing: dp(5)
            MDLabel:
                size_hint_x: None
                width: dp(95)
                canvas.before:
                    Color:
                        rgba: 0, 1, 0, 1 # Green
                    Rectangle:
                        size: self.size
                        pos: self.pos
            MDLabel:
                size_hint_x: None
                width: dp(95)
                canvas.before:
                    Color:
                        rgba: 0, 1, 0, 1 # Green
                    Rectangle:
                        size: self.size
                        pos: self.pos
            MDLabel:
                size_hint_x: None
                width: dp(95)
                canvas.before:
                    Color:
                        rgba: 1, 1, 0, 1 # Yellow
                    Rectangle:
                        size: self.size
                        pos: self.pos
            MDLabel:
                size_hint_x: None
                width: dp(95)
                canvas.before:
                    Color:
                        rgba: 0, 1, 0, 1 # Green
                    Rectangle:
                        size: self.size
                        pos: self.pos
            MDLabel:
                size_hint_x: None
                width: dp(190)
                canvas.before:
                    Color:
                        rgba: 0, 1, 0, 1 # Green
                    Rectangle:
                        size: self.size
                        pos: self.pos
            MDLabel:
                size_hint_x: None
                width: dp(190)
                canvas.before:
                    Color:
                        rgba: 1, 1, 0, 1 # Yellow
                    Rectangle:
                        size: self.size
                        pos: self.pos

"""

# Define screens
class MainScreen(Screen):
    pass

class SecondScreen(Screen):
    pass

class ThirdScreen(Screen):
    pass

class FourthScreen(Screen):
    pass

class FifthScreen(Screen):
    pass

class SixthScreen(Screen):
    pass

# Define the app
class SimpleWebsiteApp(MDApp):
    def build(self):
        self.title = "Simple Website"
        self.icon = "icon.png"
        
        # Load the KV string
        Builder.load_string(kv_string)
        
        # Create Screen Manager
        sm = ScreenManager()
        sm.add_widget(MainScreen())
        sm.add_widget(SecondScreen())
        sm.add_widget(ThirdScreen())
        sm.add_widget(FourthScreen())
        sm.add_widget(FifthScreen())
        sm.add_widget(SixthScreen())
        
        return sm

# Run the app
if __name__ == '__main__':
    SimpleWebsiteApp().run()
