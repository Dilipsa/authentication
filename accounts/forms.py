from django import forms
from django.contrib.auth.models import User


class SignUpForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='name')
    last_name = forms.CharField(max_length=30, label='last name')
    # category_choice = forms.CharField(max_length=20, label='choice', required=False)
    gender = forms.CharField(max_length=30, label='gender')
    mother_tongue = forms.CharField(max_length=255, label='mother tongue')
    profile = forms.ImageField(required=False)
    phone = forms.IntegerField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'gender', 'mother_tongue', 'profile', 'phone']

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        up = user.account

        up.gender = self.cleaned_data['gender']
        up.mother_tongue = self.cleaned_data['mother_tongue']
        up.profile = self.cleaned_data['profile']
        up.phone = self.cleaned_data['phone']

        user.save()
        up.save()


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(disabled=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']
