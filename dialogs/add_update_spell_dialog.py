from PySide6.QtWidgets import QDialog, QTableWidgetItem
from ui.add_update_spell_dialog_ui import Ui_AddUpdateSpellDialog

class AddUpdateSpellDialog(QDialog, Ui_AddUpdateSpellDialog):
    """Class for the dialog to add or update a spell"""

    def __init__(self, parent = None, item_data: QTableWidgetItem = None):
        super().__init__(parent)
        
        self.setupUi(self)

        # Setup
        self.item_data: QTableWidgetItem = item_data

        # Initialize the dialog
        self.initialize_dialog()


    def initialize_dialog(self):
        """Initialize the dialog with default or existing data if provided (in case of editing an existing spell)"""

        # Connect dialog buttonBox signals
        self.confirm_reject_spell_buttonBox.accepted.connect(self.accept)
        self.confirm_reject_spell_buttonBox.rejected.connect(self.reject)

        if self.item_data:
            row = self.item_data.row()

            # Get spell data from the item_data
            spell_data = []
            for column in range(self.item_data.tableWidget().columnCount()):
                cell_item = self.item_data.tableWidget().item(row, column)
                spell_data.append(cell_item.text() if cell_item else "")

            # Set the dialog fields with the existing spell data
            self.spell_level_spinBox.setValue(int(spell_data[0]))
            self.spell_name_lineEdit.setText(spell_data[1])
            self.spell_description_lineEdit.setText(spell_data[2])


    def get_spell_data(self) -> dict:
        """Return the data from the dialog"""

        # Spell level
        spell_level: int = self.spell_level_spinBox.value()

        # Spell name
        spell_name: str = self.spell_name_lineEdit.text()

        # Spell description
        spell_description: str = self.spell_description_lineEdit.text()

        return {
            "spell_level": spell_level,
            "spell_name": spell_name,
            "spell_description": spell_description
        }