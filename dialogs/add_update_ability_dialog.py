from PySide6.QtWidgets import QDialog, QDialogButtonBox, QLineEdit, QListWidgetItem
from ui.add_update_ability_dialog_ui import Ui_AddUpdateAbilityDialog

class AddUpdateAbilityDialog(QDialog, Ui_AddUpdateAbilityDialog):
    """Class for the dialog to add or update an ability"""

    def __init__(self, parent = None, item_data: QListWidgetItem = None):
        super().__init__(parent)
        
        self.setupUi(self)

        # Setup
        self.item_data: QListWidgetItem = item_data

        # Initialize the dialog
        self.initialize_dialog()


    def initialize_dialog(self):
        """Initialize the dialog with default or existing data if provided (in case of editing an existing ability)"""

        # Connect dialog buttonBox signals
        self.confirm_reject_ability_buttonBox.accepted.connect(self.accept)
        self.confirm_reject_ability_buttonBox.rejected.connect(self.reject)

        if self.item_data:
            self.ability_lineEdit.setText(self.item_data.text())


    def get_ability_name(self) -> str:
        """Get the ability name from the line edit"""

        return self.ability_lineEdit.text()
