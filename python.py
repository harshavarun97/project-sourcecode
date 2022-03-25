# import imp
from django.shortcuts import render
#from matplotlib.pyplot import get
import pandas as pd
from .forms import apiform
from .models import ApiWellData

#api datas from database

def annualapi(request): 
    if request.method == 'POST':
        std1 = apiform(request.POST)
        if std1.is_valid():
           data=int(request.POST['apidata'])# value taken from user
           if ApiWellData.objects.filter(wellnumber=data).exists():  #data exist
                   apidata=ApiWellData.objects.filter(wellnumber=data)
                   return render(request,'show.html',{'ApData':apidata})
           else:
            # print(type(data))
              xlfile=pd.read_excel(r'C:\Users\91940\Desktop\pythontest\pythonTest\main\files1.xls',usecols=['API WELL  NUMBER','QUARTER 1,2,3,4','OIL','GAS','BRINE']) # open and read the files1.xls
               # print(xlfile)
              rows=xlfile[xlfile['API WELL  NUMBER']== data]   # to specify the row 
           #appl.query('API WELL  NUMBER'== 34013209230000) 
              ApiWellData( wellnumber =data,gas= rows['GAS'].sum(),oil =rows['OIL'].sum(),brine =rows['BRINE'].sum()).save()
              apidata=ApiWellData.objects.filter(wellnumber=data)
              return render(request,'show.html',{'ApData':apidata})
    else:
        std1=apiform()
        return render(request,'main.html',{'form':std1})
    
       


# # it show all datas stored in a data base
# def show(request)

