from django.shortcuts import render,redirect

# Create your views here.
db={}
ls=[0]
def home(request):
    return render(request,"index.html")
def add(request):
    if(request.method=='POST'):
        sm={}
        a=request.POST['n1']
        b=request.POST['n2']
        ls.sort()
        id=ls[-1]+1
        ls.append(id)
        sm['fname']=a
        sm['lname']=b
        sm['id']=id
        db[id]=sm
        print(db)
        for i in db:
            print(i)
        return render(request,"out.html",{'fn':a,'ln':b,'db':db})
    else:
        return render(request,"out.html",{'db':db})
def delete(request):
    if(request.method=="GET"):
        e=int(request.GET['d1'])
        ls.remove(e)
        print(e)
        del db[e]
        return redirect('add')
        #return render(request,"out.html",{'db':db})
def edit(request):
    ed=int(request.GET['ed'])
    print("i am ed")
    ed=db[ed]
    return render(request,"edit.html",{'e':ed})
def save(request):
    sm={}
    id=int(request.POST['id'])
    f1=request.POST['n4']
    f2=request.POST['n5']
    sm['fname']=f1
    sm['lname']=f2
    sm['id']=id
    db[id]=sm
    return render(request,"out.html",{'db':db})
    