from django.shortcuts import render, redirect
import tensorflow as tf
import numpy as np
import math
from mysite.settings import model


def handler(request):
    result = "Input the data"
    if request.method == 'POST':
        try:
            title = request.POST['date']
            date_list = title.split("-")
            t_3 = 10219445.0	
            t_2 = 10313337.0	
            t_1 = 10310644.0
            roll_3 = 10278390.0
            roll_2 = 10260915.5
            pred = model.predict(np.array([[t_3, t_2, t_1, roll_3, roll_2, int(date_list[1]), int(date_list[2])]]))[0]
            # print(pred)
            result = math.floor(pred[0])
        except:
            result = "Error occurred"       
    return render(request, "index.html", {'response': result})
