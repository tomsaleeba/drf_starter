from dynamic_rest.fields import DynamicComputedField


def compute_first_name(name_value):
    parts = name_value.split()
    return ' '.join(parts[0:-1]) if len(parts) > 1 else name_value


def compute_surname(name_value):
    parts = name_value.split()
    return parts[-1] if len(parts) > 1 else None


class UserNameField(DynamicComputedField):
    """ convert the V2 format back to V1 """
    def get_attribute(self, instance):
        result = '%s %s' % (instance.first_name, instance.surname)
        return result.strip()

    def to_representation(self, value):
        return value


class UserFirstNameField(DynamicComputedField):
    """ convert V1 data to V2 format if required """
    def get_attribute(self, instance):
        return compute_first_name(instance.first_name)

    def to_representation(self, value):
        return value


class UserSurnameField(DynamicComputedField):
    """ convert V1 data to V2 format if required """
    def get_attribute(self, instance):
        if (instance.surname):
            return instance.surname
        return compute_surname(instance.first_name)

    def to_representation(self, value):
        return value
