# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QTabWidget, QWidget)

class Ui_CharacterManagerMainWindow(object):
    def setupUi(self, CharacterManagerMainWindow):
        if not CharacterManagerMainWindow.objectName():
            CharacterManagerMainWindow.setObjectName(u"CharacterManagerMainWindow")
        CharacterManagerMainWindow.resize(950, 855)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CharacterManagerMainWindow.sizePolicy().hasHeightForWidth())
        CharacterManagerMainWindow.setSizePolicy(sizePolicy)
        CharacterManagerMainWindow.setMinimumSize(QSize(950, 855))
        CharacterManagerMainWindow.setMaximumSize(QSize(950, 855))
        self.action_new_character_sheet = QAction(CharacterManagerMainWindow)
        self.action_new_character_sheet.setObjectName(u"action_new_character_sheet")
        self.action_save_character_sheet = QAction(CharacterManagerMainWindow)
        self.action_save_character_sheet.setObjectName(u"action_save_character_sheet")
        self.action_save_all_character_sheets = QAction(CharacterManagerMainWindow)
        self.action_save_all_character_sheets.setObjectName(u"action_save_all_character_sheets")
        self.action_exit = QAction(CharacterManagerMainWindow)
        self.action_exit.setObjectName(u"action_exit")
        self.action_delete_current_character_sheet = QAction(CharacterManagerMainWindow)
        self.action_delete_current_character_sheet.setObjectName(u"action_delete_current_character_sheet")
        self.action_about = QAction(CharacterManagerMainWindow)
        self.action_about.setObjectName(u"action_about")
        self.centralwidget = QWidget(CharacterManagerMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.character_sheet_tabWidget = QTabWidget(self.centralwidget)
        self.character_sheet_tabWidget.setObjectName(u"character_sheet_tabWidget")
        self.character_sheet_tabWidget.setGeometry(QRect(0, 0, 950, 820))
        self.character_sheet_tabWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.character_sheet_tabWidget.addTab(self.tab, "")
        CharacterManagerMainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(CharacterManagerMainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 950, 33))
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menuBar)
        self.menuHelp.setObjectName(u"menuHelp")
        CharacterManagerMainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.action_new_character_sheet)
        self.menuFile.addAction(self.action_save_character_sheet)
        self.menuFile.addAction(self.action_save_all_character_sheets)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_delete_current_character_sheet)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_exit)
        self.menuHelp.addAction(self.action_about)

        self.retranslateUi(CharacterManagerMainWindow)

        self.character_sheet_tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(CharacterManagerMainWindow)
    # setupUi

    def retranslateUi(self, CharacterManagerMainWindow):
        CharacterManagerMainWindow.setWindowTitle(QCoreApplication.translate("CharacterManagerMainWindow", u"Heimurinn Karakter Menedzser", None))
        self.action_new_character_sheet.setText(QCoreApplication.translate("CharacterManagerMainWindow", u"\u00daj karakterlap", None))
        self.action_save_character_sheet.setText(QCoreApplication.translate("CharacterManagerMainWindow", u"Karakterlap ment\u00e9se", None))
#if QT_CONFIG(shortcut)
        self.action_save_character_sheet.setShortcut(QCoreApplication.translate("CharacterManagerMainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.action_save_all_character_sheets.setText(QCoreApplication.translate("CharacterManagerMainWindow", u"\u00d6sszes karakterlap ment\u00e9se", None))
#if QT_CONFIG(shortcut)
        self.action_save_all_character_sheets.setShortcut(QCoreApplication.translate("CharacterManagerMainWindow", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.action_exit.setText(QCoreApplication.translate("CharacterManagerMainWindow", u"Kil\u00e9p\u00e9s", None))
        self.action_delete_current_character_sheet.setText(QCoreApplication.translate("CharacterManagerMainWindow", u"Jelenlegi karakterlap t\u00f6rl\u00e9se", None))
        self.action_about.setText(QCoreApplication.translate("CharacterManagerMainWindow", u"N\u00e9vjegy", None))
        self.character_sheet_tabWidget.setTabText(self.character_sheet_tabWidget.indexOf(self.tab), QCoreApplication.translate("CharacterManagerMainWindow", u"Tab 1", None))
        self.menuFile.setTitle(QCoreApplication.translate("CharacterManagerMainWindow", u"F\u00e1jl", None))
        self.menuHelp.setTitle(QCoreApplication.translate("CharacterManagerMainWindow", u"Seg\u00edts\u00e9g", None))
    # retranslateUi

