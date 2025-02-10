import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from vista.analizador_lexico import Ui_home  # Asegúrate de que esta importación sea válida
import analizador_lexi  # Importa tu analizador léxico real

class Main(QMainWindow):
    """ Clase principal de nuestra aplicación """
    def __init__(self):
        """ Inicializa la aplicación """
        super().__init__()

        # Instanciamos nuestra interfaz gráfica
        self.home = Ui_home()
        self.home.setupUi(self)

        # Conectar botones a funciones
        self.home.loadButton.clicked.connect(self.load_file)
        self.home.analyzeButton.clicked.connect(self.analyze_code)

    def load_file(self):
        """ Carga un archivo Java en el editor """
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Abrir Archivo Java", "", "Archivos Java (*.java);;Todos los archivos (*)", options=options)
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    code = file.read()
                    self.home.codeEditor.setPlainText(code)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo abrir el archivo:\n{str(e)}")

    def analyze_code(self):
        """ Realiza el análisis léxico del código ingresado """
        code = self.home.codeEditor.toPlainText().strip()
        if not code:
            QMessageBox.warning(self, "Advertencia", "El editor está vacío. Por favor, cargue o escriba código Java.")
            return
        
        # Análisis léxico del código
        tokens = analizador_lexi.lexer(code)  # Usamos el método lexer modificado

        # Mostrar resultados en el campo de texto de resultados
        if tokens:
            # Mostramos los tokens y las palabras reservadas encontradas
            resultado = "\n".join([f"{tipo}: {valor}" for tipo, valor in tokens])
            self.home.resultsViewer.setPlainText(resultado)
        else:
            self.home.resultsViewer.setPlainText("No se encontraron tokens.")

def iniciar():
    """ Inicia la aplicación """
    app = QApplication(sys.argv)
    ventana = Main()
    ventana.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    iniciar()
