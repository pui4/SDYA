import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("YouTube")
        self.setWindowIcon(QIcon("youtube.png"))
        self.setGeometry(0, 0, 1280, 800)

        self.webEngineView = QWebEngineView()
        self.setCentralWidget(self.webEngineView)
        
        self.webEngineView.page().profile().setHttpUserAgent(
            "Mozilla/5.0 (SMART-TV; Linux; Smart TV) AppleWebKit/537.36 (KHTML, like Gecko) Thano/3.0 Chrome/98.0.4758.102 TV Safari/537.36"
        )

        url = 'https://youtube.com/tv'
        self.webEngineView.load(QUrl(url))


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())