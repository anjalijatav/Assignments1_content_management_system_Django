# from django.shortcuts import render
# # # Create your views here.
from rest_framework import generics, viewsets, mixins, serializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from authour.userfield  import Userfield,UserfieldManager
from authour.contentfield import  ContentfieldManager,Contentfield
from authour.serializers import UserfieldSerializer, ContentfieldSerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

########['GET', 'POST', PUT, 'DELETE']) method
class CreateUserfieldView(viewsets.ModelViewSet):
    """Create new user in the system"""
    queryset = Userfield.objects.all().order_by('email')
    serializer_class = UserfieldSerializer
    def UserfieldView_list(self, request):
        if request.method == 'GET':
            userfields = Userfield.objects.all()
            queryset = Userfield.objects.all().order_by('email')
            serializer_class = UserfieldSerializer(userfields)
            return JsonResponse(serializer_class.data, safe=False)

        elif request.method == 'POST':
            userfields_data = JSONParser().parse(request)
            serializer_class = UserfieldSerializer(data=userfields_data)
            if serializer_class.is_valid():
                serializer_class.save()
                return JsonResponse(serializer_class.data, status=status.HTTP_201_CREATED)
            return JsonResponse(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            count = Userfield.objects.all().delete()
            return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])},
                                        status=status.HTTP_204_NO_CONTENT)


    def UserfieldView_detail(self, request, pk):
        try:
            userfields = Userfield.objects.get(pk=pk)
        except Userfield.DoesNotExist:
            return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer_class = UserfieldSerializer(userfields)
            return JsonResponse(serializer_class.data)

        elif request.method == 'PUT':
            userfields_data = JSONParser().parse(request)
            serializer_class = UserfieldSerializer(userfields, data=userfields_data)
            if serializer_class.is_valid():
                serializer_class.save()
                return JsonResponse(serializer_class.data)
            return JsonResponse(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            userfields.delete()
            return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


    def Userfield_list_published(self, request):
        userfields = Userfield.objects.filter(published=True)

        if request.method == 'GET':
            serializer_class = UserfieldSerializer(userfields, many=True)
            return JsonResponse(serializer_class.data, safe=False)

class CreateContentfieldView(viewsets.ModelViewSet):
    queryset = Contentfield.objects.all().order_by('title')
    serializer_class = ContentfieldSerializer
    def ContentfieldView_list(self, request):
        if request.method == 'GET':
            contentfield = Contentfield.objects.all()
            queryset = Contentfield.objects.all().order_by('email')
            serializer_class = ContentfieldSerializer(contentfield)
            return JsonResponse(serializer_class.data, safe=False)

        elif request.method == 'POST':
            # queryset = Userfield.objects.all().order_by('email')
            # serializer_class = UserfieldSerializer
            contentfield_data = JSONParser().parse(request)
            serializer_class = ContentfieldSerializer(data=contentfield_data)
            if serializer_class.is_valid():
                serializer_class.save()
                return JsonResponse(serializer_class.data, status=status.HTTP_201_CREATED)
            return JsonResponse(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            count = Contentfield.objects.all().delete()
            return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])},
                                status=status.HTTP_204_NO_CONTENT)

    def ContentfieldView_detail(self, request, pk):
        try:
            contentfield = Contentfield.objects.get(pk=pk)
        except Contentfield.DoesNotExist:
            return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer_class = ContentfieldSerializer(contentfield)
            return JsonResponse(serializer_class.data)

        elif request.method == 'PUT':
            contentfield_data = JSONParser().parse(request)
            serializer_class = ContentfieldSerializer(contentfield, data=contentfield_data)
            if serializer_class.is_valid():
                serializer_class.save()
                return JsonResponse(serializer_class.data)
            return JsonResponse(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            contentfield.delete()
            return JsonResponse({'message': 'Tutorial was deleted successfully!'},
                                status=status.HTTP_204_NO_CONTENT)

    def Contentfield_list_published(self, request):
        contentfield = Contentfield.objects.filter(published=True)

        if request.method == 'GET':
            serializer_class = ContentfieldSerializer(contentfield, many=True)
            return JsonResponse(serializer_class.data, safe=False)


# # ########todo Imp
# class CreateUserfieldView(viewsets.ModelViewSet):
#     """Create new user in the system"""
#     queryset = Userfield.objects.all().order_by('email')
#     serializer_class = UserfieldSerializer
#
# class CreateContentfieldView(viewsets.ModelViewSet):
#     queryset = Contentfield.objects.all().order_by('title')
#     serializer_class = ContentfieldSerializer
#     ###################################TODO till here if below one not works