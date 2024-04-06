from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
# Create your views here.
arr = ['Java','Python','Cplusplus','C','DotNet','Javascript','PHP','Swift']
globalcnt = dict()

def index(request):
    # return HttpResponse("server started")
    mydict = {
       "arr":arr 
    }
    return render(request,'index.html',context=mydict)

def getquery(request):
    q = request.GET['languages'] #languages come from the name of index.html form get
    if q in globalcnt:
        globalcnt[q] = globalcnt[q] + 1
    else:
        globalcnt[q]=1  #this is for voting count logic
    mydict = {
        "arr" : arr,
        "globalcnt":globalcnt
    }
    return render(request,'index.html',context = mydict)

def sortdata(request):
    #pass # for initially check to that this fucntion working or not
    
    global globalcnt #accessing a variable that is global
    
    globalcnt = dict(sorted(globalcnt.items(),key = lambda x:x[1],reverse=True))
    mydict = {
       "arr":arr,
       "globalcnt" : globalcnt

    }
    return render(request,'index.html',context=mydict)
