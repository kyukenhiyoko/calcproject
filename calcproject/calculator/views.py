# calculator/views.py

from django.shortcuts import render
from .forms import CalculationForm
from datetime import datetime
from xhtml2pdf import pisa
from django.http import HttpResponse
from django.template.loader import render_to_string

def render_to_pdf(template_src, context_dict={}):
    template = render_to_string(template_src, context_dict)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="calculation_result.pdf"'
    
    # PDF生成
    pisa_status = pisa.CreatePDF(template, dest=response)
    
    if pisa_status.err:
        return HttpResponse('PDF生成中にエラーが発生しました')
    return response

def calculate(request):
    result = {}

    if request.method == 'POST':
        form = CalculationForm(request.POST)

        if form.is_valid():
            # 入力項目の取得
            rent = form.cleaned_data['rent']
            maintenance = form.cleaned_data['maintenance']
            others = form.cleaned_data['others']
            date_this_month = form.cleaned_data['date_this_month']
            days_this_month = form.cleaned_data['days_this_month']
            date_next_month = form.cleaned_data['date_next_month']
            days_next_month = form.cleaned_data['days_next_month']
            deposit_months = form.cleaned_data['deposit_months']
            key_money_months = form.cleaned_data['key_money_months']
            fire_insurance = form.cleaned_data['fire_insurance']
            other1 = form.cleaned_data.get('other1', 0)  # デフォルト値を指定
            other2 = form.cleaned_data.get('other2', 0)
            other3 = form.cleaned_data.get('other3', 0)
            other4 = form.cleaned_data.get('other4', 0)
            other5 = form.cleaned_data.get('other5', 0)
            broker_fee = form.cleaned_data['broker_fee']
            discount = form.cleaned_data['discount']
            other_fees = form.cleaned_data['other_fees']

            # 賃料、共益費、その他の合計
            total_1_to_3 = rent + maintenance + others

            # 当月と次月の日数計算
            total_this_month = rent * days_this_month
            total_next_month = rent * days_next_month
            total_months = total_this_month + total_next_month

            # 敷金、礼金、火災保険、その他
            total_6_to_12 = (rent * deposit_months) + (rent * key_money_months) + fire_insurance + other1 + other2 + other3 + other4 + other5

            # 仲介手数料、紹介割引、その他の合計
            total_14_to_16 = broker_fee + discount + other_fees

            # 結果を辞書に格納
            result = {
                'rent': rent,
                'maintenance': maintenance,
                'others': others,
                'total_1_to_3': total_1_to_3,
                'days_this_month': days_this_month,
                'date_this_month': date_this_month,
                'days_next_month': days_next_month,
                'date_next_month': date_next_month,
                'total_this_month': total_this_month,
                'total_next_month': total_next_month,
                'total_months': total_months,
                'total_6_to_12': total_6_to_12,
                'broker_fee': broker_fee,
                'discount': discount,
                'other_fees': other_fees,
                'total_14_to_16': total_14_to_16
            }

            # PDF出力の場合
            if 'pdf' in request.POST:
                return render_to_pdf('calculator/pdf_template.html', result)
            else:
                return render(request, 'calculator/result.html', {'result': result})

    else:
        form = CalculationForm()

    return render(request, 'calculator/calculate.html', {'form': form})
