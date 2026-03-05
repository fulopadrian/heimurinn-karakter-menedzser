"""Weapons management functionality for character sheet"""

from PySide6.QtWidgets import QTableWidgetItem

from dialogs.add_update_weapon_dialog import AddUpdateWeaponDialog


class WeaponsManagement:
    """Mixin class for weapons management functionality"""

    def connect_weapon_signals(self):
        """Connect signals for the weapon table to handle adding, editing and deleting weapons"""

        self.add_weapon_pushButton.clicked.connect(self.add_weapon)
        self.weapons_tableWidget.itemDoubleClicked.connect(self.edit_weapon)
        self.remove_weapon_pushButton.clicked.connect(self.delete_weapon)

    
    def add_weapon(self):
        """Open the dialog to add a new weapon"""

        dialog = AddUpdateWeaponDialog(self)

        if dialog.exec() == 1:  # QDialog.Accepted
            weapon_data = dialog.get_weapon_data()

            # Check if weapon name is empty, if so, do not add the weapon and return
            if not weapon_data["weapon_name"].strip():
                return

            # Add the new weapon to the weapons table
            row_position = self.weapons_tableWidget.rowCount()
            self.weapons_tableWidget.insertRow(row_position)

            # Populate the new row with the weapon data
            for column, key in enumerate(weapon_data.keys()):
                item = QTableWidgetItem(str(weapon_data[key]))
                self.weapons_tableWidget.setItem(row_position, column, item)

            # Update the attack test combo box
            self._update_attack_test_combo_box()


    def edit_weapon(self, weapon_item):
        """Open the dialog to edit an existing weapon"""
        
        dialog = AddUpdateWeaponDialog(self, item_data=weapon_item)

        if dialog.exec() == 1:  # QDialog.Accepted
            weapon_data = dialog.get_weapon_data()

            # Check if weapon name is empty, if so, do not update the weapon and return
            if not weapon_data["weapon_name"].strip():
                return

            # Update the existing weapon in the weapons table
            row = weapon_item.row()

            for column, key in enumerate(weapon_data.keys()):
                item = QTableWidgetItem(str(weapon_data[key]))
                self.weapons_tableWidget.setItem(row, column, item)

            # Update the attack test combo box
            self._update_attack_test_combo_box()


    def delete_weapon(self):
        """Delete the selected weapon from the weapons table"""
        
        selected_items = self.weapons_tableWidget.selectedItems()

        if selected_items:
            row = selected_items[0].row()
            self.weapons_tableWidget.removeRow(row)
