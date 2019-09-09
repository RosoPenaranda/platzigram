#Django
from django.http import HttpResponse


#utilities
from datetime import datetime

def helloWorld(request):
    return HttpResponse('<html><head><body><h1>Hello World! {id}</h1></body></head></html>'.format(id=request.GET['id']))


def time(request):
    
    now = datetime.now().strftime('%b %d, %Y - %H:%M')
    return HttpResponse('hora: {now}'.format(now=str(now)))


def hi(request):
  from django.http import JsonResponse
  #import pdb;pdb.set_trace()
  numbers = [int(i) for i in request.GET['numbers'].split(',')]
  OrderNumbers = sorted(numbers)
  
  print(OrderNumbers)
  return JsonResponse({'numbers': OrderNumbers})