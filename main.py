import re
from datetime import datetime
from kivy.app import App
from kivy.lang import Builder
from telas import *
from botoes import *
import requests
from kivy.uix.textinput import TextInput
from bannervisita import BannerVisita

from BD import Oracle
import cx_Oracle

GUI = Builder.load_file("main.kv")

class MainApp(App):
    id_usuario = 1

    def build(self):
        self.banco = Oracle()
        return GUI
    def teste(self):
        pass

    #banco de dados
    def on_start(self):
        #foto de perfil
        foto_perfil = self.root.ids['foto_perfil']
        foto_perfil.source = 'icones/okj.png'

        #preencher visita
        connStr = 'APOIOAVENDAS/okajima123@192.168.254.190:1521/WINT'
        conn = cx_Oracle.connect(connStr)
        cursor = conn.cursor()
        cursor.execute('select IDVISITA, NOME, EMPRESA, DTVISITA, HORAVISITA, RESPONSAVEL, VEICULO  from fagner.visitas')
        for row in cursor:
            banner = BannerVisita(idvisita=row[0], nome=row[1], empresa=row[2], dtvisita=row[3],
                                  hrvisita=row[4], responsavel=row[5], veiculo=row[6])
            pagina_homepage = self.root.ids["homepage"]
            lista_visita = pagina_homepage.ids['lista_visita']
            lista_visita.add_widget(banner)

    #MUDAR TELA
    def mudar_tela(self, id_tela):
        gerenciador_telas = self.root.ids["screen_manager"]
        gerenciador_telas.current = id_tela



MainApp().run()