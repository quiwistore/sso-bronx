# -*- coding: utf-8 -*-
"""Inyecta enlaces contextuales internos - SLUGS REALES BRONX"""
import json, re

d = json.load(open('data/sso.json', encoding='utf-8'))

LINK_MAP = [
    # SERVICES
    (r'\bapply for SSI\b', '/apply-for-ssi-bronx/', 1),
    (r'\bSSI application\b', '/apply-for-ssi-bronx/', 1),
    (r'\bSupplemental Security Income\b', '/apply-for-ssi-bronx/', 1),
    (r'\bdisability benefits\b', '/apply-for-disability-benefits-bronx/', 1),
    (r'\bSSDI applications\b', '/apply-for-disability-benefits-bronx/', 1),
    (r'\bSocial Security retirement\b', '/apply-for-social-security-retirement-bronx/', 1),
    (r'\bretirement application\b', '/apply-for-social-security-retirement-bronx/', 1),
    (r'\bapplying for Medicare\b', '/apply-for-medicare-bronx/', 1),
    (r'\bMedicare enrollment\b', '/apply-for-medicare-bronx/', 1),
    (r'\bfirst-time Social Security card\b', '/apply-for-social-security-card-bronx/', 1),
    (r'\bapply for a Social Security card\b', '/apply-for-social-security-card-bronx/', 1),
    (r'\bSocial Security card application\b', '/apply-for-social-security-card-bronx/', 1),
    (r'\breplace a lost card\b', '/replace-social-security-card-bronx/', 1),
    (r'\bnewborn\b', '/get-social-security-number-for-newborn-bronx/', 1),
    (r'\bchange the name\b', '/change-name-on-social-security-card-bronx/', 1),
    (r'\blegal name change\b', '/change-name-on-social-security-card-bronx/', 1),
    # OFFICES (slugs REALES)
    (r'\bany Bronx SSA office\b', '/social-security-office-bronx/', 1),
    (r'\bsix Bronx SSA offices\b', '/social-security-office-bronx/', 1),
    (r'\bsix SSA offices\b', '/social-security-office-bronx/', 1),
    (r'\bSouth Bronx office\b', '/social-security-office-south-bronx/', 1),
    (r'\bEast Bronx office\b', '/social-security-office-east-bronx/', 1),
    (r'\bHunts Point office\b', '/social-security-office-hunts-point-bronx/', 1),
    (r'\bLaconia Avenue office\b', '/social-security-office-laconia-avenue-bronx/', 1),
    (r'\bNorth Bronx office\b', '/social-security-office-north-bronx/', 1),
    (r'\bWest Farms office\b', '/social-security-office-west-farms-bronx/', 1),
    (r'\boffice hours\b', '/social-security-office-hours-bronx/', 1),
    (r'\bschedule an appointment\b', '/social-security-office-appointment-bronx/', 1),
    (r'\bScheduling an appointment\b', '/social-security-office-appointment-bronx/', 1),
    (r'\bbook an appointment\b', '/social-security-office-appointment-bronx/', 1),
    (r'\bORIGINAL documents\b', '/ssa-required-documents-bronx/', 1),
    (r'\bSpanish-speaking representative\b', '/ssa-spanish-services-bronx/', 1),
    (r'\bbilingual service\b', '/ssa-spanish-services-bronx/', 1),
    (r'\bSpanish service\b', '/ssa-spanish-services-bronx/', 1),
    # LEARN
    (r'\bWhat Is Social Security\b', '/what-is-social-security/', 1),
    (r'\bSSI vs SSDI\b', '/ssi-vs-ssdi-difference/', 1),
    (r'\bappeal a disability denial\b', '/how-to-appeal-disability-denial/', 1),
    (r'\bappeals process\b', '/how-to-appeal-disability-denial/', 1),
    # TOOLS
    (r'\bretirement age calculator\b', '/retirement-age-calculator/', 1),
    (r'\bSSI Eligibility Checker\b', '/ssi-eligibility-checker/', 1),
    (r'\beligibility for SSI\b', '/ssi-eligibility-checker/', 1),
]

LINK_RE = re.compile(r'<a [^>]*>.*?</a>', re.IGNORECASE | re.DOTALL)
total_links = [0]

def linkify_paragraph(text, current_slug):
    if not isinstance(text, str):
        return text
    if len(text) < 80:
        return text
    placeholders = []
    def stash(m):
        placeholders.append(m.group(0))
        return f"\x00LNK{len(placeholders)-1}\x00"
    text_no_links = LINK_RE.sub(stash, text)
    
    for pattern, url, max_count in LINK_MAP:
        if f'/{current_slug}/' == url:
            continue
        regex = re.compile(pattern, re.IGNORECASE)
        replaced_count = [0]
        def replacer(m):
            if replaced_count[0] >= max_count:
                return m.group(0)
            replaced_count[0] += 1
            total_links[0] += 1
            return f'<a href="{url}">{m.group(0)}</a>'
        text_no_links, n = regex.subn(replacer, text_no_links, count=max_count)
    
    for i, original in enumerate(placeholders):
        text_no_links = text_no_links.replace(f"\x00LNK{i}\x00", original, 1)
    return text_no_links

def process_value(val, current_slug):
    if isinstance(val, str):
        return linkify_paragraph(val, current_slug)
    if isinstance(val, list):
        return [process_value(item, current_slug) for item in val]
    if isinstance(val, dict):
        SAFE_KEYS = {'a', 'body', 'intro'}
        new = {}
        for k, v in val.items():
            if k in SAFE_KEYS:
                new[k] = process_value(v, current_slug)
            elif k == 'items' and isinstance(v, list):
                new[k] = process_value(v, current_slug)
            elif k == 'sections' and isinstance(v, list):
                new[k] = process_value(v, current_slug)
            else:
                new[k] = v
        return new
    return val

for silo in ('services', 'office', 'learn'):
    if silo in d:
        new_pages = []
        for page in d[silo]:
            slug = page.get('slug', '')
            # IMPORTANTE: limpiar links contextuales viejos antes de reprocesar
            # (porque algunos slugs viejos como tremont-bronx ya no existen)
            new_page = process_value(page, slug)
            new_pages.append(new_page)
        d[silo] = new_pages

json.dump(d, open('data/sso.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
print(f"OK enlaces contextuales: {total_links[0]} links")
