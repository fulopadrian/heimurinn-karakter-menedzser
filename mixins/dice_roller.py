import random

class DiceRollerMixin():
    """Mixin class for dice roller funcionality"""
    
    def connect_dice_roller_signals(self):
        """Connect signals for dice roller"""

        self.attack_test_pushButton.clicked.connect(self.do_attack_test)
        self.defense_test_pushButton.clicked.connect(self.do_defense_test)
        self.attribute_test_pushButton.clicked.connect(self.do_attribute_test)
        self.skill_test_pushButton.clicked.connect(self.do_skill_test)
        self.save_test_pushButton.clicked.connect(self.do_save_test)

        self.dice_roll_pushButton.clicked.connect(self.do_dice_roll)


    def do_attack_test(self):
        """Do an attack test with the chosen weapon"""
        
        # Get the selected weapon name from the combo box
        weapon_name = self.attack_test_comboBox.currentText()
        
        # Find the weapon in the weapons table
        weapon_row = None
        for row in range(self.weapons_tableWidget.rowCount()):
            if self.weapons_tableWidget.item(row, 0).text() == weapon_name:
                weapon_row = row
                break
        
        # If weapon not found, return
        if weapon_row is None:
            return
        
        # Get the linked attribute from the second column (index 1)
        linked_attribute = self.weapons_tableWidget.item(weapon_row, 1).text()
        
        # Get the attack modifier based on the linked attribute
        if linked_attribute == "Erő":
            attack_modifier = self.close_combat_attack_spinBox.value()
        elif linked_attribute == "Ügyesség":
            attack_modifier = self.ranged_combat_attack_spinBox.value()
        else:
            return
        
        # Get the critical threshold from the third column (index 2)
        critical_threshold = self.weapons_tableWidget.item(weapon_row, 2).text()
        
        # Parse the critical threshold
        critical_parts = critical_threshold.split("-")
        critical_min = int(critical_parts[0])
        critical_max = int(critical_parts[1])
        
        # Get the custom roll modifier
        roll_modifier = self.modifier_spinBox.value()
        
        # Roll 2d10 without modifier
        roll_result = self.roll_dice(2, 10)
        
        # Check if it's a critical
        is_critical = critical_min <= roll_result <= critical_max
        critical_indicator = "- Kritikus" if is_critical else ""
        
        # Calculate the roll result
        total_result = roll_result + attack_modifier + roll_modifier
        
        # Get character name
        character_name = self.name_lineEdit.text()
        
        # Format the result
        result_text = f"{character_name} - {weapon_name} támadás -> {total_result}{critical_indicator}"
        
        # Add to roll history
        self.roll_history_listWidget.addItem(result_text)
        self.roll_history_listWidget.scrollToBottom()


    def do_defense_test(self):
        """Do a defense test with the chosen method"""
        
        # Get the selected defense mode from the combo box
        defense_mode = self.defense_test_comboBox.currentText()
        
        # Get the full defense modifier
        defense_modifier = self.defense_all_spinBox.value()
        
        # Get the shield defense modifier
        shield_modifier = self.defense_shield_spinBox.value()
        
        # Get the dexterity modifier
        dexterity_modifier = self.dexterity_mod_spinBox.value()
        
        # Get the custom roll modifier
        roll_modifier = self.modifier_spinBox.value()
        
        # Get character name
        character_name = self.name_lineEdit.text()

        if defense_mode == "Alap":
            total_modifier = defense_modifier + roll_modifier
        elif defense_mode == "Meglepetés":
            total_modifier = defense_modifier - shield_modifier - dexterity_modifier + roll_modifier
        else:
            return
            
        # Roll 1d10
        roll_result = self.roll_dice(1, 10, total_modifier)

        # Format the result
        result_text = f"{character_name} - {defense_mode} védő próba -> {roll_result}"

        # Add to roll history
        self.roll_history_listWidget.addItem(result_text)
        self.roll_history_listWidget.scrollToBottom()


    def do_attribute_test(self):
        """Do an attribute test with the chosen attribute"""
        
        # Get the selected attribute label from the combo box
        attribute_label = self.attribute_test_comboBox.currentText()
        
        # Get the attribute value using the helper method
        attribute_value = self.get_attribute_value_by_label(attribute_label)

        # Get the roll modifier
        roll_modifier = self.modifier_spinBox.value()
        
        # Roll 2d10
        roll_result = self.roll_dice(2, 10, roll_modifier)
        
        # Calculate result
        result = "Sikeres" if roll_result <= attribute_value else "Sikertelen"

        # Calculate the difference
        difference = abs(roll_result - attribute_value)
        
        # Get character name
        character_name = self.name_lineEdit.text()
        
        # Format the result
        result_text = f"{character_name} - {result} {attribute_label} próba -> {roll_result} ({difference})"
        
        # Add to roll history
        self.roll_history_listWidget.addItem(result_text)
        self.roll_history_listWidget.scrollToBottom()


    def do_skill_test(self):
        """Do a skill test with the chosen skill"""
        
        # Get the selected skill name from the combo box
        skill_name = self.skill_test_comboBox.currentText()
        
        # Find the skill in the skills table
        skill_row = None
        for row in range(self.skills_tableWidget.rowCount()):
            if self.skills_tableWidget.item(row, 0).text() == skill_name:
                skill_row = row
                break
        
        # If skill not found, return
        if skill_row is None:
            return
        
        # Get the skill modifier from the fifth column (index 4)
        skill_modifier = int(self.skills_tableWidget.item(skill_row, 4).text())
        
        # Get the roll modifier from the spin box
        roll_modifier = self.modifier_spinBox.value()
        
        # Combine the modifiers
        total_modifier = skill_modifier + roll_modifier
        
        # Roll 2d10
        roll_result = self.roll_dice(2, 10, total_modifier)
        
        # Get character name
        character_name = self.name_lineEdit.text()
        
        # Format the result
        result_text = f"{character_name} - {skill_name} próba -> {roll_result}"
        
        # Add to roll history
        self.roll_history_listWidget.addItem(result_text)
        self.roll_history_listWidget.scrollToBottom()


    def do_save_test(self):
        """Do the chosen save test"""
        
        # Get the selected save name from the combo box
        save_name = self.save_test_comboBox.currentText()
        
        # Get the save modifier based on the selected save type
        if save_name == "Kitartás":
            save_modifier = self.constitution_save_all_spinBox.value()
        elif save_name == "Reflex":
            save_modifier = self.reflex_save_all_spinBox.value()
        elif save_name == "Akarat":
            save_modifier = self.willpower_save_all_spinBox.value()
        else:
            return
        
        # Get the custom roll modifier
        roll_modifier = self.modifier_spinBox.value()
        
        # Combine the modifiers
        total_modifier = save_modifier + roll_modifier
        
        # Roll 2d10
        roll_result = self.roll_dice(2, 10, total_modifier)
        
        # Get character name
        character_name = self.name_lineEdit.text()
        
        # Format the result
        result_text = f"{character_name} - {save_name} próba -> {roll_result}"
        
        # Add to roll history
        self.roll_history_listWidget.addItem(result_text)
        self.roll_history_listWidget.scrollToBottom()


    def do_dice_roll(self):
        """Do a dice roll"""

        # Get dice roll data
        dice_number = self.dice_number_spinBox.value()
        dice_side = self.dice_side_spinBox.value()
        roll_modifier = self.dice_modifier_spinBox.value()

        # Roll dice
        roll_result = self.roll_dice(dice_number, dice_side, roll_modifier)

        # Get character name
        character_name = self.name_lineEdit.text()

        # Format the result
        result_text = f"{character_name} - Dobás -> {roll_result}"

        # Add to roll history
        self.roll_history_listWidget.addItem(result_text)
        self.roll_history_listWidget.scrollToBottom()


    def roll_dice(self, dice_number: int = 1, dice_side: int = 2, modifier: int = 0):
        """Roll the specified number of dice with the specifed number of sides and add the specified modifier"""

        result = 0

        for _ in range(dice_number):
            result += random.randint(1, dice_side)
        
        return result + modifier