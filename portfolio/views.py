
from django.shortcuts import redirect, render
import requests
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User

# Create a custom SSL context



def home(request):
    return render(request,'paginas/home.html')




def sobre(request):
    return render(request,'paginas/sobre.html')




def oferta(request):
    if request.method=='POST':
        Email = request.POST.get('email')
        name = request.POST.get('name')
        Descricao = request.POST.get('message')
        if Email =='' and Cargo =='' and name =='' and Descricao =='' :
            messages.add_message(request,messages.INFO,f'Erro,Campo estão vazios')
            return render(request,'paginas/form_oferta.html',{})
        else:
            message= f' A/O {name} entrou em contato com {Email} Sobre \n {Descricao}'
            title= 'Oferta de emprego pelo Portfolio'
            email_enviado='currifabianbatista@gmail.com'
            para_email=['currifabianbatista@gmail.com']
            send_mail(title,message,email_enviado,para_email,fail_silently=False,)
            messages.add_message(request,messages.SUCCESS,'Enviou com Sucesso,Oferta foi enviada para o Email do Fabian')
            return render(request,'paginas/form_oferta.html',{})
    if request.method == 'GET':
        return render(request,'paginas/form_oferta.html',{})
