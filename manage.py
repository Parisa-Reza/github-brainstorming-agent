#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
#!/usr/bin/env python

import os
import sys

for var in ("NO_PROXY", "no_proxy"):
    value = os.environ.get(var)
    if value:
        os.environ[var] = ",".join(
            item
            for item in value.split(",")
            if item != "prefix:local."
        )




def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
