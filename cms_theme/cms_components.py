from django import forms
from django.utils.translation import gettext_lazy as _
from djangocms_frontend.component_base import CMSFrontendComponent
from djangocms_frontend.component_pool import components
from djangocms_frontend.fields import HTMLFormField



@components.register
class Hero(CMSFrontendComponent):
    """Hero component with background grid option"""

    class Meta:
        plugin_name = _("Hero")
        render_template = "hero/hero.html"
        allow_children = True
        child_classes = [
            "TextPlugin",
            "TextLinkPlugin",
            "ImagePlugin",
            "HeadingPlugin",
            "CounterPlugin",
        ]
        mixins = ["Background", "Spacing", "Attributes"]

    background_grid = forms.BooleanField(
        label=_("Show background grid"),
        required=False,
        initial=False,
    )

@components.register
class CTAPanel(CMSFrontendComponent):
    """CTAPanel component with background grid option"""

    class Meta:
        name = _("CTA Panel")
        render_template = "cta/cta_panel.html"
        allow_children = True
        child_classes = [
            "TextLinkPlugin",
        ]
        mixins = ["Background", "Spacing", "Attributes"]

    background_grid = forms.BooleanField(
        label=_("Show background grid"),
        required=False,
        initial=False,
    )

    eyebrow_text = forms.CharField(
        label=_("Eyebrow text"),
        required=False,
    )

    main_heading = HTMLFormField(
        label=_("Main heading"),
        required=False,
    )

    content_alignment = forms.ChoiceField(
        label=_("Content alignment"),
        choices=[
            ("start", _("Start")),
            ("center", _("Center (Default)")),
            ("end", _("End"))
        ],
        initial="center",
        help_text=_("Controls horizontal alignment of all content")
    )

