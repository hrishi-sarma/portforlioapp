# portfolio.py
from kivy.app import *
from kivy.uix.gridlayout import *
from kivy.uix.label import *
from kivy.graphics import *


class PortfolioApp(App):
    def build(self):
        layout = GridLayout(cols=1, spacing=10, padding=20)
        with layout.canvas.before:
            Color(1, 0, 0, 1)
            self.rect = Rectangle(size=(layout.width, 2), pos=layout.pos)

        heading_label = Label(text="Portfolio App", font_size=32)
        layout.add_widget(heading_label)

        name_label = Label(text="Hrishikesh Sarma", font_size=24)
        layout.add_widget(name_label)

        skills_label = Label(text="Skills:", font_size=20)
        layout.add_widget(skills_label)

        skills = ["Python (intermediate)", "C (beginner)", "A little bit of GFX"]
        for skill in skills:
            skill_label = Label(text=skill, font_size=16)
            layout.add_widget(skill_label)
        custom_paragraph = "New to app development so this one might be a little bland."
        custom_paragraph_label = Label(text=custom_paragraph, font_size=18, halign="left")
        layout.add_widget(custom_paragraph_label)

        return layout


if __name__ == '__main__':
    PortfolioApp().run()
