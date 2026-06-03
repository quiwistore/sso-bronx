# -*- coding: utf-8 -*-
import json
d = json.load(open('data/sso.json', encoding='utf-8'))

js = "// AUTO-GENERADO desde data/sso.json - no editar a mano\n"
js += f"export const site = {json.dumps(d['site'], ensure_ascii=False)};\n"
js += f"export const services = {json.dumps(d['services'], ensure_ascii=False)};\n"
js += f"export const office = {json.dumps(d['office'], ensure_ascii=False)};\n"
js += f"export const learn = {json.dumps(d['learn'], ensure_ascii=False)};\n"
js += "export const allPages = [...services, ...office, ...learn];\n"
js += "export function getPage(slug){ return allPages.find(p => p.slug === slug); }\n"
js += "export const silos = {\n"
js += "  services: { label: 'Services', items: services },\n"
js += "  office:   { label: 'Office info', items: office },\n"
js += "  learn:    { label: 'Learn', items: learn },\n"
js += "};\n"

open('src/data/datos.js','w',encoding='utf-8').write(js)
print(f"OK src/data/datos.js ({len(js):,} bytes)")
