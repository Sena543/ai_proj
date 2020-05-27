from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from PIL import Image
import os
from .forms import ImageForm
from .models import ImageUpload
from .tfModelClass import Predict


'''
index api is the landing page of this web application
serves up the homepage/ prediction page of the app when called
'''
def index(request):
    #print(os.getcwd())
    context = {
        'results':'Results of the prediction would appear here' 
    } 
    context['form'] = ImageForm
    return render(request, 'pages/index.htm', context)

'''
def getImage(request):
    y = '...'
    context = {
        'results':y 
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
    return render(request, 'pages/index.htm', context) '''


'''
This api is passes the uploaded image to the prediction class which returns a prediction value
the value is sent to the client side as a response
'''
def uploadImage(request):
    load = Predict()
    y='...'
    context = {
        'results':y 
    } 
    context['form'] = ImageForm()
    if(request.method == 'POST'):
        form= ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    img = form.cleaned_data['image'].name    
    img = os.path.join(os.getcwd(),  "media", img)
    prediction =load.makePredictions(img)
    
    if(round(prediction[0][0]*100<50)):
        context['results'] = "Model does not detect the presence of cancer cells. Prediction accuracy: {} %".format(round(prediction[0][0]*100, 2))
    else:
        context['results'] = "Model detects the presence of cancer cells. Prediction accuracy: {} %".format(round(prediction[0][0]*100, 2))

    print(prediction[0][0])
            
    return render(request, 'pages/index.htm', context)

'''
TODO
convert pillow object to numpy array
pass the numpy array to the tfclass model
get the probality and the predicted classed
display on the frontend by passing into context


Model Predicts the presence of cancers cells with an accuracy of

'''

