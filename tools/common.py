"""Shared paths + content loader for the Secret Spawn pipeline.

Environment variables (all optional):
  SS_ASSETS  folder with fonts + Kokoro model   (default: <repo>/assets)
  CONTENT    day script: a file path (content/2026-11-14.py) or a module name
  OUTDIR     intermediate files: wav/json/raw video/preview frames (default: <repo>/work/out)
  FINALDIR   finished mp4 + thumbnail + upload manifest           (default: <repo>/work/final)
"""
import os, sys, importlib, importlib.util

TOOLS = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(TOOLS)
if TOOLS not in sys.path:
    sys.path.insert(0, TOOLS)

ASSETS = os.environ.get('SS_ASSETS', os.path.join(REPO, 'assets'))
BEBAS = os.path.join(ASSETS, 'BebasNeue.ttf')
LILITA = os.path.join(ASSETS, 'LilitaOne.ttf')
KOKORO_MODEL = os.path.join(ASSETS, 'kokoro-v1.0.int8.onnx')
KOKORO_VOICES = os.path.join(ASSETS, 'voices-v1.0.bin')

OUTDIR = os.environ.get('OUTDIR', os.path.join(REPO, 'work', 'out'))
FINALDIR = os.environ.get('FINALDIR', os.path.join(REPO, 'work', 'final'))


def load_content():
    """Load the day's content module (SHORTS, LONG, optional UPLOAD)."""
    c = os.environ.get('CONTENT', os.path.join(REPO, 'content', 'TEMPLATE.py'))
    if c.endswith('.py') or os.sep in c:
        path = os.path.abspath(c)
        spec = importlib.util.spec_from_file_location('ss_content', path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod
    return importlib.import_module(c)
