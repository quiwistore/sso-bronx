# -*- coding: utf-8 -*-
"""Linkifica numeros de telefono en el dataset (campos seguros solamente)"""
import json, re

d = json.load(open('data/sso.json', encoding='utf-8'))

# Patron: 1-800-XXX-XXXX o 1-800-XXX-XXXX
PHONE_RE = re.compile(r'(?<!["\d])(1-800-\d{3}-\d{4}|1-800-772-1213|1-800-325-0778)(?!["\d])')

def linkify_text(text):
    if not isinstance(text, str):
        return text
    if '<a href="tel:' in text:
        return text
    def replace_phone(m):
        phone = m.group(1)
        tel = phone.replace('-', '')
        return f'<a href="tel:+{tel}">{phone}</a>'
    return PHONE_RE.sub(replace_phone, text)

count = [0]
def process_value(val):
    if isinstance(val, str):
        new = linkify_text(val)
        if new != val:
            count[0] += new.count('<a href="tel:') - val.count('<a href="tel:')
        return new
    if isinstance(val, list):
        return [process_value(item) for item in val]
    if isinstance(val, dict):
        # Solo procesar campos seguros (a, body, intro, items que sean a o body)
        SAFE_KEYS = {'a', 'body', 'intro', 'subtext'}
        new = {}
        for k, v in val.items():
            if k in SAFE_KEYS:
                new[k] = process_value(v)
            elif k == 'items' and isinstance(v, list):
                new[k] = process_value(v)
            else:
                new[k] = v
        return new
    return val

for silo in ('services', 'office', 'learn'):
    if silo in d:
        d[silo] = [process_value(p) for p in d[silo]]

json.dump(d, open('data/sso.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
print(f"OK linkificados {count[0]} numeros de telefono")
