"""Magic/Spell management functionality for character sheet"""

from PySide6.QtWidgets import QTableWidgetItem
from functools import partial

from dialogs.add_update_spell_dialog import AddUpdateSpellDialog
from settings import CLASS_OPTIONS


class MagicManagement:
    """Mixin class for magic/spell management functionality"""

    def connect_magic_signals(self):
        """Connect signals for magic values updates"""

        # Update magic spell values if class changes
        self.class_comboBox.currentTextChanged.connect(self.update_magic_values)

        # Update magic spell values if level changes
        self.level_spinBox.valueChanged.connect(self.update_magic_values)

        # Prevent setting available spells spinBoxe values higher then the max spells spinBox values
        self.available_level_1_spinBox.valueChanged.connect(partial(self.on_available_spell_changed, 1))
        self.available_level_2_spinBox.valueChanged.connect(partial(self.on_available_spell_changed, 2))
        self.available_level_3_spinBox.valueChanged.connect(partial(self.on_available_spell_changed, 3))

        # Add, edit and remove spells
        self.add_spell_pushButton.clicked.connect(self.add_spell)
        self.spell_list_tableWidget.itemDoubleClicked.connect(self.edit_spell)
        self.remove_spell_pushButton.clicked.connect(self.delete_spell)


    def update_magic_values(self):
        """Update available and usable spell values depending on class and level"""

        character_level: int = self.level_spinBox.value()
        character_class: str = self.class_comboBox.currentText()
        character_class_data: dict = CLASS_OPTIONS.get(character_class, {})
        magic_data: dict = character_class_data.get("magic", {})

        # If the class is not a magic user, set max and available spells to 0
        if not magic_data:
            for max_spell_slot in self.max_spell_slots:
                max_spell_slot.setValue(0)

            for available_spell_slot in self.available_spell_slots:
                available_spell_slot.setValue(0)

            return

        # Set max and available spells
        current_level_magic: dict = magic_data.get(character_level)
        for spell_level, values in current_level_magic.items():
            usable: int = values.get("usable")
            
            self.max_spell_slots[spell_level - 1].setValue(usable)
            
            self.available_spell_slots[spell_level - 1].setValue(usable)


    def on_available_spell_changed(self, spell_level: int, value: int):
        """Prevent setting available spells higher than max spells for a given level"""
        
        max_value: int = self.max_spell_slots[spell_level - 1].value()
        
        if value > max_value:
            self.available_spell_slots[spell_level - 1].setValue(max_value)


    def add_spell(self):
        """Open the dialog to add a new spell"""

        dialog = AddUpdateSpellDialog(self)

        if dialog.exec() == 1:  # QDialog.Accepted
            spell_data = dialog.get_spell_data()

            # Check if spell name is empty, if so, do not add the spell and return
            if not spell_data["spell_name"].strip():
                return

            # Add the new spell to the spell table
            row_position = self.spell_list_tableWidget.rowCount()
            self.spell_list_tableWidget.insertRow(row_position)

            # Populate the new row with the spell data
            for column, key in enumerate(spell_data.keys()):
                item = QTableWidgetItem(str(spell_data[key]))
                self.spell_list_tableWidget.setItem(row_position, column, item)


    def edit_spell(self, spell_item):
        """Open the dialog to edit an existing spell"""

        dialog = AddUpdateSpellDialog(self, item_data=spell_item)

        if dialog.exec() == 1:  # QDialog.Accepted
            spell_data = dialog.get_spell_data()

            # Check if spell name is empty, if so, do not add the spell and return
            if not spell_data["spell_name"].strip():
                return
            
            # Update the existing spell in the spell table
            row = spell_item.row()

            for column, key in enumerate(spell_data.keys()):
                item = QTableWidgetItem(str(spell_data[key]))
                self.spell_list_tableWidget.setItem(row, column, item)


    def delete_spell(self):
        """Delete the selected spell from the spell table"""

        selected_items = self.spell_list_tableWidget.selectedItems()

        if selected_items:
            row = selected_items[0].row()
            self.spell_list_tableWidget.removeRow(row)
