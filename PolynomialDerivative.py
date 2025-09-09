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
            
            coeff = int(input("constant: ")) if i == 0 else int(input(f"x{PolynomialDerivative.superscripter(i)}: "))
            
            if i == 0 or coeff == 0:
                pass
            else:
                dydx_coeff = coeff * i

                if i == 1:
                    temp = str(dydx_coeff)
                elif i == 2:
                    temp = str(dydx_coeff) + 'x'
                else:
                    temp = str(dydx_coeff) + 'x' + str(PolynomialDerivative.superscripter(i - 1))
                    
                if temp[0] == '-':
                    self.answer += temp
                else:
                    self.answer = self.answer + '+' + temp
                    
                if self.answer[0] == '+':
                    self.answer = self.answer[1:]
                
        if len(self.answer) == 0:
            self.answer = "0"
                
    @staticmethod
    def superscripter(n):
        superscripts = str.maketrans("0123456789-", "⁰¹²³⁴⁵⁶⁷⁸⁹⁻")
        return str(n).translate(superscripts)