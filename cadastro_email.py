import sys
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QCheckBox, QHBoxLayout, QVBoxLayout, QMessageBox, QFrame
)


class TelaLogin(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Welcome to email")
        self.setGeometry(200, 100, 420, 520)
        self.setFixedSize(450, 520)
        self.setWindowIcon(QIcon("icone.png"))

        # Layout principal
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignCenter)
        main_layout.setContentsMargins(30, 20, 30, 0)

        # --- Cabeçalho ---
        titulo = QLabel("Welcome to email")
        titulo.setFont(QFont("Arial", 18, QFont.Bold))
        titulo.setAlignment(Qt.AlignCenter)

        subtitulo = QLabel("Please login to your account")
        subtitulo.setFont(QFont("Arial", 10))
        subtitulo.setAlignment(Qt.AlignCenter)

        main_layout.addWidget(titulo)
        main_layout.addWidget(subtitulo)

        # --- Campos de login ---
        lbl_email = QLabel("Email Address")
        self.input_email = QLineEdit()
        self.input_email.setPlaceholderText("johndoe@gmail.com")
        self.input_email.setFixedHeight(30)

        lbl_senha = QLabel("Password")
        self.input_senha = QLineEdit()
        self.input_senha.setEchoMode(QLineEdit.Password)
        self.input_senha.setFixedHeight(30)

        # --- Checkbox e "Esqueci minha senha" ---
        checkbox = QCheckBox("Remember me")
        esqueci = QLabel('<a href="#">Forgot your password?</a>')
        esqueci.setTextFormat(Qt.RichText)
        esqueci.setTextInteractionFlags(Qt.TextBrowserInteraction)
        esqueci.setOpenExternalLinks(False)
        esqueci.setAlignment(Qt.AlignRight)
        esqueci.linkActivated.connect(self.recuperar_senha)

        linha_check = QHBoxLayout()
        linha_check.addWidget(checkbox)
        linha_check.addWidget(esqueci)

        # --- Botão de login ---
        btn_login = QPushButton("LOGIN")
        btn_login.setStyleSheet(
            "background-color: #2b9bd7; color: white; font-weight: bold; height: 35px; border-radius: 5px;"
        )
        btn_login.clicked.connect(self.login)

        # --- Criar conta ---
        criar = QLabel('New User? <a href="#">Create an Account</a>')
        criar.setAlignment(Qt.AlignCenter)
        criar.setTextFormat(Qt.RichText)
        criar.setTextInteractionFlags(Qt.TextBrowserInteraction)
        criar.setOpenExternalLinks(False)
        criar.linkActivated.connect(self.criar_conta)

        # --- Separador visual ---
        ou = QLabel("──────────────  OR  ──────────────")
        ou.setAlignment(Qt.AlignCenter)
        ou.setStyleSheet("color: gray;")

        # Adiciona todos os elementos principais
        main_layout.addSpacing(15)
        main_layout.addWidget(lbl_email)
        main_layout.addWidget(self.input_email)
        main_layout.addWidget(lbl_senha)
        main_layout.addWidget(self.input_senha)
        main_layout.addLayout(linha_check)
        main_layout.addWidget(btn_login)
        main_layout.addWidget(criar)
        main_layout.addSpacing(15)
        main_layout.addWidget(ou)

        # --- Espaço flexível antes do rodapé ---
        main_layout.addStretch()

        # --- Rodapé azul ---
        rodape = QFrame()
        rodape.setStyleSheet("background-color: #2b9bd7;")
        rodape.setFixedHeight(90)  # 👈 aumenta aqui a altura do rodapé
        rodape_layout = QVBoxLayout()
        rodape_layout.setContentsMargins(30, 20, 30, 20)
        rodape_layout.setSpacing(10)

        texto_social = QLabel("Login with social media")
        texto_social.setAlignment(Qt.AlignCenter)
        texto_social.setStyleSheet("color: white; font-weight: bold;")

        btn_fb = QPushButton("Facebook")
        btn_fb.setStyleSheet("background-color: #3b5998; color: white; height: 35px; border-radius: 5px;")
        btn_fb.clicked.connect(self.login_facebook)

        btn_google = QPushButton("Google")
        btn_google.setStyleSheet("background-color: #db4437; color: white; height: 35px; border-radius: 5px;")
        btn_google.clicked.connect(self.login_google)

        linha_social = QHBoxLayout()
        linha_social.addWidget(btn_fb)
        linha_social.addWidget(btn_google)

        rodape_layout.addWidget(texto_social)
        rodape_layout.addLayout(linha_social)
        rodape.setLayout(rodape_layout)

        # Adiciona o rodapé ao layout principal
        main_layout.addWidget(rodape)

        self.setLayout(main_layout)

    # --- Funções de ação ---
    def login(self):
        email = self.input_email.text()
        senha = self.input_senha.text()

        if email == "" or senha == "":
            QMessageBox.warning(self, "Erro", "Preencha todos os campos!")
        else:
            QMessageBox.information(self, "Login", f"Bem-vindo(a), {email}!")

    def recuperar_senha(self):
        QMessageBox.information(self, "Recuperar senha", "Link de recuperação enviado ao seu e-mail.")

    def criar_conta(self):
        QMessageBox.information(self, "Nova conta", "Redirecionando para criar uma nova conta.")

    def login_facebook(self):
        QMessageBox.information(self, "Facebook", "Login com Facebook (simulado).")

    def login_google(self):
        QMessageBox.information(self, "Google", "Login com Google (simulado).")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TelaLogin()
    window.show()
    sys.exit(app.exec_())
