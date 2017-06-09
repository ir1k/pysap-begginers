# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 15:54:19 2017

@author: leno
"""

def decrypt_one_letter(shift, letter):
    """
    decrypt one letter with caesar cypher
    """
    ANCHOR = ord('A') - 1
    NB_ALPHA = 26

    # 0 <= i < NB_ALPHA,
    # i == 0 means 'A' and i == (NB_ALPHA - 1) means 'Z'
    i = ord(letter) - ANCHOR
    i = (NB_ALPHA + i - shift) % NB_ALPHA
    return chr(ANCHOR + i)

def decrypt(shift, enc_message):
    """
    caesar cypher decryption
    """

    dec = ''
    for letter in enc_message:
        dec += decrypt_one_letter(shift, letter)

    return dec

print(decrypt(13, 'FHCREABIN'))
