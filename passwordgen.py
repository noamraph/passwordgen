#!/usr/bin/env python

# This file was created by Noam Yorav-Raphael.
# It is put in the public domain.

import random
import math

LEFT = '123456qwertasdfgzxcvb'
RIGHT = '7890-=yuiop[]hjkl;\'nm,./'

def get_sides(nchars):
    """
    Get a list of valid strings of length nchars, composed of '1' and '0', with
    no side repeating more than twice
    """
    all_sides = ['{:0{}b}'.format(i, nchars).replace('0', 'L').replace('1', 'R')
                 for i in xrange(2**nchars)]
    return [x for x in all_sides if 'LLL' not in x and 'RRR' not in x]

def gen_pwd(nchars):
    rnd = random.SystemRandom()
    sides = rnd.choice(get_sides(nchars))
    pwd = ''.join(rnd.choice({'L':LEFT, 'R':RIGHT}[side]) for side in sides)
    return pwd

def calc_strength(nchars):
    """Calculate the entropy of passwords generated with nchars chars"""
    all_sides = get_sides(nchars)
    left_ent = math.log(len(LEFT), 2)
    right_ent = math.log(len(RIGHT), 2)
    sides_ent = math.log(len(all_sides), 2)
    ent = sum(left_ent*sides.count('L') + right_ent*sides.count('R') + sides_ent
              for sides in all_sides) / len(all_sides)
    return ent

def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Generate secure and easy to type passwords. "
        "The passwords will have no more than two consecutive characters from "
        "the same side of the keyboard.")
    parser.add_argument('-s', '--silent', action='store_true',
                        help="Don't print the strength of the password")
    parser.add_argument('nchars', nargs='?', default=8, type=int,
                        help='Number of characters in password '
                        '(default: 8. This gives you 42 bits of entropy.)')
    args = parser.parse_args()

    print gen_pwd(args.nchars)
    if not args.silent:
        print 'Password strength: {:.1f} bits'.format(calc_strength(args.nchars))

if __name__ == '__main__':
    main()
