# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_update_weapon_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractSpinBox, QApplication, QComboBox,
    QDialog, QDialogButtonBox, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QSizePolicy, QSpinBox,
    QWidget)

class Ui_AddUpdateWeaponDialog(object):
    def setupUi(self, AddUpdateWeaponDialog):
        if not AddUpdateWeaponDialog.objectName():
            AddUpdateWeaponDialog.setObjectName(u"AddUpdateWeaponDialog")
        AddUpdateWeaponDialog.resize(300, 240)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AddUpdateWeaponDialog.sizePolicy().hasHeightForWidth())
        AddUpdateWeaponDialog.setSizePolicy(sizePolicy)
        AddUpdateWeaponDialog.setMinimumSize(QSize(300, 240))
        AddUpdateWeaponDialog.setMaximumSize(QSize(300, 240))
        self.confirm_reject_weapon_buttonBox = QDialogButtonBox(AddUpdateWeaponDialog)
        self.confirm_reject_weapon_buttonBox.setObjectName(u"confirm_reject_weapon_buttonBox")
        self.confirm_reject_weapon_buttonBox.setGeometry(QRect(100, 210, 171, 32))
        self.confirm_reject_weapon_buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.confirm_reject_weapon_buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.critical_threshold_groupBox = QGroupBox(AddUpdateWeaponDialog)
        self.critical_threshold_groupBox.setObjectName(u"critical_threshold_groupBox")
        self.critical_threshold_groupBox.setGeometry(QRect(10, 70, 151, 51))
        self.layoutWidget = QWidget(self.critical_threshold_groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 20, 131, 26))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.critical_threshold_min_spinBox = QSpinBox(self.layoutWidget)
        self.critical_threshold_min_spinBox.setObjectName(u"critical_threshold_min_spinBox")
        self.critical_threshold_min_spinBox.setMinimum(1)
        self.critical_threshold_min_spinBox.setMaximum(20)
        self.critical_threshold_min_spinBox.setValue(19)

        self.horizontalLayout_3.addWidget(self.critical_threshold_min_spinBox)

        self.dash_separator_label = QLabel(self.layoutWidget)
        self.dash_separator_label.setObjectName(u"dash_separator_label")

        self.horizontalLayout_3.addWidget(self.dash_separator_label)

        self.critical_threshold_max_spinBox = QSpinBox(self.layoutWidget)
        self.critical_threshold_max_spinBox.setObjectName(u"critical_threshold_max_spinBox")
        self.critical_threshold_max_spinBox.setReadOnly(True)
        self.critical_threshold_max_spinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.critical_threshold_max_spinBox.setMinimum(20)
        self.critical_threshold_max_spinBox.setMaximum(20)

        self.horizontalLayout_3.addWidget(self.critical_threshold_max_spinBox)

        self.damage_groupBox = QGroupBox(AddUpdateWeaponDialog)
        self.damage_groupBox.setObjectName(u"damage_groupBox")
        self.damage_groupBox.setGeometry(QRect(10, 120, 281, 51))
        self.layoutWidget1 = QWidget(self.damage_groupBox)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 20, 261, 26))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.damage_dice_number_spinBox = QSpinBox(self.layoutWidget1)
        self.damage_dice_number_spinBox.setObjectName(u"damage_dice_number_spinBox")
        self.damage_dice_number_spinBox.setMinimum(1)

        self.horizontalLayout_4.addWidget(self.damage_dice_number_spinBox)

        self.dice_separator_label = QLabel(self.layoutWidget1)
        self.dice_separator_label.setObjectName(u"dice_separator_label")

        self.horizontalLayout_4.addWidget(self.dice_separator_label)

        self.damage_dice_side_spinBox = QSpinBox(self.layoutWidget1)
        self.damage_dice_side_spinBox.setObjectName(u"damage_dice_side_spinBox")
        self.damage_dice_side_spinBox.setMinimum(2)

        self.horizontalLayout_4.addWidget(self.damage_dice_side_spinBox)

        self.plus_separator_label = QLabel(self.layoutWidget1)
        self.plus_separator_label.setObjectName(u"plus_separator_label")

        self.horizontalLayout_4.addWidget(self.plus_separator_label)

        self.damage_dice_modifier_spinBox = QSpinBox(self.layoutWidget1)
        self.damage_dice_modifier_spinBox.setObjectName(u"damage_dice_modifier_spinBox")

        self.horizontalLayout_4.addWidget(self.damage_dice_modifier_spinBox)

        self.layoutWidget2 = QWidget(AddUpdateWeaponDialog)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 10, 281, 24))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.weapon_name_label = QLabel(self.layoutWidget2)
        self.weapon_name_label.setObjectName(u"weapon_name_label")

        self.horizontalLayout.addWidget(self.weapon_name_label)

        self.weapon_name_lineEdit = QLineEdit(self.layoutWidget2)
        self.weapon_name_lineEdit.setObjectName(u"weapon_name_lineEdit")

        self.horizontalLayout.addWidget(self.weapon_name_lineEdit)

        self.layoutWidget3 = QWidget(AddUpdateWeaponDialog)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(10, 180, 281, 24))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.weapon_special_label = QLabel(self.layoutWidget3)
        self.weapon_special_label.setObjectName(u"weapon_special_label")

        self.horizontalLayout_2.addWidget(self.weapon_special_label)

        self.weapon_special_lineEdit = QLineEdit(self.layoutWidget3)
        self.weapon_special_lineEdit.setObjectName(u"weapon_special_lineEdit")

        self.horizontalLayout_2.addWidget(self.weapon_special_lineEdit)

        self.layoutWidget4 = QWidget(AddUpdateWeaponDialog)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(10, 40, 281, 28))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.weapon_linked_attribute_label = QLabel(self.layoutWidget4)
        self.weapon_linked_attribute_label.setObjectName(u"weapon_linked_attribute_label")

        self.horizontalLayout_5.addWidget(self.weapon_linked_attribute_label)

        self.weapon_linked_attribute_comboBox = QComboBox(self.layoutWidget4)
        self.weapon_linked_attribute_comboBox.setObjectName(u"weapon_linked_attribute_comboBox")

        self.horizontalLayout_5.addWidget(self.weapon_linked_attribute_comboBox)


        self.retranslateUi(AddUpdateWeaponDialog)
        self.confirm_reject_weapon_buttonBox.accepted.connect(AddUpdateWeaponDialog.accept)
        self.confirm_reject_weapon_buttonBox.rejected.connect(AddUpdateWeaponDialog.reject)

        QMetaObject.connectSlotsByName(AddUpdateWeaponDialog)
    # setupUi

    def retranslateUi(self, AddUpdateWeaponDialog):
        AddUpdateWeaponDialog.setWindowTitle(QCoreApplication.translate("AddUpdateWeaponDialog", u"Fegyver", None))
        self.critical_threshold_groupBox.setTitle(QCoreApplication.translate("AddUpdateWeaponDialog", u"Kritikus", None))
        self.dash_separator_label.setText(QCoreApplication.translate("AddUpdateWeaponDialog", u"-", None))
        self.damage_groupBox.setTitle(QCoreApplication.translate("AddUpdateWeaponDialog", u"Sebz\u00e9s", None))
        self.dice_separator_label.setText(QCoreApplication.translate("AddUpdateWeaponDialog", u"D", None))
        self.plus_separator_label.setText(QCoreApplication.translate("AddUpdateWeaponDialog", u"+", None))
        self.weapon_name_label.setText(QCoreApplication.translate("AddUpdateWeaponDialog", u"Fegyver", None))
        self.weapon_special_label.setText(QCoreApplication.translate("AddUpdateWeaponDialog", u"Speci\u00e1lis", None))
        self.weapon_linked_attribute_label.setText(QCoreApplication.translate("AddUpdateWeaponDialog", u"Kapcsolt tulajdons\u00e1g", None))
    # retranslateUi

