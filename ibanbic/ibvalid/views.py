from django.shortcuts import render, render_to_response
from validation import IbanBicValidation
from django.template import RequestContext

def main(request):
    return render_to_response(
        'main.html',
        {},
        context_instance=RequestContext(request)
    )

def validate(request):
    iban = request.POST.get('iban')
    bic = request.POST.get('bic')
    answer = IbanBicValidation(iban, bic).val_execute()
    return render_to_response(
        'main.html',
        {
            'iban': iban,
            'bic': bic,
            'iban_ok': answer[0][0],
            'bic_ok': answer[1][0],
            'iban_message': answer[0][1],
            'bic_message': answer[1][1]
        },
        context_instance=RequestContext(request)
    )


