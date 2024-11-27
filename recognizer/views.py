import os
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import io

model_path = os.path.join(os.path.dirname(__file__), 'mnist_model.keras')
# Load the pre-trained MNIST model
model = load_model(model_path)
# Create your views here.
class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')
    

def predict(image_bytes):
    img = Image.open(io.BytesIO(image_bytes)).convert('L').resize((28, 28))
    img = np.array(img) / 255.0
    img = img.reshape(1, 28, 28, 1)
    prediction = model.predict(img)
    return np.argmax(prediction)

class SubmitImageForRecognition(View):
    def post(self, request):
        # Retrieve the uploaded image file
        image = request.FILES.get("image")
        
        if not image:
            return JsonResponse({'error': 'No image uploaded'}, status=400)

        try:
            # Read the image bytes
            image_bytes = image.read()
            
            # Predict the digit using the `predict` function
            predicted_digit = predict(image_bytes)
            
            # Return the predicted digit as a JSON response
            # print("Predicted digit:",predicted_digit)
            return JsonResponse({'digit': int(predicted_digit)})
        except Exception as e:
            # Handle errors during processing or prediction
            return JsonResponse({'error': str(e)}, status=500)
    

