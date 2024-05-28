def public_key(p, q):
    return p * q

def private_key(p, q):
    phi = (p - 1) * (q - 1)
