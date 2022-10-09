from django.http import  JsonResponse
from django.shortcuts import render
from bank_store.models import *
import json





def index(request):

    return render(request,'index.html')

def home(request):

    return render(request,'home.html')






def branchesData(request):
    data=json.loads(request.body)
    name=data['name']
    city=data['city']
    try:
        bank_id=Bank.objects.get(name__iexact=name).id
        branches=Branch.objects.filter(bank_id=bank_id) & Branch.objects.filter(city__iexact=city)
        branches_list=[]
        for branch in branches:
            
            obj={
            'IFSC':branch.ifsc,
            'BRANCH':branch.branch,
            'CITY':branch.city,
            'DISTRICT':branch.district,
            'STATE':branch.state,
            'ADRESS':branch.address
            }

            branches_list.append(obj)
  
        return JsonResponse({'branches_list':branches_list},safe=False)
    
    except:
        return  JsonResponse({'msg_error':'Only HDFC BANK Data Is Availabale.'},safe=False)

    
    

        

def ifsc(request):
    data=json.loads(request.body)

    try:

        branch=Branch.objects.get(ifsc__iexact=data['ifsc'])
        branch_obj={
            'IFSC':branch.ifsc,
            'BRANCH':branch.branch,
            'CITY':branch.city,
            'DISTRICT':branch.district,
            'STATE':branch.state,
            'ADRESS':branch.address

        }
       
        return JsonResponse({'msg':branch_obj},safe=False)    
    except:

        return  JsonResponse({'msg_error':'Either You Have Entered Wrong IFSC data or Only HDFC Bank data Is available'},safe=False)




