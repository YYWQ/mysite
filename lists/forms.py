from django import forms
from lists.models import Item
EMPTY_LIST_ERROR = "You can't have an empty list item"

#django提供的ModelForm类用于自动生成模型的表单
class ItemForm(forms.models.ModelForm):
    class Meta:
        model = Item
        fields = ('text',)
        widgets={
            'text': forms.fields.TextInput(attrs={
                'placeholder': 'Enter a to-do item',
                'class': 'form-control input-lg',
            }),
        }
        error_messages = {
            'text': {'required': EMPTY_LIST_ERROR}
        }
    