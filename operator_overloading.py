class Complex:

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, complexNum2):
        # adding two complex numbers results in a new complex number
        sumof = Complex((self.real + complexNum2.real), (self.imaginary + complexNum2.imaginary))
        return sumof

num1 = Complex(3,7)
num2 = Complex(2,5)
num3 = num1 + num2
print('real part of num3:', num3.real )                     # terminal output: real part of num3: 5
print('imaginary part of num3:', num3.imaginary )           # terminal output: imaginary part of num3: 12