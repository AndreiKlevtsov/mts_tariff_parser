from django import forms


class TariffFilterForm(forms.Form):
    is_gb = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={'class': 'btn-check', 'id': 'btncheck1',
               'autocomplete': 'on'}))
    is_tv = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={'class': 'btn-check', 'id': 'btncheck2',
               'autocomplete': 'on'}))
    is_min = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={'class': 'btn-check', 'id': 'btncheck3',
               'autocomplete': 'on'}))
