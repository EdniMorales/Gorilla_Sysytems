import flet as ft

from home_page import Home_page

class View:
    def __init__(self, page: ft.Page):
        """Interfaz grafica de la aplicacion"""
        self.page = page
        self.controller = None

    def Start_App(self):
        """Constructor de la aplicacion"""
        if self.controller is None:
            raise ValueError("No se cargo el controlador correctamente")
        
        #Instancia de las vistas de la aplicacion
        self.Home_page = Home_page(self.page, self.controller)

        self.navigate_to("/")

    def go_back(self):
        """Regresar al la vista anterior"""
        if len(self.page.views) > 1:
            self.page.views.pop()
            top_view = self.page.views[-1]
            self.page.update()

    def navigate_to(self, view_name: str):
        """Navegacion de la aplicacion"""
        page_main = self.Home_page.get_content() #Colocar la pagina principal
        match view_name:
            case "/":
                self.page.views.clear()
                self.page.views.append(page_main)

            case _:
                self.page.views.clear()
                self.page.views.append(page_main)

        self.page.update()