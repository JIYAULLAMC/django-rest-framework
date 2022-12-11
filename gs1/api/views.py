from django.shortcuts import render

# Create your views here.


# single student data
from django.http import HttpResponse, JsonResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# def student_detail(request, pk):
#     stu = Student.objects.get(id=pk)
#     serializer = StudentSerializer(stu)
#     json_data = JSONRenderer().render(serializer.data)
#     return HttpResponse(json_data, content_type="application/json")

# def student_list(request):
#     stu = Student.objects.all()
#     serializer = StudentSerializer(stu, many=True)
#     return JsonResponse(serializer.data, safe=False)


import io
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data = pythondata)
        print("--------------------")
        if serializer.is_valid():
            print("++++++++++++++")
            serializer.save()
            res = { 'msg' : 'the data is created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type="application/json")

        else:
            print("****************")
            print(serializer.errors)
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type="application/json")