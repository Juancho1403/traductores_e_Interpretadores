from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPixmap, QPalette, QBrush
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QMessageBox
from main import Analizador_lexico
from vista.analizador_lexico import Ui_analizador_lexico  # Asegúrate de que esta importación sea válida
from analizador_lexi import lexer  # Asegúrate de importar el analizador léxico

class Ui_home:
    def setupUi(self, MainWindow):
        """ Configuración de la interfaz de usuario """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)

        # Central widget
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        # Establecer fondo de la ventana con la imagen (usa ruta absoluta si es necesario)
        self.set_background_image('imagenes/palabras.jpg')  # Especifica la ruta correcta de la imagen

        # Layout principal (para centrar los elementos en la ventana)
        self.layout = QVBoxLayout(self.centralwidget)
        self.layout.setAlignment(Qt.AlignCenter)  # Alinea los elementos al centro

        # Título
        self.titleLabel = QLabel("Analizador Léxico de Python a Java", self.centralwidget)
        self.titleLabel.setAlignment(Qt.AlignCenter)
        self.titleLabel.setStyleSheet("font: 20pt; font-weight: bold; color: #4CAF50; margin-bottom: 40px;")
        self.layout.addWidget(self.titleLabel)

        # Crear un layout horizontal para centrar los botones
        self.buttonLayout = QVBoxLayout()
        self.buttonLayout.setAlignment(Qt.AlignCenter)  # Centra los botones dentro del layout

        # Botón de análisis léxico
        self.analyzeButton = QPushButton("Analizador Léxico", self.centralwidget)
        self.analyzeButton.setStyleSheet("""
            background-color: #4CAF50;
            color: white;
            font-size: 16pt;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 30px;
        """)
        self.buttonLayout.addWidget(self.analyzeButton)
        self.analyzeButton.clicked.connect(self.showLexicalAnalyzer)  # Conectar con la vista del analizador léxico

        # Botón de análisis sintáctico
        self.syntaxButton = QPushButton("Analizador Sintáctico", self.centralwidget)
        self.syntaxButton.setStyleSheet("""
            background-color: #2196F3;
            color: white;
            font-size: 16pt;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 30px;
        """)
        self.buttonLayout.addWidget(self.syntaxButton)
        self.syntaxButton.clicked.connect(self.showSyntaxMessage)  # Conectar con el mensaje

        # Agregar el layout de los botones al layout principal
        self.layout.addLayout(self.buttonLayout)

    def set_background_image(self, image_path):
        """Establecer una imagen como fondo"""
        pixmap = QPixmap(image_path)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(pixmap))
        self.centralwidget.setPalette(palette)

    def showSyntaxMessage(self):
        """ Muestra un mensaje cuando se presiona el botón 'Analizador Sintáctico' """
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Va a estar listo para la siguiente evaluación.")
        msg.setWindowTitle("Analizador Sintáctico")
        msg.exec_()

    def showLexicalAnalyzer(self):
        """ Cambia a la vista del analizador léxico """
        self.window = QMainWindow()
        self.ui = Analizador_lexico()  # Aquí se instancia la clase del analizador léxico
        self.ui.show()  # Muestra la ventana del analizador léxico
        self.window.close()  # Cierra la ventana actual (home)

def iniciar():
    """ Inicia la aplicación """
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    
    MainWindow = QMainWindow()
    ui = Ui_home()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    iniciar()
