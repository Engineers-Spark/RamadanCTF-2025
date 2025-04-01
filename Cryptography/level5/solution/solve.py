def ceil_div(a, b):
    return -(-a // b)

def floor_div(a, b):
    return a // b



def _step_1(padding_oracle, n, e, c):
    f1 = 2
    while padding_oracle((pow(f1, e, n) * c) % n):
        f1 *= 2

    return f1


# Step 2.
def _step_2(padding_oracle, n, e, c, B, f1):
    f2 = floor_div(n + B, B) * f1 // 2
    while not padding_oracle((pow(f2, e, n) * c) % n):
        f2 += f1 // 2

    return f2


# Step 3.
def _step_3(padding_oracle, n, e, c, B, f2):
    mmin = ceil_div(n, f2)
    mmax = floor_div(n + B, f2)
    while mmin < mmax:
        f = floor_div(2 * B, mmax - mmin)
        i = floor_div(f * mmin, n)
        f3 = ceil_div(i * n, mmin)
        if padding_oracle((pow(f3, e, n) * c) % n):
            mmax = floor_div(i * n + B, f3)
        else:
            mmin = ceil_div(i * n + B, f3)
    return mmin


def attack(padding_oracle, n, e, c):
    k = ceil_div(n.bit_length(), 8)
    B = 2 ** (8 * (k - 1))
    assert 2 * B < n
    print("Executing step 1...")
    f1 = _step_1(padding_oracle, n, e, c)
    print("Executing step 2...")
    f2 = _step_2(padding_oracle, n, e, c, B, f1)
    print("Executing step 3...")
    m = _step_3(padding_oracle, n, e, c, B, f2)
    return m