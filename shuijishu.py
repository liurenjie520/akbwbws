#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import string

def suiji():
    seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    salt = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    # print(salt)
    return salt


if __name__ == '__main__':
    a=suiji()
    print(a)



