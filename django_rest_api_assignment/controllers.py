from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Dog
from .serializers import DogSerializer


class DogDetail(APIView):
    def get(self, request, pk):
        dog = Dog.objects.get(pk=pk)
        serializer = DogSerializer(dog)
        return Response(serializer.data)

    def put(self, request, pk):
        dog = Dog.objects.get(pk=pk)
        serializer = DogSerializer(dog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        dog = Dog.objects.get(pk=pk)
        dog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DogList(APIView):
    def get(self, request):
        dogs = Dog.objects.all()
        serializer = DogSerializer(dogs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
