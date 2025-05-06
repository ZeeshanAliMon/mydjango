from django.shortcuts import render
import pickle  
import numpy as np
import os

path = os.path.join('static', 'models', 'cropPredictor.pkl')
with open(path, 'rb') as file:
      model = pickle.load(file)
def predict_crop(request):
    print("visited")
    if request.method == 'POST':
        print("posted")
       
        # value1 = request.POST[0]
        # value2 = request.POST[1]
        # value3 = request.POST[2]
        # value4 = request.POST[3]
        # value5 = request.POST[4]
        # value6 = request.POST[5]
        # value7 = request.POST[6]
        nitrogen = request.POST.get("nitrogen")
        phosphorus = request.POST.get("phosphorus")
        potassium = request.POST.get("potassium")
        temperature = request.POST.get("temperature")
        
        humidity = request.POST.get("humidity")
        ph = request.POST.get("ph")
        rainfall = request.POST.get("rainfall")
        features = [nitrogen,phosphorus,potassium,temperature,humidity,ph,rainfall]
        float_features = [float(x) for x in features]
        npfeatures = np.array([float_features])


        
        
        result = model.predict(npfeatures)
        print("result was ",result)

        return render(request, 'cropPredictor.html', {'result': result})
    return render(request, 'cropPredictor.html')
