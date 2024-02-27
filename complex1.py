"""
basic Python types: int, float, complex, bool, NoneType

"""
import cmath

nb1 = 3.4+4.5j 
print(nb1, type(nb1))
print(nb1.real)
print(nb1.imag)

nb1 = 4.5j 
print(nb1, type(nb1))
print(nb1.real)
print(nb1.imag)

nb1 = complex(2.3, 6.7)
print(nb1, type(nb1))
print(nb1.real)
print(nb1.imag)
print(cmath.cos(nb1))

nb1 = complex()
print(nb1, type(nb1))
print(nb1.real)
print(nb1.imag)


