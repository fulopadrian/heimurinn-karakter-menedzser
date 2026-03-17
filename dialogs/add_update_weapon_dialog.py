from PySide6.QtWidgets import QDialog, QTableWidgetItem
from ui.add_update_weapon_dialog_ui import Ui_AddUpdateWeaponDialog

class AddUpdateWeaponDialog(QDialog, Ui_AddUpdateWeaponDialog):
    """Class for the dialog to add or update a weapon"""

    def __init__(self, parent = None, item_data: QTableWidgetItem = None):
        super().__init__(parent)
        
        self.setupUi(self)

        # Setup
        self.item_data: QTableWidgetItem = item_data

        # Initialize the dialog
        self.initialize_dialog()


    def initialize_dialog(self):
        """Initialize the dialog with default or existing data if provided (in case of editing an existing weapon)"""

        # Connect dialog buttonBox signals
        self.confirm_reject_weapon_buttonBox.accepted.connect(self.accept)
        self.confirm_reject_weapon_buttonBox.rejected.connect(self.reject)

        # Set linked attribute combo box
        self.weapon_linked_attribute_comboBox.addItems(["Erő", "Ügyesség"])

        if self.item_data:
            row = self.item_data.row()

            # Get skill data from the item_data
            weapon_data = []
            for column in range(self.item_data.tableWidget().columnCount()):
                cell_item = self.item_data.tableWidget().item(row, column)
                weapon_data.append(cell_item.text() if cell_item else "")
            
            # Set the existing data to the dialog components
            self.weapon_name_lineEdit.setText(weapon_data[0])
            self.weapon_linked_attribute_comboBox.setCurrentText(weapon_data[1])

            critical_threshold_min, critical_threshold_max = self.__parse_critical_threshold(weapon_data[2])
            self.critical_threshold_min_spinBox.setValue(critical_threshold_min)
            self.critical_threshold_max_spinBox.setValue(critical_threshold_max)

            damage_dice_number, damage_dice_side, damage_dice_modifier = self.__parse_damage_dice(weapon_data[3])
            self.damage_dice_number_spinBox.setValue(damage_dice_number)
            self.damage_dice_side_spinBox.setValue(damage_dice_side)
            self.damage_dice_modifier_spinBox.setValue(damage_dice_modifier)

            self.weapon_special_lineEdit.setText(weapon_data[4])


    def __parse_critical_threshold(self, critical_threshold: str) -> tuple:
        """Parse the critical threshold string and return the minimum and maximum values as integers"""

        min_threshold, max_threshold = critical_threshold.split("-")

        return int(min_threshold), int(max_threshold)


    def __parse_damage_dice(self, damage_dice: str) -> tuple:
        """Parse the damage dice string and return the number of dice, sides and modifier as integers"""

        if "+" in damage_dice:
            dice_part, modifier_part = damage_dice.split("+")
            modifier = int(modifier_part)
        else:
            dice_part = damage_dice
            modifier = 0

        number_of_dice, sides = map(int, dice_part.split("D"))

        return number_of_dice, sides, modifier


    def get_weapon_data(self) -> dict:
        """Get the weapon data from the dialog components"""

        weapon_name = self.weapon_name_lineEdit.text()

        linked_attribute = self.weapon_linked_attribute_comboBox.currentText()

        critical_threahold = self.__convert_critical_threshold_to_string()

        damage_dice = self.__convert_damage_dice_to_string()

        weapon_special = self.weapon_special_lineEdit.text()

        return {
            "weapon_name": weapon_name,
            "linked_attribute": linked_attribute,
            "critical_threshold": critical_threahold,
            "damage_dice": damage_dice,
            "weapon_special": weapon_special
        }


    def __convert_critical_threshold_to_string(self) -> str:
        """Convert the critical threshold values to string format"""

        return f"{self.critical_threshold_min_spinBox.value()}-{self.critical_threshold_max_spinBox.value()}"
    

    def __convert_damage_dice_to_string(self) -> str:
        """Convert the damage dice values to string format"""

        damage_dice = f"{self.damage_dice_number_spinBox.value()}D{self.damage_dice_side_spinBox.value()}"
        if self.damage_dice_modifier_spinBox.value() != 0:
            damage_dice += f"+{self.damage_dice_modifier_spinBox.value()}"

        return damage_dice