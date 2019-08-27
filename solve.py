def solve(calc):
    while "(" in calc:
        calc = calc.replace(f"({calc.split(')')[0].split('(')[-1]})", str(solve(calc.split(")")[0].split("(")[-1])))
    n0 = ""
    for i in range(2):
        while "*+"[i] in calc or "/-"[i] in calc:
            for c in range(len(calc)):
                if calc[c] in ["*/", "+-"][i]:
                    n1, c0 = ("", c+1)
                    while c0 < len(calc) and not calc[c0] in "+-*/":
                        n1, c0 = (f"{n1}{calc[c0]}", c0+1)
                    n0f, n1f = (float(n0), float(n1))
                    n2 = [n0f*n1f, n0f+n1f][i] if calc[c] == "*+"[i] else [n0f/n1f, n0f-n1f][i]
                    calc, n0 = (calc.replace(f"{n0}{calc[c]}{n1}", str(n2)), "")
                    break
                elif calc[c] in "+-":
                    n0 = ""
                else:
                    n0 += calc[c]
    return float(calc)

print(solve("2+3*((1/4)*(1/2*2)/2)"))
