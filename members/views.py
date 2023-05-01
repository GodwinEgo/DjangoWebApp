from django.http import HttpResponse
from django.template import loader



def members(request):
    template = loader.get_template('FirstFile.html')
    return HttpResponse(template.render())

# Create your views here.
