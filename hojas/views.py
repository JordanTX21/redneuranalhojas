from django.http import HttpResponse, JsonResponse


def api(request):
    return JsonResponse({"success":True, "message": "validado","data":[]}, status=200)
