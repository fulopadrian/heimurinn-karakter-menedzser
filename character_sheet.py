from typing import Union
from PySide6.QtWidgets import (
    QWidget,
    QSpinBox,
    QLineEdit,
    QTextEdit,
    QDoubleSpinBox,
    QComboBox,
    QPushButton,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QTableWidget,
    QTableWidgetItem
)

from settings import CLASS_OPTIONS

from mixins.attributes_management import AttributesManagement
from mixins.combat_management import CombatManagement
from mixins.skills_management import SkillsManagement
from mixins.abilities_management import AbilitiesManagement
from mixins.weapons_management import WeaponsManagement
from mixins.equipment_management import EquipmentManagement
from mixins.small_items_management import SmallItemsManagement
from mixins.fame_management import FameManagement
from mixins.magic_management import MagicManagement
from mixins.attribute_helpers import AttributeHelpers
from mixins.dice_roller import DiceRollerMixin
from ui.character_sheet_ui import Ui_CharacterSheet

class CharacterSheet(
    QWidget,
    Ui_CharacterSheet,
    AttributeHelpers,
    AttributesManagement,
    CombatManagement,
    SkillsManagement,
    AbilitiesManagement,
    WeaponsManagement,
    EquipmentManagement,
    SmallItemsManagement,
    FameManagement,
    MagicManagement,
    DiceRollerMixin
):
    """Character sheet UI component"""

    def __init__(self, character_data: dict = None):
        super().__init__()
        
        self.setupUi(self)

        self.character_is_loading = False # Indicates if the app is loading a character
        self.character_data = character_data
        self.skald_attack_defense_priority: Union[dict, None] = None

        # Setup
        # Initialize UI components
        self.initialize_components()

        # Initialize character
        self.initialize_character()

        # Load character
        if self.character_data:
            self.load_character_data(self.character_data)


    def initialize_components(self):
        """Initialize UI components - setup attribute and spell slot lists"""

        # Setup attributes
        self.attributes = {
            "strength": {"label": self.strength_label.text(), "value": self.strength_spinBox, "modifier": self.strength_mod_spinBox},
            "dexterity": {"label": self.dexterity_label.text(), "value": self.dexterity_spinBox, "modifier": self.dexterity_mod_spinBox},
            "stamina": {"label": self.stamina_label.text(), "value": self.stamina_spinBox, "modifier": self.stamina_mod_spinBox},
            "intelligence": {"label": self.intelligence_label.text(), "value": self.intelligence_spinBox, "modifier": self.intelligence_mod_spinBox},
            "wisdom": {"label": self.wisdom_label.text(), "value": self.wisdom_spinBox, "modifier": self.wisdom_mod_spinBox},
            "charisma": {"label": self.charisma_label.text(), "value": self.charisma_spinBox, "modifier": self.charisma_mod_spinBox}
        }

        # Setup spell slots lists
        self.max_spell_slots = [
            self.max_level_1_spinBox,
            self.max_level_2_spinBox,
            self.max_level_3_spinBox
        ]

        self.available_spell_slots = [
            self.available_level_1_spinBox,
            self.available_level_2_spinBox,
            self.available_level_3_spinBox
        ]


    def initialize_character(self):
        """Initialize character"""

        # Populate class options
        self.class_comboBox.addItems(list(CLASS_OPTIONS.keys()))

        # Set default attribute values and modifiers
        for attribute_name in self.attributes:
            self.update_attribute(attribute_name)

        # Set default cold resistance value
        self.cold_resistance_spinBox.setValue(3 + self.get_attribute_modifier_by_name("stamina"))

        # Set default initiative, defense and attack values for level 1 character based on class and attributes
        self.update_combat_values()

        # Set default saves values for level 1 character based on class and attributes
        self.update_saves_values()

        # Set default max encumbrance based on strength
        self.calculate_max_encumbrance()

        # Populate dice roller combo boxes
        self._populate_attack_test_combo_box()
        self._populate_defense_test_combo_box()
        self._populate_attribute_test_combo_box()
        self._populate_skill_test_combo_box()
        self._populate_save_test_combo_box()

        # Connect signals for all management systems
        self.connect_attribute_signals()
        self.connect_skill_signals()
        self.connect_combat_value_signals()
        self.connect_saves_value_signals()
        self.connect_ability_signals()
        self.connect_weapon_signals()
        self.connect_equipment_signals()
        self.connect_small_item_signals()
        self.connect_fame_signals()
        self.connect_magic_signals()

        # Connect signals for the dice roller
        self.connect_dice_roller_signals()


    def _populate_attack_test_combo_box(self):
        """Populate the attack test combo box"""

        self.attack_test_comboBox.clear()
        
        # Add weapon names from weapons_table first column
        for row in range(self.weapons_tableWidget.rowCount()):
            weapon_name_item = self.weapons_tableWidget.item(row, 0)
            if weapon_name_item:
                self.attack_test_comboBox.addItem(weapon_name_item.text())


    def _populate_defense_test_combo_box(self):
        """Populate the defense test combo box with defense types"""

        self.defense_test_comboBox.clear()
        self.defense_test_comboBox.addItems(["Alap", "Meglepetés"])


    def _populate_attribute_test_combo_box(self):
        """Populate the attribute test combo box with attribute labels"""

        self.attribute_test_comboBox.clear()
        attribute_labels = [self.attributes[attribute]["label"] for attribute in self.attributes]
        self.attribute_test_comboBox.addItems(attribute_labels)


    def _populate_skill_test_combo_box(self):
        """Populate the skill test combo box with skill names from skills table"""

        self.skill_test_comboBox.clear()
        
        # Add skill names from skills_table first column
        for row in range(self.skills_tableWidget.rowCount()):
            skill_name_item = self.skills_tableWidget.item(row, 0)
            if skill_name_item:
                self.skill_test_comboBox.addItem(skill_name_item.text())


    def _populate_save_test_combo_box(self):
        """Populate the save test combo box with save types"""

        self.save_test_comboBox.clear()
        self.save_test_comboBox.addItems(["Kitartás", "Reflex", "Akarat"])


    def _update_attack_test_combo_box(self):
        """Update the attack test combo box with current weapon names"""

        self._populate_attack_test_combo_box()


    def _update_skill_test_combo_box(self):
        """Update the skill test combo box with current skill names"""

        self._populate_skill_test_combo_box()


    def get_character_data(self) -> dict:
        """Collect all character data from UI components and return as a dictionary"""

        character_data = {
            "skald_attack_defense_priority": self.skald_attack_defense_priority,

            # Basic info
            "name": self.name_lineEdit.text(),
            "class": self.class_comboBox.currentText(),
            "clan": self.clan_lineEdit.text(),
            "level": self.level_spinBox.value(),
            "exp": self.exp_spinBox.value(),
            "fame": self.fame_spinBox.value(),
            "faith": self.faith_lineEdit.text(),
            "fate": self.fate_spinBox.value(),

            # Background
            "background": self.background_textEdit.toPlainText(),

            # Attributes
            "attributes": {
                "strength": {
                    "value": self.strength_spinBox.value(),
                    "modifier": self.strength_mod_spinBox.value()
                },
                "dexterity": {
                    "value": self.dexterity_spinBox.value(),
                    "modifier": self.dexterity_mod_spinBox.value()
                },
                "stamina": {
                    "value": self.stamina_spinBox.value(),
                    "modifier": self.stamina_mod_spinBox.value()
                },
                "intelligence": {
                    "value": self.intelligence_spinBox.value(),
                    "modifier": self.intelligence_mod_spinBox.value()
                },
                "wisdom": {
                    "value": self.wisdom_spinBox.value(),
                    "modifier": self.wisdom_mod_spinBox.value()
                },
                "charisma": {
                    "value": self.charisma_spinBox.value(),
                    "modifier": self.charisma_mod_spinBox.value()
                }
            },

            # Skills table
            "skills": self._extract_table_data(self.skills_tableWidget),

            # Health
            "health": self.health_spinBox.value(),
            "health_max": self.health_max_spinBox.value(),

            # Cold resistance
            "cold_resistance": self.cold_resistance_spinBox.value(),

            # Initiative
            "initiative": {
                "base": self.initiative_base_spinBox.value(),
                "other": self.initiative_other_spinBox.value(),
                "all": self.initiative_all_spinBox.value()
            },

            # Defense
            "defense": {
                "base": self.defense_base_spinBox.value(),
                "shield": self.defense_shield_spinBox.value(),
                "other": self.defense_other_spinBox.value(),
                "all": self.defense_all_spinBox.value()
            },

            # Attack
            "attack": {
                "close_combat": self.close_combat_attack_spinBox.value(),
                "ranged_combat": self.ranged_combat_attack_spinBox.value()
            },

            # Armor and shield
            "armor": {
                "name": self.armor_lineEdit.text(),
                "rating": self.armor_rating_spinBox.value()
            },
            "helmet": {
                "name": self.helmet_lineEdit.text(),
                "rating": self.helmet_rating_spinBox.value()
            },
            "shield": {
                "name": self.shield_lineEdit.text(),
                "break": self.shield_break_spinBox.value()
            },

            # Saves
            "saves": {
                "constitution": {
                    "base": self.constitution_save_base_spinBox.value(),
                    "other": self.constitution_save_other_spinBox.value(),
                    "all": self.constitution_save_all_spinBox.value()
                },
                "reflex": {
                    "base": self.reflex_save_base_spinBox.value(),
                    "other": self.reflex_save_other_spinBox.value(),
                    "all": self.reflex_save_all_spinBox.value()
                },
                "willpower": {
                    "base": self.willpower_save_base_spinBox.value(),
                    "other": self.willpower_save_other_spinBox.value(),
                    "all": self.willpower_save_all_spinBox.value()
                }
            },

            # Abilities list
            "abilities": self._extract_list_data(self.abilites_listWidget),

            # Weapons table
            "weapons": self._extract_table_data(self.weapons_tableWidget),

            # Equipment table
            "equipment": self._extract_table_data(self.equipment_tableWidget),
            "current_encumbrance": self.current_encumbrance_doubleSpinBox.value(),
            "max_encumbrance": self.max_encumbrance_doubleSpinBox.value(),

            # Small items list
            "small_items": self._extract_list_data(self.small_items_listWidget),

            # Money
            "money": {
                "silver": self.money_silver_spinBox.value(),
                "iron": self.money_iron_spinBox.value()
            },

            # Fame table
            "fame": self._extract_table_data(self.fame_tableWidget),

            # Magic
            "magic": {
                "max_spell_slots": [spinbox.value() for spinbox in self.max_spell_slots],
                "available_spell_slots": [spinbox.value() for spinbox in self.available_spell_slots],
                "spells": self._extract_table_data(self.spell_list_tableWidget)
            }
        }

        return character_data


    def character_loading(func):
        """Decorator for loading characters"""

        def wrapper(self, *args, **kwargs):
            self.character_is_loading = True
            func(self, *args, **kwargs)
            self.character_is_loading = False

        return wrapper


    @character_loading
    def load_character_data(self, data: dict) -> None:
        """Load character data from a dictionary and set UI components accordingly"""

        if not data:
            return

        # Get Szkald specific attack/defense grades and update them
        self.skald_attack_defense_priority = data.get("skald_attack_defense_priority", None)
        self.update_class_attack_defense_grade("Szkald", self.skald_attack_defense_priority)

        # Basic info
        self.name_lineEdit.setText(data.get("name", ""))
        class_name = data.get("class", "")
        if class_name and self.class_comboBox.findText(class_name) >= 0:
            self.class_comboBox.setCurrentText(class_name)
        self.clan_lineEdit.setText(data.get("clan", ""))
        self.level_spinBox.setValue(data.get("level", 1))
        self.exp_spinBox.setValue(data.get("exp", 0))
        self.faith_lineEdit.setText(data.get("faith", ""))
        self.fate_spinBox.setValue(data.get("fate", 0))

        # Background
        self.background_textEdit.setPlainText(data.get("background", ""))

        # Attributes
        attributes_data = data.get("attributes", {})
        for attr_name, attr_values in attributes_data.items():
            if attr_name in self.attributes:
                self.attributes[attr_name]["value"].setValue(attr_values.get("value", 0))
                self.attributes[attr_name]["modifier"].setValue(attr_values.get("modifier", 0))

        # Skills table
        self._load_table_data(self.skills_tableWidget, data.get("skills", []))

        # Health
        self.health_spinBox.setValue(data.get("health", 0))
        self.health_max_spinBox.setValue(data.get("health_max", 0))

        # Cold resistance
        self.cold_resistance_spinBox.setValue(data.get("cold_resistance", 0))

        # Initiative
        initiative_data = data.get("initiative", {})
        self.initiative_base_spinBox.setValue(initiative_data.get("base", 0))
        self.initiative_other_spinBox.setValue(initiative_data.get("other", 0))
        self.initiative_all_spinBox.setValue(initiative_data.get("all", 0))

        # Defense
        defense_data = data.get("defense", {})
        self.defense_base_spinBox.setValue(defense_data.get("base", 0))
        self.defense_shield_spinBox.setValue(defense_data.get("shield", 0))
        self.defense_other_spinBox.setValue(defense_data.get("other", 0))
        self.defense_all_spinBox.setValue(defense_data.get("all", 0))

        # Attack
        attack_data = data.get("attack", {})
        self.close_combat_attack_spinBox.setValue(attack_data.get("close_combat", 0))
        self.ranged_combat_attack_spinBox.setValue(attack_data.get("ranged_combat", 0))

        # Armor and shield
        armor_data = data.get("armor", {})
        self.armor_lineEdit.setText(armor_data.get("name", ""))
        self.armor_rating_spinBox.setValue(armor_data.get("rating", 0))

        helmet_data = data.get("helmet", {})
        self.helmet_lineEdit.setText(helmet_data.get("name", ""))
        self.helmet_rating_spinBox.setValue(helmet_data.get("rating", 0))

        shield_data = data.get("shield", {})
        self.shield_lineEdit.setText(shield_data.get("name", ""))
        self.shield_break_spinBox.setValue(shield_data.get("break", 0))

        # Saves
        saves_data = data.get("saves", {})
        
        constitution_save = saves_data.get("constitution", {})
        self.constitution_save_base_spinBox.setValue(constitution_save.get("base", 0))
        self.constitution_save_other_spinBox.setValue(constitution_save.get("other", 0))
        self.constitution_save_all_spinBox.setValue(constitution_save.get("all", 0))

        reflex_save = saves_data.get("reflex", {})
        self.reflex_save_base_spinBox.setValue(reflex_save.get("base", 0))
        self.reflex_save_other_spinBox.setValue(reflex_save.get("other", 0))
        self.reflex_save_all_spinBox.setValue(reflex_save.get("all", 0))

        willpower_save = saves_data.get("willpower", {})
        self.willpower_save_base_spinBox.setValue(willpower_save.get("base", 0))
        self.willpower_save_other_spinBox.setValue(willpower_save.get("other", 0))
        self.willpower_save_all_spinBox.setValue(willpower_save.get("all", 0))

        # Abilities list
        self._load_list_data(self.abilites_listWidget, data.get("abilities", []))

        # Weapons table
        self._load_table_data(self.weapons_tableWidget, data.get("weapons", []))

        # Equipment table
        self._load_table_data(self.equipment_tableWidget, data.get("equipment", []))
        self.current_encumbrance_doubleSpinBox.setValue(data.get("current_encumbrance", 0.0))
        self.max_encumbrance_doubleSpinBox.setValue(data.get("max_encumbrance", 0.0))

        # Small items list
        self._load_list_data(self.small_items_listWidget, data.get("small_items", []))

        # Money
        money_data = data.get("money", {})
        self.money_silver_spinBox.setValue(money_data.get("silver", 0))
        self.money_iron_spinBox.setValue(money_data.get("iron", 0))

        # Fame table
        self._load_table_data(self.fame_tableWidget, data.get("fame", []))
        self._recalculate_current_fame()

        # Magic
        magic_data = data.get("magic", {})
        max_spells = magic_data.get("max_spell_slots", [0, 0, 0])
        for i, spinbox in enumerate(self.max_spell_slots):
            if i < len(max_spells):
                spinbox.setValue(max_spells[i])

        available_spells = magic_data.get("available_spell_slots", [0, 0, 0])
        for i, spinbox in enumerate(self.available_spell_slots):
            if i < len(available_spells):
                spinbox.setValue(available_spells[i])

        self._load_table_data(self.spell_list_tableWidget, magic_data.get("spells", []))

        # Refresh dice roller combo boxes to reflect loaded data
        self._populate_attack_test_combo_box()
        self._populate_skill_test_combo_box()


    def _extract_table_data(self, table_widget: QTableWidget) -> list:
        """Extract all data from a QTableWidget and return as a list of dictionaries"""

        table_data = []

        for row in range(table_widget.rowCount()):
            row_data = {}
            for col in range(table_widget.columnCount()):
                item = table_widget.item(row, col)
                if item:
                    row_data[f"col_{col}"] = item.text()
            if row_data:
                table_data.append(row_data)

        return table_data


    def _load_table_data(self, table_widget: QTableWidget, data: list) -> None:
        """Load data from a list of dictionaries into a QTableWidget"""

        table_widget.setRowCount(0)

        for row_data in data:
            row_position = table_widget.rowCount()
            table_widget.insertRow(row_position)

            # Sort keys to ensure consistent column order
            sorted_keys = sorted(row_data.keys())
            for col, key in enumerate(sorted_keys):
                if col < table_widget.columnCount():
                    item = QTableWidgetItem(str(row_data[key]))
                    table_widget.setItem(row_position, col, item)


    def _extract_list_data(self, list_widget: QListWidget) -> list:
        """Extract all items from a QListWidget and return as a list"""

        list_data = []

        for row in range(list_widget.count()):
            item = list_widget.item(row)
            if item:
                list_data.append(item.text())

        return list_data


    def _load_list_data(self, list_widget: QListWidget, data: list) -> None:
        """Load data from a list into a QListWidget"""
        
        list_widget.clear()

        for item_text in data:
            item = QListWidgetItem(str(item_text))
            list_widget.addItem(item)
