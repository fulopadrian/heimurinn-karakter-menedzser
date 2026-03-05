# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_update_small_item_dialog.ui'
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

class Ui_AddUpdateSmallItemDialog(object):
    def setupUi(self, AddUpdateSmallItemDialog):
        if not AddUpdateSmallItemDialog.objectName():
            AddUpdateSmallItemDialog.setObjectName(u"AddUpdateSmallItemDialog")
        AddUpdateSmallItemDialog.resize(300, 75)
        self.confirm_reject_small_item_buttonBox = QDialogButtonBox(AddUpdateSmallItemDialog)
        self.confirm_reject_small_item_buttonBox.setObjectName(u"confirm_reject_small_item_buttonBox")
        self.confirm_reject_small_item_buttonBox.setGeometry(QRect(120, 40, 171, 32))
        self.confirm_reject_small_item_buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.confirm_reject_small_item_buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.layoutWidget = QWidget(AddUpdateSmallItemDialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 281, 24))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.small_item_label = QLabel(self.layoutWidget)
        self.small_item_label.setObjectName(u"small_item_label")

        self.horizontalLayout.addWidget(self.small_item_label)

        self.small_item_lineEdit = QLineEdit(self.layoutWidget)
        self.small_item_lineEdit.setObjectName(u"small_item_lineEdit")

        self.horizontalLayout.addWidget(self.small_item_lineEdit)


        self.retranslateUi(AddUpdateSmallItemDialog)
        self.confirm_reject_small_item_buttonBox.accepted.connect(AddUpdateSmallItemDialog.accept)
        self.confirm_reject_small_item_buttonBox.rejected.connect(AddUpdateSmallItemDialog.reject)

        QMetaObject.connectSlotsByName(AddUpdateSmallItemDialog)
    # setupUi

    def retranslateUi(self, AddUpdateSmallItemDialog):
        AddUpdateSmallItemDialog.setWindowTitle(QCoreApplication.translate("AddUpdateSmallItemDialog", u"T\u00e1rgy hozz\u00e1ad\u00e1sa", None))
        self.small_item_label.setText(QCoreApplication.translate("AddUpdateSmallItemDialog", u"T\u00e1rgy", None))
    # retranslateUi

