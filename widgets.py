import flet as ft

class View_Page:
    def __init__(self, page: ft.Page, controller):
        """Pagina en blanco"""
        self.page = page
        self.controller = controller

    def build_page(self):
        """Constructor de la pagina"""
        Content = ft.Container()

        return Content
    
    def get_content(self):
        """Inicializador de la pagina"""
        return self.build_page()