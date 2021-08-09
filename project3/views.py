from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

arr=['Java','C++','C','Python','Javascript','Perl','Html','CSS','PHP','Django','Flask','Swift','SQL']
globalcnt = dict()
def fun(request):
    mydic={
        "arr":arr
    }
    return render(request,'index.html',context=mydic)

def getqurey(request):
    q=request.GET['language']
    if q in globalcnt:
        # if q is already present
        globalcnt[q] = globalcnt[q]+1
    else:
        # for 1st time occurrence
        globalcnt[q]=1
    mydic={
        "arr":arr,
        "globalcnt" : globalcnt
    }
    return render(request,'index.html',context=mydic)

def sortdata(request):
    global globalcnt
    globalcnt = dict(sorted(globalcnt.items(),key=lambda x:x[1],reverse=True))
    mydic={
        "arr":arr,
        "globalcnt" : globalcnt
    }
    return render(request,'index.html',context=mydic)