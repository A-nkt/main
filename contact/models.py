from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, FieldRowPanel, InlinePanel, MultiFieldPanel
from wagtail.core.fields import RichTextField
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtailcaptcha.models import WagtailCaptchaEmailForm


# Create your models here.
class FormField(AbstractFormField):  # Formのフィールドを定義
    Page = ParentalKey(
        'ContactPage',  # 反応させるclass名を入力
        on_delete=models.CASCADE,
        related_name='form_fields',
    )


# フォーム機能を実装したclassを定義
class ContactPage(WagtailCaptchaEmailForm):
    template = "contact/contact_page.html"  # 返すhtmlファイルを定義
    landing_page_template = "contact/contact_page_landing.html"

    intro = RichTextField(blank=True)  # RichTextFieldを定義
    thank_you_text = RichTextField(blank=True)  # RichTextFieldを定義

    # adminのパネルを定義
    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro'),
        InlinePanel('form_fields', label='Form Fields'),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldRowPanel([FieldPanel('to_address', classname='col6')]),
            FieldPanel('subject'),
        ], heading="Email Settings")
    ]
