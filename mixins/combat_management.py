"""Combat and attributes management functionality for character sheet"""

from settings import CLASS_OPTIONS, LEVELING


class CombatManagement:
    """Mixin class for combat values and attributes management"""

    def connect_combat_value_signals(self):
        """Connect signals for combat value updates"""

        # Update combat values when character class change
        self.class_comboBox.currentTextChanged.connect(self.update_combat_values)

        # Update combat values when character level change
        self.level_spinBox.valueChanged.connect(self.update_combat_values)

        # Update combat valuse when shield or other modifiers change
        self.defense_shield_spinBox.valueChanged.connect(self.update_combat_values)
        self.defense_other_spinBox.valueChanged.connect(self.update_combat_values)
        self.initiative_other_spinBox.valueChanged.connect(self.update_combat_values)


    def update_combat_values(self):
        """Update the combat values (initiative, defense and attack) based on the character's class, level and attributes"""

        # Get the character's class, level and relevant attribute modifiers
        character_class: str = self.class_comboBox.currentText()
        character_class_data = CLASS_OPTIONS.get(character_class, {})
        character_class_attack_grade = character_class_data.get("attack", "bad")
        character_class_defense_grade = character_class_data.get("defense", "bad")

        character_level: int = self.level_spinBox.value()
        character_level_data = LEVELING.get(character_level, {})
        strength_modifier: int = self.get_attribute_modifier_by_name("strength")
        dexterity_modifier: int = self.get_attribute_modifier_by_name("dexterity")

        # Set initiative
        self.initiative_base_spinBox.setValue(dexterity_modifier)
        self.initiative_all_spinBox.setValue(self.initiative_base_spinBox.value() + self.initiative_other_spinBox.value())

        # Set defense
        defense_base = 6 + character_level_data.get("defense", {}).get(character_class_defense_grade, 0)
        self.defense_base_spinBox.setValue(defense_base)
        self.defense_all_spinBox.setValue(self.defense_base_spinBox.value() + self.defense_shield_spinBox.value() + self.defense_other_spinBox.value() + dexterity_modifier)

        # Set attack
        close_combat_attack = character_level_data.get("attack", {}).get(character_class_attack_grade, 0) + strength_modifier
        self.close_combat_attack_spinBox.setValue(close_combat_attack)

        ranged_combat_attack = character_level_data.get("attack", {}).get(character_class_attack_grade, 0) + dexterity_modifier
        self.ranged_combat_attack_spinBox.setValue(ranged_combat_attack)


    def connect_saves_value_signals(self):
        """Connect signals for saves value updates"""

        # Update saves values when character class change
        self.class_comboBox.currentTextChanged.connect(self.update_saves_values)

        # Update saves values when character level change
        self.level_spinBox.valueChanged.connect(self.update_saves_values)

        # Update saves valuse when other modifiers change
        self.constitution_save_other_spinBox.valueChanged.connect(self.update_saves_values)
        self.reflex_save_other_spinBox.valueChanged.connect(self.update_saves_values)
        self.willpower_save_other_spinBox.valueChanged.connect(self.update_saves_values)


    def update_saves_values(self):
        """Update the saves values (constitution, reflex and willpower) based on the character's class, level and attributes"""

        # Get the character's class, level and relevant attribute modifiers
        character_class: str = self.class_comboBox.currentText()
        character_class_data = CLASS_OPTIONS.get(character_class, {})
        character_class_willpower_save_grade = character_class_data.get("willpower_save", "bad")
        character_class_reflex_save_grade = character_class_data.get("reflex_save", "bad")
        character_class_constitution_save_grade = character_class_data.get("constitution_save", "bad")

        character_level: int = self.level_spinBox.value()
        character_level_data = LEVELING.get(character_level, {})
        dexterity_modifier: int = self.get_attribute_modifier_by_name("dexterity")
        stamina_modifier: int = self.get_attribute_modifier_by_name("stamina")
        wisdom_modifier: int = self.get_attribute_modifier_by_name("wisdom")

        # Set constitution save
        constitution_save_base = character_level_data.get("saves", {}).get(character_class_constitution_save_grade, 0) + stamina_modifier
        self.constitution_save_base_spinBox.setValue(constitution_save_base)
        self.constitution_save_all_spinBox.setValue(constitution_save_base + self.constitution_save_other_spinBox.value())

        # Set reflex save
        reflex_save_base = character_level_data.get("saves", {}).get(character_class_reflex_save_grade, 0) + dexterity_modifier
        self.reflex_save_base_spinBox.setValue(reflex_save_base)
        self.reflex_save_all_spinBox.setValue(reflex_save_base + self.reflex_save_other_spinBox.value())

        # Set willpower save
        willpower_save_base = character_level_data.get("saves", {}).get(character_class_willpower_save_grade, 0) + wisdom_modifier
        self.willpower_save_base_spinBox.setValue(willpower_save_base)
        self.willpower_save_all_spinBox.setValue(willpower_save_base + self.willpower_save_other_spinBox.value())
