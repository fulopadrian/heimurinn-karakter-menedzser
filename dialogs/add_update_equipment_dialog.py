from PySide6.QtWidgets import QDialog, QTableWidgetItem
from ui.add_update_equipment_dialog_ui import Ui_AddUpdateEquipmentDialog

class AddUpdateEquipmentDialog(QDialog, Ui_AddUpdateEquipmentDialog):
    """Class for the dialog to add or update an equipment"""

    def __init__(self, parent = None, item_data: QTableWidgetItem = None):
        super().__init__(parent)
        
        self.setupUi(self)

        # Setup
        self.item_data: QTableWidgetItem = item_data

        # Initialize the dialog
        self.initialize_dialog()


    def initialize_dialog(self):
        """Initialize the dialog with default or existing data if provided (in case of editing an existing equipment)"""

        # Connect dialog buttonBox signals
        self.confirm_reject_equipment_buttonBox.accepted.connect(self.accept)
        self.confirm_reject_equipment_buttonBox.rejected.connect(self.reject)

        if self.item_data:
            row = self.item_data.row()

            # Get equipment data from the item_data
            equipment_data = []
            for column in range(self.item_data.tableWidget().columnCount()):
                cell_item = self.item_data.tableWidget().item(row, column)
                equipment_data.append(cell_item.text() if cell_item else "")
            
            # Set the existing data to the dialog components
            self.equipment_name_lineEdit.setText(equipment_data[2])
            self.equipment_count_spinBox.setValue(int(equipment_data[0]))
            self.equipment_encumbrance_doubleSpinBox.setValue(float(equipment_data[1]))


    def get_equipment_data(self) -> dict:
        """Get the equipment data from the dialog components"""

        equipment_name = self.equipment_name_lineEdit.text()
        equipment_count = self.equipment_count_spinBox.value()
        equipment_encumbrance = self.equipment_encumbrance_doubleSpinBox.value()

        return {
            "equipment_count": equipment_count,
            "equipment_encumbrance": equipment_encumbrance,
            "equipment_name": equipment_name
        }