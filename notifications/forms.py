from django import forms
from django.utils import timezone

from .models import User, Notification


class NotificationForm(forms.ModelForm):
    participants = forms.ModelMultipleChoiceField(queryset=User.objects.all(), widget=forms.CheckboxSelectMultiple,
                                                  required=True)

    class Meta:
        model = Notification
        fields = ('subject', 'message', 'participants', 'send_at',)

    def clean_send_at(self):
        now = timezone.now()
        data = self.cleaned_data['send_at']
        if data < now:
            self.add_error('send_at', 'The date must not be less than today')
        return data
