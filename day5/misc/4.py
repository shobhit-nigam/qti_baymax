strc = b"\xC0\xC4\xC1"
print(strc)
print(type(strc))

strd = strc.decode('cp855')
print(strd)
print(type(strd))
