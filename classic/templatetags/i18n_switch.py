from django import template
from django.conf import settings

register = template.Library()

@register.simple_tag(takes_context=True)
def language_label(context, code):
    labels = {
        'fr': 'Français',
        'en': 'English',
    }
    return labels.get(code, code)

@register.simple_tag(takes_context=True)
def switch_language_url(context, lang):
    request = context.get('request')
    if not request:
        return f'/{lang}/'

    path = request.get_full_path()
    if path.startswith('/fr/'):
        path = path.replace('/fr/', f'/{lang}/', 1)
    elif path.startswith('/en/'):
        path = path.replace('/en/', f'/{lang}/', 1)
    elif path.startswith('/'):
        path = f'/{lang}{path}'
    else:
        path = f'/{lang}/{path}'
    return path
