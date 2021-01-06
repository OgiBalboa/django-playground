import os
packages = ["django", "python-decouple", "django-allauth", "django-crispy-forms","django-countries","django-debug-toolbar","stripe","pillow",]

code = "pip install {}".format(" ".join(packages))
os.system(code)