from django import forms


class ContactForm(forms.Form):
    """
    Contact Form on Landing Page
    """
    SUBJECT_CHOICES = (
        ('Bulk order request',
         'Bulk order request'),
        ('Product complaint', 'Product complaint'),
        ('Coorperation request', 'Coorperation request'),
        ('Other', 'Other'),
    )

    name = forms.CharField(
        label="Name"
    )
    email = forms.EmailField(
        label="Email"
    )
    subject = forms.CharField(
        label="Subject",
        widget=forms.Select(choices=SUBJECT_CHOICES),
    )
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(attrs={
            "rows": 7,
        })
    )

    class Meta:
        fields = ['name', 'email', 'subject', 'message']