import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage, QWebEngineProfile, QWebEngineSettings

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the browser window
        self.setWindowTitle("Python Web Browser")
        self.setGeometry(100, 100, 1200, 800)

        # Create a QWebEngineView
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))
        self.setCentralWidget(self.browser)

        # Create navigation bar
        navbar = QToolBar()
        self.addToolBar(navbar)

        # Add back button
        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        # Add forward button
        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        # Add reload button
        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        # Add address bar
        self.address_bar = QLineEdit(self)
        self.address_bar.returnPressed.connect(self.load_url_from_address_bar)
        navbar.addWidget(self.address_bar)

        # Update address bar when URL changes
        self.browser.urlChanged.connect(self.update_address_bar)

    def load_url_from_address_bar(self):
        url = self.address_bar.text()
        if not url.startswith("http"):
            url = "http://" + url
        self.browser.setUrl(QUrl(url))

    def update_address_bar(self, qurl):
        self.address_bar.setText(qurl.toString())

# Run the browser
app = QApplication(sys.argv)
QApplication.setApplicationName("Python Web Browser")
window = Browser()
window.show()
app.exec_()
