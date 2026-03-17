from PySide6.QtWidgets import QDialog
from ui.skald_attack_defense_options_dialog import Ui_SkaldAttackDefenseOptionsDialog
from settings import SKALD_ATTACK_DEFENSE_OPTION_RULE

class SkaldAttackDefenseOptionsDialog(QDialog, Ui_SkaldAttackDefenseOptionsDialog):
    """Class for the dialog to apply optional priority for attack or defense for skalds"""

    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.setupUi(self)

        # Initialize the dialog
        self.initialize_dialog()


    def initialize_dialog(self):
        """Initialize the dialog"""

        # Connect dialog buttonBox signals
        self.confirm_reject_skald_attack_defense_options_buttonBox.accepted.connect(self.accept)
        self.confirm_reject_skald_attack_defense_options_buttonBox.rejected.connect(self.reject)

        # Set rule description
        self.rule_description_textEdit.setText(SKALD_ATTACK_DEFENSE_OPTION_RULE)


    def get_attack_defense_option(self) -> dict:
        """Get the choosen attack or defense option"""

        result = {
            "attack": "good" if self.higher_attack_radioButton.isChecked() else "average",
            "defense": "good" if self.higher_defense_radioButton.isChecked() else "average"
        }

        return result