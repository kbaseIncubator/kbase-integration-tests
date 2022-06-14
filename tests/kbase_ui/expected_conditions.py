class element_attribute_is_value(object):
    def __init__(self, element, name, value):
        self.element = element
        self.name = name
        self.value = value

    def __call__(self, driver):
        if self.element.get_attribute(self.name) == self.value:
            return self.element
        else:
            return False


class element_attribute_has_value(object):
    def __init__(self, element, name, value):
        self.element = element
        self.name = name
        self.value = value

    def __call__(self, driver):
        if self.value in self.element.get_attribute(self.name):
            return self.element
        else:
            return False
