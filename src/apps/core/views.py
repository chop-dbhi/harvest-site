from django.http import HttpResponse, Http404
from django.template import RequestContext, TemplateDoesNotExist
from django.template.loader import get_template

TEMPLATE_EXTENSION = '.html'

def direct_to_template(request, path):
    "Attempts to find and render the page based on the path."
    template_name = path + TEMPLATE_EXTENSION
    try:
        template = get_template(template_name)
    except TemplateDoesNotExist:
        raise Http404
    context = RequestContext(request)
    return HttpResponse(template.render(context))
