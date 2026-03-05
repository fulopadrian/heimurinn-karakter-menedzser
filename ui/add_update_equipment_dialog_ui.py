# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_update_equipment_dialog.ui'
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
    QDoubleSpinBox, QHBoxLayout, QLabel, QLineEdit,
    QSizePolicy, QSpinBox, QVBoxLayout, QWidget)

class Ui_AddUpdateEquipmentDialog(object):
    def setupUi(self, AddUpdateEquipmentDialog):
        if not AddUpdateEquipmentDialog.objectName():
            AddUpdateEquipmentDialog.setObjectName(u"AddUpdateEquipmentDialog")
        AddUpdateEquipmentDialog.resize(250, 150)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AddUpdateEquipmentDialog.sizePolicy().hasHeightForWidth())
        AddUpdateEquipmentDialog.setSizePolicy(sizePolicy)
        AddUpdateEquipmentDialog.setMaximumSize(QSize(250, 150))
        self.confirm_reject_equipment_buttonBox = QDialogButtonBox(AddUpdateEquipmentDialog)
        self.confirm_reject_equipment_buttonBox.setObjectName(u"confirm_reject_equipment_buttonBox")
        self.confirm_reject_equipment_buttonBox.setGeometry(QRect(70, 110, 171, 32))
        self.confirm_reject_equipment_buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.confirm_reject_equipment_buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.layoutWidget = QWidget(AddUpdateEquipmentDialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 10, 241, 90))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.equipment_name_label = QLabel(self.layoutWidget)
        self.equipment_name_label.setObjectName(u"equipment_name_label")

        self.horizontalLayout.addWidget(self.equipment_name_label)

        self.equipment_name_lineEdit = QLineEdit(self.layoutWidget)
        self.equipment_name_lineEdit.setObjectName(u"equipment_name_lineEdit")

        self.horizontalLayout.addWidget(self.equipment_name_lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.equipment_count_label = QLabel(self.layoutWidget)
        self.equipment_count_label.setObjectName(u"equipment_count_label")

        self.horizontalLayout_2.addWidget(self.equipment_count_label)

        self.equipment_count_spinBox = QSpinBox(self.layoutWidget)
        self.equipment_count_spinBox.setObjectName(u"equipment_count_spinBox")
        self.equipment_count_spinBox.setMinimum(1)

        self.horizontalLayout_2.addWidget(self.equipment_count_spinBox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.equipment_encumbrance_label = QLabel(self.layoutWidget)
        self.equipment_encumbrance_label.setObjectName(u"equipment_encumbrance_label")

        self.horizontalLayout_3.addWidget(self.equipment_encumbrance_label)

        self.equipment_encumbrance_doubleSpinBox = QDoubleSpinBox(self.layoutWidget)
        self.equipment_encumbrance_doubleSpinBox.setObjectName(u"equipment_encumbrance_doubleSpinBox")

        self.horizontalLayout_3.addWidget(self.equipment_encumbrance_doubleSpinBox)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(AddUpdateEquipmentDialog)
        self.confirm_reject_equipment_buttonBox.accepted.connect(AddUpdateEquipmentDialog.accept)
        self.confirm_reject_equipment_buttonBox.rejected.connect(AddUpdateEquipmentDialog.reject)

        QMetaObject.connectSlotsByName(AddUpdateEquipmentDialog)
    # setupUi

    def retranslateUi(self, AddUpdateEquipmentDialog):
        AddUpdateEquipmentDialog.setWindowTitle(QCoreApplication.translate("AddUpdateEquipmentDialog", u"Felszerel\u00e9s hozz\u00e1ad\u00e1sa", None))
        self.equipment_name_label.setText(QCoreApplication.translate("AddUpdateEquipmentDialog", u"Felszerel\u00e9s neve", None))
        self.equipment_count_label.setText(QCoreApplication.translate("AddUpdateEquipmentDialog", u"Mennyis\u00e9g", None))
        self.equipment_encumbrance_label.setText(QCoreApplication.translate("AddUpdateEquipmentDialog", u"Egys\u00e9gnyi terhel\u00e9s", None))
    # retranslateUi

