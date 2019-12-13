from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('xss_sample/index.html')
    context = {
        'body_context': '<script>confirm("This is hacked");</script>&<>"\'/',
        'username': '" /> <script>confirm("This is hacked");</script> <input>',
        'bg_color': 'green; background-color: red;',
        'js_script': 'confirm("you are hacked");',
        'href_val': 'javascript: confirm("hacked");',
    }
    return HttpResponse(template.render(context, request))
