from django.template.response import TemplateResponse
from .forms import FeedbackForm, FileForm


def index(request):
    return TemplateResponse(request, 'main/index.html')


def hello(request):
    return TemplateResponse(request, 'main/hello.html')


def test_batch(request):
    return TemplateResponse(request, 'main/test_batch.html')


def js_api(request):
    return TemplateResponse(request, 'main/js_api.html')


def form(request):
    context = {
        'form': FeedbackForm()
    }
    return TemplateResponse(request, 'main/form.html', context)


def upload_form(request):
    context = {
        'form': FileForm()
    }
    return TemplateResponse(request, 'main/upload_form.html', context)
