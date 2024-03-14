import os

os.system("python setup.py bdist_wheel")
os.system("pip install dist/gFrame-1.0.0-py3-none-any.whl --force-reinstall")