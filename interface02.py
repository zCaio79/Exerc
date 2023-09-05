import sys
import PySide6
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QMessageBox
from PySide6.QtCore import Qt

#Função para pegar os textos dos inputs
def enviar_info():
    #Guarda as informações nas variaveis nome e mensage
    name = nameinput.text()
    mensage = mensageinput.text()
    #Se ambos os campos forém preenchidos ele retorna o resultado, senão ele da um aviso
    if name!="" and mensage!="":
        janela.setStyleSheet("color: pink; background-color: black; font-size: 16px;")
        QMessageBox.information(janela, "Mensagem Recebida", f"{name} disse:   {mensage}")
        janela.setStyleSheet("color: black; background-color: black;")
    else:
        janela.setStyleSheet("color: red; background-color: black; font-size: 16px;")
        QMessageBox.warning(janela, "Inválido", "Campo Inválido, Tente Novamente!!")
        janela.setStyleSheet("color: black; background-color: black;")

#Cria a Janela, ponha titulo e muda a cor do fundo
app = QApplication(sys.argv)
janela = QMainWindow()
janela.setWindowTitle("Enviar Mensagem")
janela.setStyleSheet("background-color: black;")

#Cria a label para indicar a caixa Nome:
name = QLabel(janela)
name.setText("[Nome]")
name.setStyleSheet("font-size: 16px; color: white;")
name.setGeometry(10, 10, 280, 30)

#Cria uma caixa de input para o usuario digitar seu nome
nameinput = QLineEdit(janela)
nameinput.setStyleSheet("font-size: 16px; background-color: white;")
nameinput.setAlignment(Qt.AlignCenter)
nameinput.setGeometry(10, 40, 280, 30)

#Cria a label para indicar a caixa Mensagem:
mensage = QLabel(janela)
mensage.setText("[Mensagem]")
mensage.setStyleSheet("font-size: 16px; color: white;")
mensage.setGeometry(10, 80, 280, 30)

#Cria uma caixa de input para o usuario digitar sua mensagem
mensageinput = QLineEdit(janela)
mensageinput.setStyleSheet("font-size: 16px; background-color: white;")
mensageinput.setAlignment(Qt.AlignCenter)
mensageinput.setGeometry(10, 110, 280, 30)

#Cria um botão para enviar as informações para salvar as Informações
submit_info = QPushButton(janela)
submit_info.setText("Enviar")
submit_info.setStyleSheet("font-size: 18px; background-color: pink; color: black;")
submit_info.setGeometry(10, 150, 280, 30)
#Quando clicado o botão chama a função enviar_info
submit_info.clicked.connect(enviar_info)
#Seta o tamanho da janela
janela.setGeometry(100, 100, 300, 200)
janela.show()
#Só ira fechar quando o usuario fechar a janela
sys.exit(app.exec())