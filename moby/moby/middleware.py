from django.conf import settings
from django.utils import translation
from django.utils.deprecation import MiddlewareMixin
from django.utils.translation import gettext_lazy as _


class LanguageMiddleware(MiddlewareMixin):

    def process_request(self, request):
        print(request.GET, 8888)
        if 'lang' in request.GET:
            language = request.GET.get('lang', 'ru')
            if language in dict(settings.LANGUAGES).keys():
                request.session['_language'] = language
        print(request.session.get('_language'), 9999)
        language = request.session.get('_language', 'ru')
        translation.activate(language)
