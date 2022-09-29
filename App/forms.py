from django import forms
from .models import Train
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime


class TrainForm(forms.ModelForm):
    class Meta:
        model = Train
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TrainForm, self).__init__(*args, **kwargs)
        self.fields['date'] = JalaliDateField(label=('زمان'), widget=AdminJalaliDateWidget)
