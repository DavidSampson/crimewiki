from django.forms.fields import MultiValueField


class BooleanModelChoiceField(MultiValueField):
    def __init__(self, **kwargs):
        fields = (

        )
        super().__init__(
            error_messages=error_messages, fields=fields,
            require_all_fields=False, **kwargs
        )
