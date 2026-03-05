"""Abilities management functionality for character sheet"""

from PySide6.QtWidgets import QListWidgetItem

from dialogs.add_update_ability_dialog import AddUpdateAbilityDialog


class AbilitiesManagement:
    """Mixin class for abilities management functionality"""

    def connect_ability_signals(self):
        """Connect signals for the ability list to handle adding, editing and deleting abilites"""

        self.add_ability_pushButton.clicked.connect(self.add_ability)
        self.abilites_listWidget.itemDoubleClicked.connect(self.edit_ability)
        self.remove_ability_pushButton.clicked.connect(self.remove_ability)


    def add_ability(self):
        """Open the dialog to add a new ability"""

        dialog = AddUpdateAbilityDialog(self)

        if dialog.exec() == 1:  # QDialog.Accepted
            ability_name = dialog.get_ability_name()

            # Check if ability name is empty, if so, do not add the ability and return
            if not ability_name.strip():
                return

            # Add the new ability to the abilities list
            item = QListWidgetItem(ability_name)
            self.abilites_listWidget.addItem(item)


    def edit_ability(self, ability_item):
        """Open the dialog to edit an existing ability"""

        dialog = AddUpdateAbilityDialog(self, item_data=ability_item)

        if dialog.exec() == 1:  # QDialog.Accepted
            ability_name = dialog.get_ability_name()

            # Check if ability name is empty, if so, do not update the ability and return
            if not ability_name.strip():
                return

            # Update the existing ability in the abilities list
            ability_item.setText(ability_name)


    def remove_ability(self):
        """Delete the selected ability from the ability list"""

        selected_item = self.abilites_listWidget.currentItem()

        if selected_item:
            row = self.abilites_listWidget.row(selected_item)
            self.abilites_listWidget.takeItem(row)
