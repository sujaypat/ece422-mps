#!/usr/bin/python
# -*- coding: utf-8 -*-
from hashlib import sha256
from urllib import quote
good = "I come in peace."
evil = "Prepare to be destroyed!"
blob = """
               �Kx^U����&�;�tQŠ0ёɸC�BmO�V����L�&k�R���T&T�`�����x�RͤL��������Ƴ��tWK���t*+� X`H��UX��a���Q[3�Q���mϺ �ZwI�j
"""
if sha256(blob).hexdigest() == '01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b':
    print good
else:
    print evil
