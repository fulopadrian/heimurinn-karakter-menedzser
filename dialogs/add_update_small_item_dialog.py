from PySide6.QtWidgets import QDialog, QListWidgetItem
from ui.add_update_small_item_dialog_ui import Ui_AddUpdateSmallItemDialog

class AddUpdateSmallItemDialog(QDialog, Ui_AddUpdateSmallItemDialog):
    """Class for the dialog to add or update a small item"""

    def __init__(self, parent = None, item_data: QListWidgetItem = None):
        super().__init__(parent)
        
        self.setupUi(self)

        # Setup
        self.item_data: QListWidgetItem = item_data

        # Initialize the dialog
        self.initialize_dialog()


    def initialize_dialog(self):
        """Initialize the dialog with default or existing data if provided (in case of editing an existing small item)"""

        # Connect dialog buttonBox signals
        self.confirm_reject_small_item_buttonBox.accepted.connect(self.accept)
        self.confirm_reject_small_item_buttonBox.rejected.connect(self.reject)

        if self.item_data:
            self.small_item_lineEdit.setText(self.item_data.text())


    def get_small_item_name(self) -> str:
        """Get the small item name from the line edit"""

        return self.small_item_lineEdit.text()