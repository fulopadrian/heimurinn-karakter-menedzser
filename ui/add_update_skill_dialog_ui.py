# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_update_skill_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QHBoxLayout, QLabel, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_AddUpdateSkillDialog(object):
    def setupUi(self, AddUpdateSkillDialog):
        if not AddUpdateSkillDialog.objectName():
            AddUpdateSkillDialog.setObjectName(u"AddUpdateSkillDialog")
        AddUpdateSkillDialog.resize(375, 115)
        AddUpdateSkillDialog.setMinimumSize(QSize(375, 115))
        AddUpdateSkillDialog.setMaximumSize(QSize(375, 115))
        self.confirm_reject_skill_buttonBox = QDialogButtonBox(AddUpdateSkillDialog)
        self.confirm_reject_skill_buttonBox.setObjectName(u"confirm_reject_skill_buttonBox")
        self.confirm_reject_skill_buttonBox.setGeometry(QRect(170, 80, 171, 32))
        self.confirm_reject_skill_buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.confirm_reject_skill_buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.layoutWidget = QWidget(AddUpdateSkillDialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 10, 371, 68))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.skill_label = QLabel(self.layoutWidget)
        self.skill_label.setObjectName(u"skill_label")

        self.horizontalLayout.addWidget(self.skill_label)

        self.skill_comboBox = QComboBox(self.layoutWidget)
        self.skill_comboBox.setObjectName(u"skill_comboBox")

        self.horizontalLayout.addWidget(self.skill_comboBox)


        self.horizontalLayout_5.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.skill_level_label = QLabel(self.layoutWidget)
        self.skill_level_label.setObjectName(u"skill_level_label")

        self.horizontalLayout_3.addWidget(self.skill_level_label)

        self.skill_level_spinBox = QSpinBox(self.layoutWidget)
        self.skill_level_spinBox.setObjectName(u"skill_level_spinBox")
        self.skill_level_spinBox.setMinimum(0)

        self.horizontalLayout_3.addWidget(self.skill_level_spinBox)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.attribute_label = QLabel(self.layoutWidget)
        self.attribute_label.setObjectName(u"attribute_label")

        self.horizontalLayout_2.addWidget(self.attribute_label)

        self.attribute_comboBox = QComboBox(self.layoutWidget)
        self.attribute_comboBox.setObjectName(u"attribute_comboBox")

        self.horizontalLayout_2.addWidget(self.attribute_comboBox)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.other_mod_label = QLabel(self.layoutWidget)
        self.other_mod_label.setObjectName(u"other_mod_label")

        self.horizontalLayout_4.addWidget(self.other_mod_label)

        self.other_mod_spinBox = QSpinBox(self.layoutWidget)
        self.other_mod_spinBox.setObjectName(u"other_mod_spinBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.other_mod_spinBox.sizePolicy().hasHeightForWidth())
        self.other_mod_spinBox.setSizePolicy(sizePolicy)
        self.other_mod_spinBox.setMinimum(-10)

        self.horizontalLayout_4.addWidget(self.other_mod_spinBox)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addLayout(self.horizontalLayout_6)


        self.retranslateUi(AddUpdateSkillDialog)
        self.confirm_reject_skill_buttonBox.accepted.connect(AddUpdateSkillDialog.accept)
        self.confirm_reject_skill_buttonBox.rejected.connect(AddUpdateSkillDialog.reject)

        QMetaObject.connectSlotsByName(AddUpdateSkillDialog)
    # setupUi

    def retranslateUi(self, AddUpdateSkillDialog):
        AddUpdateSkillDialog.setWindowTitle(QCoreApplication.translate("AddUpdateSkillDialog", u"J\u00e1rtass\u00e1g", None))
        self.skill_label.setText(QCoreApplication.translate("AddUpdateSkillDialog", u"J\u00e1rtass\u00e1g", None))
        self.skill_level_label.setText(QCoreApplication.translate("AddUpdateSkillDialog", u"Szint", None))
        self.attribute_label.setText(QCoreApplication.translate("AddUpdateSkillDialog", u"Tulajdons\u00e1g", None))
        self.other_mod_label.setText(QCoreApplication.translate("AddUpdateSkillDialog", u"Egy\u00e9b", None))
    # retranslateUi

