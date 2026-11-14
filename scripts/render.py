import argparse
from pathlib import Path
import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent

ap = argparse.ArgumentParser()
ap.add_argument(
    "-d", "--definition", type=Path, default=REPO_ROOT / "updated_image.yaml"
)
ap.add_argument(
    "-t",
    "--template",
    type=Path,
    default=REPO_ROOT / "template" / "Dockerfile.template",
)
ap.add_argument("-o", "--output", type=Path, default=REPO_ROOT / "Dockerfile")
ap.add_argument("--base-tag", help="override base image tag")
ap.add_argument(
    "--pkg",
    action="append",
    default=[],
    metavar="NAME=VERSION",
    help="override/add a package version (repeatable)",
)
args = ap.parse_args()

with open(args.definition) as f:
    cfg = yaml.safe_load(f)

if args.base_tag:
    cfg["base"]["tag"] = args.base_tag
for item in args.pkg:
    name, _, version = item.partition("=")
    cfg["packages"][name] = version or None

cfg["apk_packages"] = " \\\n    ".join(
    f"{name}={ver}" if ver else name for name, ver in cfg["packages"].items()
)

env = Environment(
    loader=FileSystemLoader(args.template.parent),
    undefined=StrictUndefined,
    keep_trailing_newline=True,
)
rendered = env.get_template(args.template.name).render(**cfg)

args.output.write_text(rendered)
print(f"Rendered {args.output}")
