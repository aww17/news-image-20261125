import os
import shutil

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)

source = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
shutil.copyfile(source, os.path.join(output_dir, "entry.png"))
