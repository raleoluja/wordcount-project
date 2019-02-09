from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request, 'home.html')

def ralens(request):
    return render(request, 'ralens.html')

def count(request):
    fulltext = request.GET['fulltext']

    worldlist = fulltext.split()

    worddictionary = {}


    for word in worldlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1


    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)





    return render(request, 'count.html', {'fulltext':fulltext, 'count': len(worldlist), 'sortedwords': sortedwords})


