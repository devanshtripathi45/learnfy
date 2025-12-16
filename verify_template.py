import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','learnfy.settings')
django.setup()
from django.template.loader import get_template
try:
    get_template('admin/index.html')
    print('TEMPLATE_FOUND')
except Exception as e:
    print('TEMPLATE_ERROR:', type(e).__name__, str(e))
