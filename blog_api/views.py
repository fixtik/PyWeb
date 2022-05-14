from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
import rest_framework.status as status
from django.shortcuts import get_object_or_404

from blog.models import Note
from . import serializers
# Create your views here.

class NoteListCreateAPIView(APIView):

    def get(self, request: Request) -> Response:
        """Получение списка всех записей"""
        objects = Note.objects.all()
        return Response(
            [serializers.note_to_json(obj)
                for obj in objects])

    def post(self,  request: Request) -> Response:
        data = request.data
        note = Note(**data)
        note.save(force_insert=True)
        return Response(serializers.note_create(note), status.HTTP_201_CREATED)

class NoteDetailAPIView(APIView):
    """Получение единичной записи"""
    def get(self, request: Request, pk) -> Response:
        ans = get_object_or_404(Note, pk=pk)
        return Response(serializers.note_to_json(ans))

    def put(self,  request: Request, pk) -> Response:
        """Обновление записи по ключу"""
        note = get_object_or_404(Note, pk=pk)
        note.title = request.data['title']
        note.message = request.data['message']
        note.save()
        return Response(serializers.note_create(note), status.HTTP_200_OK)



