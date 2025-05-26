from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Document
from .serializers import DocumentSerializer
import google.generativeai as genai
import os
from django.conf import settings

# Create your views here.

class DocumentViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer

    def get_queryset(self):
        return Document.objects.filter(user=self.request.user)

    @action(detail=True, methods=['post'])
    def ask(self, request, pk=None):
        document = self.get_object()
        question = request.data.get('question')
        
        if not question:
            return Response({'error': 'Question is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Configure Gemini API
            genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
            model = genai.GenerativeModel('gemini-pro')

            # Prepare context from document content
            context = f"Document content: {document.content}\n\nQuestion: {question}"
            
            # Generate response
            response = model.generate_content(context)
            
            return Response({'answer': response.text})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
