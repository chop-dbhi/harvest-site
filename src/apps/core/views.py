from django.http import HttpResponse, Http404
from django.template import RequestContext, TemplateDoesNotExist
from django.template.loader import select_template

TEMPLATE_INDEX = 'index'
TEMPLATE_EXTENSION = 'html'

def direct_to_template(request, path):
    # Since we are mapping to HTML files, catch '/foobar/index' requests
    # and return 404
    if path.endswith('/{}'.format(TEMPLATE_INDEX)):
        raise Http404

    # Possible templates. Check for a file of the path name or a directory
    # with the name with an index.html file
    templates = [
        '{}.{}'.format(path, TEMPLATE_EXTENSION), # e.g. foobar.html
        '{}/{}.{}'.format(path, TEMPLATE_INDEX, TEMPLATE_EXTENSION) # foobar/index.html
    ]

    try:
        template = select_template(templates)
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(RequestContext(request)))
