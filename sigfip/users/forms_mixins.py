from django.forms import ModelForm, Textarea, TextInput


class NameFormFields(ModelForm):

    class Meta:

        fields = ['name', 'description']
        widgets = {
            'name': TextInput(),
            'description': Textarea(),
        }
