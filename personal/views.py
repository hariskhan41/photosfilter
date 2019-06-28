from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.views.generic import TemplateView
import cv2

# Create your views here.

def index(request):
    return render(request, 'personal/home.html')

def contact(request):
    return render(request, 'personal/basic.html', {'content':['If you would like to contact me please email me', 'hariskhan3465@gmail.com']})

def ApplyNegativeFilter(request):
    if request.method == 'POST':
    	uploaded_file = request.FILES['mydoc']
    	fs = FileSystemStorage();
    	uploaded_file = fs.save(uploaded_file.name, uploaded_file)
    	uploaded_file_url = fs.url(uploaded_file)
    	read_image = cv2.imread('F:/UET/FYP/Django Tutorial/mysite' + uploaded_file_url, 1)
    	negative_image = negative_filter(read_image)
    	cv2.imwrite("media/negative_filter.png", negative_image)
    	negative_image_url = fs.url('negative_filter.png')
    	return render(request, 'personal/negativefilter.html', {'uploaded_file_url':uploaded_file_url, 'negative_image_url':negative_image_url})
    return render(request, 'personal/negativefilter.html')    	
    
    

def negative_filter(image):
	out_image = 255 - image
	return out_image