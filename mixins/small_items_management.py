"""Small items management functionality for character sheet"""

from PySide6.QtWidgets import QListWidgetItem

from dialogs.add_update_small_item_dialog import AddUpdateSmallItemDialog


class SmallItemsManagement:
    """Mixin class for small items management functionality"""

    def connect_small_item_signals(self):
        """Connect signals for the small items list to handle adding, editing and deleting small items"""

        self.add_small_item_pushButton.clicked.connect(self.add_small_item)
        self.small_items_listWidget.itemDoubleClicked.connect(self.edit_small_item)
        self.remove_small_item_pushButton.clicked.connect(self.delete_small_item)


    def add_small_item(self):
        """Open the dialog to add a new small item"""

        dialog = AddUpdateSmallItemDialog(self)

        if dialog.exec() == 1:  # QDialog.Accepted
            small_item_name = dialog.get_small_item_name()

            # Check if small item name is empty, if so, do not add the small item and return
            if not small_item_name.strip():
                return

            # Add the new small item to the small item list
            item = QListWidgetItem(small_item_name)
            self.small_items_listWidget.addItem(item)


    def edit_small_item(self, small_item):
        """Open the dialog to edit an existing small item"""

        dialog = AddUpdateSmallItemDialog(self, item_data=small_item)

        if dialog.exec() == 1:  # QDialog.Accepted
            small_item_name = dialog.get_small_item_name()

            # Check if small item name is empty, if so, do not update the small item and return
            if not small_item_name.strip():
                return

            # Update the existing small item in the small items list
            small_item.setText(small_item_name)


    def delete_small_item(self):
        """Delete the selected small item from the small items list"""

        selected_item = self.small_items_listWidget.currentItem()

        if selected_item:
            row = self.small_items_listWidget.row(selected_item)
            self.small_items_listWidget.takeItem(row)
