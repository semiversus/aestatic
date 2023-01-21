import sys
import shutil
from pathlib import *

from .markdown import process as md_process

file_type_register = {
    '.md': md_process
}

source_files = set(p for p in Path('content').rglob('*') if p.is_file())

for suffix, function in file_type_register.items():
    files = {f for f in source_files if f.suffix == suffix}
    function(files)
    source_files -= files

for file in source_files:
    output_path = 'output' / file.relative_to('content')
    output_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(file, output_path)

sys.exit()
