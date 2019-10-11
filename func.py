def func(a, b):
    if isinstance(a, int):
        a += 1
    elif isinstance(a, str):
        a = int(a)
    elif isinstance(a, list):
        a = len(a) + sum(a)
    else:
        a = 0
        
    if isinstance(b, int):
        b *= 100
    elif isinstance(b, str):
        b = len(b)
    elif isinstance(b, list):
        b = b[-1]
    else:
        b = a
        
    return a + b