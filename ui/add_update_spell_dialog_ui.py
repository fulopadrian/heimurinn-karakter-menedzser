# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_update_spell_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QLineEdit, QSizePolicy, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_AddUpdateSpellDialog(object):
    def setupUi(self, AddUpdateSpellDialog):
        if not AddUpdateSpellDialog.objectName():
            AddUpdateSpellDialog.setObjectName(u"AddUpdateSpellDialog")
        AddUpdateSpellDialog.resize(300, 150)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AddUpdateSpellDialog.sizePolicy().hasHeightForWidth())
        AddUpdateSpellDialog.setSizePolicy(sizePolicy)
        AddUpdateSpellDialog.setMinimumSize(QSize(300, 150))
        AddUpdateSpellDialog.setMaximumSize(QSize(300, 150))
        self.confirm_reject_spell_buttonBox = QDialogButtonBox(AddUpdateSpellDialog)
        self.confirm_reject_spell_buttonBox.setObjectName(u"confirm_reject_spell_buttonBox")
        self.confirm_reject_spell_buttonBox.setGeometry(QRect(120, 110, 171, 32))
        self.confirm_reject_spell_buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.confirm_reject_spell_buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.layoutWidget = QWidget(AddUpdateSpellDialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 81, 48))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.spell_level_label = QLabel(self.layoutWidget)
        self.spell_level_label.setObjectName(u"spell_level_label")

        self.verticalLayout.addWidget(self.spell_level_label)

        self.spell_level_spinBox = QSpinBox(self.layoutWidget)
        self.spell_level_spinBox.setObjectName(u"spell_level_spinBox")
        self.spell_level_spinBox.setMinimum(1)
        self.spell_level_spinBox.setMaximum(3)

        self.verticalLayout.addWidget(self.spell_level_spinBox)

        self.layoutWidget1 = QWidget(AddUpdateSpellDialog)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(100, 10, 191, 46))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.spell_name_label = QLabel(self.layoutWidget1)
        self.spell_name_label.setObjectName(u"spell_name_label")

        self.verticalLayout_2.addWidget(self.spell_name_label)

        self.spell_name_lineEdit = QLineEdit(self.layoutWidget1)
        self.spell_name_lineEdit.setObjectName(u"spell_name_lineEdit")

        self.verticalLayout_2.addWidget(self.spell_name_lineEdit)

        self.layoutWidget2 = QWidget(AddUpdateSpellDialog)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 60, 281, 46))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.spell_description_label = QLabel(self.layoutWidget2)
        self.spell_description_label.setObjectName(u"spell_description_label")

        self.verticalLayout_3.addWidget(self.spell_description_label)

        self.spell_description_lineEdit = QLineEdit(self.layoutWidget2)
        self.spell_description_lineEdit.setObjectName(u"spell_description_lineEdit")

        self.verticalLayout_3.addWidget(self.spell_description_lineEdit)


        self.retranslateUi(AddUpdateSpellDialog)
        self.confirm_reject_spell_buttonBox.accepted.connect(AddUpdateSpellDialog.accept)
        self.confirm_reject_spell_buttonBox.rejected.connect(AddUpdateSpellDialog.reject)

        QMetaObject.connectSlotsByName(AddUpdateSpellDialog)
    # setupUi

    def retranslateUi(self, AddUpdateSpellDialog):
        AddUpdateSpellDialog.setWindowTitle(QCoreApplication.translate("AddUpdateSpellDialog", u"Var\u00e1zslat", None))
        self.spell_level_label.setText(QCoreApplication.translate("AddUpdateSpellDialog", u"Szint", None))
        self.spell_name_label.setText(QCoreApplication.translate("AddUpdateSpellDialog", u"Var\u00e1zslat", None))
        self.spell_description_label.setText(QCoreApplication.translate("AddUpdateSpellDialog", u"Le\u00edr\u00e1s", None))
    # retranslateUi

