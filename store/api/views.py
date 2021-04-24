from rest_framework.response import Response
from rest_framework import status
from store.models import Store
from .serializers import StoreSerializer, UserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework import generics
from rest_framework import viewsets


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def index(request):
    posts = Store.objects.all()
    serializer = StoreSerializer(instance=posts, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def create(request):
    serializer = StoreSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success": True,
            "message": "book has been added successfully"
        }, status=status.HTTP_201_CREATED)

    return Response(data={
        "success": False,
        "errors": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def api_signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success": True,
            "message": "user has been registered successfully"
        }, status=status.HTTP_201_CREATED)

    return Response(data={
        "success": False,
        "errors": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete(request, id):
    book = Store.objects.get(pk=id)
    serializer = StoreSerializer(instance=book, many=False)
    serializer.delete()
    return Response(data={
        'message': 'deleted',
        'success': True
    }, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update(request, id):
    book = Store.objects.get(pk=id)
    serializer = StoreSerializer(instance=book, many=False, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            'message': 'book updated',
            'success': True
        }, status=status.HTTP_201_CREATED)
    return Response(data={
        'Error': serializer.errors,
        'success': False
    }, status=status.HTTP_400_BAD_REQUEST)


class CreateBook(generics.CreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class ListBook(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class CrudBook(generics.RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
