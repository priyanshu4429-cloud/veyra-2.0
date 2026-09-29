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
        
    # Ensure act is imported
    if " act " not in content and "{ act," not in content and ", act " not in content and ", act}" not in content:
        content = re.sub(r"import \{(.*?)\} from '@testing-library/react';", 
                         r"import {\1, act} from '@testing-library/react';", 
                         content)

    # Replace render calls
    # Match render(<App />);
    content = re.sub(r"render\(<App(.*?)\);", r"await act(async () => { render(<App\1); });", content)
    
    # Match render(<MultiLocationPanel />);
    content = re.sub(r"render\(<MultiLocationPanel(.*?)\);", r"await act(async () => { render(<MultiLocationPanel\1); });", content)
    
    # Match render(<SpatialReliabilityPanel />);
    content = re.sub(r"render\(<SpatialReliabilityPanel(.*?)\);", r"await act(async () => { render(<SpatialReliabilityPanel\1); });", content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for fname in FILES_TO_PROCESS:
    process_file(fname)
    
print("Finished patching test files.")
