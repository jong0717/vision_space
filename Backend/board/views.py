from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Board, Tab, Type, Note, History
from .serializers import BoardSerializer, TabSerializer, TypeSerializer, NoteSerializer, HistorySerializer

# Create your views here.
from rest_framework import generics, mixins
from rest_framework.generics import GenericAPIView
from rest_framework import status

# class BoardView(generics.ListCreateAPIView):
#     queryset = Board.objects.all()
#     serializer_class = BoardSerializer
    
# class BoardDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Board.objects.all()
#     serializer_class = BoardSerializer

class BoardView(mixins.CreateModelMixin, 
                    mixins.ListModelMixin,
                    GenericAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class BoardDetailView(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        GenericAPIView):
    def get(self, request, *args, **kwargs):
            return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
            return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
            return self.destroy(request, *args, **kwargs)



# class BoardDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Board.objects.all()
#     serializer_class = BoardSerializer
#     print('board시리얼라이저 코드는',serializer_class)

class TabView(generics.ListCreateAPIView):
    queryset = Tab.objects.all()
    serializer_class = TabSerializer
    print('tab시리얼라이즈',serializer_class)


# class BoardView(GenericAPIView):
#     permission_classes = (IsAuthenticated, )

#     def get(self, request, *args, **kwargs):
#         boards = Board.objects.all()
#         serializer = BoardSerializer(boards, many=True)
#         return Response(serializer.data)

#     def post(self, request, *args, **kwargs):
#         serializer = BoardSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request, pk, *args, **kwargs):
#         board = self.get_object(pk)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, *args, **kwargs):
#         board = self.get_object(pk)
#         board.delete()
#         return Response("DEBUG")


class TabView(GenericAPIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        return Response("DEBUG")

    def post(self, request, *args, **kwargs):
        return Response("DEBUG")

    def put(self, request, *args, **kwargs):
        return Response("DEBUG")

    def delete(self, request, *args, **kwargs):
        return Response("DEBUG")

class NoteView(GenericAPIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        return Response("DEBUG")

    def post(self, request, *args, **kwargs):
        return Response("DEBUG")

    def patch(self, request, *args, **kwargs):
        return Response("DEBUG")

    def delete(self, request, *args, **kwargs):
        return Response("DEBUG")

class TypeView(GenericAPIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        return Response("DEBUG")

    def post(self, request, *args, **kwargs):
        return Response("DEBUG")

    def delete(self, request, *args, **kwargs):
        return Response("DEBUG")

class HistoryView(GenericAPIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        return Response("DEBUG")

    def post(self, request, *args, **kwargs):
        return Response("DEBUG")

    def delete(self, request, *args, **kwargs):
        return Response("DEBUG")