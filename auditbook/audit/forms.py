from django import forms
from django.forms import widgets
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import *
from captcha.fields import CaptchaField




class Login(forms.Form):
    user = forms.CharField(min_length=3,label='用户名',error_messages={'required':'该字段不能为空'})
    pwd = forms.CharField(min_length=3,label='密码',error_messages={'required':'该字段不能为空'},widget=widgets.PasswordInput())



class Reg(forms.Form):
    user = forms.CharField(min_length=3,label='用户名',error_messages={'required':'该字段不能为空'},widget=widgets.TextInput(attrs={'class':'form-control'}))
    pwd = forms.CharField(min_length=3,label='密码',error_messages={'required':'该字段不能为空'},widget=widgets.PasswordInput())
    repwd = forms.CharField(min_length=3,label='确认密码',error_messages={'required':'该字段不能为空'},widget=widgets.PasswordInput())
    email = forms.EmailField(label='邮箱地址',error_messages={'required':'该字段不能为空'})
    yanzhengma = CaptchaField()
    def clean_user(self):
        user = self.cleaned_data.get('user')
        user1 = User.objects.filter(username=user)
        if not user1:
            return user
        else:
            raise ValidationError('该用户已存在')

    def clean(self):
        pwd = self.cleaned_data.get('pwd')
        repwd = self.cleaned_data.get('repwd')
        if pwd and repwd:
            if pwd == repwd:
                return self.cleaned_data
            else:
                raise ValidationError('两次密码不一致')
        else:
            return self.cleaned_data


class Uploadfile(forms.ModelForm):
    class Meta:
        model = Zhiliangshouce
        fields = ['shouceno','shoucename','shouceauthor','shouceadd','fileclass']
        widgets = {
            'shouceno':forms.TextInput(attrs={'class':'form-control'}),
            'shoucename':forms.TextInput(attrs={'class':'form-control'}),
            'shouceauthor':forms.Select(attrs={'class':'form-control'}),
            'fileclass':forms.Select(attrs={'class':'form-control'}),
            'shouceadd':forms.FileInput(attrs={'class':'form-control'}),
        }


class Uploadstd(forms.ModelForm):
    class Meta:
        model = Stardands
        fields = '__all__'
        widgets = {
            'stdno':forms.TextInput(attrs={'class':'form-control'}),
            'stdname':forms.TextInput(attrs={'class':'form-control'}),
            'stdadd':forms.FileInput(attrs={'class':'form-control'}),
            'stdclass':forms.Select(attrs={'class':'form-control'}),
        }


class Personels(forms.ModelForm):
    class Meta:
        model = Personel
        fields = '__all__'
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'position':forms.TextInput(attrs={'class':'form-control'}),
            'profession':forms.Select(attrs={'class':'form-control'}),
        }


class Equips(forms.ModelForm):
    class Meta:
        model = Equip
        fields = '__all__'
        widgets = {
            'equipname':forms.TextInput(attrs={'class':'form-control'}),
            'equipno':forms.TextInput(attrs={'class':'form-control'}),
            'equipmodel':forms.TextInput(attrs={'class':'form-control'}),
            'equipfield':forms.Select(attrs={'class':'form-control'}),
        }


class Records(forms.ModelForm):
    class Meta:
        model = Record
        fields = '__all__'
        widgets = {
            'tabno':forms.TextInput(attrs={'class':'form-control'}),
            'tabname':forms.TextInput(attrs={'class':'form-control'}),
            'tabtype':forms.Select(attrs={'class':'form-control'}),
            'tabfile':forms.FileInput(attrs={'class':'form-control'}),
            'tabtime':forms.DateInput(attrs={'type':'date','class':'form-control'}),
        }

