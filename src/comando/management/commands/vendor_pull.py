import helpers
from django.core.management.base import BaseCommand
from django.conf import settings
from typing import Any


STATICFILES_VENDOR_DIR = getattr(settings, "STATICFILES_VENDOR_DIR")

VENDOR_STATICFILES = {
    "flowbite.min.js":"https://cdn.jsdelivr.net/npm/flowbite@2.5.1/dist/flowbite.min.js",
    "flowbite.min.js.map":"https://cdn.jsdelivr.net/npm/flowbite@2.5.1/dist/flowbite.min.js.map",
    "flowbite.min.css":"https://cdn.jsdelivr.net/npm/flowbite@2.5.1/dist/flowbite.min.css"
}

class Command(BaseCommand):
    def handle(self, *args:Any, **options: Any):
        print("Downloading files")
        completed_urls = []
        for name,url in VENDOR_STATICFILES.items():
            outpath = STATICFILES_VENDOR_DIR / name
            dl_success = helpers.download_to_local(url, outpath)
            if dl_success:
                completed_urls.append(url)
            else:
                self.stdout.write(
                    self.style.ERROR(f"failed to download {url}")
                )
        if set(completed_urls) == set(VENDOR_STATICFILES.values()):
                self.stdout.write(
                    self.style.SUCCESS(f"successfully updated")
                )
        else:
                self.stdout.write(
                    self.style.ERROR(f"failed to download {url}")
                )
