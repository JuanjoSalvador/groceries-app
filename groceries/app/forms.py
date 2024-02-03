from django.forms import (
    ModelForm,
    CharField,
    ChoiceField,
    FloatField,
    TextInput,
    Textarea,
    NumberInput,
)
from django.forms.utils import ErrorList

from .models import Store, Product


class ProductAddForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductAddForm, self).__init__(*args, **kwargs)
        stores = Store.objects.values_list("id", "name")
        self.fields["store"] = ChoiceField(choices=(*stores,))

    name = CharField(
        widget=TextInput(
            attrs={"class": "input", "maxlength": 80, "autocomplete": "off"}
        )
    )
    brand = CharField(
        widget=TextInput(
            attrs={"class": "input", "maxlength": 80, "autocomplete": "off"}
        )
    )
    description = CharField(
        widget=Textarea(
            attrs={"class": "textarea", "maxlength": 500, "autocomplete": "off"}
        )
    )
    price = FloatField(
        widget=NumberInput(attrs={"class": "input", "autocomplete": "off"})
    )
    weight = FloatField(
        widget=NumberInput(attrs={"class": "input", "autocomplete": "off"})
    )
    volume = FloatField(
        widget=NumberInput(attrs={"class": "input", "autocomplete": "off"})
    )

    def clean_store(self):
        data = self.cleaned_data["store"]
        return Store.objects.get(pk=data)

    class Meta:
        model = Product
        fields = ["name", "brand", "description", "price", "weight", "volume", "store"]

    # def clean_last_name(self):
    #     data = self.cleaned_data['last_name']

    #     if len(data) > 30:
    #         raise ValidationError('Apellidos demasiado largos.')

    #     return data

    # def clean_email(self):
    #     data = self.cleaned_data['email']

    #     if len(data) > 60:
    #         raise ValidationError('Correo electrónico demasiado largo.')

    #     return data

    # def clean_phone_number(self):
    #     data = self.cleaned_data['phone_number']

    #     if not re.search("[0-9]{9}", data):
    #         raise ValidationError('Introduce un teléfono válido.')

    #     return data


class BulmaErrorList(ErrorList):
    def __str__(self):
        return self.as_text()

    def as_text(self):
        return "%s" % "".join(["%s" % e for e in self])
