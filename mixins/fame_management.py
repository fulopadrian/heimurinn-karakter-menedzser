from PySide6.QtWidgets import QTableWidgetItem
from dialogs.add_update_fame_dialog import AddUpdateFameDialog


class FameManagement:
    """Mixin class for fame management functionality"""

    def connect_fame_signals(self):
        """Connect signals for fame updates"""
        
        self.add_fame_pushButton.clicked.connect(self.add_fame)
        self.fame_tableWidget.itemDoubleClicked.connect(self.edit_fame)
        self.remove_fame_pushButton.clicked.connect(self.delete_fame)


    def add_fame(self):
        """Open dialog to add fame"""

        dialog = AddUpdateFameDialog(self)

        if dialog.exec() == 1:  # QDialog.Accepted
            fame_data = dialog.get_fame_data()

            # Check if fame description is empty, if so, do not add the fame and return
            if not fame_data["fame_description"].strip():
                return

            # Add the new fame to the fame table
            row_position = self.fame_tableWidget.rowCount()
            self.fame_tableWidget.insertRow(row_position)

            # Populate the new row with the fame data
            for column, key in enumerate(fame_data.keys()):
                item = QTableWidgetItem(str(fame_data[key]))
                self.fame_tableWidget.setItem(row_position, column, item)
            
            self._recalculate_current_fame()


    def edit_fame(self, fame_item):
        """Open dialog to edit an existing fame item"""

        dialog = AddUpdateFameDialog(self, item_data=fame_item)

        if dialog.exec() == 1:  # QDialog.Accepted
            fame_data = dialog.get_fame_data()

            # Check if fame name is empty, if so, do not add the fame and return
            if not fame_data["fame_description"].strip():
                return
            
            # Update the existing fame in the fame table
            row = fame_item.row()

            for column, key in enumerate(fame_data.keys()):
                item = QTableWidgetItem(str(fame_data[key]))
                self.fame_tableWidget.setItem(row, column, item)
            
            self._recalculate_current_fame()


    def delete_fame(self):
        """Delete the selected fame item from the fame list"""

        selected_items = self.fame_tableWidget.selectedItems()

        if selected_items:
            row = selected_items[0].row()
            self.fame_tableWidget.removeRow(row)
            
            self._recalculate_current_fame()


    def _recalculate_current_fame(self):
        """Update fame sum if fame added, modified or removed"""
        
        total_fame = 0
        
        for row in range(self.fame_tableWidget.rowCount()):
            fame_value_item = self.fame_tableWidget.item(row, 1)
            
            if fame_value_item:
                try:
                    fame_value = int(fame_value_item.text())
                    total_fame += fame_value
                except ValueError:
                    pass
        
        self.fame_spinBox.setValue(total_fame)
