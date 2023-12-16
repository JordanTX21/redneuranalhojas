import base64
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import ImageUploadSerializer
from minisom import MiniSom
import pickle
import numpy as np
from skimage import color, io, transform, filters, img_as_float
import pandas as pd
from io import BytesIO
import matplotlib.pyplot as plt

class ImageView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ImageUploadSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({"success":False,"message":"Error de validación","data":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
        file = request.data.get('file')

        # Guarda el archivo en el sistema de archivos temporal
        with open(r'hojas\public\archivo_temporal.jpg', 'wb') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        # AQUI IRIA EL ALGORITMO DE MAPEO

        # Cargar la imagen
        # img = io.imread(r'LUCUMA\IMG_20231112_133040.jpg')
        img = io.imread(r'hojas\public\archivo_temporal.jpg')

        # Coordenadas de inicio y fin para el recorte
        start_row, end_row = 1, 254  # Recortar desde la fila 1 hasta la fila 254 (254 píxeles)
        start_col, end_col = 1, 254  # Recortar desde la columna 1 hasta la columna 254 (254 píxeles)

        # Convertir la imagen a escala de grises
        img_gray = color.rgb2gray(img)

        # Aplicar filtro Sobel
        img_sobel = filters.sobel(img_gray)

        # Normalizar los píxeles
        img_normalized = img_as_float(img_sobel)

        # Coordenadas de inicio y fin para el recorte
        start_row, end_row = 1, 254  # Recortar desde la fila 1 hasta la fila 254 (254 píxeles)
        start_col, end_col = 1, 254  # Recortar desde la columna 1 hasta la columna 254 (254 píxeles)

        # Realizar el recorte
        img_recortada = img_normalized[start_row:end_row, start_col:end_col]

        # Aplicar mediana a la imagen redimensionada
        img = np.median(img_recortada, axis=(0, 1))

        # Redimensionar la imagen recortada a 18x18
        resized_img = transform.resize(img, (18, 18), mode='reflect', anti_aliasing=True)

        # Convertir la matriz 18x18 a un vector de 1x324
        vectorized_img = resized_img.reshape(1, -1)

        #print(vectorized_img)


        # Cargar la red SOM entrenada
        with open(r'hojas\public\modelo_som_entrenado.pkl', 'rb') as f:
            som = pickle.load(f)


        # Asignar categoría A a los primeros 25 datos y categoría B a los demás
        # Cargar las categorías desde el archivo Excel
        df_categorias = pd.read_excel(r'hojas\public\categorias_excel.xlsx')

        # Obtener las dimensiones de la red SOM
        som_size = som.get_weights().shape[:2]

        # Obtener las coordenadas de la BMU para cada dato en 'vectorized_img'
        winners = np.array([som.winner(x) for x in vectorized_img])

        # Asegurarse de que 'categories' tenga la forma correcta (2D)
        categories = np.reshape(df_categorias, (som.get_weights().shape[0], som.get_weights().shape[1]))

        # Obtener las categorías asociadas a los datos cercanos a la BMU
        cercanas_categorias = categories[winners[:, 0], winners[:, 1]]

        # Mostrar las coordenadas de la BMU y las categorías asociadas
        for bmu, categoria in zip(winners, cercanas_categorias):
            if(categoria=='A'):
                print(f"Coordenadas de la BMU: {bmu}, Categoría: {categoria}") #, Tipo: 1 Lito - Normal TAZA
            elif(categoria=='B'):
                print(f"Coordenadas de la BMU: {bmu}, Categoría: {categoria}")#, Tipo: 650 ml - Alcalina AUDIFONO
            else:
                print(f"Coordenadas de la BMU: {bmu}, Categoría: {categoria}")#, Tipo: V

        imagenes_base64 = {}
        imagenes_base64['Gris'] = base64_image(img_gray)
        imagenes_base64['Sobel'] = base64_image(img_sobel)
        imagenes_base64['Normalized'] = base64_image(img_normalized)
        imagenes_base64['Recortada'] = base64_image(img_recortada)
        imagenes_base64['Resized'] = base64_image(resized_img)

        return Response({"success":True,"message": "Imagen recibida con éxito","data":{
            "images": imagenes_base64,
            "bmu": bmu,
            "categoria": categoria
        }}, status=status.HTTP_200_OK)

class MapView(APIView):
    def post(self, request, *args, **kwargs):
        file = request.data.get('file')

        # Guarda el archivo en el sistema de archivos temporal
        with open(r'hojas\public\modelo_som_entrenado.pkl', 'wb') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        return Response({"success":True,"message":"subido"})

class RedView(APIView):
    def post(self, request, *args, **kwargs):
        
        return Response({"success":True,"message":"subido"})

def base64_image(img):
    buffer = BytesIO()
    plt.imsave(buffer, img, cmap='gray', format='png')
    img_str = base64.b64encode(buffer.getvalue()).decode('utf-8')
    return "data:image/png;base64,"+img_str