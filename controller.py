import flet as ft
import model as md

class Controller:
    def __init__(self, view):
        """Controlador de la aplicacion"""
        self.view = view
        self.model = md.Model()
