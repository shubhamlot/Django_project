from django.shortcuts import render,redirect
from django.contrib.auth import logout
from .models import Client,Message
from django.http import HttpResponseRedirect
import hashlib
def signup(request):
	if request.method == "POST":
		name = request.POST.get("name")
		password = request.POST.get("password")
		password = hashlib.sha256(password.encode())
		password = password.hexdigest()
		c=Client(username= name,password=password)
		c.save()
		request.session['username'] = name
		return redirect(home)
	else:
		return render(request,"app/signup.html")
def login(request):
	if request.method == "POST":
		name = request.POST.get("name")
		password = request.POST.get("password")
		password = hashlib.sha256(password.encode())
		password = password.hexdigest()
		if Client.objects.filter(username= name,password=password).exists():
			request.session['username'] =name
			return redirect(home)
		else:
			return render(request,"app/login.html")
	else:
		return render(request,"app/login.html")

def home(request):
	if request.session.has_key('username'):
		alert=0
		name = request.session['username']
		m = Message.objects.filter(userto=name).all()
		if request.method == "POST":
			userto = request.POST.get('userto')
			c=Client.objects.filter(username=userto).exists()
			if(c):
				heading = request.POST.get('heading')
				userto = request.POST.get('userto')
				texting = request.POST.get('texting')
				d = Message(userfrom=name,userto=userto,header=heading,message=texting)
				alert=2
				d.save()
			else:
				alert = 1	
		param = {'username':name,'allmessages':m,'alert':alert}
		return render(request,"app/home.html",param)
	else:
		return render(request,"app/login.html")

def logout(request):
    try:
        del request.session['username']
    except:
     pass
    return redirect(login)

def delete(request,post_id=None):
    message_to_delete=Message.objects.get(id=post_id)
    message_to_delete.delete()
    return redirect(home)


	


