from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from PIL import Image

from .forms import ImageForm
from .models import ImageUpload

# Create your views here.
def index(request):
    y = 459989845+459480-987958
    context = {
        'y_value':y 
    } 
    context['form'] = ImageForm
    return render(request, 'pages/index.htm', context)


def getImage(request):
    y = 459989845+459480-987958
    context = {
        'y_value':y 
    } 
    context['form'] = ImageForm()
    if(request.method == 'POST'):
        image = request.FILES["image_"]
        fs = FileSystemStorage()
        #print(image.name)
        saved_img = fs.save(image.name, image)
        url = fs.url(saved_img)
        print(url) 
        rrr = image.read()  
        print(rrr)
        #read = Image.open(url)
        #print(read)  
    return render(request, 'pages/index.htm', context)


def uploadImage(request):
    y = 459989845+459480-987958
    context = {
        'y_value':y 
    } 
    context['form'] = ImageForm()
    if(request.method == 'POST'):
        form= ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    img = form.cleaned_data['image']
    print(img.image.width)
            
    return render(request, 'pages/index.htm', context)

'''
TODO
convert pillow object to numpy array
pass the numpy array to the tfclass model
get the probality and the predicted classed
display on the frontend by passing into context
'''


'''

use model.predict() to predict the probalibilties- gives the probality_prediction 
and model.predict_classes() get the predictions of each class- gives the rounded_prediction

plotting confusion matrix for the classes with sciktit learn
call the confusion matrix funtion on the test_labels and the rounded_predictions
get confusion_matrix code from the scikit-learn site

'''