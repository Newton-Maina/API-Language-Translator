from django.shortcuts import render
from googletrans import Translator

def translator(request):
    return render(request, 'translator.html', {'navbar': 'translator'})

def index(request):
    return render(request, 'index.html', {'navbar': 'home'})

def translation(request):
    if request.method == 'GET':
        text = request.GET.get('text')
        lang = request.GET.get('lang')

        if not text or not lang:
            return render(request, 'index.html', {'error_message': 'Text or language not provided.'})

        try:
            translator = Translator()

            # Detect language if source language is not provided
            dt = translator.detect(text)
            dt2 = dt.lang

            # Translate text to target language
            translation = translator.translate(text, dest=lang)
            tr = translation.text

            return render(request, 'translation.html', {
                'original_text': text,
                'translation': tr,
                'u_lang': dt2,
                't_lang': lang
            })
        except Exception as e:
            return render(request, 'index.html', {'error_message': f'Error during translation: {str(e)}'})
    else:
        return render(request, 'index.html', {'error_message': 'Invalid request method.'})