from django.conf import settings
from django.utils import translation


class LanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        lang = request.GET.get('lang')
        # validate language
        supported = {code for code, _ in getattr(settings, 'LANGUAGES', [('fr', 'Français'), ('en', 'English')])}
        if lang not in supported:
            lang = request.session.get('language', getattr(settings, 'LANGUAGE_CODE', 'fr'))
        else:
            request.session['language'] = lang

        request.session['language'] = lang
        # activate translation for this request
        translation.activate(lang)
        request.LANGUAGE_CODE = translation.get_language()
        # keep backward-compatible attribute used in templates
        request.language = request.LANGUAGE_CODE

        response = self.get_response(request)
        if hasattr(response, 'set_cookie'):
            # use Django's LANGUAGE_COOKIE_NAME when possible
            cookie_name = getattr(settings, 'LANGUAGE_COOKIE_NAME', 'language')
            response.set_cookie(cookie_name, request.LANGUAGE_CODE, max_age=60 * 60 * 24 * 30)
        return response
