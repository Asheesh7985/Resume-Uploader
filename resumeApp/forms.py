from django import forms 
from .models import Resume

gender_choice = (
    ('Male','Male'),
    ('Female','Female')
)

JOB_CITY_CHOICE = (
    ('Lucknow','Lucknow'),
    ('Kolkata','KOlkata'),
    ('Delhi NCR','Delhi NCR'),
    ('Pune','Pune'),
    ('Mumbai','Mumbai'),
)

class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=gender_choice,widget=forms.RadioSelect)
    job_city = forms.MultipleChoiceField(label='Preferd Job Locations', 
               choices=JOB_CITY_CHOICE,widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Resume 
        fields = '__all__'

        labels = {'name':'Full Name','dob': 'Date of Birth','pin':'Pin Code','mobile':'Contact',
                  'email':'Email ID','profile_image':'Profile Image','my_file':'Document'}
        

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pin':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-select'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            
            }
