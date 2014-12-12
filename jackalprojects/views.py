from django.shortcuts import render_to_response
from django.template import RequestContext
from member.models import On_Sales, Member
from django.http import HttpResponseRedirect, HttpResponse

__author__ = 'cemkiy'
__author__ = 'barisariburnu'
__author__ = 'kaykisizcom'

# Create your views here.


def home_page(request):
    tickets = On_Sales.objects.filter(active=True)
    return render_to_response('home_page.html', locals(), context_instance=RequestContext(request))

def ticket_pool(request):
    tickets = On_Sales.objects.filter(active=True)
    return render_to_response('ticket_pool.html', locals())

def contact_us(request):
    return render_to_response('contact_us.html', locals(), context_instance=RequestContext(request))

def forgotten_password(request):
    return render_to_response('forgotten_password.html', locals(), context_instance=RequestContext(request))

def public_profile(request, user_id):
    try:
        member = Member.objects.filter(username=request.user.username)[0]
    except Exception as e:
        print e
        return HttpResponseRedirect('/sorry')
    return render_to_response('public_profile.html', locals())

def page_sorry(request):
    return render_to_response('sorry.html', locals())
