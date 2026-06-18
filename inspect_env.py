import sys
import os
import site
import importlib.util

print('executable:', sys.executable)
print('version:', sys.version)
print('prefix:', sys.prefix)
print('base_prefix:', getattr(sys, 'base_prefix', None))
print('venv:', 'VIRTUAL_ENV' in os.environ and os.environ['VIRTUAL_ENV'])
print('sys.path:')
for p in sys.path:
    print('  ', p)
print('site-packages:')
try:
    for p in site.getsitepackages():
        print('  ', p)
except Exception as e:
    print('  site.getsitepackages() failed:', e)

for name in ['PyPDF2', 'pymysql', 'sentence_transformers']:
    spec = importlib.util.find_spec(name)
    print(f"{name}:", spec)
    if spec:
        print('   origin:', spec.origin)
