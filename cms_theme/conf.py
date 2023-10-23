from django.conf import settings
from django.utils.translation import gettext_lazy as _


def _get_layouts(name: str) -> tuple:
    return getattr(settings, name, (("default", _("Default")),))


CASE_STUDY_LAYOUTS = _get_layouts("CASE_STUDY_LAYOUTS")
FEATURE_LAYOUTS = _get_layouts("FEATURE_LAYOUTS")
PERSON_LAYOUTS = _get_layouts("PERSON_LAYOUTS")
PROMO_LAYOUTS = _get_layouts("PROMO_LAYOUTS")
