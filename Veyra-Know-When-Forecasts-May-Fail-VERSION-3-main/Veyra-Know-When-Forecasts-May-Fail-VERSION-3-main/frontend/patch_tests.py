import os, re
frontend_src = r"d:\Veyra-\Veyra-Know-When-Forecasts-May-Fail-VERSION-3-main\Veyra-Know-When-Forecasts-May-Fail-VERSION-3-main\frontend\src"

def patch_file(filepath, pattern, replacement):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    new_content = re.sub(pattern, replacement, content)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

test_dir = os.path.join(frontend_src, "test")
tests = ["Dashboard.test.tsx", "ForecastDisagreement.test.tsx", "ForecastRevision.test.tsx", "MultiLocation.test.tsx", "ParityVerification.test.tsx", "RiskTimeline.test.tsx", "SpatialReliability.test.tsx"]

for test_file in tests:
    path = os.path.join(test_dir, test_file)
    if os.path.exists(path):
        patch_file(path, r"384h", r"240h")
        patch_file(path, r"384", r"240")
        patch_file(path, r"16_DAY", r"10_DAY")
        patch_file(path, r"16 Day", r"10 Day")
        patch_file(path, r"16-Day", r"10-Day")
        patch_file(path, r"16 days", r"10 days")
        patch_file(path, r"264h–240h", r"") # cleanup from blind replacement

print("Tests patched")
