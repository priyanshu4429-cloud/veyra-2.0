import os
import re

TEST_DIR = r"d:\Veyra-\veyra-2.0\frontend\src\test"

FILES_TO_PROCESS = [
    "Dashboard.test.tsx",
    "RiskTimeline.test.tsx",
    "ParityVerification.test.tsx",
    "MultiLocation.test.tsx",
    "SpatialReliability.test.tsx"
]

def process_file(filename):
    filepath = os.path.join(TEST_DIR, filename)
    if not os.path.exists(filepath):
        return
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find `it('...', () => {` or `it("...", () => {` and make it async
    # There could be `it('...', () => {` or `it('...', () => {`
    # We can use regex to match `it(..., () => {` where `async` is missing.
    # Note: Javascript arrow functions could also be `it(..., function() {` but React tests usually use `() => {`.
    
    # regex: look for `it(` followed by string, then `, () => {`
    content = re.sub(r"it\((['\"].*?['\"]),\s*\(\)\s*=>\s*\{", r"it(\1, async () => {", content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for fname in FILES_TO_PROCESS:
    process_file(fname)
    
print("Finished making tests async.")
