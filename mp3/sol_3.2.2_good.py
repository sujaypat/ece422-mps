#!/usr/bin/python
# -*- coding: utf-8 -*-
from hashlib import sha256
from urllib import quote
good = "I come in peace."
evil = "Prepare to be destroyed!"
blob = """
               �Kx^U����&�;�tQŠ�ёɸC�BmO�V����L�&k�R�A�T&T�`�����x@RͤL��������Ƴ��tWK��ot*+� X`H��UX��a���Q[38Q���mϺ ��wI�j
"""
if sha256(blob).hexdigest() == '01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b':
    print good
else:
    print evil
