#i have created this file -Agnik
from django.http import HttpResponse
from django.shortcuts import render
import sql_data
def index(request):
    
    return render(request,'index.html')
    #return HttpResponse("Home <a href='/removepunc'>removepunc</a> <a href='/capitalizefirst'>capfirst</a> <a href='/newlineremove'>newlineremove</a><a href='/spaceremove'>spaceremove</a><a href='/charcount'>charcount</a>")
def removepunc(text):
    analyzed = ''
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for char in text:
        if char not in punctuations:
            analyzed += char
    return analyzed

def fullcaps(text):
    analyzed = ''
    for char in text:
        analyzed += char.upper()
    return analyzed

def newlineremover(text):
    analyzed = ''
    for char in text:
        if char != "\n" and char!='\r':
            analyzed += char
    return analyzed

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    remove_punc = request.POST.get('removepunc', 'off')
    full_caps = request.POST.get('fullcaps', 'off')
    newline_remover = request.POST.get('newlineremover', 'off')
    
    analyzed_text = djtext
    
    if remove_punc == "on":
        analyzed_text = removepunc(analyzed_text)
       # print(analyzed_text)
    if full_caps == 'on':
        analyzed_text = fullcaps(analyzed_text)
      #  print(analyzed_text)
    if newline_remover == 'on':
        analyzed_text = newlineremover(analyzed_text)
     #   print(analyzed_text)

    #print(analyzed_text)
    
    params = {'purpose': 'Analyzed Text', 'analyzed_text': analyzed_text}
    return render(request, 'analyze.html', params)
def about_us(request):
    return render(request,"about_us.html")
def contact_us(request):

    return render(request,'contact_us.html')
def submit(request):
    email = request.POST.get('email', 'default')
    message=request.POST.get('message','default')
    sql_data.write_data({"email":email,"message":message})
    params={"message":"Message Sent!!"}
    return render(request,'contact_us.html',params)


'''def capfirst(request):
    return HttpResponse("capitalize first <a href='..'>home</a>")

def newlineremove(request):
    return HttpResponse("capitalize first <a href='..'>home</a>")


def spaceremove(request):
    return HttpResponse("space remover <a href='..'>home</a>")

def charcount(request):
    return HttpResponse("charcount <a href='..'>home</a>")
    '''
