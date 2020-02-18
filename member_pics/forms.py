from django.forms import ModelForm
from .models import MemberPic

class EditMemberPicForm(ModelForm):
    class Meta:
        model = MemberPic
        fields = ['photo', 'caption']

class DeleteMemberPicForm(ModelForm):
    class Meta:
        model = MemberPic
        fields = []