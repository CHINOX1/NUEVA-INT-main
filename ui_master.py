# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'masteroYzylM.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QStackedWidget, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_Formmaster(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(331, 528)
        Form.setStyleSheet(u"background-color: rgb(170, 0, 127);\n"
"background-color: rgb(102, 0, 0);")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 15pt \"Rockwell Condensed\";\n"
"background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.btn_continuar = QPushButton(self.widget)
        self.btn_continuar.setObjectName(u"btn_continuar")
        self.btn_continuar.setStyleSheet(u"font: 15pt \"Rockwell Condensed\";\n"
"background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        icon = QIcon()
        icon.addFile(u"iconos/procesamiento-de-datos.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_continuar.setIcon(icon)
        self.btn_continuar.setIconSize(QSize(34, 34))

        self.verticalLayout_2.addWidget(self.btn_continuar)

        self.btn_nueva = QPushButton(self.widget)
        self.btn_nueva.setObjectName(u"btn_nueva")
        self.btn_nueva.setStyleSheet(u"font: 15pt \"Rockwell Condensed\";\n"
"background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        icon1 = QIcon()
        icon1.addFile(u"iconos/libro-de-historia.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_nueva.setIcon(icon1)
        self.btn_nueva.setIconSize(QSize(34, 34))

        self.verticalLayout_2.addWidget(self.btn_nueva)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.stackedWidget = QStackedWidget(self.widget_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 30))
        self.label_2.setStyleSheet(u"font: 15pt \"Rockwell Condensed\";\n"
"background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")

        self.verticalLayout_4.addWidget(self.label_2)

        self.tex_nuevo = QLineEdit(self.page)
        self.tex_nuevo.setObjectName(u"tex_nuevo")
        self.tex_nuevo.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.tex_nuevo)

        self.label_3 = QLabel(self.page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 30))
        self.label_3.setStyleSheet(u"font: 15pt \"Rockwell Condensed\";\n"
"background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")

        self.verticalLayout_4.addWidget(self.label_3)

        self.text_sala = QLineEdit(self.page)
        self.text_sala.setObjectName(u"text_sala")
        self.text_sala.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.text_sala)

        self.btn_crear = QPushButton(self.page)
        self.btn_crear.setObjectName(u"btn_crear")
        self.btn_crear.setStyleSheet(u"font: 15pt \"Rockwell Condensed\";\n"
"background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        icon2 = QIcon()
        icon2.addFile(u"iconos/forjar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_crear.setIcon(icon2)

        self.verticalLayout_4.addWidget(self.btn_crear)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_5 = QVBoxLayout(self.page_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_4 = QLabel(self.page_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 15pt \"Rockwell Condensed\";\n"
"background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")

        self.verticalLayout_5.addWidget(self.label_4)

        self.nombre_sala = QLineEdit(self.page_2)
        self.nombre_sala.setObjectName(u"nombre_sala")
        self.nombre_sala.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_5.addWidget(self.nombre_sala)

        self.label_5 = QLabel(self.page_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font: 15pt \"Rockwell Condensed\";\n"
"background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")

        self.verticalLayout_5.addWidget(self.label_5)

        self.text_refe = QTextBrowser(self.page_2)
        self.text_refe.setObjectName(u"text_refe")
        self.text_refe.setStyleSheet(u"font: 15pt \"Rockwell Condensed\";\n"
"background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")

        self.verticalLayout_5.addWidget(self.text_refe)

        self.btn_inicio = QPushButton(self.page_2)
        self.btn_inicio.setObjectName(u"btn_inicio")
        self.btn_inicio.setStyleSheet(u"font: 15pt \"Rockwell Condensed\";\n"
"background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        icon3 = QIcon()
        icon3.addFile(u"iconos/personaje.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_inicio.setIcon(icon3)
        self.btn_inicio.setIconSize(QSize(34, 34))

        self.verticalLayout_5.addWidget(self.btn_inicio)

        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.widget_2)


        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"GAME MASTER", None))
        self.btn_continuar.setText(QCoreApplication.translate("Form", u"CONTINUAR", None))
        self.btn_nueva.setText(QCoreApplication.translate("Form", u"NUEVA AVENTURA", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"NOMBRE DE LA AVENTURA", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"NOMBRE DE LA SALA", None))
        self.btn_crear.setText(QCoreApplication.translate("Form", u"CREAR", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"INGRESE NOMBRE DE LA SALA", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u00bf ES ESTA?", None))
        self.btn_inicio.setText(QCoreApplication.translate("Form", u"INICIAR", None))
    # retranslateUi

