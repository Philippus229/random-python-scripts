innum0 = [1,1,0,1,0]
innum1 = [1,1,1,0,0]

def AND(in0, in1):
    return in0 and in1

def XOR(in0, in1):
    return (in0 or in1) and not (in0 and in1)

def PLG(in0, in1, in2):
    return (XOR(XOR(in0, in1), in2), XOR(AND(in0, in1), AND(XOR(in0, in1), in2)))

out = ""
x = False
for i in range(len(innum0)):
    outc, x = PLG(x, innum0[i], innum1[i])
    out = ['0', '1'][outc] + out
print(out)
