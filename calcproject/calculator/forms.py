# calculator/forms.py

from django import forms

class CalculationForm(forms.Form):
    rent = forms.DecimalField(label='賃料', decimal_places=2, required=True)
    maintenance = forms.DecimalField(label='共益費', decimal_places=2, required=True)
    others = forms.DecimalField(label='その他', decimal_places=2, required=True)
    date_this_month = forms.DateField(label='指定した当月の日付', required=True)
    days_this_month = forms.IntegerField(label='当月の日数', required=True)
    date_next_month = forms.DateField(label='次月の日付', required=True)
    days_next_month = forms.IntegerField(label='次月の日数', required=True)
    deposit_months = forms.DecimalField(label='敷金のヶ月', decimal_places=2, required=True)
    key_money_months = forms.DecimalField(label='礼金のヶ月', decimal_places=2, required=True)
    fire_insurance = forms.DecimalField(label='火災保険の金額', decimal_places=2, required=True)
    other1 = forms.DecimalField(label='その他1', decimal_places=2, required=False)
    other2 = forms.DecimalField(label='その他2', decimal_places=2, required=False)
    other3 = forms.DecimalField(label='その他3', decimal_places=2, required=False)
    other4 = forms.DecimalField(label='その他4', decimal_places=2, required=False)
    other5 = forms.DecimalField(label='その他5', decimal_places=2, required=False)
    broker_fee = forms.DecimalField(label='仲介手数料', decimal_places=2, required=True)
    discount = forms.DecimalField(label='ご紹介割引', decimal_places=2, required=True)
    other_fees = forms.DecimalField(label='その他', decimal_places=2, required=True)
