from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django import forms

from petstagram.pets.models import Pet


class PetForm(ModelForm):
    class Meta:
        model = Pet
        fields = ('name', 'date_of_birth', 'pet_photo')

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Pet name'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'pet_photo': forms.URLInput(attrs={'placeholder': 'Link to image'}),

        }

        labels = {
            'name': 'Pet name',
            'pet_photo': 'Link to image'
        }


class PetCreateForm(PetForm):
    pass


class ReadonlyFieldsFormMixin:
    readonly_fields = ()

    def _apply_readonly_on_fields(self):
        for field_name in self.readonly_field_names:
            self.fields[field_name].widget.attrs['readonly'] = 'readonly'

    @property
    def readonly_field_names(self):
        if self.readonly_fields == '__all__':
            return self.fields.keys()
        return self.readonly_fields


class PetEditForm(PetForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_of_birth'].widget.attrs['readonly'] = 'readonly'

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data.get('date_of_birth')
        if date_of_birth != self.instance.date_of_birth:
            raise ValidationError('Date of birth is readonly!')

        return self.instance.date_of_birth


class PetDeleteForm(ReadonlyFieldsFormMixin, PetForm):
    readonly_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_readonly_on_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
