# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_update_fame_dialog.ui'
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
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QRadioButton, QSizePolicy, QSpinBox, QWidget)

class Ui_AddUpdateFameDialog(object):
    def setupUi(self, AddUpdateFameDialog):
        if not AddUpdateFameDialog.objectName():
            AddUpdateFameDialog.setObjectName(u"AddUpdateFameDialog")
        AddUpdateFameDialog.resize(350, 115)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AddUpdateFameDialog.sizePolicy().hasHeightForWidth())
        AddUpdateFameDialog.setSizePolicy(sizePolicy)
        AddUpdateFameDialog.setMinimumSize(QSize(350, 115))
        AddUpdateFameDialog.setMaximumSize(QSize(350, 115))
        self.confirm_reject_fame_buttonBox = QDialogButtonBox(AddUpdateFameDialog)
        self.confirm_reject_fame_buttonBox.setObjectName(u"confirm_reject_fame_buttonBox")
        self.confirm_reject_fame_buttonBox.setGeometry(QRect(170, 80, 171, 32))
        self.confirm_reject_fame_buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.confirm_reject_fame_buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.fame_type_groupBox = QGroupBox(AddUpdateFameDialog)
        self.fame_type_groupBox.setObjectName(u"fame_type_groupBox")
        self.fame_type_groupBox.setGeometry(QRect(0, 0, 131, 81))
        self.glory_radioButton = QRadioButton(self.fame_type_groupBox)
        self.glory_radioButton.setObjectName(u"glory_radioButton")
        self.glory_radioButton.setGeometry(QRect(10, 20, 61, 24))
        self.glory_radioButton.setChecked(True)
        self.notoriety_radioButton = QRadioButton(self.fame_type_groupBox)
        self.notoriety_radioButton.setObjectName(u"notoriety_radioButton")
        self.notoriety_radioButton.setGeometry(QRect(10, 50, 81, 24))
        self.layoutWidget = QWidget(AddUpdateFameDialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(140, 50, 201, 24))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.fame_description_label = QLabel(self.layoutWidget)
        self.fame_description_label.setObjectName(u"fame_description_label")

        self.horizontalLayout.addWidget(self.fame_description_label)

        self.fame_description_lineEdit = QLineEdit(self.layoutWidget)
        self.fame_description_lineEdit.setObjectName(u"fame_description_lineEdit")

        self.horizontalLayout.addWidget(self.fame_description_lineEdit)

        self.layoutWidget1 = QWidget(AddUpdateFameDialog)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(140, 10, 101, 26))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.fame_value_label = QLabel(self.layoutWidget1)
        self.fame_value_label.setObjectName(u"fame_value_label")

        self.horizontalLayout_2.addWidget(self.fame_value_label)

        self.fame_value_spinBox = QSpinBox(self.layoutWidget1)
        self.fame_value_spinBox.setObjectName(u"fame_value_spinBox")
        self.fame_value_spinBox.setMinimum(1)

        self.horizontalLayout_2.addWidget(self.fame_value_spinBox)


        self.retranslateUi(AddUpdateFameDialog)
        self.confirm_reject_fame_buttonBox.accepted.connect(AddUpdateFameDialog.accept)
        self.confirm_reject_fame_buttonBox.rejected.connect(AddUpdateFameDialog.reject)

        QMetaObject.connectSlotsByName(AddUpdateFameDialog)
    # setupUi

    def retranslateUi(self, AddUpdateFameDialog):
        AddUpdateFameDialog.setWindowTitle(QCoreApplication.translate("AddUpdateFameDialog", u"H\u00edrn\u00e9v hozz\u00e1ad\u00e1sa", None))
        self.fame_type_groupBox.setTitle(QCoreApplication.translate("AddUpdateFameDialog", u"Dics\u0151 vagy dicstelen", None))
        self.glory_radioButton.setText(QCoreApplication.translate("AddUpdateFameDialog", u"Dics\u0151", None))
        self.notoriety_radioButton.setText(QCoreApplication.translate("AddUpdateFameDialog", u"Dicstelen", None))
        self.fame_description_label.setText(QCoreApplication.translate("AddUpdateFameDialog", u"Le\u00edr\u00e1s", None))
        self.fame_value_label.setText(QCoreApplication.translate("AddUpdateFameDialog", u"\u00c9rt\u00e9k", None))
    # retranslateUi

