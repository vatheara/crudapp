from django.shortcuts import render
from django.http import HttpResponse
import requests
def test(request):
    return HttpResponse("yes it's works!")
def fb_cmt(request):
    TOKEN = "EAAEDHsLYgpUBAOoOargWFsAFKTmcs3AgvZAE8axX2Qr2ZArCC8HK2yxc2ZBZCqVHFP8p1vKqLZCIAp3aGLKsfcj6TNAWCGCxRMc6wxJbTphOF0ZAHfoaUuLrXmPzyVwY8ieQGPcPr0RV5kwE7nR0VUuGtbH8BfljJqnpkGt2VSxwZDZD"
    r = requests.get("https://graph.facebook.com/v8.0/950349465447726/comments?access_token="+TOKEN)
    cmt_count = len(r.json()['data'])
    all_cmt = []
    for i in range(cmt_count):
        c = r.json()['data'][i]['from']['name'] + " : " + r.json()['data'][i]['message']
        all_cmt.append(c)
    #return  HttpResponse(r.json()['data'][0]['from']['name'] + " : " + r.json()['data'][0]['message'])
    #return HttpResponse(len(r.json()['data']))
    return render(request,'index.html',
                  {'count':cmt_count,
                    'cmt': all_cmt,
                   })
def fb_token(request):
    pass

