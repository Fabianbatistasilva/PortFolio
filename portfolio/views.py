
from django.shortcuts import redirect, render
import requests
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User
import ssl

# Create a custom SSL context
ssl_context = ssl.create_default_context()
ssl_context.options |= ssl.OP_NO_RENEGOTIATION

def home(request):
    return render(request,'paginas/home.html')




def sobre(request):
    return render(request,'paginas/sobre.html')




def oferta(request):
    local = requests.get('https://servicodados.ibge.gov.br/api/v1/localidades/municipios', verify=False, ).json()
    if request.method=='POST':
        Empresa = request.POST.get('nomeEmpresa')
        Cargo = request.POST.get('cargo')
        Local = request.POST.get('localizar')
        Descricao = request.POST.get('descricao_vaga')
        Salario = request.POST.get('salario_vaga')
        if Empresa =='' and Cargo =='' and Local =='' and Descricao =='' and Salario =='':
            messages.add_message(request,messages.INFO,f'Erro,Campo estão vazios')
            return render(request,'paginas/form_oferta.html',{'local':local})
        if Cargo.isalpha()==False:
            messages.add_message(request,messages.INFO,f'Erro, Cargo só aceita letras')
            return render(request,'paginas/form_oferta.html',{'local':local})
        if Cargo.isspace()==True :
            messages.add_message(request,messages.INFO,f'Erro, Cargo com valor invalido')
            return render(request,'paginas/form_oferta.html',{'local':local})
        if Empresa.isspace() :
            messages.add_message(request,messages.INFO,f'Erro, Empresa com valor invalido')
            return render(request,'paginas/form_oferta.html',{'local':local})
        if Salario.isdecimal()==False:
            messages.add_message(request,messages.INFO,'Erro, Descrição com valor invalido')
            return render(request,'paginas/form_oferta.html',{'local':local})
        if Salario.isspace()==True :
            messages.add_message(request,messages.INFO,f'Erro, Salario com valor invalido')
            return render(request,'paginas/form_oferta.html',{'local':local})
        else:
            Contrato =  request.POST.get('contato_vaga')
            Tipo =  request.POST.get('tipo_vaga')
            Email = request.POST.get('EmailEmpresa')
            message= f' A {Empresa} ofereceu {Cargo} em {Local} \n Descrição da Vaga \n {Descricao} \n Salario: {Salario}\n Contrato:{Contrato} Tipo : {Tipo} Email:{Email}'
            title= 'Oferta de emprego pelo Portfolio'
            email_enviado='currifabianbatista@gmail.com'
            para_email=['currifabianbatista@gmail.com']
            send_mail(title,message,email_enviado,para_email,fail_silently=False,)
            messages.add_message(request,messages.SUCCESS,'Enviou com Sucesso,Oferta foi enviada para o Email do Fabian')
    return render(request,'paginas/form_oferta.html',{'local':local})
