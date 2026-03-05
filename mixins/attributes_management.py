"""Attributes management functionality for character sheet"""

from functools import partial
from settings import ATTRIBUTE_MODIFIERS


class AttributesManagement():
    """Mixin class for attributes management functionality"""

    def connect_attribute_signals(self):
        """Connect signals for attribute spinboxes to update modifiers"""

        for attribute_name in self.attributes:
            attribute_spinbox = self.attributes[attribute_name]["value"]
            attribute_spinbox.valueChanged.connect(partial(self.on_attribute_changed, attribute_name))


    def on_attribute_changed(self, attribute_name: str, attribute_value: int):
        """Handle changes to attribute values"""

        # Update the modifier for the changed attribute
        self.update_attribute(attribute_name, attribute_value)

        # Recalculate cold resistance if stamina was changed
        if attribute_name == "stamina":
            self.cold_resistance_spinBox.setValue(3 + self.get_attribute_modifier_by_name("stamina"))

        # Recalculate skill values for skills based on the changed attribute
        self.recalculate_skills(attribute_name)

        # Recalculate max encumbrance if strength was changed
        if attribute_name == "strength":
            self.calculate_max_encumbrance()

        # Recalculate combat values if strength or dexterity was changed
        if attribute_name in ["strength", "dexterity"]:
            self.update_combat_values()

        # Recalculate saves values if stamina, dexterity or wisdom was changed
        if attribute_name in ["stamina", "dexterity", "wisdom"]:
            self.update_saves_values()


    def update_attribute(self, attribute_name: str, attribute_value: int = None):
        """Update the modifier for a given attribute based on its value"""

        if attribute_value is None:
            attribute_value = self.get_attribute_value_by_name(attribute_name)

        for limit, modifier in ATTRIBUTE_MODIFIERS.items():
            if attribute_value >= limit:
                self.set_attribute_modifier_by_name(attribute_name, modifier)
                break


    def calculate_max_encumbrance(self):
        """Recalculate the maximum encumbrance based on the character's strength modifier"""

        strength_modifier = self.get_attribute_modifier_by_name("strength")
        max_encumbrance = 20 + (strength_modifier * 3)

        self.max_encumbrance_doubleSpinBox.setValue(max_encumbrance)



