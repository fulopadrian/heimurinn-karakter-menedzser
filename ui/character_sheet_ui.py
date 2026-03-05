# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'character_sheet.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QComboBox,
    QDoubleSpinBox, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSpinBox, QTableWidget, QTableWidgetItem, QTextEdit,
    QToolBox, QVBoxLayout, QWidget)

class Ui_CharacterSheet(object):
    def setupUi(self, CharacterSheet):
        if not CharacterSheet.objectName():
            CharacterSheet.setObjectName(u"CharacterSheet")
        CharacterSheet.resize(950, 800)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CharacterSheet.sizePolicy().hasHeightForWidth())
        CharacterSheet.setSizePolicy(sizePolicy)
        CharacterSheet.setMinimumSize(QSize(950, 800))
        CharacterSheet.setMaximumSize(QSize(950, 800))
        self.character_sheet_toolBox = QToolBox(CharacterSheet)
        self.character_sheet_toolBox.setObjectName(u"character_sheet_toolBox")
        self.character_sheet_toolBox.setGeometry(QRect(0, 0, 951, 611))
        self.character_sheet_toolBoxPage1 = QWidget()
        self.character_sheet_toolBoxPage1.setObjectName(u"character_sheet_toolBoxPage1")
        self.character_sheet_toolBoxPage1.setGeometry(QRect(0, 0, 951, 491))
        self.attributes_groupBox = QGroupBox(self.character_sheet_toolBoxPage1)
        self.attributes_groupBox.setObjectName(u"attributes_groupBox")
        self.attributes_groupBox.setGeometry(QRect(0, 130, 211, 221))
        self.layoutWidget = QWidget(self.attributes_groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 20, 191, 188))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.strength_label = QLabel(self.layoutWidget)
        self.strength_label.setObjectName(u"strength_label")

        self.horizontalLayout_4.addWidget(self.strength_label)

        self.strength_spinBox = QSpinBox(self.layoutWidget)
        self.strength_spinBox.setObjectName(u"strength_spinBox")
        self.strength_spinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.strength_spinBox.setMinimum(1)
        self.strength_spinBox.setMaximum(22)
        self.strength_spinBox.setValue(1)

        self.horizontalLayout_4.addWidget(self.strength_spinBox)

        self.strength_mod_spinBox = QSpinBox(self.layoutWidget)
        self.strength_mod_spinBox.setObjectName(u"strength_mod_spinBox")
        self.strength_mod_spinBox.setReadOnly(True)
        self.strength_mod_spinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.strength_mod_spinBox.setMinimum(-3)
        self.strength_mod_spinBox.setMaximum(5)

        self.horizontalLayout_4.addWidget(self.strength_mod_spinBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.dexterity_label = QLabel(self.layoutWidget)
        self.dexterity_label.setObjectName(u"dexterity_label")

        self.horizontalLayout_5.addWidget(self.dexterity_label)

        self.dexterity_spinBox = QSpinBox(self.layoutWidget)
        self.dexterity_spinBox.setObjectName(u"dexterity_spinBox")
        self.dexterity_spinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.dexterity_spinBox.setMinimum(1)
        self.dexterity_spinBox.setMaximum(22)
        self.dexterity_spinBox.setValue(1)

        self.horizontalLayout_5.addWidget(self.dexterity_spinBox)

        self.dexterity_mod_spinBox = QSpinBox(self.layoutWidget)
        self.dexterity_mod_spinBox.setObjectName(u"dexterity_mod_spinBox")
        self.dexterity_mod_spinBox.setReadOnly(True)
        self.dexterity_mod_spinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.dexterity_mod_spinBox.setMinimum(-3)
        self.dexterity_mod_spinBox.setMaximum(5)

        self.horizontalLayout_5.addWidget(self.dexterity_mod_spinBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.stamina_label = QLabel(self.layoutWidget)
        self.stamina_label.setObjectName(u"stamina_label")

        self.horizontalLayout_6.addWidget(self.stamina_label)

        self.stamina_spinBox = QSpinBox(self.layoutWidget)
        self.stamina_spinBox.setObjectName(u"stamina_spinBox")
        self.stamina_spinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.stamina_spinBox.setMinimum(1)
        self.stamina_spinBox.setMaximum(22)
        self.stamina_spinBox.setValue(1)

        self.horizontalLayout_6.addWidget(self.stamina_spinBox)

        self.stamina_mod_spinBox = QSpinBox(self.layoutWidget)
        self.stamina_mod_spinBox.setObjectName(u"stamina_mod_spinBox")
        self.stamina_mod_spinBox.setReadOnly(True)
        self.stamina_mod_spinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.stamina_mod_spinBox.setMinimum(-3)
        self.stamina_mod_spinBox.setMaximum(5)

        self.horizontalLayout_6.addWidget(self.stamina_mod_spinBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.intelligence_label = QLabel(self.layoutWidget)
        self.intelligence_label.setObjectName(u"intelligence_label")

        self.horizontalLayout_7.addWidget(self.intelligence_label)

        self.intelligence_spinBox = QSpinBox(self.layoutWidget)
        self.intelligence_spinBox.setObjectName(u"intelligence_spinBox")
        self.intelligence_spinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.intelligence_spinBox.setMinimum(1)
        self.intelligence_spinBox.setMaximum(22)
        self.intelligence_spinBox.setValue(1)

        self.horizontalLayout_7.addWidget(self.intelligence_spinBox)

        self.intelligence_mod_spinBox = QSpinBox(self.layoutWidget)
        self.intelligence_mod_spinBox.setObjectName(u"intelligence_mod_spinBox")
        self.intelligence_mod_spinBox.setReadOnly(True)
        self.intelligence_mod_spinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.intelligence_mod_spinBox.setMinimum(-3)
        self.intelligence_mod_spinBox.setMaximum(5)

        self.horizontalLayout_7.addWidget(self.intelligence_mod_spinBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.wisdom_label = QLabel(self.layoutWidget)
        self.wisdom_label.setObjectName(u"wisdom_label")

        self.horizontalLayout_8.addWidget(self.wisdom_label)

        self.wisdom_spinBox = QSpinBox(self.layoutWidget)
        self.wisdom_spinBox.setObjectName(u"wisdom_spinBox")
        self.wisdom_spinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.wisdom_spinBox.setMinimum(1)
        self.wisdom_spinBox.setMaximum(22)
        self.wisdom_spinBox.setValue(1)

        self.horizontalLayout_8.addWidget(self.wisdom_spinBox)

        self.wisdom_mod_spinBox = QSpinBox(self.layoutWidget)
        self.wisdom_mod_spinBox.setObjectName(u"wisdom_mod_spinBox")
        self.wisdom_mod_spinBox.setReadOnly(True)
        self.wisdom_mod_spinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.wisdom_mod_spinBox.setMinimum(-3)
        self.wisdom_mod_spinBox.setMaximum(5)

        self.horizontalLayout_8.addWidget(self.wisdom_mod_spinBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.charisma_label = QLabel(self.layoutWidget)
        self.charisma_label.setObjectName(u"charisma_label")

        self.horizontalLayout_9.addWidget(self.charisma_label)

        self.charisma_spinBox = QSpinBox(self.layoutWidget)
        self.charisma_spinBox.setObjectName(u"charisma_spinBox")
        self.charisma_spinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.charisma_spinBox.setMinimum(1)
        self.charisma_spinBox.setMaximum(22)
        self.charisma_spinBox.setValue(1)

        self.horizontalLayout_9.addWidget(self.charisma_spinBox)

        self.charisma_mod_spinBox = QSpinBox(self.layoutWidget)
        self.charisma_mod_spinBox.setObjectName(u"charisma_mod_spinBox")
        self.charisma_mod_spinBox.setReadOnly(True)
        self.charisma_mod_spinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.charisma_mod_spinBox.setMinimum(-3)
        self.charisma_mod_spinBox.setMaximum(5)

        self.horizontalLayout_9.addWidget(self.charisma_mod_spinBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.health_groupBox = QGroupBox(self.character_sheet_toolBoxPage1)
        self.health_groupBox.setObjectName(u"health_groupBox")
        self.health_groupBox.setGeometry(QRect(220, 130, 161, 141))
        self.layoutWidget_2 = QWidget(self.health_groupBox)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 20, 137, 112))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.health_spinBox = QSpinBox(self.layoutWidget_2)
        self.health_spinBox.setObjectName(u"health_spinBox")
        font = QFont()
        font.setPointSize(20)
        self.health_spinBox.setFont(font)
        self.health_spinBox.setMinimum(-10)

        self.verticalLayout_4.addWidget(self.health_spinBox)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.health_max_label = QLabel(self.layoutWidget_2)
        self.health_max_label.setObjectName(u"health_max_label")

        self.horizontalLayout_10.addWidget(self.health_max_label)

        self.health_max_spinBox = QSpinBox(self.layoutWidget_2)
        self.health_max_spinBox.setObjectName(u"health_max_spinBox")

        self.horizontalLayout_10.addWidget(self.health_max_spinBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.cold_resistance_label = QLabel(self.layoutWidget_2)
        self.cold_resistance_label.setObjectName(u"cold_resistance_label")

        self.horizontalLayout_11.addWidget(self.cold_resistance_label)

        self.cold_resistance_spinBox = QSpinBox(self.layoutWidget_2)
        self.cold_resistance_spinBox.setObjectName(u"cold_resistance_spinBox")

        self.horizontalLayout_11.addWidget(self.cold_resistance_spinBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.background_groupBox = QGroupBox(self.character_sheet_toolBoxPage1)
        self.background_groupBox.setObjectName(u"background_groupBox")
        self.background_groupBox.setGeometry(QRect(490, 10, 451, 121))
        self.background_textEdit = QTextEdit(self.background_groupBox)
        self.background_textEdit.setObjectName(u"background_textEdit")
        self.background_textEdit.setGeometry(QRect(10, 20, 431, 91))
        self.baseinfo_groupBox = QGroupBox(self.character_sheet_toolBoxPage1)
        self.baseinfo_groupBox.setObjectName(u"baseinfo_groupBox")
        self.baseinfo_groupBox.setGeometry(QRect(0, 10, 481, 121))
        self.layoutWidget_3 = QWidget(self.baseinfo_groupBox)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(10, 20, 464, 94))
        self.verticalLayout = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.name_label = QLabel(self.layoutWidget_3)
        self.name_label.setObjectName(u"name_label")

        self.horizontalLayout.addWidget(self.name_label)

        self.name_lineEdit = QLineEdit(self.layoutWidget_3)
        self.name_lineEdit.setObjectName(u"name_lineEdit")

        self.horizontalLayout.addWidget(self.name_lineEdit)

        self.class_label = QLabel(self.layoutWidget_3)
        self.class_label.setObjectName(u"class_label")

        self.horizontalLayout.addWidget(self.class_label)

        self.class_comboBox = QComboBox(self.layoutWidget_3)
        self.class_comboBox.setObjectName(u"class_comboBox")

        self.horizontalLayout.addWidget(self.class_comboBox)

        self.clan_label = QLabel(self.layoutWidget_3)
        self.clan_label.setObjectName(u"clan_label")

        self.horizontalLayout.addWidget(self.clan_label)

        self.clan_lineEdit = QLineEdit(self.layoutWidget_3)
        self.clan_lineEdit.setObjectName(u"clan_lineEdit")

        self.horizontalLayout.addWidget(self.clan_lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.level_label = QLabel(self.layoutWidget_3)
        self.level_label.setObjectName(u"level_label")

        self.horizontalLayout_2.addWidget(self.level_label)

        self.level_spinBox = QSpinBox(self.layoutWidget_3)
        self.level_spinBox.setObjectName(u"level_spinBox")
        self.level_spinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.level_spinBox.setMinimum(1)
        self.level_spinBox.setMaximum(10)

        self.horizontalLayout_2.addWidget(self.level_spinBox)

        self.exp_label = QLabel(self.layoutWidget_3)
        self.exp_label.setObjectName(u"exp_label")

        self.horizontalLayout_2.addWidget(self.exp_label)

        self.exp_spinBox = QSpinBox(self.layoutWidget_3)
        self.exp_spinBox.setObjectName(u"exp_spinBox")
        self.exp_spinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.exp_spinBox.setMaximum(1305)

        self.horizontalLayout_2.addWidget(self.exp_spinBox)

        self.fame_label = QLabel(self.layoutWidget_3)
        self.fame_label.setObjectName(u"fame_label")

        self.horizontalLayout_2.addWidget(self.fame_label)

        self.fame_spinBox = QSpinBox(self.layoutWidget_3)
        self.fame_spinBox.setObjectName(u"fame_spinBox")
        self.fame_spinBox.setReadOnly(True)
        self.fame_spinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.fame_spinBox.setMaximum(100)

        self.horizontalLayout_2.addWidget(self.fame_spinBox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.faith_label = QLabel(self.layoutWidget_3)
        self.faith_label.setObjectName(u"faith_label")

        self.horizontalLayout_3.addWidget(self.faith_label)

        self.faith_lineEdit = QLineEdit(self.layoutWidget_3)
        self.faith_lineEdit.setObjectName(u"faith_lineEdit")

        self.horizontalLayout_3.addWidget(self.faith_lineEdit)

        self.fate_label = QLabel(self.layoutWidget_3)
        self.fate_label.setObjectName(u"fate_label")

        self.horizontalLayout_3.addWidget(self.fate_label)

        self.fate_spinBox = QSpinBox(self.layoutWidget_3)
        self.fate_spinBox.setObjectName(u"fate_spinBox")
        self.fate_spinBox.setMaximum(5)

        self.horizontalLayout_3.addWidget(self.fate_spinBox)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.skills_groupBox = QGroupBox(self.character_sheet_toolBoxPage1)
        self.skills_groupBox.setObjectName(u"skills_groupBox")
        self.skills_groupBox.setGeometry(QRect(390, 130, 551, 361))
        self.skills_tableWidget = QTableWidget(self.skills_groupBox)
        if (self.skills_tableWidget.columnCount() < 5):
            self.skills_tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.skills_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.skills_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.skills_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.skills_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.skills_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.skills_tableWidget.setObjectName(u"skills_tableWidget")
        self.skills_tableWidget.setGeometry(QRect(10, 20, 531, 311))
        self.skills_tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.skills_tableWidget.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.skills_tableWidget.setCornerButtonEnabled(True)
        self.skills_tableWidget.setRowCount(0)
        self.skills_tableWidget.setSupportedDragActions(Qt.DropAction.MoveAction)
        self.add_skill_pushButton = QPushButton(self.skills_groupBox)
        self.add_skill_pushButton.setObjectName(u"add_skill_pushButton")
        self.add_skill_pushButton.setGeometry(QRect(10, 330, 151, 26))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListAdd))
        self.add_skill_pushButton.setIcon(icon)
        self.remove_skill_pushButton = QPushButton(self.skills_groupBox)
        self.remove_skill_pushButton.setObjectName(u"remove_skill_pushButton")
        self.remove_skill_pushButton.setGeometry(QRect(160, 330, 121, 26))
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListRemove))
        self.remove_skill_pushButton.setIcon(icon1)
        self.character_sheet_toolBox.addItem(self.character_sheet_toolBoxPage1, u"Alap inform\u00e1ci\u00f3k")
        self.character_sheet_toolBoxPage2 = QWidget()
        self.character_sheet_toolBoxPage2.setObjectName(u"character_sheet_toolBoxPage2")
        self.character_sheet_toolBoxPage2.setGeometry(QRect(0, 0, 96, 26))
        self.abilities_groupBox = QGroupBox(self.character_sheet_toolBoxPage2)
        self.abilities_groupBox.setObjectName(u"abilities_groupBox")
        self.abilities_groupBox.setGeometry(QRect(0, 270, 291, 221))
        self.abilites_listWidget = QListWidget(self.abilities_groupBox)
        self.abilites_listWidget.setObjectName(u"abilites_listWidget")
        self.abilites_listWidget.setGeometry(QRect(10, 20, 271, 171))
        self.abilites_listWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.add_ability_pushButton = QPushButton(self.abilities_groupBox)
        self.add_ability_pushButton.setObjectName(u"add_ability_pushButton")
        self.add_ability_pushButton.setGeometry(QRect(10, 190, 151, 26))
        self.add_ability_pushButton.setIcon(icon)
        self.remove_ability_pushButton = QPushButton(self.abilities_groupBox)
        self.remove_ability_pushButton.setObjectName(u"remove_ability_pushButton")
        self.remove_ability_pushButton.setGeometry(QRect(160, 190, 121, 26))
        self.remove_ability_pushButton.setIcon(icon1)
        self.initiative_groupBox = QGroupBox(self.character_sheet_toolBoxPage2)
        self.initiative_groupBox.setObjectName(u"initiative_groupBox")
        self.initiative_groupBox.setGeometry(QRect(0, 10, 291, 51))
        self.layoutWidget_4 = QWidget(self.initiative_groupBox)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(10, 20, 275, 26))
        self.horizontalLayout_12 = QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.initiative_base_label = QLabel(self.layoutWidget_4)
        self.initiative_base_label.setObjectName(u"initiative_base_label")

        self.horizontalLayout_12.addWidget(self.initiative_base_label)

        self.initiative_base_spinBox = QSpinBox(self.layoutWidget_4)
        self.initiative_base_spinBox.setObjectName(u"initiative_base_spinBox")
        self.initiative_base_spinBox.setReadOnly(True)
        self.initiative_base_spinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.initiative_base_spinBox.setMinimum(-10)

        self.horizontalLayout_12.addWidget(self.initiative_base_spinBox)

        self.initiative_other_label = QLabel(self.layoutWidget_4)
        self.initiative_other_label.setObjectName(u"initiative_other_label")

        self.horizontalLayout_12.addWidget(self.initiative_other_label)

        self.initiative_other_spinBox = QSpinBox(self.layoutWidget_4)
        self.initiative_other_spinBox.setObjectName(u"initiative_other_spinBox")
        self.initiative_other_spinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.initiative_other_spinBox.setMinimum(-10)

        self.horizontalLayout_12.addWidget(self.initiative_other_spinBox)

        self.initiative_all_label = QLabel(self.layoutWidget_4)
        self.initiative_all_label.setObjectName(u"initiative_all_label")

        self.horizontalLayout_12.addWidget(self.initiative_all_label)

        self.initiative_all_spinBox = QSpinBox(self.layoutWidget_4)
        self.initiative_all_spinBox.setObjectName(u"initiative_all_spinBox")
        self.initiative_all_spinBox.setReadOnly(True)
        self.initiative_all_spinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.initiative_all_spinBox.setMinimum(-10)

        self.horizontalLayout_12.addWidget(self.initiative_all_spinBox)

        self.defense_groupBox = QGroupBox(self.character_sheet_toolBoxPage2)
        self.defense_groupBox.setObjectName(u"defense_groupBox")
        self.defense_groupBox.setGeometry(QRect(0, 60, 291, 91))
        self.layoutWidget_5 = QWidget(self.defense_groupBox)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(9, 20, 290, 60))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.defense_base_label = QLabel(self.layoutWidget_5)
        self.defense_base_label.setObjectName(u"defense_base_label")

        self.horizontalLayout_14.addWidget(self.defense_base_label)

        self.defense_base_spinBox = QSpinBox(self.layoutWidget_5)
        self.defense_base_spinBox.setObjectName(u"defense_base_spinBox")
        self.defense_base_spinBox.setReadOnly(True)
        self.defense_base_spinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.defense_base_spinBox.setMinimum(-10)

        self.horizontalLayout_14.addWidget(self.defense_base_spinBox)

        self.defense_shield_label = QLabel(self.layoutWidget_5)
        self.defense_shield_label.setObjectName(u"defense_shield_label")

        self.horizontalLayout_14.addWidget(self.defense_shield_label)

        self.defense_shield_spinBox = QSpinBox(self.layoutWidget_5)
        self.defense_shield_spinBox.setObjectName(u"defense_shield_spinBox")

        self.horizontalLayout_14.addWidget(self.defense_shield_spinBox)

        self.defense_other_label = QLabel(self.layoutWidget_5)
        self.defense_other_label.setObjectName(u"defense_other_label")

        self.horizontalLayout_14.addWidget(self.defense_other_label)

        self.defense_other_spinBox = QSpinBox(self.layoutWidget_5)
        self.defense_other_spinBox.setObjectName(u"defense_other_spinBox")

        self.horizontalLayout_14.addWidget(self.defense_other_spinBox)


        self.verticalLayout_5.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.defense_all_label = QLabel(self.layoutWidget_5)
        self.defense_all_label.setObjectName(u"defense_all_label")

        self.horizontalLayout_15.addWidget(self.defense_all_label)

        self.defense_all_spinBox = QSpinBox(self.layoutWidget_5)
        self.defense_all_spinBox.setObjectName(u"defense_all_spinBox")
        self.defense_all_spinBox.setReadOnly(True)
        self.defense_all_spinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)

        self.horizontalLayout_15.addWidget(self.defense_all_spinBox)


        self.verticalLayout_5.addLayout(self.horizontalLayout_15)

        self.armor_shield_groupBox = QGroupBox(self.character_sheet_toolBoxPage2)
        self.armor_shield_groupBox.setObjectName(u"armor_shield_groupBox")
        self.armor_shield_groupBox.setGeometry(QRect(0, 150, 291, 121))
        self.layoutWidget_6 = QWidget(self.armor_shield_groupBox)
        self.layoutWidget_6.setObjectName(u"layoutWidget_6")
        self.layoutWidget_6.setGeometry(QRect(10, 20, 271, 92))
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.armor_label = QLabel(self.layoutWidget_6)
        self.armor_label.setObjectName(u"armor_label")

        self.horizontalLayout_16.addWidget(self.armor_label)

        self.armor_lineEdit = QLineEdit(self.layoutWidget_6)
        self.armor_lineEdit.setObjectName(u"armor_lineEdit")

        self.horizontalLayout_16.addWidget(self.armor_lineEdit)

        self.armor_rating_label = QLabel(self.layoutWidget_6)
        self.armor_rating_label.setObjectName(u"armor_rating_label")

        self.horizontalLayout_16.addWidget(self.armor_rating_label)

        self.armor_rating_spinBox = QSpinBox(self.layoutWidget_6)
        self.armor_rating_spinBox.setObjectName(u"armor_rating_spinBox")

        self.horizontalLayout_16.addWidget(self.armor_rating_spinBox)


        self.verticalLayout_6.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.helmet_label = QLabel(self.layoutWidget_6)
        self.helmet_label.setObjectName(u"helmet_label")

        self.horizontalLayout_17.addWidget(self.helmet_label)

        self.helmet_lineEdit = QLineEdit(self.layoutWidget_6)
        self.helmet_lineEdit.setObjectName(u"helmet_lineEdit")

        self.horizontalLayout_17.addWidget(self.helmet_lineEdit)

        self.helmet_rating_label = QLabel(self.layoutWidget_6)
        self.helmet_rating_label.setObjectName(u"helmet_rating_label")

        self.horizontalLayout_17.addWidget(self.helmet_rating_label)

        self.helmet_rating_spinBox = QSpinBox(self.layoutWidget_6)
        self.helmet_rating_spinBox.setObjectName(u"helmet_rating_spinBox")

        self.horizontalLayout_17.addWidget(self.helmet_rating_spinBox)


        self.verticalLayout_6.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.shield_label = QLabel(self.layoutWidget_6)
        self.shield_label.setObjectName(u"shield_label")

        self.horizontalLayout_18.addWidget(self.shield_label)

        self.shield_lineEdit = QLineEdit(self.layoutWidget_6)
        self.shield_lineEdit.setObjectName(u"shield_lineEdit")

        self.horizontalLayout_18.addWidget(self.shield_lineEdit)

        self.shield_break_label = QLabel(self.layoutWidget_6)
        self.shield_break_label.setObjectName(u"shield_break_label")

        self.horizontalLayout_18.addWidget(self.shield_break_label)

        self.shield_break_spinBox = QSpinBox(self.layoutWidget_6)
        self.shield_break_spinBox.setObjectName(u"shield_break_spinBox")

        self.horizontalLayout_18.addWidget(self.shield_break_spinBox)


        self.verticalLayout_6.addLayout(self.horizontalLayout_18)

        self.attack_groupBox = QGroupBox(self.character_sheet_toolBoxPage2)
        self.attack_groupBox.setObjectName(u"attack_groupBox")
        self.attack_groupBox.setGeometry(QRect(300, 10, 641, 341))
        self.layoutWidget_7 = QWidget(self.attack_groupBox)
        self.layoutWidget_7.setObjectName(u"layoutWidget_7")
        self.layoutWidget_7.setGeometry(QRect(10, 20, 268, 26))
        self.horizontalLayout_13 = QHBoxLayout(self.layoutWidget_7)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.close_combat_attack_label = QLabel(self.layoutWidget_7)
        self.close_combat_attack_label.setObjectName(u"close_combat_attack_label")

        self.horizontalLayout_13.addWidget(self.close_combat_attack_label)

        self.close_combat_attack_spinBox = QSpinBox(self.layoutWidget_7)
        self.close_combat_attack_spinBox.setObjectName(u"close_combat_attack_spinBox")
        self.close_combat_attack_spinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.close_combat_attack_spinBox.setMinimum(-10)

        self.horizontalLayout_13.addWidget(self.close_combat_attack_spinBox)

        self.ranged_combat_attack_label = QLabel(self.layoutWidget_7)
        self.ranged_combat_attack_label.setObjectName(u"ranged_combat_attack_label")

        self.horizontalLayout_13.addWidget(self.ranged_combat_attack_label)

        self.ranged_combat_attack_spinBox = QSpinBox(self.layoutWidget_7)
        self.ranged_combat_attack_spinBox.setObjectName(u"ranged_combat_attack_spinBox")
        self.ranged_combat_attack_spinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.ranged_combat_attack_spinBox.setMinimum(-10)
        self.ranged_combat_attack_spinBox.setMaximum(103)

        self.horizontalLayout_13.addWidget(self.ranged_combat_attack_spinBox)

        self.weapons_tableWidget = QTableWidget(self.attack_groupBox)
        if (self.weapons_tableWidget.columnCount() < 5):
            self.weapons_tableWidget.setColumnCount(5)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.weapons_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.weapons_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.weapons_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.weapons_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.weapons_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        self.weapons_tableWidget.setObjectName(u"weapons_tableWidget")
        self.weapons_tableWidget.setGeometry(QRect(10, 50, 621, 261))
        self.weapons_tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.weapons_tableWidget.setSupportedDragActions(Qt.DropAction.MoveAction)
        self.add_weapon_pushButton = QPushButton(self.attack_groupBox)
        self.add_weapon_pushButton.setObjectName(u"add_weapon_pushButton")
        self.add_weapon_pushButton.setGeometry(QRect(10, 310, 141, 26))
        self.add_weapon_pushButton.setIcon(icon)
        self.remove_weapon_pushButton = QPushButton(self.attack_groupBox)
        self.remove_weapon_pushButton.setObjectName(u"remove_weapon_pushButton")
        self.remove_weapon_pushButton.setGeometry(QRect(150, 310, 121, 26))
        self.remove_weapon_pushButton.setIcon(icon1)
        self.save_groupBox = QGroupBox(self.character_sheet_toolBoxPage2)
        self.save_groupBox.setObjectName(u"save_groupBox")
        self.save_groupBox.setGeometry(QRect(300, 350, 301, 141))
        self.layoutWidget_8 = QWidget(self.save_groupBox)
        self.layoutWidget_8.setObjectName(u"layoutWidget_8")
        self.layoutWidget_8.setGeometry(QRect(10, 20, 285, 111))
        self.gridLayout = QGridLayout(self.layoutWidget_8)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.willpower_save_base_spinBox = QSpinBox(self.layoutWidget_8)
        self.willpower_save_base_spinBox.setObjectName(u"willpower_save_base_spinBox")
        self.willpower_save_base_spinBox.setReadOnly(True)
        self.willpower_save_base_spinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.willpower_save_base_spinBox.setMinimum(-10)

        self.gridLayout.addWidget(self.willpower_save_base_spinBox, 7, 1, 1, 1)

        self.constitution_save_other_spinBox = QSpinBox(self.layoutWidget_8)
        self.constitution_save_other_spinBox.setObjectName(u"constitution_save_other_spinBox")
        self.constitution_save_other_spinBox.setMinimum(-10)

        self.gridLayout.addWidget(self.constitution_save_other_spinBox, 3, 3, 1, 1)

        self.reflex_save_other_spinBox = QSpinBox(self.layoutWidget_8)
        self.reflex_save_other_spinBox.setObjectName(u"reflex_save_other_spinBox")
        self.reflex_save_other_spinBox.setMinimum(-10)

        self.gridLayout.addWidget(self.reflex_save_other_spinBox, 4, 3, 1, 1)

        self.reflex_save_base_spinBox = QSpinBox(self.layoutWidget_8)
        self.reflex_save_base_spinBox.setObjectName(u"reflex_save_base_spinBox")
        self.reflex_save_base_spinBox.setReadOnly(True)
        self.reflex_save_base_spinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.reflex_save_base_spinBox.setMinimum(-10)

        self.gridLayout.addWidget(self.reflex_save_base_spinBox, 4, 1, 1, 1)

        self.reflex_save_label = QLabel(self.layoutWidget_8)
        self.reflex_save_label.setObjectName(u"reflex_save_label")

        self.gridLayout.addWidget(self.reflex_save_label, 4, 0, 1, 1)

        self.save_all_label = QLabel(self.layoutWidget_8)
        self.save_all_label.setObjectName(u"save_all_label")

        self.gridLayout.addWidget(self.save_all_label, 1, 4, 1, 1)

        self.save_other_label = QLabel(self.layoutWidget_8)
        self.save_other_label.setObjectName(u"save_other_label")

        self.gridLayout.addWidget(self.save_other_label, 1, 3, 1, 1)

        self.constitution_save_label = QLabel(self.layoutWidget_8)
        self.constitution_save_label.setObjectName(u"constitution_save_label")

        self.gridLayout.addWidget(self.constitution_save_label, 3, 0, 1, 1)

        self.constitution_save_all_spinBox = QSpinBox(self.layoutWidget_8)
        self.constitution_save_all_spinBox.setObjectName(u"constitution_save_all_spinBox")
        self.constitution_save_all_spinBox.setReadOnly(True)
        self.constitution_save_all_spinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.constitution_save_all_spinBox.setMinimum(-10)

        self.gridLayout.addWidget(self.constitution_save_all_spinBox, 3, 4, 1, 1)

        self.constitution_save_base_spinBox = QSpinBox(self.layoutWidget_8)
        self.constitution_save_base_spinBox.setObjectName(u"constitution_save_base_spinBox")
        self.constitution_save_base_spinBox.setReadOnly(True)
        self.constitution_save_base_spinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.constitution_save_base_spinBox.setMinimum(-10)

        self.gridLayout.addWidget(self.constitution_save_base_spinBox, 3, 1, 1, 1)

        self.willpower_save_label = QLabel(self.layoutWidget_8)
        self.willpower_save_label.setObjectName(u"willpower_save_label")

        self.gridLayout.addWidget(self.willpower_save_label, 7, 0, 1, 1)

        self.willpower_save_other_spinBox = QSpinBox(self.layoutWidget_8)
        self.willpower_save_other_spinBox.setObjectName(u"willpower_save_other_spinBox")
        self.willpower_save_other_spinBox.setMinimum(-10)

        self.gridLayout.addWidget(self.willpower_save_other_spinBox, 7, 3, 1, 1)

        self.reflex_save_all_spinBox = QSpinBox(self.layoutWidget_8)
        self.reflex_save_all_spinBox.setObjectName(u"reflex_save_all_spinBox")
        self.reflex_save_all_spinBox.setReadOnly(True)
        self.reflex_save_all_spinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.reflex_save_all_spinBox.setMinimum(-10)

        self.gridLayout.addWidget(self.reflex_save_all_spinBox, 4, 4, 1, 1)

        self.willpower_save_all_spinBox = QSpinBox(self.layoutWidget_8)
        self.willpower_save_all_spinBox.setObjectName(u"willpower_save_all_spinBox")
        self.willpower_save_all_spinBox.setReadOnly(True)
        self.willpower_save_all_spinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.willpower_save_all_spinBox.setMinimum(-10)

        self.gridLayout.addWidget(self.willpower_save_all_spinBox, 7, 4, 1, 1)

        self.save_base_label = QLabel(self.layoutWidget_8)
        self.save_base_label.setObjectName(u"save_base_label")

        self.gridLayout.addWidget(self.save_base_label, 1, 1, 1, 1)

        self.character_sheet_toolBox.addItem(self.character_sheet_toolBoxPage2, u"Kezdem\u00e9nyez\u0151, T\u00e1mad\u00f3, V\u00e9d\u0151, Ment\u0151dob\u00e1sok \u00e9s K\u00e9pess\u00e9gek")
        self.character_sheet_toolBoxPage3 = QWidget()
        self.character_sheet_toolBoxPage3.setObjectName(u"character_sheet_toolBoxPage3")
        self.character_sheet_toolBoxPage3.setGeometry(QRect(0, 0, 96, 26))
        self.equipment_money_groupBox = QGroupBox(self.character_sheet_toolBoxPage3)
        self.equipment_money_groupBox.setObjectName(u"equipment_money_groupBox")
        self.equipment_money_groupBox.setGeometry(QRect(0, 10, 941, 251))
        self.layoutWidget1 = QWidget(self.equipment_money_groupBox)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(850, 20, 77, 104))
        self.verticalLayout_10 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.money_silver_label = QLabel(self.layoutWidget1)
        self.money_silver_label.setObjectName(u"money_silver_label")

        self.verticalLayout_9.addWidget(self.money_silver_label)

        self.money_silver_spinBox = QSpinBox(self.layoutWidget1)
        self.money_silver_spinBox.setObjectName(u"money_silver_spinBox")
        self.money_silver_spinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.money_silver_spinBox.setMaximum(999)

        self.verticalLayout_9.addWidget(self.money_silver_spinBox)


        self.verticalLayout_10.addLayout(self.verticalLayout_9)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.money_iron_label = QLabel(self.layoutWidget1)
        self.money_iron_label.setObjectName(u"money_iron_label")

        self.verticalLayout_8.addWidget(self.money_iron_label)

        self.money_iron_spinBox = QSpinBox(self.layoutWidget1)
        self.money_iron_spinBox.setObjectName(u"money_iron_spinBox")
        self.money_iron_spinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.money_iron_spinBox.setMaximum(999)

        self.verticalLayout_8.addWidget(self.money_iron_spinBox)


        self.verticalLayout_10.addLayout(self.verticalLayout_8)

        self.layoutWidget2 = QWidget(self.equipment_money_groupBox)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(610, 20, 231, 201))
        self.verticalLayout_7 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.small_item_label = QLabel(self.layoutWidget2)
        self.small_item_label.setObjectName(u"small_item_label")

        self.verticalLayout_7.addWidget(self.small_item_label)

        self.small_items_listWidget = QListWidget(self.layoutWidget2)
        self.small_items_listWidget.setObjectName(u"small_items_listWidget")

        self.verticalLayout_7.addWidget(self.small_items_listWidget)

        self.equipment_tableWidget = QTableWidget(self.equipment_money_groupBox)
        if (self.equipment_tableWidget.columnCount() < 3):
            self.equipment_tableWidget.setColumnCount(3)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.equipment_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.equipment_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.equipment_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        self.equipment_tableWidget.setObjectName(u"equipment_tableWidget")
        self.equipment_tableWidget.setGeometry(QRect(10, 20, 591, 201))
        self.equipment_tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.equipment_tableWidget.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.equipment_tableWidget.setSupportedDragActions(Qt.DropAction.MoveAction)
        self.add_equipment_pushButton = QPushButton(self.equipment_money_groupBox)
        self.add_equipment_pushButton.setObjectName(u"add_equipment_pushButton")
        self.add_equipment_pushButton.setGeometry(QRect(10, 220, 161, 26))
        self.add_equipment_pushButton.setIcon(icon)
        self.remove_equipment_pushButton = QPushButton(self.equipment_money_groupBox)
        self.remove_equipment_pushButton.setObjectName(u"remove_equipment_pushButton")
        self.remove_equipment_pushButton.setGeometry(QRect(170, 220, 131, 26))
        self.remove_equipment_pushButton.setIcon(icon1)
        self.add_small_item_pushButton = QPushButton(self.equipment_money_groupBox)
        self.add_small_item_pushButton.setObjectName(u"add_small_item_pushButton")
        self.add_small_item_pushButton.setGeometry(QRect(610, 220, 131, 26))
        self.add_small_item_pushButton.setIcon(icon)
        self.remove_small_item_pushButton = QPushButton(self.equipment_money_groupBox)
        self.remove_small_item_pushButton.setObjectName(u"remove_small_item_pushButton")
        self.remove_small_item_pushButton.setGeometry(QRect(740, 220, 101, 26))
        self.remove_small_item_pushButton.setIcon(icon1)
        self.layoutWidget3 = QWidget(self.equipment_money_groupBox)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(420, 220, 180, 26))
        self.horizontalLayout_20 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.encumbrance_label = QLabel(self.layoutWidget3)
        self.encumbrance_label.setObjectName(u"encumbrance_label")

        self.horizontalLayout_20.addWidget(self.encumbrance_label)

        self.current_encumbrance_doubleSpinBox = QDoubleSpinBox(self.layoutWidget3)
        self.current_encumbrance_doubleSpinBox.setObjectName(u"current_encumbrance_doubleSpinBox")
        self.current_encumbrance_doubleSpinBox.setReadOnly(True)
        self.current_encumbrance_doubleSpinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)

        self.horizontalLayout_20.addWidget(self.current_encumbrance_doubleSpinBox)

        self.slash_separator_label = QLabel(self.layoutWidget3)
        self.slash_separator_label.setObjectName(u"slash_separator_label")

        self.horizontalLayout_20.addWidget(self.slash_separator_label)

        self.max_encumbrance_doubleSpinBox = QDoubleSpinBox(self.layoutWidget3)
        self.max_encumbrance_doubleSpinBox.setObjectName(u"max_encumbrance_doubleSpinBox")
        self.max_encumbrance_doubleSpinBox.setReadOnly(True)
        self.max_encumbrance_doubleSpinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.max_encumbrance_doubleSpinBox.setProperty(u"showGroupSeparator", False)

        self.horizontalLayout_20.addWidget(self.max_encumbrance_doubleSpinBox)

        self.fame_groupBox = QGroupBox(self.character_sheet_toolBoxPage3)
        self.fame_groupBox.setObjectName(u"fame_groupBox")
        self.fame_groupBox.setGeometry(QRect(0, 260, 941, 231))
        self.fame_tableWidget = QTableWidget(self.fame_groupBox)
        if (self.fame_tableWidget.columnCount() < 3):
            self.fame_tableWidget.setColumnCount(3)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.fame_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.fame_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.fame_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem15)
        self.fame_tableWidget.setObjectName(u"fame_tableWidget")
        self.fame_tableWidget.setGeometry(QRect(10, 20, 771, 201))
        self.fame_tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.fame_tableWidget.setSupportedDragActions(Qt.DropAction.MoveAction)
        self.add_fame_pushButton = QPushButton(self.fame_groupBox)
        self.add_fame_pushButton.setObjectName(u"add_fame_pushButton")
        self.add_fame_pushButton.setGeometry(QRect(780, 20, 141, 26))
        self.add_fame_pushButton.setIcon(icon)
        self.remove_fame_pushButton = QPushButton(self.fame_groupBox)
        self.remove_fame_pushButton.setObjectName(u"remove_fame_pushButton")
        self.remove_fame_pushButton.setGeometry(QRect(780, 50, 141, 26))
        self.remove_fame_pushButton.setIcon(icon1)
        self.character_sheet_toolBox.addItem(self.character_sheet_toolBoxPage3, u"Felszerel\u00e9s, p\u00e9nz \u00e9s h\u00edrn\u00e9v")
        self.character_sheet_toolBoxPage4 = QWidget()
        self.character_sheet_toolBoxPage4.setObjectName(u"character_sheet_toolBoxPage4")
        self.character_sheet_toolBoxPage4.setGeometry(QRect(0, 0, 96, 26))
        self.magic_groupBox = QGroupBox(self.character_sheet_toolBoxPage4)
        self.magic_groupBox.setObjectName(u"magic_groupBox")
        self.magic_groupBox.setGeometry(QRect(0, 10, 941, 481))
        self.gridLayoutWidget = QWidget(self.magic_groupBox)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 20, 301, 80))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.max_level_2_spinBox = QSpinBox(self.gridLayoutWidget)
        self.max_level_2_spinBox.setObjectName(u"max_level_2_spinBox")
        self.max_level_2_spinBox.setReadOnly(True)
        self.max_level_2_spinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)

        self.gridLayout_2.addWidget(self.max_level_2_spinBox, 1, 2, 1, 1)

        self.available_spells_label = QLabel(self.gridLayoutWidget)
        self.available_spells_label.setObjectName(u"available_spells_label")

        self.gridLayout_2.addWidget(self.available_spells_label, 2, 0, 1, 1)

        self.max_spells_label = QLabel(self.gridLayoutWidget)
        self.max_spells_label.setObjectName(u"max_spells_label")

        self.gridLayout_2.addWidget(self.max_spells_label, 1, 0, 1, 1)

        self.max_level_1_spinBox = QSpinBox(self.gridLayoutWidget)
        self.max_level_1_spinBox.setObjectName(u"max_level_1_spinBox")
        self.max_level_1_spinBox.setReadOnly(True)
        self.max_level_1_spinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)

        self.gridLayout_2.addWidget(self.max_level_1_spinBox, 1, 1, 1, 1)

        self.max_level_3_spinBox = QSpinBox(self.gridLayoutWidget)
        self.max_level_3_spinBox.setObjectName(u"max_level_3_spinBox")
        self.max_level_3_spinBox.setReadOnly(True)
        self.max_level_3_spinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)

        self.gridLayout_2.addWidget(self.max_level_3_spinBox, 1, 3, 1, 1)

        self.level_3_label = QLabel(self.gridLayoutWidget)
        self.level_3_label.setObjectName(u"level_3_label")

        self.gridLayout_2.addWidget(self.level_3_label, 0, 3, 1, 1)

        self.level_2_label = QLabel(self.gridLayoutWidget)
        self.level_2_label.setObjectName(u"level_2_label")

        self.gridLayout_2.addWidget(self.level_2_label, 0, 2, 1, 1)

        self.level_1_label = QLabel(self.gridLayoutWidget)
        self.level_1_label.setObjectName(u"level_1_label")

        self.gridLayout_2.addWidget(self.level_1_label, 0, 1, 1, 1)

        self.available_level_1_spinBox = QSpinBox(self.gridLayoutWidget)
        self.available_level_1_spinBox.setObjectName(u"available_level_1_spinBox")

        self.gridLayout_2.addWidget(self.available_level_1_spinBox, 2, 1, 1, 1)

        self.available_level_2_spinBox = QSpinBox(self.gridLayoutWidget)
        self.available_level_2_spinBox.setObjectName(u"available_level_2_spinBox")

        self.gridLayout_2.addWidget(self.available_level_2_spinBox, 2, 2, 1, 1)

        self.available_level_3_spinBox = QSpinBox(self.gridLayoutWidget)
        self.available_level_3_spinBox.setObjectName(u"available_level_3_spinBox")

        self.gridLayout_2.addWidget(self.available_level_3_spinBox, 2, 3, 1, 1)

        self.layoutWidget_9 = QWidget(self.magic_groupBox)
        self.layoutWidget_9.setObjectName(u"layoutWidget_9")
        self.layoutWidget_9.setGeometry(QRect(320, 10, 611, 461))
        self.verticalLayout_11 = QVBoxLayout(self.layoutWidget_9)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.spell_list_label = QLabel(self.layoutWidget_9)
        self.spell_list_label.setObjectName(u"spell_list_label")

        self.verticalLayout_11.addWidget(self.spell_list_label)

        self.spell_list_tableWidget = QTableWidget(self.layoutWidget_9)
        if (self.spell_list_tableWidget.columnCount() < 3):
            self.spell_list_tableWidget.setColumnCount(3)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.spell_list_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.spell_list_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.spell_list_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem18)
        self.spell_list_tableWidget.setObjectName(u"spell_list_tableWidget")
        self.spell_list_tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        self.verticalLayout_11.addWidget(self.spell_list_tableWidget)

        self.add_spell_pushButton = QPushButton(self.magic_groupBox)
        self.add_spell_pushButton.setObjectName(u"add_spell_pushButton")
        self.add_spell_pushButton.setGeometry(QRect(160, 420, 151, 26))
        self.add_spell_pushButton.setIcon(icon)
        self.remove_spell_pushButton = QPushButton(self.magic_groupBox)
        self.remove_spell_pushButton.setObjectName(u"remove_spell_pushButton")
        self.remove_spell_pushButton.setGeometry(QRect(190, 450, 121, 26))
        self.remove_spell_pushButton.setIcon(icon1)
        self.character_sheet_toolBox.addItem(self.character_sheet_toolBoxPage4, u"M\u00e1gia")
        self.roll_history_listWidget = QListWidget(CharacterSheet)
        self.roll_history_listWidget.setObjectName(u"roll_history_listWidget")
        self.roll_history_listWidget.setGeometry(QRect(0, 620, 381, 171))
        self.roll_history_listWidget.setAutoScroll(True)
        self.roll_history_listWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.dice_roller_groupBox = QGroupBox(CharacterSheet)
        self.dice_roller_groupBox.setObjectName(u"dice_roller_groupBox")
        self.dice_roller_groupBox.setGeometry(QRect(640, 700, 301, 91))
        self.dice_roll_pushButton = QPushButton(self.dice_roller_groupBox)
        self.dice_roll_pushButton.setObjectName(u"dice_roll_pushButton")
        self.dice_roll_pushButton.setGeometry(QRect(100, 60, 81, 26))
        self.layoutWidget4 = QWidget(self.dice_roller_groupBox)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(10, 20, 281, 26))
        self.horizontalLayout_24 = QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.dice_number_spinBox = QSpinBox(self.layoutWidget4)
        self.dice_number_spinBox.setObjectName(u"dice_number_spinBox")
        self.dice_number_spinBox.setMinimum(1)

        self.horizontalLayout_24.addWidget(self.dice_number_spinBox)

        self.dice_sign_label = QLabel(self.layoutWidget4)
        self.dice_sign_label.setObjectName(u"dice_sign_label")
        font1 = QFont()
        font1.setBold(True)
        self.dice_sign_label.setFont(font1)
        self.dice_sign_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_24.addWidget(self.dice_sign_label)

        self.dice_side_spinBox = QSpinBox(self.layoutWidget4)
        self.dice_side_spinBox.setObjectName(u"dice_side_spinBox")
        self.dice_side_spinBox.setMinimum(2)
        self.dice_side_spinBox.setMaximum(100)
        self.dice_side_spinBox.setValue(6)

        self.horizontalLayout_24.addWidget(self.dice_side_spinBox)

        self.plus_sign_label = QLabel(self.layoutWidget4)
        self.plus_sign_label.setObjectName(u"plus_sign_label")
        self.plus_sign_label.setFont(font1)
        self.plus_sign_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_24.addWidget(self.plus_sign_label)

        self.dice_modifier_spinBox = QSpinBox(self.layoutWidget4)
        self.dice_modifier_spinBox.setObjectName(u"dice_modifier_spinBox")
        self.dice_modifier_spinBox.setMinimum(-20)

        self.horizontalLayout_24.addWidget(self.dice_modifier_spinBox)

        self.layoutWidget5 = QWidget(CharacterSheet)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.layoutWidget5.setGeometry(QRect(390, 620, 241, 166))
        self.verticalLayout_12 = QVBoxLayout(self.layoutWidget5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.attack_test_comboBox = QComboBox(self.layoutWidget5)
        self.attack_test_comboBox.setObjectName(u"attack_test_comboBox")

        self.horizontalLayout_19.addWidget(self.attack_test_comboBox)

        self.attack_test_pushButton = QPushButton(self.layoutWidget5)
        self.attack_test_pushButton.setObjectName(u"attack_test_pushButton")

        self.horizontalLayout_19.addWidget(self.attack_test_pushButton)


        self.verticalLayout_12.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.defense_test_comboBox = QComboBox(self.layoutWidget5)
        self.defense_test_comboBox.setObjectName(u"defense_test_comboBox")

        self.horizontalLayout_21.addWidget(self.defense_test_comboBox)

        self.defense_test_pushButton = QPushButton(self.layoutWidget5)
        self.defense_test_pushButton.setObjectName(u"defense_test_pushButton")

        self.horizontalLayout_21.addWidget(self.defense_test_pushButton)


        self.verticalLayout_12.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.attribute_test_comboBox = QComboBox(self.layoutWidget5)
        self.attribute_test_comboBox.setObjectName(u"attribute_test_comboBox")

        self.horizontalLayout_22.addWidget(self.attribute_test_comboBox)

        self.attribute_test_pushButton = QPushButton(self.layoutWidget5)
        self.attribute_test_pushButton.setObjectName(u"attribute_test_pushButton")

        self.horizontalLayout_22.addWidget(self.attribute_test_pushButton)


        self.verticalLayout_12.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.skill_test_comboBox = QComboBox(self.layoutWidget5)
        self.skill_test_comboBox.setObjectName(u"skill_test_comboBox")

        self.horizontalLayout_23.addWidget(self.skill_test_comboBox)

        self.skill_test_pushButton = QPushButton(self.layoutWidget5)
        self.skill_test_pushButton.setObjectName(u"skill_test_pushButton")

        self.horizontalLayout_23.addWidget(self.skill_test_pushButton)


        self.verticalLayout_12.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.save_test_comboBox = QComboBox(self.layoutWidget5)
        self.save_test_comboBox.setObjectName(u"save_test_comboBox")

        self.horizontalLayout_25.addWidget(self.save_test_comboBox)

        self.save_test_pushButton = QPushButton(self.layoutWidget5)
        self.save_test_pushButton.setObjectName(u"save_test_pushButton")

        self.horizontalLayout_25.addWidget(self.save_test_pushButton)


        self.verticalLayout_12.addLayout(self.horizontalLayout_25)

        self.layoutWidget6 = QWidget(CharacterSheet)
        self.layoutWidget6.setObjectName(u"layoutWidget6")
        self.layoutWidget6.setGeometry(QRect(640, 620, 87, 48))
        self.verticalLayout_13 = QVBoxLayout(self.layoutWidget6)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.modifier_label = QLabel(self.layoutWidget6)
        self.modifier_label.setObjectName(u"modifier_label")
        self.modifier_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.modifier_label)

        self.modifier_spinBox = QSpinBox(self.layoutWidget6)
        self.modifier_spinBox.setObjectName(u"modifier_spinBox")
        self.modifier_spinBox.setMinimum(-20)

        self.verticalLayout_13.addWidget(self.modifier_spinBox)


        self.retranslateUi(CharacterSheet)

        QMetaObject.connectSlotsByName(CharacterSheet)
    # setupUi

    def retranslateUi(self, CharacterSheet):
        CharacterSheet.setWindowTitle(QCoreApplication.translate("CharacterSheet", u"Form", None))
        self.attributes_groupBox.setTitle(QCoreApplication.translate("CharacterSheet", u"Tulajdons\u00e1gok", None))
        self.strength_label.setText(QCoreApplication.translate("CharacterSheet", u"Er\u0151", None))
        self.strength_spinBox.setPrefix("")
        self.dexterity_label.setText(QCoreApplication.translate("CharacterSheet", u"\u00dcgyess\u00e9g", None))
        self.dexterity_spinBox.setPrefix("")
        self.stamina_label.setText(QCoreApplication.translate("CharacterSheet", u"\u00c1ll\u00f3k\u00e9pess\u00e9g", None))
        self.stamina_spinBox.setPrefix("")
        self.intelligence_label.setText(QCoreApplication.translate("CharacterSheet", u"Intelligencia", None))
        self.intelligence_spinBox.setPrefix("")
        self.wisdom_label.setText(QCoreApplication.translate("CharacterSheet", u"B\u00f6lcsess\u00e9g", None))
        self.wisdom_spinBox.setPrefix("")
        self.charisma_label.setText(QCoreApplication.translate("CharacterSheet", u"Karizma", None))
        self.charisma_spinBox.setPrefix("")
        self.health_groupBox.setTitle(QCoreApplication.translate("CharacterSheet", u"\u00c9leter\u0151 (\u00c9P)", None))
        self.health_max_label.setText(QCoreApplication.translate("CharacterSheet", u"\u00c9P max", None))
        self.cold_resistance_label.setText(QCoreApplication.translate("CharacterSheet", u"Hidegt\u0171r\u00e9s", None))
        self.background_groupBox.setTitle(QCoreApplication.translate("CharacterSheet", u"H\u00e1tt\u00e9r \u00e9s m\u00f3dos\u00edt\u00f3i", None))
        self.baseinfo_groupBox.setTitle(QCoreApplication.translate("CharacterSheet", u"Alap inform\u00e1ci\u00f3k", None))
        self.name_label.setText(QCoreApplication.translate("CharacterSheet", u"N\u00e9v", None))
        self.class_label.setText(QCoreApplication.translate("CharacterSheet", u"Oszt\u00e1ly", None))
        self.clan_label.setText(QCoreApplication.translate("CharacterSheet", u"Kl\u00e1n", None))
        self.level_label.setText(QCoreApplication.translate("CharacterSheet", u"Szint", None))
        self.exp_label.setText(QCoreApplication.translate("CharacterSheet", u"TP", None))
        self.fame_label.setText(QCoreApplication.translate("CharacterSheet", u"H\u00edrn\u00e9v", None))
        self.faith_label.setText(QCoreApplication.translate("CharacterSheet", u"Vall\u00e1s", None))
        self.fate_label.setText(QCoreApplication.translate("CharacterSheet", u"Sorspont", None))
        self.skills_groupBox.setTitle(QCoreApplication.translate("CharacterSheet", u"J\u00e1rtass\u00e1gok", None))
        ___qtablewidgetitem = self.skills_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("CharacterSheet", u"J\u00e1rtass\u00e1g", None));
        ___qtablewidgetitem1 = self.skills_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("CharacterSheet", u"Tulajdons\u00e1g", None));
        ___qtablewidgetitem2 = self.skills_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("CharacterSheet", u"Szint", None));
        ___qtablewidgetitem3 = self.skills_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("CharacterSheet", u"Egy\u00e9b", None));
        ___qtablewidgetitem4 = self.skills_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("CharacterSheet", u"\u00d6sszes", None));
        self.add_skill_pushButton.setText(QCoreApplication.translate("CharacterSheet", u"J\u00e1rtass\u00e1g hozz\u00e1ad\u00e1sa", None))
        self.remove_skill_pushButton.setText(QCoreApplication.translate("CharacterSheet", u"J\u00e1rtass\u00e1g t\u00f6rl\u00e9se", None))
        self.character_sheet_toolBox.setItemText(self.character_sheet_toolBox.indexOf(self.character_sheet_toolBoxPage1), QCoreApplication.translate("CharacterSheet", u"Alap inform\u00e1ci\u00f3k", None))
        self.abilities_groupBox.setTitle(QCoreApplication.translate("CharacterSheet", u"K\u00e9pess\u00e9gek", None))
        self.add_ability_pushButton.setText(QCoreApplication.translate("CharacterSheet", u"K\u00e9pess\u00e9g hozz\u00e1ad\u00e1sa", None))
        self.remove_ability_pushButton.setText(QCoreApplication.translate("CharacterSheet", u"K\u00e9pess\u00e9g t\u00f6rl\u00e9se", None))
        self.initiative_groupBox.setTitle(QCoreApplication.translate("CharacterSheet", u"Kezdem\u00e9nyez\u00e9s (K\u00c9)", None))
        self.initiative_base_label.setText(QCoreApplication.translate("CharacterSheet", u"Alap", None))
        self.initiative_other_label.setText(QCoreApplication.translate("CharacterSheet", u"Egy\u00e9b", None))
        self.initiative_all_label.setText(QCoreApplication.translate("CharacterSheet", u"\u00d6sszes", None))
        self.defense_groupBox.setTitle(QCoreApplication.translate("CharacterSheet", u"V\u00e9dekez\u00e9s (V\u00c9)", None))
        self.defense_base_label.setText(QCoreApplication.translate("CharacterSheet", u"Alap", None))
        self.defense_shield_label.setText(QCoreApplication.translate("CharacterSheet", u"Pajzs", None))
        self.defense_other_label.setText(QCoreApplication.translate("CharacterSheet", u"Egy\u00e9b", None))
        self.defense_all_label.setText(QCoreApplication.translate("CharacterSheet", u"\u00d6sszes", None))
        self.armor_shield_groupBox.setTitle(QCoreApplication.translate("CharacterSheet", u"P\u00e1nc\u00e9l \u00e9s Pajzs", None))
        self.armor_label.setText(QCoreApplication.translate("CharacterSheet", u"P\u00e1nc\u00e9l", None))
        self.armor_rating_label.setText(QCoreApplication.translate("CharacterSheet", u"SF\u00c9", None))
        self.helmet_label.setText(QCoreApplication.translate("CharacterSheet", u"Sisak", None))
        self.helmet_rating_label.setText(QCoreApplication.translate("CharacterSheet", u"SF\u00c9", None))
        self.shield_label.setText(QCoreApplication.translate("CharacterSheet", u"Pajzs", None))
        self.shield_break_label.setText(QCoreApplication.translate("CharacterSheet", u"T\u00f6r\u00e9s", None))
        self.attack_groupBox.setTitle(QCoreApplication.translate("CharacterSheet", u"T\u00e1mad\u00e1s (T\u00c9)", None))
        self.close_combat_attack_label.setText(QCoreApplication.translate("CharacterSheet", u"K\u00f6zelharci", None))
        self.ranged_combat_attack_label.setText(QCoreApplication.translate("CharacterSheet", u"T\u00e1vols\u00e1gi", None))
        ___qtablewidgetitem5 = self.weapons_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("CharacterSheet", u"Fegyver", None));
        ___qtablewidgetitem6 = self.weapons_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("CharacterSheet", u"Kapcsolt tulajdons\u00e1g", None));
        ___qtablewidgetitem7 = self.weapons_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("CharacterSheet", u"Kritikus", None));
        ___qtablewidgetitem8 = self.weapons_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("CharacterSheet", u"Sebz\u00e9s", None));
        ___qtablewidgetitem9 = self.weapons_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("CharacterSheet", u"Speci\u00e1lis", None));
        self.add_weapon_pushButton.setText(QCoreApplication.translate("CharacterSheet", u"Fegyver hozz\u00e1ad\u00e1sa", None))
        self.remove_weapon_pushButton.setText(QCoreApplication.translate("CharacterSheet", u"Fegyver t\u00f6rl\u00e9se", None))
        self.save_groupBox.setTitle(QCoreApplication.translate("CharacterSheet", u"Ment\u0151dob\u00e1sok", None))
        self.reflex_save_label.setText(QCoreApplication.translate("CharacterSheet", u"Reflex", None))
        self.save_all_label.setText(QCoreApplication.translate("CharacterSheet", u"\u00d6sszes", None))
        self.save_other_label.setText(QCoreApplication.translate("CharacterSheet", u"Egy\u00e9b", None))
        self.constitution_save_label.setText(QCoreApplication.translate("CharacterSheet", u"Kitart\u00e1s", None))
        self.willpower_save_label.setText(QCoreApplication.translate("CharacterSheet", u"Akarat", None))
        self.save_base_label.setText(QCoreApplication.translate("CharacterSheet", u"Alap", None))
        self.character_sheet_toolBox.setItemText(self.character_sheet_toolBox.indexOf(self.character_sheet_toolBoxPage2), QCoreApplication.translate("CharacterSheet", u"Kezdem\u00e9nyez\u0151, T\u00e1mad\u00f3, V\u00e9d\u0151, Ment\u0151dob\u00e1sok \u00e9s K\u00e9pess\u00e9gek", None))
        self.equipment_money_groupBox.setTitle(QCoreApplication.translate("CharacterSheet", u"Felszerel\u00e9s \u00e9s p\u00e9nz", None))
        self.money_silver_label.setText(QCoreApplication.translate("CharacterSheet", u"Ez\u00fcst", None))
        self.money_iron_label.setText(QCoreApplication.translate("CharacterSheet", u"Vas", None))
        self.small_item_label.setText(QCoreApplication.translate("CharacterSheet", u"Helyet nem foglal\u00f3 apr\u00f3s\u00e1gok", None))
        ___qtablewidgetitem10 = self.equipment_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("CharacterSheet", u"Mennyis\u00e9g", None));
        ___qtablewidgetitem11 = self.equipment_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("CharacterSheet", u"Terhel\u00e9s", None));
        ___qtablewidgetitem12 = self.equipment_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("CharacterSheet", u"Megnevez\u00e9s", None));
        self.add_equipment_pushButton.setText(QCoreApplication.translate("CharacterSheet", u"Felszerel\u00e9s hozz\u00e1ad\u00e1sa", None))
        self.remove_equipment_pushButton.setText(QCoreApplication.translate("CharacterSheet", u"Felszerel\u00e9s t\u00f6rl\u00e9se", None))
        self.add_small_item_pushButton.setText(QCoreApplication.translate("CharacterSheet", u"T\u00e1rgy hozz\u00e1ad\u00e1sa", None))
        self.remove_small_item_pushButton.setText(QCoreApplication.translate("CharacterSheet", u"T\u00e1rgy t\u00f6rl\u00e9se", None))
        self.encumbrance_label.setText(QCoreApplication.translate("CharacterSheet", u"Teherb\u00edr\u00e1s", None))
        self.slash_separator_label.setText(QCoreApplication.translate("CharacterSheet", u"/", None))
        self.fame_groupBox.setTitle(QCoreApplication.translate("CharacterSheet", u"Dics\u0151 \u00e9s dicstelen tettek", None))
        ___qtablewidgetitem13 = self.fame_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("CharacterSheet", u"Dics\u0151/Dicstelen", None));
        ___qtablewidgetitem14 = self.fame_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("CharacterSheet", u"\u00c9rt\u00e9k", None));
        ___qtablewidgetitem15 = self.fame_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("CharacterSheet", u"Le\u00edr\u00e1s", None));
        self.add_fame_pushButton.setText(QCoreApplication.translate("CharacterSheet", u"H\u00edrn\u00e9v hozz\u00e1ad\u00e1sa", None))
        self.remove_fame_pushButton.setText(QCoreApplication.translate("CharacterSheet", u"H\u00edrn\u00e9v t\u00f6rl\u00e9se", None))
        self.character_sheet_toolBox.setItemText(self.character_sheet_toolBox.indexOf(self.character_sheet_toolBoxPage3), QCoreApplication.translate("CharacterSheet", u"Felszerel\u00e9s, p\u00e9nz \u00e9s h\u00edrn\u00e9v", None))
        self.magic_groupBox.setTitle(QCoreApplication.translate("CharacterSheet", u"M\u00e1gia", None))
        self.available_spells_label.setText(QCoreApplication.translate("CharacterSheet", u"El\u00e9rhet\u0151", None))
        self.max_spells_label.setText(QCoreApplication.translate("CharacterSheet", u"Max", None))
        self.level_3_label.setText(QCoreApplication.translate("CharacterSheet", u"III: szint", None))
        self.level_2_label.setText(QCoreApplication.translate("CharacterSheet", u"II. szint", None))
        self.level_1_label.setText(QCoreApplication.translate("CharacterSheet", u"I. szint", None))
        self.spell_list_label.setText(QCoreApplication.translate("CharacterSheet", u"Ismert var\u00e1zslatok", None))
        ___qtablewidgetitem16 = self.spell_list_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("CharacterSheet", u"Szint", None));
        ___qtablewidgetitem17 = self.spell_list_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("CharacterSheet", u"Megnevez\u00e9s", None));
        ___qtablewidgetitem18 = self.spell_list_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("CharacterSheet", u"Le\u00edr\u00e1s", None));
        self.add_spell_pushButton.setText(QCoreApplication.translate("CharacterSheet", u"Var\u00e1zslat hozz\u00e1ad\u00e1sa", None))
        self.remove_spell_pushButton.setText(QCoreApplication.translate("CharacterSheet", u"Var\u00e1zslat t\u00f6rl\u00e9se", None))
        self.character_sheet_toolBox.setItemText(self.character_sheet_toolBox.indexOf(self.character_sheet_toolBoxPage4), QCoreApplication.translate("CharacterSheet", u"M\u00e1gia", None))
        self.dice_roller_groupBox.setTitle(QCoreApplication.translate("CharacterSheet", u"Kockadob\u00e1s", None))
        self.dice_roll_pushButton.setText(QCoreApplication.translate("CharacterSheet", u"Dob\u00e1s", None))
        self.dice_sign_label.setText(QCoreApplication.translate("CharacterSheet", u"D", None))
        self.plus_sign_label.setText(QCoreApplication.translate("CharacterSheet", u"+", None))
        self.attack_test_pushButton.setText(QCoreApplication.translate("CharacterSheet", u"T\u00e1mad\u00e1s", None))
        self.defense_test_pushButton.setText(QCoreApplication.translate("CharacterSheet", u"V\u00e9dekez\u00e9s", None))
        self.attribute_test_pushButton.setText(QCoreApplication.translate("CharacterSheet", u"Tulajdons\u00e1g pr\u00f3ba", None))
        self.skill_test_pushButton.setText(QCoreApplication.translate("CharacterSheet", u"J\u00e1rtass\u00e1g pr\u00f3ba", None))
        self.save_test_pushButton.setText(QCoreApplication.translate("CharacterSheet", u"Ment\u0151dob\u00e1s", None))
        self.modifier_label.setText(QCoreApplication.translate("CharacterSheet", u"Pr\u00f3ba m\u00f3dos\u00edt\u00f3", None))
    # retranslateUi

