from django import forms

from polls.models import Question, Person


class ContactForm(forms.Form):
    email = forms.EmailField(label='Recepient email', help_text = "can't end with test1")
    subject = forms.CharField(label='Subject', max_length=100, widget=forms.TextInput(attrs={"placeholder": "Subject"}))
    message = forms.CharField(label='Message', widget=forms.Textarea)

    def clean_email(self):
        email = self.cleaned_data['email']
        if email.endswith("@test1.com"):
            raise forms.ValidationError("Email cant' ends with 'test.com '")
        return email

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        subject = cleaned_data.get('subject')
        if email == subject:
            raise forms.ValidationError("Can't be email same with subject")

class QuestionForm(forms.Form):
    class Meta:
        model = Question
        field = ['question_text', 'pub_date']


class TriangleForm(forms.Form):
    a = forms.FloatField(label='Cathinus a',
                         widget=forms.TextInput(attrs={'placeholder': 'Number > 0'}))
    b = forms.FloatField(label='Cathinus b',
                         widget=forms.TextInput(attrs={'placeholder': 'Number > 0'}))

    def cleaning(self):
        a = self.cleaned_data.get('a')
        if a <= 0:
            raise forms.ValidationError("Cathinus can't be less 0 ")
        return a

    def cleaning_b(self):
        b = self.cleaned_data.get('b')
        if b <= 0:
            raise forms.ValidationError("The second corner of Canthious can't be 0")
        return b

class PersonForms(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'family_name']

