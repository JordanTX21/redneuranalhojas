import base64
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import ImageUploadSerializer

class ImageView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ImageUploadSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({"success":False,"message":"Error de validación","data":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
        file = request.data.get('file')

        # AQUI IRIA EL ALGORITMO DE MAPEO

        encoded_image = base64.b64encode(file.read()).decode('utf-8')

        return Response({"success":True,"message": "Imagen recibida con éxito","data":encoded_image}, status=status.HTTP_200_OK)