# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'skald_attack_defense_options_dialog.ui'
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
    QGroupBox, QRadioButton, QSizePolicy, QTextEdit,
    QWidget)

class Ui_SkaldAttackDefenseOptionsDialog(object):
    def setupUi(self, SkaldAttackDefenseOptionsDialog):
        if not SkaldAttackDefenseOptionsDialog.objectName():
            SkaldAttackDefenseOptionsDialog.setObjectName(u"SkaldAttackDefenseOptionsDialog")
        SkaldAttackDefenseOptionsDialog.resize(400, 150)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SkaldAttackDefenseOptionsDialog.sizePolicy().hasHeightForWidth())
        SkaldAttackDefenseOptionsDialog.setSizePolicy(sizePolicy)
        SkaldAttackDefenseOptionsDialog.setMinimumSize(QSize(400, 150))
        SkaldAttackDefenseOptionsDialog.setMaximumSize(QSize(400, 150))
        self.confirm_reject_skald_attack_defense_options_buttonBox = QDialogButtonBox(SkaldAttackDefenseOptionsDialog)
        self.confirm_reject_skald_attack_defense_options_buttonBox.setObjectName(u"confirm_reject_skald_attack_defense_options_buttonBox")
        self.confirm_reject_skald_attack_defense_options_buttonBox.setGeometry(QRect(220, 110, 171, 32))
        self.confirm_reject_skald_attack_defense_options_buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.confirm_reject_skald_attack_defense_options_buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.skald_attack_defense_options_groupBox = QGroupBox(SkaldAttackDefenseOptionsDialog)
        self.skald_attack_defense_options_groupBox.setObjectName(u"skald_attack_defense_options_groupBox")
        self.skald_attack_defense_options_groupBox.setGeometry(QRect(10, 10, 131, 101))
        self.default_radioButton = QRadioButton(self.skald_attack_defense_options_groupBox)
        self.default_radioButton.setObjectName(u"default_radioButton")
        self.default_radioButton.setGeometry(QRect(10, 10, 121, 24))
        self.default_radioButton.setChecked(True)
        self.higher_attack_radioButton = QRadioButton(self.skald_attack_defense_options_groupBox)
        self.higher_attack_radioButton.setObjectName(u"higher_attack_radioButton")
        self.higher_attack_radioButton.setGeometry(QRect(10, 40, 98, 24))
        self.higher_defense_radioButton = QRadioButton(self.skald_attack_defense_options_groupBox)
        self.higher_defense_radioButton.setObjectName(u"higher_defense_radioButton")
        self.higher_defense_radioButton.setGeometry(QRect(10, 70, 98, 24))
        self.rule_description_textEdit = QTextEdit(SkaldAttackDefenseOptionsDialog)
        self.rule_description_textEdit.setObjectName(u"rule_description_textEdit")
        self.rule_description_textEdit.setGeometry(QRect(150, 10, 241, 101))
        self.rule_description_textEdit.setReadOnly(True)
        self.rule_description_textEdit.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.retranslateUi(SkaldAttackDefenseOptionsDialog)
        self.confirm_reject_skald_attack_defense_options_buttonBox.accepted.connect(SkaldAttackDefenseOptionsDialog.accept)
        self.confirm_reject_skald_attack_defense_options_buttonBox.rejected.connect(SkaldAttackDefenseOptionsDialog.reject)

        QMetaObject.connectSlotsByName(SkaldAttackDefenseOptionsDialog)
    # setupUi

    def retranslateUi(self, SkaldAttackDefenseOptionsDialog):
        SkaldAttackDefenseOptionsDialog.setWindowTitle(QCoreApplication.translate("SkaldAttackDefenseOptionsDialog", u"Szkald", None))
        self.skald_attack_defense_options_groupBox.setTitle("")
        self.default_radioButton.setText(QCoreApplication.translate("SkaldAttackDefenseOptionsDialog", u"Alap\u00e9rtelmezett", None))
        self.higher_attack_radioButton.setText(QCoreApplication.translate("SkaldAttackDefenseOptionsDialog", u"T\u00e1mad\u00f3", None))
        self.higher_defense_radioButton.setText(QCoreApplication.translate("SkaldAttackDefenseOptionsDialog", u"V\u00e9d\u0151", None))
        self.rule_description_textEdit.setPlaceholderText("")
    # retranslateUi

