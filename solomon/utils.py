import random
import string
    

def random_string(length=8, only_digit=False, only_lower=False):
    if only_digit:
        return ''.join(random.choice(string.digits) for _ in range(length))
    else:
        if only_lower:
            return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))
        else:
            return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))


def random_bool():
    import random
    return random.choice([False, True])
