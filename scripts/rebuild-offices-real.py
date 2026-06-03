# -*- coding: utf-8 -*-
"""Reconstruye las paginas de oficinas con direcciones REALES verificadas."""
import json

# 6 oficinas SSA federales del Bronx (datos verificados via SSA oficial)
OFFICES = [
    {
        "slug":"social-security-office-south-bronx",
        "name":"South Bronx",
        "address":"820 Concourse Village West, 3rd Floor, Bronx, NY 10451",
        "address_short":"820 Concourse Village West, 3rd Fl, Bronx, NY 10451",
        "zip":"10451",
        "neighborhoods":"Mott Haven, Highbridge, Concourse, Melrose, and the south-central Bronx",
        "neighborhoods_short":"Mott Haven, Highbridge, Concourse",
        "subway":"Yankee Stadium-161st Street (B, D, 4 trains)",
        "subway_short":"Yankee Stadium-161st St (B, D, 4)",
        "local_phone":"1-855-531-1684",
        "h1_loc":"South Bronx (Concourse Village West)",
    },
    {
        "slug":"social-security-office-east-bronx",
        "name":"East Bronx",
        "address":"1380 Parker Street, 2nd Floor, Bronx, NY 10462",
        "address_short":"1380 Parker St, 2nd Fl, Bronx, NY 10462",
        "zip":"10462",
        "neighborhoods":"Parkchester, Castle Hill, Soundview, Westchester Square, and the central-east Bronx",
        "neighborhoods_short":"Parkchester, Castle Hill, Soundview",
        "subway":"Parkchester or Castle Hill Avenue (6 train)",
        "subway_short":"Parkchester or Castle Hill Av (6)",
        "local_phone":"1-866-931-2526",
        "h1_loc":"East Bronx (Parker Street)",
    },
    {
        "slug":"social-security-office-hunts-point-bronx",
        "name":"Hunts Point",
        "address":"1029 East 163rd Street, 3rd Floor, Bronx, NY 10459",
        "address_short":"1029 E 163rd St, 3rd Fl, Bronx, NY 10459",
        "zip":"10459",
        "neighborhoods":"Hunts Point, Longwood, Foxhurst, Bronx River, and the south-eastern Bronx",
        "neighborhoods_short":"Hunts Point, Longwood, Foxhurst",
        "subway":"Hunts Point Avenue (6 train)",
        "subway_short":"Hunts Point Av (6)",
        "local_phone":"1-866-220-7889",
        "h1_loc":"Hunts Point (East 163rd Street)",
    },
    {
        "slug":"social-security-office-laconia-avenue-bronx",
        "name":"Laconia Avenue",
        "address":"3247 Laconia Avenue, Bronx, NY 10469",
        "address_short":"3247 Laconia Ave, Bronx, NY 10469",
        "zip":"10469",
        "neighborhoods":"Wakefield, Williamsbridge, Eastchester, Edenwald, Pelham Gardens, and the northern Bronx",
        "neighborhoods_short":"Wakefield, Williamsbridge, Eastchester",
        "subway":"Baychester Avenue or Eastchester-Dyre Avenue (5 train)",
        "subway_short":"Baychester Av (5)",
        "local_phone":"1-866-513-2391",
        "h1_loc":"Laconia Avenue (Wakefield / Eastchester)",
    },
    {
        "slug":"social-security-office-north-bronx",
        "name":"North Bronx",
        "address":"2501 Grand Concourse, 2nd Floor, Bronx, NY 10468",
        "address_short":"2501 Grand Concourse, 2nd Fl, Bronx, NY 10468",
        "zip":"10468",
        "neighborhoods":"Fordham, Mt Eden, Mt Hope, Tremont, Bedford Park, University Heights, and Kingsbridge Heights",
        "neighborhoods_short":"Fordham, Mt Eden, Tremont, Bedford Park",
        "subway":"Burnside Avenue or 183rd Street (4 train), or Fordham Road (B, D)",
        "subway_short":"Burnside Av (4) or Fordham Rd (B, D)",
        "local_phone":"1-877-619-2852",
        "h1_loc":"North Bronx (Grand Concourse / Fordham)",
    },
    {
        "slug":"social-security-office-west-farms-bronx",
        "name":"West Farms",
        "address":"1829 Southern Boulevard, Bronx, NY 10460",
        "address_short":"1829 Southern Blvd, Bronx, NY 10460",
        "zip":"10460",
        "neighborhoods":"West Farms, Crotona, East Tremont, Belmont, Bronxdale, and the central-west Bronx",
        "neighborhoods_short":"West Farms, Crotona, Belmont, Bronxdale",
        "subway":"174th Street or West Farms Sq-East Tremont (2, 5 trains)",
        "subway_short":"174th St or West Farms Sq (2, 5)",
        "local_phone":"1-866-964-2558",
        "h1_loc":"West Farms (Southern Boulevard)",
    },
]

# Cargar dataset actual
d = json.load(open('data/sso.json', encoding='utf-8'))

# Filtrar oficinas: mantener solo las informativas (no las 4 con direcciones inventadas)
KEEP_SLUGS_GENERIC = {
    'social-security-office-bronx',  # HUB - regeneramos abajo
    'social-security-office-hours-bronx',
    'social-security-office-appointment-bronx',
    'social-security-office-near-me-bronx',
    'ssa-required-documents-bronx',
    'ssa-spanish-services-bronx',
}
d['office'] = [p for p in d['office'] if p['slug'] in KEEP_SLUGS_GENERIC]
print(f"Filtradas paginas viejas. Conservadas: {len(d['office'])} genericas")

# Generar las 6 oficinas reales
office_pages_real = []
for off in OFFICES:
    others = [o for o in OFFICES if o['slug'] != off['slug']]
    office_pages_real.append({
        "slug": off['slug'], "silo":"office",
        "h1": f"SSA Office in the {off['h1_loc']}, Bronx",
        "title": f"{off['name']} Social Security Office, Bronx NY ({off['address_short']})",
        "meta": f"Complete guide to the {off['name']} Social Security office at {off['address_short']}. Hours, transit, services, and how to book an appointment.",
        "intro": f"The {off['name']} Social Security Administration field office is located at {off['address']}. It serves residents of {off['neighborhoods']}. This page covers the address, subway access, neighborhoods served, services available, and tips for making your visit efficient.",
        "sections":[
            {"type":"quick_answer","heading":"The quick answer",
             "body": f"The {off['name']} SSA office is located at <strong>{off['address']}</strong>. Closest subway: {off['subway']}. It serves {off['neighborhoods_short']} and surrounding areas. The office handles all SSA services including SSN cards, SSDI, SSI, retirement, and Medicare. Open Monday-Friday 9:00 AM to 4:00 PM. Local appointment line: {off['local_phone']}; national: 1-800-772-1213. Appointments are now required for most in-person services as of 2025."},
            {"type":"section","heading":"Neighborhoods served",
             "body":[
                f"The {off['name']} field office at {off['address_short']} primarily serves residents of {off['neighborhoods']}. Each Bronx SSA office is assigned specific ZIP codes; this office covers ZIP {off['zip']} and adjacent ones. To confirm whether this is your assigned office for a specific service, enter your ZIP code at ssa.gov/locator or call 1-800-772-1213.",
                f"That said, for most routine services any Bronx SSA office can help — you do not strictly need to visit the one assigned to your ZIP, though more complex local cases may require it."
             ]},
            {"type":"section","heading":"How to get there by subway",
             "body":[
                f"The closest subway access is {off['subway']}, then a short walk to the office at {off['address_short']}. New York City's subway is the most reliable way to reach any Bronx SSA office — street parking in the area is limited and time-restricted.",
                f"If you are coming from outside the Bronx, allow extra time during weekday rush hours (7-9 AM and 4-6 PM) when service is more variable. Plan for half a day total when traveling from another borough: most appointments take 15-30 minutes, but travel plus security screening adds up."
             ]},
            {"type":"section","heading":"Services available at the " + off['name'] + " office",
             "body":[
                f"Every Bronx SSA field office handles the full range of Social Security services. At the {off['name']} location you can apply for a first-time Social Security card, replace a lost card, change the name on your card, apply for disability benefits (SSDI and SSI), apply for retirement, enroll in Medicare, get a Social Security number for a newborn, and handle most immigration-related changes to your record.",
                "Some services can also be completed entirely online at ssa.gov without visiting any office — replacement cards for qualifying applicants, retirement applications, address changes, and benefit verification letters. Visit the office in person for services that require original documents or for situations where face-to-face guidance is helpful."
             ]},
            {"type":"checklist","heading":"Before visiting this office",
             "items":[
                f"Call <strong>{off['local_phone']}</strong> (local line for the {off['name']} office) or <strong>1-800-772-1213</strong> (national) to schedule an appointment. As of January 2025, the SSA requires appointments for most in-person services.",
                "Bring ORIGINAL documents — never photocopies. They will be photocopied at the office and originals returned the same day.",
                "Arrive 15 minutes early for federal building security screening.",
                "Mondays and the day after a federal holiday are the busiest — Tuesday-Friday mid-morning has shorter waits.",
                "If you need bilingual service, request a Spanish-speaking representative when you book the appointment."
             ]},
            {"type":"faq_extra","items":[
                {"q": f"What is the local phone number for the {off['name']} office?",
                 "a": f"The local number is {off['local_phone']}, which routes to the {off['name']} field office. You can also use the national SSA line at 1-800-772-1213 to schedule appointments or get general information."},
                {"q": f"What if I cannot get to the {off['name']} office?",
                 "a": f"The other Bronx SSA field offices are: " + ", ".join(f"{o['name']} ({o['address_short'].split(',')[0]})" for o in others[:3]) + ", and others. For most services, any Bronx office can help — confirm by calling 1-800-772-1213 or using ssa.gov/locator."},
                {"q":"Are appointments now required?",
                 "a":"As of January 6, 2025, the SSA requires appointments for most in-person services at all field offices, including the Bronx locations. Walk-ins for limited services may still be accepted but expect long waits. Schedule by calling 1-800-772-1213 or the local office line."},
                {"q":"Is the office wheelchair accessible?",
                 "a":"Yes. All SSA field offices, including this one, meet federal accessibility standards. If you need additional assistance, mention it when scheduling the appointment."}
            ]}
        ]
    })

# Insertar las 6 oficinas reales en el dataset
# Ubicarlas justo despues del HUB (que vamos a regenerar tambien)
d['office'].extend(office_pages_real)
print(f"Agregadas: {len(office_pages_real)} paginas de oficinas reales")

# ============== Regenerar el HUB con las 6 oficinas correctas ==============
hub_page = {
    "slug":"social-security-office-bronx","silo":"office",
    "h1":"Social Security Offices in the Bronx, NY",
    "title":"Social Security Office in the Bronx, NY: All 6 Locations (2026)",
    "meta":"Complete directory of the six Social Security Administration field offices in the Bronx, NY. Real addresses, local phone lines, transit access, and services.",
    "intro":"The Bronx is served by six Social Security Administration field offices: South Bronx, East Bronx, Hunts Point, Laconia Avenue, North Bronx, and West Farms. Each serves specific neighborhoods and ZIP codes. This page lists all six with verified addresses, transit, and local phone lines, plus information on which office serves your address.",
    "sections":[
        {"type":"quick_answer","heading":"The quick answer",
         "body":"The Bronx has six SSA field offices, each serving specific neighborhoods: <strong>South Bronx</strong> (820 Concourse Village West, 10451), <strong>East Bronx</strong> (1380 Parker St, 10462), <strong>Hunts Point</strong> (1029 E 163rd St, 10459), <strong>Laconia Avenue</strong> (3247 Laconia Ave, 10469), <strong>North Bronx</strong> (2501 Grand Concourse, 10468), and <strong>West Farms</strong> (1829 Southern Blvd, 10460). Each office handles all SSA services. The office assigned to your address depends on your ZIP — check ssa.gov/locator or call 1-800-772-1213."},
        {"type":"section","heading":"The six SSA field offices in the Bronx",
         "body":[
            "<strong>South Bronx</strong> — 820 Concourse Village West, 3rd Fl, Bronx, NY 10451. Serves Mott Haven, Highbridge, Concourse, Melrose. Local line: 1-855-531-1684. Closest subway: Yankee Stadium-161st St (B, D, 4).",
            "<strong>East Bronx</strong> — 1380 Parker Street, 2nd Fl, Bronx, NY 10462. Serves Parkchester, Castle Hill, Soundview, Westchester Square. Local line: 1-866-931-2526. Closest subway: Parkchester (6).",
            "<strong>Hunts Point</strong> — 1029 East 163rd Street, 3rd Fl, Bronx, NY 10459. Serves Hunts Point, Longwood, Foxhurst, Bronx River. Local line: 1-866-220-7889. Closest subway: Hunts Point Av (6).",
            "<strong>Laconia Avenue</strong> — 3247 Laconia Avenue, Bronx, NY 10469. Serves Wakefield, Williamsbridge, Eastchester, Edenwald, Pelham Gardens. Local line: 1-866-513-2391. Closest subway: Baychester Av (5).",
            "<strong>North Bronx</strong> — 2501 Grand Concourse, 2nd Fl, Bronx, NY 10468. Serves Fordham, Mt Eden, Tremont, Bedford Park, University Heights, Kingsbridge Heights. Local line: 1-877-619-2852. Closest subway: Burnside Av (4) or Fordham Rd (B, D).",
            "<strong>West Farms</strong> — 1829 Southern Boulevard, Bronx, NY 10460. Serves West Farms, Crotona, East Tremont, Belmont, Bronxdale. Local line: 1-866-964-2558. Closest subway: 174th St or West Farms Sq (2, 5)."
         ]},
        {"type":"section","heading":"Which office serves your address",
         "body":[
            "The SSA assigns each ZIP code in the Bronx to one of the six offices. Generally you must visit the office that serves your address, though for most routine services any office can help. Use the official locator at ssa.gov/locator to confirm — enter your ZIP and it returns the assigned office.",
            "If you live near the Bronx but in Manhattan, Westchester, or Queens, your assigned office will be elsewhere. The Bronx offices specifically serve Bronx ZIPs."
         ]},
        {"type":"section","heading":"Appointments are now required (2025 change)",
         "body":[
            "Effective January 6, 2025, the SSA requires customers to schedule an appointment for most in-person services at any field office, including all six Bronx locations. Walk-ins for limited services may still be accepted but expect long waits.",
            "Schedule by calling the national number 1-800-772-1213 or the local line of the specific office. Appointments are typically available within 2-4 weeks."
         ]},
        {"type":"checklist","heading":"Common to all six Bronx offices",
         "items":[
            "National SSA phone: 1-800-772-1213 (works for all offices).",
            "TTY: 1-800-325-0778.",
            "Hours: Monday-Friday 9:00 AM to 4:00 PM (subject to change).",
            "Closed: weekends and all federal holidays.",
            "Appointments now required for most services (2025).",
            "Bilingual service (English/Spanish) at all Bronx offices.",
            "Bring ORIGINAL documents — never photocopies."
         ]},
        {"type":"faq_extra","items":[
            {"q":"Can I visit any Bronx SSA office or only my assigned one?",
             "a":"For most services, any office can help regardless of which one is assigned to your ZIP. For complex matters tied to your record, the assigned office may need to handle it. When in doubt, call 1-800-772-1213 first."},
            {"q":"Which Bronx SSA office is the largest?",
             "a":"The South Bronx office at 820 Concourse Village West is the largest and most centrally located, near Yankee Stadium. It is also the most-connected to the subway network."},
            {"q":"How do I know which office serves my ZIP code?",
             "a":"Use the official SSA office locator at ssa.gov/locator. Enter your ZIP code and the assigned field office is returned. You can also call 1-800-772-1213 to ask."},
            {"q":"Are all six Bronx offices wheelchair accessible?",
             "a":"Yes. All SSA field offices meet federal accessibility standards. If you need additional assistance for your visit, mention it when you schedule the appointment."}
        ]}
    ]
}

# Insertar el HUB primero en el silo office
d['office'].insert(0, hub_page)
print(f"OK HUB regenerado con 6 oficinas reales")

# ============== Reescribir social-security-office-near-me-bronx ==============
nearme_page = next(p for p in d['office'] if p['slug'] == 'social-security-office-near-me-bronx')
nearme_page['intro'] = "'Social Security office near me' is one of the most-searched queries by Bronx residents, and the answer depends on which neighborhood you live in. The borough has six SSA field offices, each covering specific areas. This page explains which office is nearest by neighborhood and how to confirm the right one for your exact address."
nearme_page['sections'] = [
    {"type":"quick_answer","heading":"The quick answer",
     "body":"The Bronx has six SSA field offices: <strong>South Bronx</strong> (820 Concourse Village W, 10451), <strong>East Bronx</strong> (1380 Parker St, 10462), <strong>Hunts Point</strong> (1029 E 163rd St, 10459), <strong>Laconia Avenue</strong> (3247 Laconia Ave, 10469), <strong>North Bronx</strong> (2501 Grand Concourse, 10468), and <strong>West Farms</strong> (1829 Southern Blvd, 10460). Each covers specific ZIPs. Use ssa.gov/locator with your ZIP to find your assigned office."},
    {"type":"section","heading":"Which office is nearest by neighborhood",
     "body":[
        "<strong>Mott Haven, Highbridge, Concourse, Melrose</strong> → South Bronx office at 820 Concourse Village West.",
        "<strong>Hunts Point, Longwood, Foxhurst, Bronx River</strong> → Hunts Point office at 1029 East 163rd Street.",
        "<strong>Parkchester, Castle Hill, Soundview, Westchester Square</strong> → East Bronx office at 1380 Parker Street.",
        "<strong>West Farms, Crotona, East Tremont, Belmont, Bronxdale</strong> → West Farms office at 1829 Southern Boulevard.",
        "<strong>Fordham, Mt Eden, Tremont, Bedford Park, University Heights, Kingsbridge Heights</strong> → North Bronx office at 2501 Grand Concourse.",
        "<strong>Wakefield, Williamsbridge, Eastchester, Edenwald, Co-op City, Pelham Gardens</strong> → Laconia Avenue office at 3247 Laconia Avenue."
     ]},
    {"type":"section","heading":"What if you live near the Bronx but not in it",
     "body":[
        "Residents of nearby Westchester County (Yonkers, Mount Vernon, New Rochelle) generally have their own SSA offices closer to home. Upper Manhattan (Inwood, Washington Heights, Harlem) has its own offices and is not served by Bronx locations. Use ssa.gov/locator to confirm which office is assigned to your address.",
        "The SSA assigns each ZIP code to a specific field office — there is no choice. You go to whichever office covers your address, regardless of which is closer to your workplace."
     ]},
    {"type":"checklist","heading":"Tips for finding your nearest office",
     "items":[
        "Use ssa.gov/locator with your ZIP code — official tool from the SSA.",
        "Call 1-800-772-1213 to ask which office is assigned to your address.",
        "Note your address's specific neighborhood (Bronx has many) to map it to one of the six offices.",
        "Use the subway — parking near Bronx SSA offices is generally limited.",
        "All six Bronx offices are wheelchair accessible."
     ]},
    {"type":"faq_extra","items":[
        {"q":"Can I visit any Bronx office or only the one for my ZIP code?",
         "a":"For most services, any Bronx office can help regardless of your assigned office. For some local matters tied to your record, your assigned office may need to handle it. Confirm with 1-800-772-1213 if in doubt."},
        {"q":"What about residents of upper Manhattan?",
         "a":"Upper Manhattan has its own SSA offices and is not served by Bronx offices. Residents of Inwood, Washington Heights, and Harlem should check ssa.gov/locator for the right office."},
        {"q":"How do I get to the offices without a car?",
         "a":"All six Bronx SSA offices are accessible by subway and bus. The South Bronx office at 820 Concourse Village West is the most-connected (B, D, 4 trains at Yankee Stadium-161st Street)."},
        {"q":"Is there parking at any office?",
         "a":"Street parking near Bronx SSA offices is limited and time-restricted in most areas. The Laconia Avenue office (in the more residential northern Bronx) tends to have more parking availability than the central offices. Public transit is still strongly recommended."}
    ]}
]
print(f"OK near-me actualizado con 6 oficinas reales")

# Guardar dataset actualizado
json.dump(d, open('data/sso.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
total = len(d['services']) + len(d['office']) + len(d['learn'])
print(f"")
print(f"OK dataset guardado: {total} paginas totales")
print(f"  SERVICES: {len(d['services'])}")
print(f"  OFFICES:  {len(d['office'])} (HUB + 6 oficinas reales + 5 informativas)")
print(f"  LEARN:    {len(d['learn'])}")
