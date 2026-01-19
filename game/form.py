from django import forms


class GameForm(forms.Form):
    COLOR_CHOICES = (
        ('', '---'),
        ('white', 'White'),
        ('black', 'Black'),
    )

    VARIANT_CHOICES = (('standard', 'Standard'), ('', 'By correspondence'))

    username = forms.CharField(label="Name", max_length=100)
    rated = forms.BooleanField(label="Rated", initial=False, required=False)
    clock_limit = forms.IntegerField(label="Clock Limit", initial=15 * 60, min_value=1) # 15 min
    clock_increment = forms.IntegerField(label="Clock Limit", initial=15, min_value=1)
    color = forms.ChoiceField(label="I play", choices=COLOR_CHOICES, required=False)
    variant = forms.ChoiceField(label="Variant", choices=VARIANT_CHOICES, initial='standard')


