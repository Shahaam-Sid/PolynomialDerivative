from http.client import PROCESSING


class PolynomialDerivative:
    def __init__(self, degree):
        self.degree = degree
        self.answer = ""
    @property
    def degree(self):
        return self._degree
    @degree.setter
    def degree(self, value):
        if not isinstance(value, int):
            raise TypeError('Degree can only be a integer value')
        if value < 0:
            raise ValueError('Degree cannot be a negative integer')
        
        self._degree = value
        
    @property
    def answer(self):
        return self._answer
    
    @answer.setter
    def answer(self, value):
        self._answer = value
        
        
    def equation(self):
        for i in range(self.degree, -1, -1):
            coeff = int(input(f"x{PolynomialDerivative.int_to_superscript(i)}: "))
            if i == 0 or coeff == 0:
                pass
            else:
                dydx_coeff = coeff * i

                temp = str(dydx_coeff) + 'x' + str(PolynomialDerivative.int_to_superscript(i - 1))
                
                if temp[0] == '-':
                    self.answer += temp
                else:
                    self.answer = self.answer + '+' + temp
                
    @staticmethod
    def int_to_superscript(n):
        superscripts = str.maketrans("0123456789-", "⁰¹²³⁴⁵⁶⁷⁸⁹⁻")
        return str(n).translate(superscripts)
    
x = PolynomialDerivative(5)
x.equation()
print(x.answer)