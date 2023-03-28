from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Canvas, Rectangle
from datetime import datetime


class BannerVisita(GridLayout):

    def __init__(self, **kwargs):
        self.rows = 1
        super().__init__()

        #itens da tela
        idvista = kwargs['idvisita']
        nome = kwargs['nome']
        empresa = kwargs['empresa']
        dtvisita = kwargs['dtvisita']
        hrvisita = kwargs['hrvisita']
        responsavel = kwargs['responsavel']

        #esquerda da tela
        esquerda = FloatLayout()
        esquerda_imagem = Image(pos_hint={'right': 0.8, "top": 0.85}, size_hint=(1, 0.66),
                                source=f'icones/foto.png')
        esquerda_label = Label(text=nome, size_hint=(1, 0.3), pos_hint={"right": 0.8, "top": 0.15})
        esquerda.add_widget(esquerda_imagem)
        esquerda.add_widget(esquerda_label)

        #meio da tela
        meio = FloatLayout()
        meio_label_cima = Label(text=f"Empresa: {empresa}     Responsavel: {responsavel}", size_hint=(1, 0.25), pos_hint={"right": 0.55, "top": 0.55})
        meio_label_baixo = Label(text=f"Horario: {hrvisita}      Data da Visita: {dtvisita}", size_hint=(1, 0.25), pos_hint={"right": 0.55, "top": 0.2})

        meio.add_widget(meio_label_cima)
        meio.add_widget(meio_label_baixo)


        #direita da tela
        #direita = FloatLayout()



        self.add_widget(esquerda)
        self.add_widget(meio)
        #self.add_widget(direita)