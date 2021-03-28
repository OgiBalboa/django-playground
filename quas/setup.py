import os
packages = ["django", "python-decouple", "django-allauth", "django-crispy-forms",
            "django-countries","django-debug-toolbar","stripe","pillow","django-multiselectfield",
            "django-ajax", "django_rest_framework"]

code = "pip install {}".format(" ".join(packages))
os.system(code)