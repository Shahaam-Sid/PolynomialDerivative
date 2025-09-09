from PolynomialDerivative import PolynomialDerivative

if __name__ == "__main__":
    
    print("--Polynomial-Derivative-Calculator--")
    x = PolynomialDerivative(int(input("Degree: ")))
    x.equation()
    print("---------------Anwser---------------")
    print("derivative:", x.answer)
    print("------------------------------------")
