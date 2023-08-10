from kivymd.tools.hotreload.app import MDApp
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.button import MDRoundFlatIconButton
from kivy.core.text import LabelBase
from screens.screens import *


class WindowsManager(ScreenManager):
    pass


class Cutemi(MDApp):
    CLASSES = {
        'Welcome': 'screens.welcome',
        'Login': 'screens/login',
        'Signup': 'screens/signup'
    }
    AUTORELOADER_PATHS = [
        ('.', {'recursive': True})
    ]
    KV_FILES = [
        'kv/welcome.kv',
        'kv/login.kv',
        'kv/signup.kv'
    ]

    def build_app(self):
        self.wm = WindowsManager()
        screens = [
            Welcome(name="welcome"),
            Login(name="login"),
            Signup(name="signup")

        ]
        for screens in screens:
            self.wm.add_widget(screens)

        return self.wm


if __name__ == "__main__":
    LabelBase.register(
        name="tech", fn_regular='assets/fonts/Transformers_Movie.ttf')
    Cutemi().run()
