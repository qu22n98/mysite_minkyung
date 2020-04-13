from django.shortcuts import render
import re



# Create your views here.

def home(request):
    return render(request,'today_expense/home.html')
#home이라는 함수에서 request변수를 받고 그 내용을 today_expense의 home.html로 보낼거임
#그 경로가 저 주황글씨

def result(request):
    text=request.GET['fulltext']
    count=0

    numbers = re.findall("\d+", text)

    for a in numbers:
        count+=int(a)

    return render(request,'today_expense/result.html',{'count':count})
