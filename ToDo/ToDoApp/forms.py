from django import forms

from .models import Todo

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class ToDoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Todo
        exclude = ('user', 'done')
        widgets = {
            'date': DateInput(),
            'time': TimeInput()
        }

