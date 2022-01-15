import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE","my_site.settings")
django.setup()