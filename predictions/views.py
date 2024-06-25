from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import numpy as np
from keras.models import load_model
import tensorflow as tf
from .serializers import PredictGenreSerializer

# Cargar el modelo usando la ruta completa
model_path = 'clf_music_genre.h5'
model = load_model(model_path)

# Lista de géneros en el mismo orden que LabelEncoder
genres = ['Blues', 'Classical', 'Country', 'Electronic', 'HipHop', 'Jazz', 'Metal', 'Pop', 'Reggae', 'Rock']

class PredictGenre(APIView):
    def post(self, request, format=None):
        serializer = PredictGenreSerializer(data=request.data)
        if serializer.is_valid():
            features = [serializer.validated_data[key] for key in serializer.validated_data.keys()]
            features_array = np.array([features])
            
            # Hacer la predicción
            prediction = model.predict(features_array)
            predicted_genre = genres[np.argmax(prediction)]
            
            return Response({'predicted_genre': predicted_genre}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def home(request):
    return render(request, 'index.html')
