# src/interfaces/gui.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class GysinIAGUI(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.output = Label(text="Bem-vindo à Gysin IA!")
        self.input = TextInput(multiline=False)
        submit = Button(text="Enviar")
        submit.bind(on_press=self.handle_input)

        layout.add_widget(self.output)
        layout.add_widget(self.input)
        layout.add_widget(submit)
        return layout

    def handle_input(self, instance):
        user_input = self.input.text
        # Processar input e obter resposta da assistente
        response = "Resposta da Gysin IA"  # Placeholder
        self.output.text = response
        self.input.text = ""

if __name__ == '__main__':
    GysinIAGUI().run()