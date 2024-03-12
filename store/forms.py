from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django import forms
from .models import Profile




class UserInfoForm(forms.ModelForm):

	phone = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'تلفن'}), required=False)
	app =  forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'پیام رسانی که استفاده میکنید'}), required=False)
	city =  forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'شهر'}), required=False)
	address1 = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'آدرس اول'}), required=False)
	address2 = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'آدرس دوم'}), required=False)
	post = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'کد پستی'}), required=False)

	class Meta:
		model = Profile
		fields = ('phone', 'app', 'city', 'address1', 'address2', 'post',)










class ChangePasswordForm(SetPasswordForm):
	class Meta :
		model = User
		fields = ['new_password1', 'new_password2']
	

	def __init__(self, *args, **kwargs):
		super(ChangePasswordForm, self).__init__(*args, **kwargs)

		self.fields['new_password1'].widget.attrs['class'] = 'input-field'
		self.fields['new_password1'].widget.attrs['placeholder'] = 'رمز عبور'
		self.fields['new_password1'].label = ''
		self.fields['new_password1'].help_text = '<ul class="form-text text-muted small"><li>رمز شما باید حداقل 8 کارکتر داشته باشد.</li><li>از اشکال هم در رمز خود استفاده کنید.</li><li>از حروف انگلیسی استفاده کنید .</li></ul>'

		self.fields['new_password2'].widget.attrs['class'] = 'input-field'
		self.fields['new_password2'].widget.attrs['placeholder'] = 'تکرار رمز عبور'
		self.fields['new_password2'].label = ''
		self.fields['new_password2'].help_text = ''




class UpdateUserForm(UserChangeForm):
	password = None
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'input-field', 'placeholder':'ایمیل' }))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'input-field', 'placeholder':'نام'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'input-field', 'placeholder':'نام خانوادگی'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email')

	def __init__(self, *args, **kwargs):
		super(UpdateUserForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'input-field'
		self.fields['username'].widget.attrs['placeholder'] = 'نام کاربری'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>ترجیحا با حروف انگلیسی پر شود. نهایت 150 حرف و از اشکال @/./+/-/_ نمیتوان استفاده کرد ,  (در صورت تکراری بودن نام کاربری نمیتوانید ثبت نام کنید).</small></span>'




class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'input-field', 'placeholder':'ایمیل' }), required=False)
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'input-field', 'placeholder':'نام'}), required=False)
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'input-field', 'placeholder':'نام خانوادگی'}), required=False)

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'input-field'
		self.fields['username'].widget.attrs['placeholder'] = 'نام کاربری'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>ترجیحا با حروف انگلیسی پر شود. نهایت 150 حرف و از اشکال @/./+/-/_ نمیتوان استفاده کرد ,  (در صورت تکراری بودن نام کاربری نمیتوانید ثبت نام کنید).</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'input-field'
		self.fields['password1'].widget.attrs['placeholder'] = 'رمز عبور'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>رمز شما باید حداقل 8 کارکتر داشته باشد.</li><li>از اشکال هم در رمز خود استفاده کنید.</li><li>از حروف انگلیسی استفاده کنید .</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'input-field'
		self.fields['password2'].widget.attrs['placeholder'] = 'تکرار رمز عبور'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = ''


