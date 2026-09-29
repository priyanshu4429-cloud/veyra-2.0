import glob
import re

files = [
    'd:/Veyra-/veyra-2.0/frontend/src/components/MultiLocationPanel.tsx',
    'd:/Veyra-/veyra-2.0/frontend/src/components/ForecastDisagreementPanel.tsx',
    'd:/Veyra-/veyra-2.0/frontend/src/components/ForecastRevisionPanel.tsx',
    'd:/Veyra-/veyra-2.0/frontend/src/components/SpatialReliabilityPanel.tsx'
]

replacements = {
    "background: '#ffffff'": "background: 'rgba(255, 255, 255, 0.05)'",
    "background: '#f8fafc'": "background: 'rgba(255, 255, 255, 0.05)'",
    "background: '#fff'": "background: 'rgba(255, 255, 255, 0.05)'",
    "backgroundColor: '#ffffff'": "backgroundColor: 'rgba(255, 255, 255, 0.05)'",
    "border: '1px solid #e2e8f0'": "border: '1px solid rgba(255,255,255,0.1)'",
    "border: '1px solid #cbd5e1'": "border: '1px solid rgba(255,255,255,0.1)'",
    "color: '#475569'": "color: '#94a3b8'",
    "color: '#1e293b'": "color: '#f8fafc'",
    "color: '#334155'": "color: '#f8fafc'",
    "background: isCertifiedScope ? '#f8fafc' : '#fffbeb'": "background: 'rgba(255, 255, 255, 0.05)'"
}

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    for old, new in replacements.items():
        content = content.replace(old, new)
        
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f'Processed {f}')
