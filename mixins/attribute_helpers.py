class AttributeHelpers:
    """Mixin class providing reusable attribute helper methods"""

    def get_attribute_modifier_by_name(self, attribute_name: str) -> int:
        """Return the modifier for a given attribute by its name"""

        return self.attributes[attribute_name]["modifier"].value()


    def set_attribute_modifier_by_name(self, attribute_name: str, modifier_value: int):
        """Set the modifier for a given attribute by its name"""

        self.attributes[attribute_name]["modifier"].setValue(modifier_value)


    def get_attribute_value_by_name(self, attribute_name: str) -> int:
        """Return the value for a given attribute by its name"""

        return self.attributes[attribute_name]["value"].value()


    def get_attribute_label_by_name(self, attribute_name: str) -> str:
        """Return the label for a given attribute by its name"""

        return self.attributes[attribute_name]["label"]


    def get_attribute_modifier_by_label(self, attribute_label: str) -> int:
        """Return the modifier for a given attribute by its label"""

        for _, attribute_values in self.attributes.items():
            if attribute_values["label"] == attribute_label:
                return attribute_values["modifier"].value()


    def get_attribute_value_by_label(self, attribute_label: str) -> int:
        """Return the value for a given attribute by its label"""

        for _, attribute_values in self.attributes.items():
            if attribute_values["label"] == attribute_label:
                return attribute_values["value"].value()
