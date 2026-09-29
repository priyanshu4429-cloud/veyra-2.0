import os
import zipfile
import shutil

def create_zip():
    zip_filename = 'Veyra-2.0-95PLUS-release.zip'
    source_dir = '.'
    
    exclude_dirs = {'.git', '.venv', 'node_modules', 'dist', '.pytest_cache', '__pycache__', 'scratch'}
    
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            for file in files:
                if file == zip_filename:
                    continue
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, source_dir)
                zipf.write(file_path, arcname)

if __name__ == '__main__':
    create_zip()
