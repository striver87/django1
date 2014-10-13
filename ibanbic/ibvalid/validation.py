import sys
import re
from models import Length

class IbanBicValidation(object):

    def __init__(self, iban, bic):
        self.iban = iban
        self.bic = bic

    def convert_num(self, pos_integer):
        if pos_integer.isalpha():
            return str(ord(pos_integer.lower()) - ord('a') + 10)
        else:
            return pos_integer

    def iban_validation(self):
        if self.iban == "":
            return [True, u""]
        if not self.iban.isalnum():
            return [False, u'In IBAN only alfanumeric sighns are possible']

        prefix = self.iban[:2].lower()
        if not prefix.isalpha():
            return [False, u'Number should start with the country code']

        try:
            expected_length = Length.objects.get(country=prefix)
        except:
            expected_length = None

        if expected_length is not None:
            if expected_length.length != len(self.iban):
                return False, u'''
                    For country %s expected \
                    length of IBAN is %s, not %s''' % (
                        prefix,
                        expected_length.length,
                        len(self.iban)
                    )

        control_sum = int(''.join(map(self.convert_num, self.iban[4:] + self.iban[:4])))
        if control_sum % 97 != 1:
            return [False, u'IBAN number is incorrect']

        return [True, u'IBAN number is correct']

    def bic_validation(self):
        if self.bic == "":
            return [True, u""]
        if re.search(r'^([a-zA-Z]){4}([a-zA-Z]){2}([0-9a-zA-Z]){2}([0-9a-zA-Z]{3})?$', self.bic):
            return [True, u'BIC is correct']
        else:
            return [False, u'BIC is incorrect']

    def val_execute(self):
        return self.iban_validation(), self.bic_validation()
