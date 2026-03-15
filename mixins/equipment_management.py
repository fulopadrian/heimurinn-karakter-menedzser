from PySide6.QtWidgets import QTableWidgetItem
from dialogs.add_update_equipment_dialog import AddUpdateEquipmentDialog


class EquipmentManagement:
    """Mixin class for equipment management functionality"""

    def connect_equipment_signals(self):
        """Connect signals for the equipment table to handle adding, editing and deleting equipment"""

        self.add_equipment_pushButton.clicked.connect(self.add_equipment)
        self.equipment_tableWidget.itemDoubleClicked.connect(self.edit_equipment)
        self.remove_equipment_pushButton.clicked.connect(self.delete_equipment)


    def add_equipment(self):
        """Open the dialog to add a new equipment"""

        dialog = AddUpdateEquipmentDialog(self)

        if dialog.exec() == 1:  # QDialog.Accepted
            equipment_data = dialog.get_equipment_data()

            # Check if equipment name is empty, if so, do not add the equipment and return
            if not equipment_data["equipment_name"].strip():
                return

            # Add the new equipment to the equipment table
            row_position = self.equipment_tableWidget.rowCount()
            self.equipment_tableWidget.insertRow(row_position)

            # Populate the new row with the equipment data
            for column, key in enumerate(equipment_data.keys()):
                item = QTableWidgetItem(str(equipment_data[key]))
                self.equipment_tableWidget.setItem(row_position, column, item)

            self._recalculate_current_encumbrance()


    def edit_equipment(self, equipment_item):
        """Open the dialog to edit an existing equipment"""

        dialog = AddUpdateEquipmentDialog(self, item_data=equipment_item)

        if dialog.exec() == 1:  # QDialog.Accepted
            equipment_data = dialog.get_equipment_data()

            # Check if equipment name is empty, if so, do not add the equipment and return
            if not equipment_data["equipment_name"].strip():
                return
            
            # Update the existing equipment in the equipment table
            row = equipment_item.row()

            for column, key in enumerate(equipment_data.keys()):
                item = QTableWidgetItem(str(equipment_data[key]))
                self.equipment_tableWidget.setItem(row, column, item)

            self._recalculate_current_encumbrance()


    def delete_equipment(self):
        """Delete the selected equipment from the equipment table"""

        selected_items = self.equipment_tableWidget.selectedItems()

        if selected_items:
            row = selected_items[0].row()
            self.equipment_tableWidget.removeRow(row)

            self._recalculate_current_encumbrance()


    def _recalculate_current_encumbrance(self):
        """Recalculate the current encumbrance based on the equipment in the equipment table"""

        total_encumbrance = 0.0

        for row in range(self.equipment_tableWidget.rowCount()):
            item_count = self.equipment_tableWidget.item(row, 0)
            item_encumbrance = self.equipment_tableWidget.item(row, 1)

            if item_count and item_encumbrance:
                try:
                    encumbrance = float(item_encumbrance.text()) * int(item_count.text())
                    total_encumbrance += encumbrance
                except ValueError:
                    pass
            
        self.current_encumbrance_doubleSpinBox.setValue(total_encumbrance)
