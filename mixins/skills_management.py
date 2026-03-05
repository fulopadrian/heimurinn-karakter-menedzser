"""Skills management functionality for character sheet"""

from PySide6.QtWidgets import QTableWidgetItem

from dialogs.add_update_skill_dialog import AddUpdateSkillDialog


class SkillsManagement:
    """Mixin class for skills management functionality"""

    def connect_skill_signals(self):
        """Connect signals for the skill table to handle adding, editing and deleting skills"""
        
        self.add_skill_pushButton.clicked.connect(self.add_skill)
        self.skills_tableWidget.itemDoubleClicked.connect(self.edit_skill)
        self.remove_skill_pushButton.clicked.connect(self.delete_skill)


    def add_skill(self):
        """Open the dialog to add a new skill"""
        
        dialog = AddUpdateSkillDialog(self, character_level=self.level_spinBox.value())

        if dialog.exec() == 1:  # QDialog.Accepted
            skill_data = dialog.get_skill_data()

            # Calculate the total skill value (sum)
            attribute_label = skill_data["skill_attribute"]
            skill_data["sum"] = skill_data["skill_level"] + skill_data["other_modifier"] + self.get_attribute_modifier_by_label(attribute_label)

            # Add the new skill to the skills table
            row_position = self.skills_tableWidget.rowCount()
            self.skills_tableWidget.insertRow(row_position)

            # Populate the new row with the skill data
            for column, key in enumerate(skill_data.keys()):
                item = QTableWidgetItem(str(skill_data[key]))
                self.skills_tableWidget.setItem(row_position, column, item)

            # Update the skill test combo box
            self._update_skill_test_combo_box()


    def edit_skill(self, skill_item):
        """Open the dialog to edit an existing skill"""
        
        dialog = AddUpdateSkillDialog(self, character_level=self.level_spinBox.value(), item_data=skill_item)

        if dialog.exec() == 1:  # QDialog.Accepted
            skill_data = dialog.get_skill_data()

            # Get attribute modifier for the skill
            attribute_name = skill_data["skill_attribute"]

            # Calculate the total skill value (sum)
            skill_data["sum"] = skill_data["skill_level"] + skill_data["other_modifier"] + self.get_attribute_modifier_by_label(attribute_name)

            # Update the existing skill in the skills table
            row = skill_item.row()

            for column, key in enumerate(skill_data.keys()):
                item = QTableWidgetItem(str(skill_data[key]))
                self.skills_tableWidget.setItem(row, column, item)

            # Update the skill test combo box
            self._update_skill_test_combo_box()


    def delete_skill(self):
        """Delete the selected skill from the skills table"""

        selected_items = self.skills_tableWidget.selectedItems()

        if selected_items:
            row = selected_items[0].row()
            self.skills_tableWidget.removeRow(row)

            # Update the skill test combo box
            self._update_skill_test_combo_box()


    def recalculate_skills(self, attribute_name: str):
        """Recalculate the skill values for all skills that are based on the given attribute"""

        for row in range(self.skills_tableWidget.rowCount()):
            # Get skill attribute
            skill_attribute = self.skills_tableWidget.item(row, 1)

            # Update skill values if the skill is based on the changed attribute
            if skill_attribute and skill_attribute.text() == self.get_attribute_label_by_name(attribute_name):
                # Get skill level
                skill_level = self.skills_tableWidget.item(row, 2)

                # Get skill other modifier
                other_modifier = self.skills_tableWidget.item(row, 3)

                if skill_level and other_modifier:
                    skill_level = int(skill_level.text())
                    other_modifier = int(other_modifier.text())
                    attribute_modifier: int = self.get_attribute_modifier_by_name(attribute_name)

                    # Calculate the new total skill value (sum)
                    total_skill_value = skill_level + other_modifier + attribute_modifier

                    # Update the total skill value in the table
                    total_skill_value = QTableWidgetItem(str(total_skill_value))
                    self.skills_tableWidget.setItem(row, 4, total_skill_value)
