from PySide6.QtWidgets import QDialog, QDialogButtonBox, QLineEdit, QSpinBox, QTableWidgetItem, QRadioButton
from ui.add_update_fame_dialog_ui import Ui_AddUpdateFameDialog

class AddUpdateFameDialog(QDialog, Ui_AddUpdateFameDialog):
    """Class for the dialog to add or update a spell"""

    def __init__(self, parent = None, item_data: QTableWidgetItem = None):
        super().__init__(parent)
        
        self.setupUi(self)

        # Setup
        self.item_data: QTableWidgetItem = item_data

        # Initialize the dialog
        self.initialize_dialog()


    def initialize_dialog(self):
        """Initialize the dialog with default or existing data if provided (in case of editing an existing fame)"""

        # Connect dialog buttonBox signals
        self.confirm_reject_fame_buttonBox.accepted.connect(self.accept)
        self.confirm_reject_fame_buttonBox.rejected.connect(self.reject)

        if self.item_data:
            row = self.item_data.row()

            # Get fame data from the item_data
            fame_data = []
            for column in range(self.item_data.tableWidget().columnCount()):
                cell_item = self.item_data.tableWidget().item(row, column)
                fame_data.append(cell_item.text() if cell_item else "")

            # Set the dialog fields with the existing fame data
            if fame_data[0] == "Dicső":
                self.glory_radioButton.setChecked(True)
            else:
                self.notoriety_radioButton.setChecked(True)

            self.fame_value_spinBox.setValue(int(fame_data[1]))
            self.fame_description_lineEdit.setText(fame_data[2])


    def get_fame_data(self) -> dict:
        """Return the data from the dialog"""

        # Fame type
        fame_type: str = "Dicső" if self.glory_radioButton.isChecked() else "Dicstelen"

        # Fame value
        fame_value: int = self.fame_value_spinBox.value()

        # Fame description
        fame_description: str = self.fame_description_lineEdit.text()

        return {
            "fame_type": fame_type,
            "fame_value": fame_value,
            "fame_description": fame_description
        }