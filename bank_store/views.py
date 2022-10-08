from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from bank_store.models import *
import json
import pandas as pd
from  django.db import transaction



def getBanks(request):
    banks=Bank.objects.all()
    data=len(banks)
    
    return render(request,'data.html',{'data':data})

def getBranches(request):
    banks=Branch.objects.all()
    data=len(banks)
    return render(request,'data.html',{'data':data})


def deleteBanks(request):
    Bank.objects.all().delete()
    return render(request,'data.html')

def deleteBranches(request):
    Branch.objects.all().delete()
    return render(request,'data.html')


def insertBanks(request):

    df=pd.read_csv('static/bank_branches.csv')
    names=df['bank_name']
    ids=df['bank_id']

    d=dict()
    for i in range(len(names)):
        d[ids[i]]=names[i]

    with transaction.atomic():
        idx=0
        for x in d:
            name=d[x]
            id=x
            idx=idx+1
            print(idx)
            
            queryset=Bank.objects.create(name=name,id=id)
            queryset.save()

    return render(request,'index.html')



def insertBranches(request):
    df=pd.read_csv('static/bank_branches.csv')
    print(len(df))
    #data=df['ifsc'][:100]
#-----------------------------------------------------------------------------------------------------------------------
   
    df=df[15200:20000]
    ifsc_list=[]
    id_list=[]
    branch_list=[]
    address_list=[]
    city_list=[]
    district_list=[]
    state_list=[]

    

    
    for ifsc in df['ifsc']:
        ifsc_list.append(ifsc)

    for id in df['bank_id']:
        id_list.append(id)
    
    for branch in df['branch']:
        branch_list.append(branch)
    
    for add in df['address']:
        address_list.append(add)
    for city in df['city']:
        city_list.append(city)
    for dis in df['district']:
        district_list.append(dis)
    for state in df['state']:
        state_list.append(state)

    d=dict()
    print(len(ifsc_list),len(id_list),len(branch_list),len(address_list),len(city_list),len(district_list),len(state_list))
    
    with transaction.atomic():
        idx=0
        for i in range(len(id_list)):
            ifsc=ifsc_list[i]
            id=id_list[i]
            branch=branch_list[i]
            address=address_list[i]
            city=city_list[i]
            district=district_list[i]
            state=state_list[i]
            print(ifsc,id,branch,address,city,district,state)

            idx=idx+1
            print(idx)


            bank=Bank.objects.get(id=id)
            queryset1 = Branch.objects.create(ifsc=ifsc,bank_id=bank,branch=branch,address=address,
                                            city=city,district=district,state=state)  
            queryset1.save()
    
    data=len(Branch.objects.all())
        
    
    return render(request,'data.html',{'data':data})




def insertBranches2(request):
    df=pd.read_csv('static/bank_branches.csv')
    print(len(df))
    #data=df['ifsc'][:100]
 #-----------------------------------------------------------------------------------------------------------------------
   
    df=df[5001:10000]
    ifsc_list=[]
    id_list=[]
    branch_list=[]
    address_list=[]
    city_list=[]
    district_list=[]
    state_list=[]

    

    
    for ifsc in df['ifsc']:
        ifsc_list.append(ifsc)

    for id in df['bank_id']:
        id_list.append(id)
    
    for branch in df['branch']:
        branch_list.append(branch)
    
    for add in df['address']:
        address_list.append(add)
    for city in df['city']:
        city_list.append(city)
    for dis in df['district']:
        district_list.append(dis)
    for state in df['state']:
        state_list.append(state)

    d=dict()
    print(len(ifsc_list),len(id_list),len(branch_list),len(address_list),len(city_list),len(district_list),len(state_list))
    
    with transaction.atomic():
        idx=0
        for i in range(len(id_list)):
            ifsc=ifsc_list[i]
            id=id_list[i]
            branch=branch_list[i]
            address=address_list[i]
            city=city_list[i]
            district=district_list[i]
            state=state_list[i]
            print(ifsc,id,branch,address,city,district,state)

            idx=idx+1
            print(idx)


            bank=Bank.objects.get(id=id)
            queryset1 = Branch.objects.create(ifsc=ifsc,bank_id=bank,branch=branch,address=address,
                                            city=city,district=district,state=state)  
            queryset1.save()
    
    data=len(Branch.objects.all())
        
    
    return render(request,'data.html',{'data':data})



def insertBranches3(request):
    df=pd.read_csv('static/bank_branches.csv')
    print(len(df))
    #data=df['ifsc'][:100]
#-----------------------------------------------------------------------------------------------------------------------
    
    df=df[10001:15000]
    ifsc_list=[]
    id_list=[]
    branch_list=[]
    address_list=[]
    city_list=[]
    district_list=[]
    state_list=[]

    

    
    for ifsc in df['ifsc']:
        ifsc_list.append(ifsc)

    for id in df['bank_id']:
        id_list.append(id)
    
    for branch in df['branch']:
        branch_list.append(branch)
    
    for add in df['address']:
        address_list.append(add)
    for city in df['city']:
        city_list.append(city)
    for dis in df['district']:
        district_list.append(dis)
    for state in df['state']:
        state_list.append(state)

    d=dict()
    print(len(ifsc_list),len(id_list),len(branch_list),len(address_list),len(city_list),len(district_list),len(state_list))
    
    with transaction.atomic():
        idx=0
        for i in range(len(id_list)):
            ifsc=ifsc_list[i]
            id=id_list[i]
            branch=branch_list[i]
            address=address_list[i]
            city=city_list[i]
            district=district_list[i]
            state=state_list[i]
            print(ifsc,id,branch,address,city,district,state)

            idx=idx+1
            print(idx)


            bank=Bank.objects.get(id=id)
            queryset1 = Branch.objects.create(ifsc=ifsc,bank_id=bank,branch=branch,address=address,
                                            city=city,district=district,state=state)  
            queryset1.save()
    
    data=len(Branch.objects.all())
        
    
    return render(request,'data.html',{'data':data})


def insertBranches4(request):
    df=pd.read_csv('static/bank_branches.csv')
    print(len(df))
    #data=df['ifsc'][:100]
#-----------------------------------------------------------------------------------------------------------------------
    df=df[18001:20000]
    ifsc_list=[]
    id_list=[]
    branch_list=[]
    address_list=[]
    city_list=[]
    district_list=[]
    state_list=[]

    

    
    for ifsc in df['ifsc']:
        ifsc_list.append(ifsc)

    for id in df['bank_id']:
        id_list.append(id)
    
    for branch in df['branch']:
        branch_list.append(branch)
    
    for add in df['address']:
        address_list.append(add)
    for city in df['city']:
        city_list.append(city)
    for dis in df['district']:
        district_list.append(dis)
    for state in df['state']:
        state_list.append(state)

    d=dict()
    print(len(ifsc_list),len(id_list),len(branch_list),len(address_list),len(city_list),len(district_list),len(state_list))
    
    with transaction.atomic():
        idx=0
        for i in range(len(id_list)):
            ifsc=ifsc_list[i]
            id=id_list[i]
            branch=branch_list[i]
            address=address_list[i]
            city=city_list[i]
            district=district_list[i]
            state=state_list[i]
            print(ifsc,id,branch,address,city,district,state)

            idx=idx+1
            print(idx)


            bank=Bank.objects.get(id=id)
            queryset1 = Branch.objects.create(ifsc=ifsc,bank_id=bank,branch=branch,address=address,
                                            city=city,district=district,state=state)  
            queryset1.save()
    
    data=len(Branch.objects.all())
        
    
    return render(request,'data.html',{'data':data})




def insertBranches5(request):
    df=pd.read_csv('static/bank_branches.csv')
    print(len(df))
    #data=df['ifsc'][:100]
#-----------------------------------------------------------------------------------------------------------------------
    df=df[20001:22000]
    ifsc_list=[]
    id_list=[]
    branch_list=[]
    address_list=[]
    city_list=[]
    district_list=[]
    state_list=[]

    

    
    for ifsc in df['ifsc']:
        ifsc_list.append(ifsc)

    for id in df['bank_id']:
        id_list.append(id)
    
    for branch in df['branch']:
        branch_list.append(branch)
    
    for add in df['address']:
        address_list.append(add)
    for city in df['city']:
        city_list.append(city)
    for dis in df['district']:
        district_list.append(dis)
    for state in df['state']:
        state_list.append(state)

    d=dict()
    print(len(ifsc_list),len(id_list),len(branch_list),len(address_list),len(city_list),len(district_list),len(state_list))
    
    with transaction.atomic():
        idx=0
        for i in range(len(id_list)):
            ifsc=ifsc_list[i]
            id=id_list[i]
            branch=branch_list[i]
            address=address_list[i]
            city=city_list[i]
            district=district_list[i]
            state=state_list[i]
            print(ifsc,id,branch,address,city,district,state)

            idx=idx+1
            print(idx)


            bank=Bank.objects.get(id=id)
            queryset1 = Branch.objects.create(ifsc=ifsc,bank_id=bank,branch=branch,address=address,
                                            city=city,district=district,state=state)  
            queryset1.save()
    
    data=len(Branch.objects.all())
        
    
    return render(request,'data.html',{'data':data})



def insertBranches6(request):
    df=pd.read_csv('static/bank_branches.csv')
    print(len(df))
    #data=df['ifsc'][:100]
#-----------------------------------------------------------------------------------------------------------------------
    df=df[22001:24000]
    ifsc_list=[]
    id_list=[]
    branch_list=[]
    address_list=[]
    city_list=[]
    district_list=[]
    state_list=[]

    

    
    for ifsc in df['ifsc']:
        ifsc_list.append(ifsc)

    for id in df['bank_id']:
        id_list.append(id)
    
    for branch in df['branch']:
        branch_list.append(branch)
    
    for add in df['address']:
        address_list.append(add)
    for city in df['city']:
        city_list.append(city)
    for dis in df['district']:
        district_list.append(dis)
    for state in df['state']:
        state_list.append(state)

    d=dict()
    print(len(ifsc_list),len(id_list),len(branch_list),len(address_list),len(city_list),len(district_list),len(state_list))
    
    with transaction.atomic():
        idx=0
        for i in range(len(id_list)):
            ifsc=ifsc_list[i]
            id=id_list[i]
            branch=branch_list[i]
            address=address_list[i]
            city=city_list[i]
            district=district_list[i]
            state=state_list[i]
            print(ifsc,id,branch,address,city,district,state)

            idx=idx+1
            print(idx)


            bank=Bank.objects.get(id=id)
            queryset1 = Branch.objects.create(ifsc=ifsc,bank_id=bank,branch=branch,address=address,
                                            city=city,district=district,state=state)  
            queryset1.save()
    
    data=len(Branch.objects.all())
        
    
    return render(request,'data.html',{'data':data})



def insertBranches7(request):
    df=pd.read_csv('static/bank_branches.csv')
    print(len(df))
    #data=df['ifsc'][:100]
#-----------------------------------------------------------------------------------------------------------------------
    df=df[24001:26000]
    ifsc_list=[]
    id_list=[]
    branch_list=[]
    address_list=[]
    city_list=[]
    district_list=[]
    state_list=[]

    

    
    for ifsc in df['ifsc']:
        ifsc_list.append(ifsc)

    for id in df['bank_id']:
        id_list.append(id)
    
    for branch in df['branch']:
        branch_list.append(branch)
    
    for add in df['address']:
        address_list.append(add)
    for city in df['city']:
        city_list.append(city)
    for dis in df['district']:
        district_list.append(dis)
    for state in df['state']:
        state_list.append(state)

    d=dict()
    print(len(ifsc_list),len(id_list),len(branch_list),len(address_list),len(city_list),len(district_list),len(state_list))
    
    with transaction.atomic():
        idx=0
        for i in range(len(id_list)):
            ifsc=ifsc_list[i]
            id=id_list[i]
            branch=branch_list[i]
            address=address_list[i]
            city=city_list[i]
            district=district_list[i]
            state=state_list[i]
            print(ifsc,id,branch,address,city,district,state)

            idx=idx+1
            print(idx)


            bank=Bank.objects.get(id=id)
            queryset1 = Branch.objects.create(ifsc=ifsc,bank_id=bank,branch=branch,address=address,
                                            city=city,district=district,state=state)  
            queryset1.save()
    
    data=len(Branch.objects.all())
        
    
    return render(request,'data.html',{'data':data})






def insertBranches8(request):
    df=pd.read_csv('static/bank_branches.csv')
    print(len(df))
    #data=df['ifsc'][:100]
#-----------------------------------------------------------------------------------------------------------------------
    df=df[26001:28000]
    ifsc_list=[]
    id_list=[]
    branch_list=[]
    address_list=[]
    city_list=[]
    district_list=[]
    state_list=[]

    

    
    for ifsc in df['ifsc']:
        ifsc_list.append(ifsc)

    for id in df['bank_id']:
        id_list.append(id)
    
    for branch in df['branch']:
        branch_list.append(branch)
    
    for add in df['address']:
        address_list.append(add)
    for city in df['city']:
        city_list.append(city)
    for dis in df['district']:
        district_list.append(dis)
    for state in df['state']:
        state_list.append(state)

    d=dict()
    print(len(ifsc_list),len(id_list),len(branch_list),len(address_list),len(city_list),len(district_list),len(state_list))
    
    with transaction.atomic():
        idx=0
        for i in range(len(id_list)):
            ifsc=ifsc_list[i]
            id=id_list[i]
            branch=branch_list[i]
            address=address_list[i]
            city=city_list[i]
            district=district_list[i]
            state=state_list[i]
            print(ifsc,id,branch,address,city,district,state)

            idx=idx+1
            print(idx)


            bank=Bank.objects.get(id=id)
            queryset1 = Branch.objects.create(ifsc=ifsc,bank_id=bank,branch=branch,address=address,
                                            city=city,district=district,state=state)  
            queryset1.save()
    
    data=len(Branch.objects.all())
        
    
    return render(request,'data.html',{'data':data})



def insertBranches9(request):
    df=pd.read_csv('static/bank_branches.csv')
    print(len(df))
    #data=df['ifsc'][:100]
#-----------------------------------------------------------------------------------------------------------------------
    df=df[28001:30000]
    ifsc_list=[]
    id_list=[]
    branch_list=[]
    address_list=[]
    city_list=[]
    district_list=[]
    state_list=[]

    

    
    for ifsc in df['ifsc']:
        ifsc_list.append(ifsc)

    for id in df['bank_id']:
        id_list.append(id)
    
    for branch in df['branch']:
        branch_list.append(branch)
    
    for add in df['address']:
        address_list.append(add)
    for city in df['city']:
        city_list.append(city)
    for dis in df['district']:
        district_list.append(dis)
    for state in df['state']:
        state_list.append(state)

    d=dict()
    print(len(ifsc_list),len(id_list),len(branch_list),len(address_list),len(city_list),len(district_list),len(state_list))
    
    with transaction.atomic():
        idx=0
        for i in range(len(id_list)):
            ifsc=ifsc_list[i]
            id=id_list[i]
            branch=branch_list[i]
            address=address_list[i]
            city=city_list[i]
            district=district_list[i]
            state=state_list[i]
            print(ifsc,id,branch,address,city,district,state)

            idx=idx+1
            print(idx)


            bank=Bank.objects.get(id=id)
            queryset1 = Branch.objects.create(ifsc=ifsc,bank_id=bank,branch=branch,address=address,
                                            city=city,district=district,state=state)  
            queryset1.save()
    
    data=len(Branch.objects.all())
        
    
    return render(request,'data.html',{'data':data})


def insertBranches10(request):
    df=pd.read_csv('static/bank_branches.csv')
    print(len(df))
    #data=df['ifsc'][:100]
#-----------------------------------------------------------------------------------------------------------------------
    df=df[30001:32000]
    ifsc_list=[]
    id_list=[]
    branch_list=[]
    address_list=[]
    city_list=[]
    district_list=[]
    state_list=[]

    

    
    for ifsc in df['ifsc']:
        ifsc_list.append(ifsc)

    for id in df['bank_id']:
        id_list.append(id)
    
    for branch in df['branch']:
        branch_list.append(branch)
    
    for add in df['address']:
        address_list.append(add)
    for city in df['city']:
        city_list.append(city)
    for dis in df['district']:
        district_list.append(dis)
    for state in df['state']:
        state_list.append(state)

    d=dict()
    print(len(ifsc_list),len(id_list),len(branch_list),len(address_list),len(city_list),len(district_list),len(state_list))
    
    with transaction.atomic():
        idx=0
        for i in range(len(id_list)):
            ifsc=ifsc_list[i]
            id=id_list[i]
            branch=branch_list[i]
            address=address_list[i]
            city=city_list[i]
            district=district_list[i]
            state=state_list[i]
            print(ifsc,id,branch,address,city,district,state)

            idx=idx+1
            print(idx)


            bank=Bank.objects.get(id=id)
            queryset1 = Branch.objects.create(ifsc=ifsc,bank_id=bank,branch=branch,address=address,
                                            city=city,district=district,state=state)  
            queryset1.save()
    
    data=len(Branch.objects.all())
        
    
    return render(request,'data.html',{'data':data})


def insertBranches11(request):
    df=pd.read_csv('static/bank_branches.csv')
    print(len(df))
    #data=df['ifsc'][:100]
#-----------------------------------------------------------------------------------------------------------------------
    df=df[32001:34000]
    ifsc_list=[]
    id_list=[]
    branch_list=[]
    address_list=[]
    city_list=[]
    district_list=[]
    state_list=[]

    

    
    for ifsc in df['ifsc']:
        ifsc_list.append(ifsc)

    for id in df['bank_id']:
        id_list.append(id)
    
    for branch in df['branch']:
        branch_list.append(branch)
    
    for add in df['address']:
        address_list.append(add)
    for city in df['city']:
        city_list.append(city)
    for dis in df['district']:
        district_list.append(dis)
    for state in df['state']:
        state_list.append(state)

    d=dict()
    print(len(ifsc_list),len(id_list),len(branch_list),len(address_list),len(city_list),len(district_list),len(state_list))
    
    with transaction.atomic():
        idx=0
        for i in range(len(id_list)):
            ifsc=ifsc_list[i]
            id=id_list[i]
            branch=branch_list[i]
            address=address_list[i]
            city=city_list[i]
            district=district_list[i]
            state=state_list[i]
            print(ifsc,id,branch,address,city,district,state)

            idx=idx+1
            print(idx)


            bank=Bank.objects.get(id=id)
            queryset1 = Branch.objects.create(ifsc=ifsc,bank_id=bank,branch=branch,address=address,
                                            city=city,district=district,state=state)  
            queryset1.save()
    
    data=len(Branch.objects.all())
        
    
    return render(request,'data.html',{'data':data})



def insertBranches12(request):
    df=pd.read_csv('static/bank_branches.csv')
    print(len(df))
    #data=df['ifsc'][:100]
#-----------------------------------------------------------------------------------------------------------------------
    df=df[34001:36000]
    ifsc_list=[]
    id_list=[]
    branch_list=[]
    address_list=[]
    city_list=[]
    district_list=[]
    state_list=[]

    

    
    for ifsc in df['ifsc']:
        ifsc_list.append(ifsc)

    for id in df['bank_id']:
        id_list.append(id)
    
    for branch in df['branch']:
        branch_list.append(branch)
    
    for add in df['address']:
        address_list.append(add)
    for city in df['city']:
        city_list.append(city)
    for dis in df['district']:
        district_list.append(dis)
    for state in df['state']:
        state_list.append(state)

    d=dict()
    print(len(ifsc_list),len(id_list),len(branch_list),len(address_list),len(city_list),len(district_list),len(state_list))
    
    with transaction.atomic():
        idx=0
        for i in range(len(id_list)):
            ifsc=ifsc_list[i]
            id=id_list[i]
            branch=branch_list[i]
            address=address_list[i]
            city=city_list[i]
            district=district_list[i]
            state=state_list[i]
            print(ifsc,id,branch,address,city,district,state)

            idx=idx+1
            print(idx)


            bank=Bank.objects.get(id=id)
            queryset1 = Branch.objects.create(ifsc=ifsc,bank_id=bank,branch=branch,address=address,
                                            city=city,district=district,state=state)  
            queryset1.save()
    
    data=len(Branch.objects.all())
        
    
    return render(request,'data.html',{'data':data})



def insertBranches13(request):
    df=pd.read_csv('static/bank_branches.csv')
    print(len(df))
    #data=df['ifsc'][:100]
#-----------------------------------------------------------------------------------------------------------------------
    df=df[36001:38000]
    ifsc_list=[]
    id_list=[]
    branch_list=[]
    address_list=[]
    city_list=[]
    district_list=[]
    state_list=[]

    

    
    for ifsc in df['ifsc']:
        ifsc_list.append(ifsc)

    for id in df['bank_id']:
        id_list.append(id)
    
    for branch in df['branch']:
        branch_list.append(branch)
    
    for add in df['address']:
        address_list.append(add)
    for city in df['city']:
        city_list.append(city)
    for dis in df['district']:
        district_list.append(dis)
    for state in df['state']:
        state_list.append(state)

    d=dict()
    print(len(ifsc_list),len(id_list),len(branch_list),len(address_list),len(city_list),len(district_list),len(state_list))
    
    with transaction.atomic():
        idx=0
        for i in range(len(id_list)):
            ifsc=ifsc_list[i]
            id=id_list[i]
            branch=branch_list[i]
            address=address_list[i]
            city=city_list[i]
            district=district_list[i]
            state=state_list[i]
            print(ifsc,id,branch,address,city,district,state)

            idx=idx+1
            print(idx)


            bank=Bank.objects.get(id=id)
            queryset1 = Branch.objects.create(ifsc=ifsc,bank_id=bank,branch=branch,address=address,
                                            city=city,district=district,state=state)  
            queryset1.save()
    
    data=len(Branch.objects.all())
        
    
    return render(request,'data.html',{'data':data})


def insertBranches14(request):
    df=pd.read_csv('static/bank_branches.csv')
    print(len(df))
    #data=df['ifsc'][:100]
#-----------------------------------------------------------------------------------------------------------------------
    df=df[38001:40000]
    ifsc_list=[]
    id_list=[]
    branch_list=[]
    address_list=[]
    city_list=[]
    district_list=[]
    state_list=[]

    

    
    for ifsc in df['ifsc']:
        ifsc_list.append(ifsc)

    for id in df['bank_id']:
        id_list.append(id)
    
    for branch in df['branch']:
        branch_list.append(branch)
    
    for add in df['address']:
        address_list.append(add)
    for city in df['city']:
        city_list.append(city)
    for dis in df['district']:
        district_list.append(dis)
    for state in df['state']:
        state_list.append(state)

    d=dict()
    print(len(ifsc_list),len(id_list),len(branch_list),len(address_list),len(city_list),len(district_list),len(state_list))
    
    with transaction.atomic():
        idx=0
        for i in range(len(id_list)):
            ifsc=ifsc_list[i]
            id=id_list[i]
            branch=branch_list[i]
            address=address_list[i]
            city=city_list[i]
            district=district_list[i]
            state=state_list[i]
            print(ifsc,id,branch,address,city,district,state)

            idx=idx+1
            print(idx)


            bank=Bank.objects.get(id=id)
            queryset1 = Branch.objects.create(ifsc=ifsc,bank_id=bank,branch=branch,address=address,
                                            city=city,district=district,state=state)  
            queryset1.save()
    
    data=len(Branch.objects.all())
        
    
    return render(request,'data.html',{'data':data})


def insertBranches15(request):
    df=pd.read_csv('static/bank_branches.csv')
    print(len(df))
    #data=df['ifsc'][:100]
#-----------------------------------------------------------------------------------------------------------------------
    df=df[40001:42000]
    ifsc_list=[]
    id_list=[]
    branch_list=[]
    address_list=[]
    city_list=[]
    district_list=[]
    state_list=[]

    

    
    for ifsc in df['ifsc']:
        ifsc_list.append(ifsc)

    for id in df['bank_id']:
        id_list.append(id)
    
    for branch in df['branch']:
        branch_list.append(branch)
    
    for add in df['address']:
        address_list.append(add)
    for city in df['city']:
        city_list.append(city)
    for dis in df['district']:
        district_list.append(dis)
    for state in df['state']:
        state_list.append(state)

    d=dict()
    print(len(ifsc_list),len(id_list),len(branch_list),len(address_list),len(city_list),len(district_list),len(state_list))
    
    with transaction.atomic():
        idx=0
        for i in range(len(id_list)):
            ifsc=ifsc_list[i]
            id=id_list[i]
            branch=branch_list[i]
            address=address_list[i]
            city=city_list[i]
            district=district_list[i]
            state=state_list[i]
            print(ifsc,id,branch,address,city,district,state)

            idx=idx+1
            print(idx)


            bank=Bank.objects.get(id=id)
            queryset1 = Branch.objects.create(ifsc=ifsc,bank_id=bank,branch=branch,address=address,
                                            city=city,district=district,state=state)  
            queryset1.save()
    
    data=len(Branch.objects.all())
        
    
    return render(request,'data.html',{'data':data})


    df=pd.read_csv('static/bank_branches.csv')
    print(len(df))
    #data=df['ifsc'][:100]
#-----------------------------------------------------------------------------------------------------------------------
    df=df[11001:12000]
    ifsc_list=[]
    id_list=[]
    branch_list=[]
    address_list=[]
    city_list=[]
    district_list=[]
    state_list=[]

    

    
    for ifsc in df['ifsc']:
        ifsc_list.append(ifsc)

    for id in df['bank_id']:
        id_list.append(id)
    
    for branch in df['branch']:
        branch_list.append(branch)
    
    for add in df['address']:
        address_list.append(add)
    for city in df['city']:
        city_list.append(city)
    for dis in df['district']:
        district_list.append(dis)
    for state in df['state']:
        state_list.append(state)

    d=dict()
    print(len(ifsc_list),len(id_list),len(branch_list),len(address_list),len(city_list),len(district_list),len(state_list))
    
    with transaction.atomic():
        idx=0
        for i in range(len(id_list)):
            ifsc=ifsc_list[i]
            id=id_list[i]
            branch=branch_list[i]
            address=address_list[i]
            city=city_list[i]
            district=district_list[i]
            state=state_list[i]
            print(ifsc,id,branch,address,city,district,state)

            idx=idx+1
            print(idx)


            bank=Bank.objects.get(id=id)
            queryset1 = Branch.objects.create(ifsc=ifsc,bank_id=bank,branch=branch,address=address,
                                            city=city,district=district,state=state)  
            queryset1.save()
    
    data=len(Branch.objects.all())
        
    
    return render(request,'data.html',{'data':data})























def index(request):

    return render(request,'index.html')

def home(request):

    return render(request,'home.html')


def test(ifsc):
    branch=Branch.objects.get(ifsc=ifsc)
    return render('index.html',{'branch':branch})



def branchesData(request):
    data=json.loads(request.body)
    name=data['name']
    city=data['city']
    bank_id=Bank.objects.get(name__iexact=name).id

    print('bankid',bank_id)
    branches=Branch.objects.filter(bank_id=bank_id) & Branch.objects.filter(city__iexact=city)
    branch=branches[0]
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

def ifsc(request):
    data=json.loads(request.body)
    print(data['ifsc'])
    branch=Branch.objects.get(ifsc__iexact=data['ifsc'])
    branch_obj={
        'IFSC':branch.ifsc,
        'BRANCH':branch.branch,
        'CITY':branch.city,
        'DISTRICT':branch.district,
        'STATE':branch.state,
        'ADRESS':branch.address

    }
    print('msg',branch_obj)

    
    return JsonResponse({'msg':branch_obj},safe=False)




def insert(request):
    queryset=Bank.objects.create(name='SBI',id=60)
    queryset.save()

    bank=Bank.objects.get(id=60)
    queryset1 = Branch.objects.create(ifsc='SBIN1212126',bank_id=bank,branch='vasnan',address='adress ahemdabad',city='Ahmedabad',district='ahmedabad',state='Gujrat')  
    
        
    queryset1.save()
    return render(request,'index.html')

