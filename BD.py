import re
import cx_Oracle
from kivy.app import App
from kivy.uix.textinput import TextInput
from datetime import datetime

class Oracle(TextInput):

    def autenticar_usuario(self, usuario, senha):
        connStr = 'FAGNER/261285@192.168.254.190:1521/WINT'
        conn = cx_Oracle.connect(connStr)
        cursor = conn.cursor()

        cursor.execute(f"SELECT COUNT(USUARIOBD)  FROM FAGNER.USUARIOAPP WHERE USUARIOBD  = '{usuario}'AND DECRYPT(SENHABD,USUARIOBD) ='{senha}'")
        resultado = cursor.fetchone()

        if resultado[0] == 1:
            flag = True
            print("ok")
            meuapp = App.get_running_app()
            meuapp.mudar_tela("homepage")
        else:
            flag = False
            print("not")
            meu_aplicativo = App.get_running_app()
            pagina_login = meu_aplicativo.root.ids["loginpage"]
            pagina_login.ids["msg_login"].text = "Senha/Usuario errado"
            pagina_login.ids["msg_login"].color = (1, 0, 0, 1)

        cursor.close()
        conn.close()

        return flag

    def criar_visita(self, data_visita):
        #data
        string_data = data_visita
        data_datetime = datetime.strptime(string_data,'%d/%m/%Y')
        data_date = data_datetime.date()


        return print(data_date)

    def insert_text(self, substring, from_undo=False):
        # remove caracteres não numéricos
        substring = ''.join([c for c in substring if c.isnumeric()])

        # formata a data
        if len(substring) > 0:
            substring = f"{substring[:2]}/{substring[2:4]}/{substring[4:8]}"
            substring = substring[:10]
        print(len(substring))
        # insere o texto formatado
        return substring