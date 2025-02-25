import flet as ft
import widgets as wg

class Home_page(wg.View_Page):
    def __init__(self, page, controller):
        """Pagina de inicio"""
        super().__init__(page, controller)

    def build_page(self):
        """Constructor de la pagina"""
        Content = ft.Container()

        return Content