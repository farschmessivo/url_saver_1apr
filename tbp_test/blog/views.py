from blog.forms import UrlForm
from blog.mozscape import Mozscape
from django.shortcuts import render
from django.http import HttpResponseRedirect
import requests


def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UrlForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            url = form.save(commit=False)
            url.upa = get_upa(url.url)
            url.pda = get_pda(url.url)
            url.save()
            return HttpResponseRedirect('blog/thanks')
        else:
            return render(request, 'blog/index.html', {
                'form': form,
                'message': 'There is smth wrong with your URL'})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = UrlForm()
    # Will handle the bad form, new form, or no form supplied cases.
    #  Render the form with error messages (if any).
    return render(request, 'blog/index.html', {'form': form})


def thanks(request):
    form = UrlForm()
    return render(request, 'blog/index.html', {'form': form, 'message': 'Thank you'})

client = Mozscape(
        'mozscape-7580c7d84a',
        '2badc7841aa72676a9b8ebb2fd856bf5')


def get_upa(url):
    metric = client.urlMetrics(url)
    print(metric)
    return metric['upa']


def get_pda(url):
    metric = client.urlMetrics(url)
    print(metric)
    return metric['pda']


# upa =  Mozscape.UMCols.domainAuthority
# pda = Mozscape.UMCols.pageAuthority




# upa = 34359738368
# pda = 68719476736
#
# def get_metric(url, col):
#     return requests.get("http://lsapi.seomoz.com/linkscape/url-metrics/"+url+"?Cols="+str(col)+"&AccessID=mozscape-7580c7d84a&Expires=1225138899&Signature=2badc7841aa72676a9b8ebb2fd856bf5", auth=('mozscape-7580c7d84a','2badc7841aa72676a9b8ebb2fd856bf5'))
#
#
# def get_upa(url):
#     metric = get_metric(url, upa)
#     return metric.json()['upa']
#
#
# def get_pda(url):
#     metric = get_metric(url, pda)
#     return metric.json()['pda']

