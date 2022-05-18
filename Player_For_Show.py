import sys

from PyQt5 import  QtWidgets, QtCore
from PyQt5.QtCore import QUrl, QFile
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QApplication
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtWidgets import *


# Создаем класс с определением окна приложения
class MyWindow(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("Видеопроигрыватель")
#   Включение отслеживания движения мыши. Первый уровень. Надо включать везде по вложению виджетов до самого последнего.
        self.setMouseTracking(True)

#   Высчитываем размер окна для старта на основании разрешения экрана
        desktop_SIze = QApplication.desktop()
        self.screen_Width = desktop_SIze.width()
        self.screen_Height = desktop_SIze.height()
        if self.screen_Width > 1920 and self.screen_Height == 1080:
            self.screen_Width = 1920
        elif self.screen_Width == 1920 and self.screen_Height > 1080:
            self.screen_Height = 1080
        self.size_Width  = int(self.screen_Width/2)
        self.size_Height = int(self.screen_Height/2)
        self.resize(self.size_Width,self.size_Height)
        print(self.size_Width,self.size_Height)
        self.move(int(self.size_Width/2),int(self.size_Height/2))

        self.make_VideoWidget()
        self.make_menu()
#        self.play_Widget()
#   Изменение размеров окна. Переопределяю перехват изменения размера окна.
    def resizeEvent(self, event):
        rect = self.geometry()
#   Изменяю размер меню
        self.menubar.setGeometry(QtCore.QRect(0, 0, rect.width(), 20))
#   Возвращаю управления встроенному модулю обработки изменения размера окна
        return QtWidgets.QWidget.resizeEvent(self, event)

#   Меню
    def make_menu(self):
        self.menubar      = QtWidgets.QMenuBar(self)
#   1
        self.menu         = QtWidgets.QMenu(self.menubar)
        self.menu.setTitle("Выбор канала")
#
        self.action1      = QtWidgets.QAction(self)
        self.action2      = QtWidgets.QAction(self)
        self.action3      = QtWidgets.QAction(self)
        self.action4      = QtWidgets.QAction(self)
        self.action5      = QtWidgets.QAction(self)
        self.action1.setText("Камера Офис Интернет")
        self.action2.setText("Камера Офис")
        self.action3.setText("OKKO_TV")
        self.action4.setText("Nature_TV")
        self.action5.setText("Открыть файл")
        self.menu.addAction(self.action1)
        self.menu.addAction(self.action2)
        self.menu.addAction(self.action3)
        self.menu.addAction(self.action4)
        self.menu.addAction(self.action5)
#   Слоты для пунктов меню 1P
        self.action1.triggered.connect(self.play_Widget_1)
        self.action2.triggered.connect(self.play_Widget_2)
        self.action3.triggered.connect(self.play_Widget_3)
        self.action4.triggered.connect(self.play_Widget_4)
        self.action5.triggered.connect(self.play_Widget_5)
#   2
        self.menu_2       = QtWidgets.QMenu(self.menubar)
        self.action_full  = QtWidgets.QAction(self)
        self.action_norm  = QtWidgets.QAction(self)
        self.menu_2.addAction(self.action_full)
        self.menu_2.addAction(self.action_norm)
        self.menu_2.setTitle("Режим показа")
        self.action_full.setText("Полноэкранный")
        self.action_norm.setText("Нормальный")
#   Добавляем созданные подменю в menubar
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.setGeometry(QtCore.QRect(0, -10 , self.size_Width, 20))

#   Показ меню на полном экране
#   Движение мыши. Переопределяю модуль движения мыши.
    def mouseMoveEvent(self, e):
#        print("Перемещение мыши", e.x(), e.y())
        if (e.y() <= 15 or e.y() >= (self.screen_Height -15)) and self.isFullScreen():
            self.menubar.show()
        elif (e.y() > 15 or e.y() < (self.screen_Height -15)) and self.isFullScreen():
            self.menubar.hide()
#   Возвращаю управления встроенному модулю обработки движения мыши
        QtWidgets.QWidget.mouseMoveEvent(self, e)


#   Создаем Видеовиджет, размещаем его в vbox и vbox размещаем в окне
    def make_VideoWidget(self):

        self.mediaPlayer = QMediaPlayer(self,QMediaPlayer.StreamPlayback)

        self.container_for_ALL = QtWidgets.QWidget()
#   Включение отслеживания движения мыши. Второй уровень. Надо включать везде по вложению виджетов до самого последнего.
        self.container_for_ALL.setMouseTracking(True)
        self.setCentralWidget(self.container_for_ALL)
        self.videoWidget = QVideoWidget()
#   Включение отслеживания движения мыши. Третий уровень. Надо включать везде по вложению виджетов до самого последнего.
        self.videoWidget.setMouseTracking(True)
        self.mediaPlayer.setVideoOutput(self.videoWidget)

        self.vbox_V = QtWidgets.QVBoxLayout(self.container_for_ALL)
        self.vbox_V.setContentsMargins(0,0,0,0)
        self.vbox_V.addWidget(self.videoWidget)

    def play_Widget_1(self):
        sPlaylistURL = "rtsp://admin:Admin2020@109.195.101.141:5554/ISAPI/Streaming/Channels/101"
        self.mediaPlayer.setMedia(QMediaContent(QUrl(sPlaylistURL)))
        self.mediaPlayer.play()

    def play_Widget_2(self):
        sPlaylistURL = "rtsp://admin:Admin2020@192.168.0.133:554/ISAPI/Streaming/Channels/101"
        self.mediaPlayer.setMedia(QMediaContent(QUrl(sPlaylistURL)))
        self.mediaPlayer.play()

    def play_Widget_3(self):
        sPlaylistURL = "https://okkotv-live.cdnvideo.ru/channel/TV1000_HD/1080p.m3u8"
        self.mediaPlayer.setMedia(QMediaContent(QUrl(sPlaylistURL)))
        self.mediaPlayer.play()

    def play_Widget_4(self):
        sPlaylistURL = "https://stirr.ott-channels.stingray.com/naturescape/master_1920x1080_4500kbps.m3u8"
        self.mediaPlayer.setMedia(QMediaContent(QUrl(sPlaylistURL)))
        self.mediaPlayer.play()

    def play_Widget_5(self):
            path = QFileDialog.getOpenFileName(self, "Открыть файл", "/")
            filepath = path[0]
            print(filepath)
            if filepath == '':
                return
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filepath)))
            self.mediaPlayer.play()

    def mouseDoubleClickEvent(self, e):
        if self.isFullScreen():
            self.menubar.show()
            print("To Normal")
            self.showNormal()
        else:
            print("To Full")
            self.menubar.hide()
            self.showFullScreen()

if __name__ =="__main__":
    # Создаем приложение
    app = QtWidgets.QApplication(sys.argv)
    # Создаем окно приложения
    window = MyWindow()
    # Определяем для window метод show
    window.show()
    # Запускаем приложение
    sys.exit(app.exec_())


