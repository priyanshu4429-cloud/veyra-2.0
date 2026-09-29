import os, re

frontend_src = r"d:\Veyra-\Veyra-Know-When-Forecasts-May-Fail-VERSION-3-main\Veyra-Know-When-Forecasts-May-Fail-VERSION-3-main\frontend\src"
files = [
    os.path.join(frontend_src, "components", "SpatialReliabilityPanel.tsx"),
    os.path.join(frontend_src, "components", "ForecastRevisionPanel.tsx"),
    os.path.join(frontend_src, "components", "ForecastDisagreementPanel.tsx"),
    os.path.join(frontend_src, "components", "MultiLocationPanel.tsx")
]

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove the objects from HORIZON_OPTIONS with scope EXTENDED_OPERATIONAL_HORIZON
    content = re.sub(
        r"\s*\{\s*lead:\s*(264|288|312|336|360|384).*?'EXTENDED_OPERATIONAL_HORIZON'\s*\},",
        "",
        content
    )
    
    # Remove the optgroup for Extended Operational Horizon
    content = re.sub(
        r'<optgroup\s+label="Extended\s+Operational\s+Horizon\s*\(264h–384h\)".*?</optgroup>',
        "",
        content,
        flags=re.DOTALL
    )
    
    # Update ternary logic replacing the 384h string
    content = content.replace(
        "EXTENDED OPERATIONAL HORIZON (264h-384h)",
        "EXTENDED OPERATIONAL HORIZON (UNAVAILABLE)"
    )
    content = content.replace(
        "EXTENDED OPERATIONAL HORIZON (264–384h): Evaluated for operational situational awareness; beyond the frozen 240h benchmark scope.",
        "EXTENDED OPERATIONAL HORIZON (UNAVAILABLE)"
    )

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated panel files.")
