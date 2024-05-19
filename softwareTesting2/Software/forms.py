from django import forms


class CommentForm(forms.Form):
    author = forms.CharField(max_length=50)
    email = forms.EmailField()
    website = forms.URLField(required=False)
    content = forms.CharField(widget=forms.Textarea)


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '********'}))
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'custom-control-input'}))