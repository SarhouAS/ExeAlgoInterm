def classifier_triangle(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return False, ""
    if a == b == c:
        return True, "équilatéral"
    cotes = sorted([a, b, c])

    if cotes[0]**2 + cotes[1]**2 == cotes[2]**2:
        return True, "rectangle"

    if a == b or b == c or a == c:
        return True, "isocèle"

    return True, "quelconque"


# Tests
tests = [
    (3, 4, 5),
    (2, 2, 2),
    (1, 2, 3),
    (3, 3, 5),
    (4, 6, 8)
]

for a, b, c in tests:
    valide, type_triangle = classifier_triangle(a, b, c)
    if valide:
        print(f"a={a}, b={b}, c={c} → true, \"{type_triangle}\"")
    else:
        print(f"a={a}, b={b}, c={c} → false")