from django.forms import ModelForm
from .models import Member

class EditMemberForm(ModelForm):
    class Meta:
        model = Member
        fields = ['display_name', 'branch', 'work', 'address', 'country', 'indian_state', 'email', 'phone', 'photo']