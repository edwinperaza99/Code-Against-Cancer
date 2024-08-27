from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

CANCER_TYPE_CHOICES = [
    ('bone', 'Bone Cancer'),
    ('brain_nervous', 'Brain and Nervous System Cancer'),
    ('breast', 'Breast Cancer'),
    ('colorectal', 'Colorectal Cancer'),
    ('digestive', 'Digestive System Cancer'),
    ('endocrine', 'Endocrine System Cancer'),
    ('eye', 'Eye Cancer'),
    ('genitourinary', 'Genitourinary Cancer'),
    ('gynecologic', 'Gynecologic Cancer'),
    ('head_neck', 'Head and Neck Cancer'),
    ('hematologic', 'Hematologic Cancer'),
    ('liver', 'Liver Cancer'),
    ('lung', 'Lung Cancer'),
    ('lymphoma', 'Lymphoma'),
    ('melanoma_skin', 'Melanoma and Skin Cancer'),
    ('oral', 'Oral Cancer'),
    ('pancreatic', 'Pancreatic Cancer'),
    ('prostate', 'Prostate Cancer'),
    ('sarcoma', 'Sarcoma'),
    ('stomach', 'Stomach Cancer'),
]

CANCER_STAGE_CHOICES = [
    ('I', 'Stage I'),
    ('II', 'Stage II'),
    ('III', 'Stage III'),
    ('IV', 'Stage IV'),
]

GENDER_CHOICES = [
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
]

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    cancer_type = forms.ChoiceField(choices=CANCER_TYPE_CHOICES)
    date_diagnosed = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2100)))
    cancer_stage = forms.ChoiceField(choices=CANCER_STAGE_CHOICES)
    gender = forms.ChoiceField(choices=GENDER_CHOICES)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'cancer_type', 'date_diagnosed', 'cancer_stage', 'gender']

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        
        if commit:
            user.save()
            # Check if UserProfile exists before creating
            user_profile, created = UserProfile.objects.get_or_create(
                user=user,
                defaults={
                    'cancer_type': self.cleaned_data['cancer_type'],
                    'date_diagnosed': self.cleaned_data['date_diagnosed'],
                    'cancer_stage': self.cleaned_data['cancer_stage'],
                    'gender': self.cleaned_data['gender']
                }
            )
            if not created:  # Update the existing profile with new data
                user_profile.cancer_type = self.cleaned_data['cancer_type']
                user_profile.date_diagnosed = self.cleaned_data['date_diagnosed']
                user_profile.cancer_stage = self.cleaned_data['cancer_stage']
                user_profile.gender = self.cleaned_data['gender']
                user_profile.save()

        return user