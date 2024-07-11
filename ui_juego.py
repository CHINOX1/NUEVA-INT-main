# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'JUEGOfFhCon.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTextBrowser,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(759, 862)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_superior = QFrame(self.centralwidget)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setStyleSheet(u"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));")
        self.frame_superior.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_superior.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_superior)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.widget_3 = QWidget(self.frame_superior)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_11 = QVBoxLayout(self.widget_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.sala_name = QLabel(self.widget_3)
        self.sala_name.setObjectName(u"sala_name")
        self.sala_name.setMaximumSize(QSize(1000, 40))
        self.sala_name.setStyleSheet(u"font: 15pt \"Rockwell Condensed\";\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));")
        self.sala_name.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.sala_name)


        self.verticalLayout_10.addWidget(self.widget_3)

        self.frame = QFrame(self.frame_superior)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(8000, 100))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_envio_2 = QPushButton(self.frame)
        self.btn_envio_2.setObjectName(u"btn_envio_2")
        self.btn_envio_2.setMaximumSize(QSize(50, 50))
        self.btn_envio_2.setStyleSheet(u"font: 15pt \"Rockwell Condensed\";\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));")
        icon = QIcon()
        icon.addFile(u"iconos/exportacion-de-archivos.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_envio_2.setIcon(icon)
        self.btn_envio_2.setIconSize(QSize(34, 34))

        self.horizontalLayout_2.addWidget(self.btn_envio_2)

        self.btn_m = QPushButton(self.frame)
        self.btn_m.setObjectName(u"btn_m")
        self.btn_m.setMaximumSize(QSize(50, 50))
        self.btn_m.setStyleSheet(u"font: 15pt \"Rockwell Condensed\";\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));")
        icon1 = QIcon()
        icon1.addFile(u"iconos/desplazarse-viejo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_m.setIcon(icon1)
        self.btn_m.setIconSize(QSize(34, 34))

        self.horizontalLayout_2.addWidget(self.btn_m)

        self.btn_tpa = QPushButton(self.frame)
        self.btn_tpa.setObjectName(u"btn_tpa")
        self.btn_tpa.setMaximumSize(QSize(50, 50))
        self.btn_tpa.setStyleSheet(u"font: 15pt \"Rockwell Condensed\";\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));")
        icon2 = QIcon()
        icon2.addFile(u"iconos/personaje.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_tpa.setIcon(icon2)
        self.btn_tpa.setIconSize(QSize(34, 34))

        self.horizontalLayout_2.addWidget(self.btn_tpa)

        self.btn_dados = QPushButton(self.frame)
        self.btn_dados.setObjectName(u"btn_dados")
        self.btn_dados.setMaximumSize(QSize(50, 50))
        self.btn_dados.setStyleSheet(u"font: 15pt \"Rockwell Condensed\";\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));")
        icon3 = QIcon()
        icon3.addFile(u"iconos/dados-d20.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_dados.setIcon(icon3)
        self.btn_dados.setIconSize(QSize(34, 34))

        self.horizontalLayout_2.addWidget(self.btn_dados)

        self.btn_md = QPushButton(self.frame)
        self.btn_md.setObjectName(u"btn_md")
        self.btn_md.setMaximumSize(QSize(50, 50))
        self.btn_md.setStyleSheet(u"font: 15pt \"Rockwell Condensed\";\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));")
        icon4 = QIcon()
        icon4.addFile(u"iconos/mejoramiento.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_md.setIcon(icon4)
        self.btn_md.setIconSize(QSize(34, 34))

        self.horizontalLayout_2.addWidget(self.btn_md)


        self.verticalLayout_10.addWidget(self.frame)

        self.label = QLabel(self.frame_superior)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(100, 100))
        self.label.setStyleSheet(u"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.label)

        self.widget_4 = QWidget(self.frame_superior)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMaximumSize(QSize(8000, 600))
        self.horizontalLayout = QHBoxLayout(self.widget_4)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, 0, 0)
        self.game_edit = QTextEdit(self.widget_4)
        self.game_edit.setObjectName(u"game_edit")
        self.game_edit.setMaximumSize(QSize(8000, 500))
        self.game_edit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Rockwell Condensed\";")

        self.horizontalLayout.addWidget(self.game_edit)


        self.verticalLayout_10.addWidget(self.widget_4)


        self.verticalLayout.addWidget(self.frame_superior)

        self.frame_medio = QFrame(self.centralwidget)
        self.frame_medio.setObjectName(u"frame_medio")
        self.frame_medio.setStyleSheet(u"background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.frame_medio.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_medio.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_medio)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(100, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_4.addItem(self.verticalSpacer)

        self.stackedWidget = QStackedWidget(self.frame_medio)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMaximumSize(QSize(2000, 300))
        self.stackedWidget.setStyleSheet(u"background-color: rgb(170, 0, 127);\n"
"background-color: rgb(102, 0, 0);")
        self.pagina_1 = QWidget()
        self.pagina_1.setObjectName(u"pagina_1")
        self.pagina_1.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.pagina_1)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.btn_aleatorio = QPushButton(self.pagina_1)
        self.btn_aleatorio.setObjectName(u"btn_aleatorio")
        self.btn_aleatorio.setStyleSheet(u"font: 15pt \"Rockwell Condensed\";\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));")
        icon5 = QIcon()
        icon5.addFile(u"iconos/barajar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_aleatorio.setIcon(icon5)
        self.btn_aleatorio.setIconSize(QSize(34, 34))

        self.verticalLayout_7.addWidget(self.btn_aleatorio)

        self.btn_crear = QPushButton(self.pagina_1)
        self.btn_crear.setObjectName(u"btn_crear")
        self.btn_crear.setStyleSheet(u"font: 15pt \"Rockwell Condensed\";\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));")
        icon6 = QIcon()
        icon6.addFile(u"iconos/crear.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_crear.setIcon(icon6)
        self.btn_crear.setIconSize(QSize(34, 34))

        self.verticalLayout_7.addWidget(self.btn_crear)

        self.label_8 = QLabel(self.pagina_1)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 30))
        self.label_8.setStyleSheet(u"font: 15pt \"Rockwell Condensed\";\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_8)

        self.b_ms = QLineEdit(self.pagina_1)
        self.b_ms.setObjectName(u"b_ms")
        self.b_ms.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_7.addWidget(self.b_ms)

        self.btn_mison = QPushButton(self.pagina_1)
        self.btn_mison.setObjectName(u"btn_mison")
        self.btn_mison.setStyleSheet(u"font: 15pt \"Rockwell Condensed\";\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));")
        icon7 = QIcon()
        icon7.addFile(u"iconos/procesamiento-de-datos.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_mison.setIcon(icon7)
        self.btn_mison.setIconSize(QSize(34, 34))

        self.verticalLayout_7.addWidget(self.btn_mison)

        self.btn_pp = QPushButton(self.pagina_1)
        self.btn_pp.setObjectName(u"btn_pp")
        self.btn_pp.setStyleSheet(u"font: 15pt \"Rockwell Condensed\";\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));")
        icon8 = QIcon()
        icon8.addFile(u"iconos/analisis.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_pp.setIcon(icon8)
        self.btn_pp.setIconSize(QSize(34, 34))

        self.verticalLayout_7.addWidget(self.btn_pp)

        self.stackedWidget.addWidget(self.pagina_1)
        self.pagina_2 = QWidget()
        self.pagina_2.setObjectName(u"pagina_2")
        self.verticalLayout_3 = QVBoxLayout(self.pagina_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.pagina_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 50))
        self.label_4.setStyleSheet(u"font: 15pt \"Rockwell Condensed\";\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));")

        self.verticalLayout_3.addWidget(self.label_4)

        self.name_m = QTextEdit(self.pagina_2)
        self.name_m.setObjectName(u"name_m")
        self.name_m.setMaximumSize(QSize(16777215, 30))
        self.name_m.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_3.addWidget(self.name_m)

        self.label_3 = QLabel(self.pagina_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 50))
        self.label_3.setStyleSheet(u"font: 15pt \"Rockwell Condensed\";\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));")

        self.verticalLayout_3.addWidget(self.label_3)

        self.descrip_m = QTextEdit(self.pagina_2)
        self.descrip_m.setObjectName(u"descrip_m")
        self.descrip_m.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_3.addWidget(self.descrip_m)

        self.label_2 = QLabel(self.pagina_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 15pt \"Rockwell Condensed\";\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));")

        self.verticalLayout_3.addWidget(self.label_2)

        self.tex_condi = QTextEdit(self.pagina_2)
        self.tex_condi.setObjectName(u"tex_condi")
        self.tex_condi.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_3.addWidget(self.tex_condi)

        self.label_5 = QLabel(self.pagina_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 50))
        self.label_5.setStyleSheet(u"font: 15pt \"Rockwell Condensed\";\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));")

        self.verticalLayout_3.addWidget(self.label_5)

        self.recom_m = QTextEdit(self.pagina_2)
        self.recom_m.setObjectName(u"recom_m")
        self.recom_m.setMaximumSize(QSize(16777215, 100))
        self.recom_m.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_3.addWidget(self.recom_m)

        self.btn_crearM = QPushButton(self.pagina_2)
        self.btn_crearM.setObjectName(u"btn_crearM")
        self.btn_crearM.setStyleSheet(u"font: 15pt \"Rockwell Condensed\";\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));")
        icon9 = QIcon()
        icon9.addFile(u"iconos/forjar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_crearM.setIcon(icon9)
        self.btn_crearM.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.btn_crearM)

        self.stackedWidget.addWidget(self.pagina_2)
        self.pagina_3 = QWidget()
        self.pagina_3.setObjectName(u"pagina_3")
        self.pagina_3.setStyleSheet(u"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));")
        self.verticalLayout_4 = QVBoxLayout(self.pagina_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.comboBox_2 = QComboBox(self.pagina_3)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setStyleSheet(u"font: 15pt \"Rockwell Condensed\";\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));")

        self.verticalLayout_4.addWidget(self.comboBox_2)

        self.inicio_p = QLabel(self.pagina_3)
        self.inicio_p.setObjectName(u"inicio_p")
        self.inicio_p.setMaximumSize(QSize(800, 16777215))
        self.inicio_p.setPixmap(QPixmap(u"fondos/mundo funki.jpg"))
        self.inicio_p.setScaledContents(True)

        self.verticalLayout_4.addWidget(self.inicio_p)

        self.stackedWidget.addWidget(self.pagina_3)
        self.pagina_6 = QWidget()
        self.pagina_6.setObjectName(u"pagina_6")
        self.pagina_6.setMaximumSize(QSize(1000, 16777215))
        self.pagina_6.setStyleSheet(u"background-color: rgb(170, 0, 127);\n"
"background-color: rgb(102, 0, 0);")
        self.horizontalLayout_6 = QHBoxLayout(self.pagina_6)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.btn_envio = QPushButton(self.pagina_6)
        self.btn_envio.setObjectName(u"btn_envio")
        self.btn_envio.setMaximumSize(QSize(100, 16777215))
        self.btn_envio.setStyleSheet(u"font: 15pt \"Rockwell Condensed\";\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));")
        icon10 = QIcon()
        icon10.addFile(u"iconos/exportacion-de-archivos.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_envio.setIcon(icon10)
        self.btn_envio.setIconSize(QSize(34, 34))

        self.horizontalLayout_6.addWidget(self.btn_envio)

        self.text_mis = QTextEdit(self.pagina_6)
        self.text_mis.setObjectName(u"text_mis")
        self.text_mis.setMaximumSize(QSize(300, 300))
        self.text_mis.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")

        self.horizontalLayout_6.addWidget(self.text_mis)

        self.btn_c = QPushButton(self.pagina_6)
        self.btn_c.setObjectName(u"btn_c")
        self.btn_c.setMaximumSize(QSize(100, 16777215))
        self.btn_c.setStyleSheet(u"font: 15pt \"Rockwell Condensed\";\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));")
        icon11 = QIcon()
        icon11.addFile(u"iconos/victoria.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_c.setIcon(icon11)
        self.btn_c.setIconSize(QSize(30, 30))

        self.horizontalLayout_6.addWidget(self.btn_c)

        self.btn_f = QPushButton(self.pagina_6)
        self.btn_f.setObjectName(u"btn_f")
        self.btn_f.setMaximumSize(QSize(100, 16777215))
        self.btn_f.setStyleSheet(u"font: 15pt \"Rockwell Condensed\";\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));")
        icon12 = QIcon()
        icon12.addFile(u"iconos/prohibido.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_f.setIcon(icon12)
        self.btn_f.setIconSize(QSize(30, 30))

        self.horizontalLayout_6.addWidget(self.btn_f)

        self.stackedWidget.addWidget(self.pagina_6)
        self.pagina_5 = QWidget()
        self.pagina_5.setObjectName(u"pagina_5")
        self.horizontalLayout_5 = QHBoxLayout(self.pagina_5)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.pagina_5)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.verticalLayout_5 = QVBoxLayout(self.widget)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.vivo_muerto = QLabel(self.widget)
        self.vivo_muerto.setObjectName(u"vivo_muerto")
        self.vivo_muerto.setMaximumSize(QSize(450, 16777215))
        self.vivo_muerto.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.vivo_muerto.setPixmap(QPixmap(u"gif/esqueleto.gif"))
        self.vivo_muerto.setScaledContents(True)

        self.verticalLayout_5.addWidget(self.vivo_muerto)


        self.horizontalLayout_5.addWidget(self.widget)

        self.widget_2 = QWidget(self.pagina_5)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(300, 16777215))
        self.widget_2.setStyleSheet(u"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));")
        self.verticalLayout_6 = QVBoxLayout(self.widget_2)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.text_re = QTextEdit(self.widget_2)
        self.text_re.setObjectName(u"text_re")
        self.text_re.setMaximumSize(QSize(300, 100))
        self.text_re.setStyleSheet(u"background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")

        self.verticalLayout_6.addWidget(self.text_re)

        self.label_9 = QLabel(self.widget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 50))
        self.label_9.setStyleSheet(u"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));\n"
"\n"
"font: 15pt \"Rockwell Condensed\";")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_9)

        self.comboBox = QComboBox(self.widget_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_6.addWidget(self.comboBox)

        self.btn_stado = QPushButton(self.widget_2)
        self.btn_stado.setObjectName(u"btn_stado")
        self.btn_stado.setStyleSheet(u"font: 15pt \"Rockwell Condensed\";\n"
"background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        icon13 = QIcon()
        icon13.addFile(u"iconos/guardar-el-archivo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_stado.setIcon(icon13)
        self.btn_stado.setIconSize(QSize(34, 34))

        self.verticalLayout_6.addWidget(self.btn_stado)


        self.horizontalLayout_5.addWidget(self.widget_2)

        self.stackedWidget.addWidget(self.pagina_5)
        self.pagina_4 = QWidget()
        self.pagina_4.setObjectName(u"pagina_4")
        self.pagina_4.setStyleSheet(u"background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.verticalLayout_9 = QVBoxLayout(self.pagina_4)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.pagina_4)

        self.horizontalLayout_4.addWidget(self.stackedWidget)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_4.addItem(self.verticalSpacer_2)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_8)


        self.verticalLayout.addWidget(self.frame_medio)

        self.frame_inferior = QFrame(self.centralwidget)
        self.frame_inferior.setObjectName(u"frame_inferior")
        self.frame_inferior.setMaximumSize(QSize(16777215, 1000))
        self.frame_inferior.setStyleSheet(u"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.frame_inferior.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_inferior.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_inferior)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.tex_vita = QTextBrowser(self.frame_inferior)
        self.tex_vita.setObjectName(u"tex_vita")
        self.tex_vita.setMaximumSize(QSize(16777215, 1000))
        self.tex_vita.setStyleSheet(u"background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")

        self.verticalLayout_8.addWidget(self.tex_vita)

        self.btn_guardado = QPushButton(self.frame_inferior)
        self.btn_guardado.setObjectName(u"btn_guardado")
        self.btn_guardado.setStyleSheet(u"font: 15pt \"Rockwell Condensed\";\n"
"background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.btn_guardado.setIcon(icon13)

        self.verticalLayout_8.addWidget(self.btn_guardado)

        self.btn_his = QPushButton(self.frame_inferior)
        self.btn_his.setObjectName(u"btn_his")
        self.btn_his.setStyleSheet(u"font: 15pt \"Rockwell Condensed\";\n"
"background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        icon14 = QIcon()
        icon14.addFile(u"iconos/libro-de-historia.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_his.setIcon(icon14)
        self.btn_his.setIconSize(QSize(34, 34))

        self.verticalLayout_8.addWidget(self.btn_his)


        self.verticalLayout.addWidget(self.frame_inferior)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.sala_name.setText("")
        self.btn_envio_2.setText("")
        self.btn_m.setText("")
        self.btn_tpa.setText("")
        self.btn_dados.setText("")
        self.btn_md.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"GAME MASTER", None))
        self.game_edit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Rockwell Condensed'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:10pt;\">comienza la historia</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.btn_aleatorio.setText(QCoreApplication.translate("MainWindow", u" EVENTO ALEATORIO", None))
        self.btn_crear.setText(QCoreApplication.translate("MainWindow", u"CREAR MISION", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"INGRESE NOMBRE DE LA MISION", None))
        self.btn_mison.setText(QCoreApplication.translate("MainWindow", u"INICIAR MISION", None))
        self.btn_pp.setText(QCoreApplication.translate("MainWindow", u" ESTADO DE PERSONAJES", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"NOMBRE MISION", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"DESCRIPCION", None))
        self.descrip_m.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"CONDICION", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"RECOMPENSA", None))
        self.recom_m.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.btn_crearM.setText(QCoreApplication.translate("MainWindow", u"CREAR MISION", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"etapa1", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"etapa2", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"etapa3", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"etapa4", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"etapa5", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("MainWindow", u"etapa6", None))
        self.comboBox_2.setItemText(6, QCoreApplication.translate("MainWindow", u"jefe", None))

        self.inicio_p.setText("")
        self.btn_envio.setText(QCoreApplication.translate("MainWindow", u"enviar", None))
        self.text_mis.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">cree su logica para pasar la mision, luego se registrara en la vitacora,puedes presionar enviar cuantas veces quierar para registrarlo en la vitacora, luego presiona mision cumplida o derrota </p></body></html>", None))
        self.btn_c.setText(QCoreApplication.translate("MainWindow", u"CUMPLIDA", None))
        self.btn_f.setText(QCoreApplication.translate("MainWindow", u"FRACASO", None))
        self.vivo_muerto.setText("")
        self.text_re.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">aqui simplementes puedes tirar los datos para editar el estado o invertar una cruzada para revivir a un compa\u00f1ero depdende de tu imaginacion</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"EDITAR ESTADO", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"muerto", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"vivo", None))

        self.btn_stado.setText(QCoreApplication.translate("MainWindow", u"enviar", None))
        self.tex_vita.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#aa0000;\">ESTA ES LA VITACORA</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#aa0000;\"><br /></p></body></html>", None))
        self.btn_guardado.setText(QCoreApplication.translate("MainWindow", u"GUARDAR", None))
        self.btn_his.setText(QCoreApplication.translate("MainWindow", u"BITACORA", None))
    # retranslateUi



