from PySide6.QtWidgets import QDialog, QTableWidgetItem
from ui.add_update_skill_dialog_ui import Ui_AddUpdateSkillDialog

from settings import SKILLS

class AddUpdateSkillDialog(QDialog, Ui_AddUpdateSkillDialog):
    """Class for the dialog to add or update a skills"""

    def __init__(self, parent = None, character_level: int = 1, item_data: QTableWidgetItem = None):
        super().__init__(parent)
        
        self.setupUi(self)

        # Setup
        self.item_data: QTableWidgetItem = item_data
        self.skill_list = list(SKILLS.keys())

        # Initialize the dialog
        self.initialize_dialog(character_level)


    def initialize_dialog(self, character_level: int = 1):
        """Initialize the dialog with default or existing data if provided (in case of editing an existing skill)"""

        # Connect dialog buttonBox signals
        self.confirm_reject_skill_buttonBox.accepted.connect(self.accept)
        self.confirm_reject_skill_buttonBox.rejected.connect(self.reject)
        
        # Connect skill combo box signal
        self.skill_comboBox.currentTextChanged.connect(self.update_attribute_options)

        # Set the default values for adding a new skill
        self.skill_comboBox.addItems(self.skill_list)

        # Set the maximum allowed skill level to the character level + 1
        self.skill_level_spinBox.setMaximum(character_level + 1)

        if self.item_data:
            row = self.item_data.row()

            # Get skill data from the item_data
            skill_data = []
            for column in range(self.item_data.tableWidget().columnCount()):
                cell_item = self.item_data.tableWidget().item(row, column)
                skill_data.append(cell_item.text() if cell_item else "")

            # Set the dialog fields with the existing skill data
            self.skill_comboBox.setCurrentText(skill_data[0])
            self.attribute_comboBox.setCurrentText(skill_data[1])
            self.skill_level_spinBox.setValue(int(skill_data[2]))
            self.other_mod_spinBox.setValue(int(skill_data[3]))


    def update_attribute_options(self, skill_name: str):
        """Set the attribute options based on the selected skill"""

        self.attribute_comboBox.clear()
        self.attribute_comboBox.addItems(SKILLS[skill_name])


    def get_skill_data(self) -> dict:
        """Return the data from the dialog"""
        
        # Selected skill name
        skill_name = self.skill_comboBox.currentText()

        # Selected attribute for the skill
        skill_attribute = self.attribute_comboBox.currentText()

        # Selected skill level
        skill_level = self.skill_level_spinBox.value()

        # Selected other modifier
        other_modifier = self.other_mod_spinBox.value()

        return {
            "skill_name": skill_name,
            "skill_attribute": skill_attribute,
            "skill_level": skill_level,
            "other_modifier": other_modifier
        }