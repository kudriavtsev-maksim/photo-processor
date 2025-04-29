from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ProcessedImage
import random
import time
import os
import uuid
from django.conf import settings
import threading


def process_image(image_path, original_filename):
    start_time = time.time()
    
    
    time.sleep(10)
    
    
    result = random.randint(1, 1000)
    
    
    processing_time = time.time() - start_time

    
    ProcessedImage.objects.create(
        filename=os.path.basename(image_path),
        original_filename=original_filename,
        result_number=result,
        processing_time=processing_time
    )
    
    
    return result

@csrf_exempt
def upload_image(request):
    if request.method == 'POST':
        if 'image' not in request.FILES:
            return JsonResponse({'error':'No image provided'}, status=400)
        
        
        image_file = request.FILES['image']
        
        
        unique_filename = f"{uuid.uuid4()}_{image_file.name}"
        image_path = os.path.join(settings.MEDIA_ROOT, unique_filename)
        
        
        os.makedirs(settings.MEDIA_ROOT, exist_ok=True)
        
        
        with open(image_path, 'wb+') as destination:
            for chunk in image_file.chunks():
                destination.write(chunk)
       
        
        
        threading.Thread(
            target=process_image,
            args=(image_path, image_file.name)
        ).start()
        
        return JsonResponse({'message': 'Image uploaded and processing started'}) 
    
    
    return JsonResponse({'error': 'Only POST merhod allowed'}, status=405)


@csrf_exempt
def upload_multiple_images(request):
    if request.method == 'POST':
        if 'image' not in request.FILES:
            return JsonResponse({'error': 'No image provided'}, status=400)
        
        
        image_file = request.FILES['image']
        
        
        unique_filename = f"{uuid.uuid4()}_{image_file.name}"
        image_path = os.path.join(settings.MEDIA_ROOT, unique_filename)
        
        
        os.makedirs(settings.MEDIA_ROOT, exist_ok=True)
        os.makedirs(settings.MEDIA_ROOT, exist_ok=True)
        
        
        with open(image_path, 'wb+') as destination:
            for chunk in image_file.chunks():
                destination.write(chunk)
        
        
        
        for i in range(100):
            threading.Thread(
                target=process_image,
                args=(image_path, f"test_{i+1}_{image_file.name}")
            ).start()
            
        return JsonResponse({'message': 'Started 100 processing tasks'})
    
    return JsonResponse({'error': 'only POST method allowed'}, status=405)

def index(request):
    images = ProcessedImage.objects.all().order_by('-upload_time')
    return render(request, 'processor/index.html',{'images': images})