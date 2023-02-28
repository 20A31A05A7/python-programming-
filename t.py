real={"sam":24,"ange":18,"kumar":35}
print(real)
print(real.items())
new={name:age for name,age in real.items()}
print(new)
new1={name:age for name,age in real.items() if name=="sam" or age>=20}
print(new1)
