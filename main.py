from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from init import session
from models import Word
from kivymd.app import MDApp
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivy.uix.boxlayout import BoxLayout

class MainArea(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def add_word(self, instance):
        english = self.ids.english_word.text.strip()
        translation = self.ids.translation.text.strip()

        if english and translation:
            word = Word(eng=english, rus=translation)
            session.add(word)
            session.commit()

            self.ids.english_word.text = ''
            self.ids.translation.text = ''

class Evolve_page(Screen):
    def on_enter(self):
        words = session.query(Word).all()
        word_text = "\n".join([f"{word.eng} - {word.rus}" for word in words])
        self.ids.word_list_label.text = word_text

class AllWords(Screen):
    def on_enter(self):
        words = session.query(Word).all()
        word_text = "\n".join([f"{word.eng} - {word.rus}" for word in words])
        self.ids.word_list_label.text = word_text

class TestApp(MDApp):
    def build(self):
        Builder.load_file('views/main.kv')
        
        sm = ScreenManager()
        sm.add_widget(MainArea(name='MainArea'))
        sm.add_widget(Evolve_page(name='Evolve_page'))
        sm.add_widget(AllWords(name='AllWords'))

        return sm

    def change_screen(self, screen_name, tab_name):
        self.root.current = screen_name

if __name__ == '__main__':
    TestApp().run()
