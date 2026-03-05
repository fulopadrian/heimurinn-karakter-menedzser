# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_update_ability_dialog.ui'
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
    QHBoxLayout, QLabel, QLineEdit, QSizePolicy,
    QWidget)

class Ui_AddUpdateAbilityDialog(object):
    def setupUi(self, AddUpdateAbilityDialog):
        if not AddUpdateAbilityDialog.objectName():
            AddUpdateAbilityDialog.setObjectName(u"AddUpdateAbilityDialog")
        AddUpdateAbilityDialog.resize(300, 75)
        self.confirm_reject_ability_buttonBox = QDialogButtonBox(AddUpdateAbilityDialog)
        self.confirm_reject_ability_buttonBox.setObjectName(u"confirm_reject_ability_buttonBox")
        self.confirm_reject_ability_buttonBox.setGeometry(QRect(120, 40, 171, 32))
        self.confirm_reject_ability_buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.confirm_reject_ability_buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.layoutWidget = QWidget(AddUpdateAbilityDialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 281, 24))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.ability_label = QLabel(self.layoutWidget)
        self.ability_label.setObjectName(u"ability_label")

        self.horizontalLayout.addWidget(self.ability_label)

        self.ability_lineEdit = QLineEdit(self.layoutWidget)
        self.ability_lineEdit.setObjectName(u"ability_lineEdit")

        self.horizontalLayout.addWidget(self.ability_lineEdit)


        self.retranslateUi(AddUpdateAbilityDialog)
        self.confirm_reject_ability_buttonBox.accepted.connect(AddUpdateAbilityDialog.accept)
        self.confirm_reject_ability_buttonBox.rejected.connect(AddUpdateAbilityDialog.reject)

        QMetaObject.connectSlotsByName(AddUpdateAbilityDialog)
    # setupUi

    def retranslateUi(self, AddUpdateAbilityDialog):
        AddUpdateAbilityDialog.setWindowTitle(QCoreApplication.translate("AddUpdateAbilityDialog", u"K\u00e9pess\u00e9g hozz\u00e1ad\u00e1sa", None))
        self.ability_label.setText(QCoreApplication.translate("AddUpdateAbilityDialog", u"K\u00e9pess\u00e9g", None))
    # retranslateUi

