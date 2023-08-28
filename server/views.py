from django.http import JsonResponse



def  hello(request):
    print('je;;;;;;;;;;;;')
    return JsonResponse({'success': True})

