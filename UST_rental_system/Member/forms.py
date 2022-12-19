from django import forms
from .models import Member

class MemberModelForm(forms.ModelForm):
    
    class Meta:
        model = Member
        fields = ('email','password', 'name', 'school_id','identity','sex','birthday','tel','image')
        
        #choices
        identity_choices = [('1','一般會員'), ('2','場材管理員'),('3','系統管理員')]
        gender_choices=[('1','男'), ('2','女')]

        widgets = {
            'email':forms.EmailInput(attrs={'class': 'form-control'}),
            'password':forms.PasswordInput(attrs={'class': 'form-control'}),
            'name':forms.TextInput(attrs={'class': 'form-control'}),
            'school_id': forms.Select(attrs={'class': 'form-select'}),
            'identity': forms.Select(choices=(identity_choices), attrs={'class': 'form-select'}),
            'sex': forms.Select(choices=(gender_choices), attrs={'class': 'form-select'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control datetimepicker-input', 'data-target': '#datetimepicker1','type':'date'}),
            'tel': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'})
        }
        
        labels = {
            'email': '電子信箱',
            'password': '密碼',
            'name': '姓名',
            'school_id': '所屬學校',
            'identity': '身份',
            'sex': '性別',
            'birthday': '生日',
            'tel': '聯絡電話',
            'image': '個人照片(近三個月)',
        }


class LoginModelForm(forms.ModelForm):
    
    class Meta:
        model = Member
        fields = ('email','password')

        widgets = {
            'email':forms.EmailInput(attrs={'class': 'form-control'}),
            'password':forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        
        labels = {
            'email': '電子信箱',
            'password': '密碼'
        }

# class UpdateModelForm(forms.ModelForm):
    
#     class Meta:
#         model = Member
#         fields = ('name','oldpassword','newpassword','telephone')

#         widgets = {
#             'name':forms.TextInput(attrs={'class': 'form-control'}),
#             'oldpassword':forms.PasswordInput(attrs={'class': 'form-control'}),
#             'newpassword':forms.PasswordInput(attrs={'class': 'form-control'}),
#             'telephone': forms.TextInput(attrs={'class': 'form-control'})
#         }
        
#         labels = {
#             'name': '姓名',
#             'oldpassword': '原本密碼',
#             'newpassword':'修改密碼',
#             'telephone':'電話'
#         }
