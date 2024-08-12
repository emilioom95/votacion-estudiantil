from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import LoginForm, VotoForm
from .models import Candidato, Voto
from django.shortcuts import render
from .forms import RegistroForm, CandidatoForm
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from .models import Resultado
from django.template.loader import get_template 
from django.db import models
from django.db.models import Sum

def inicio_view(request):
    return render(request, 'elecciones/inicio.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('añadir_candidato') 
            else:
                return redirect('votacion')  
        else:
            return render(request, 'elecciones/login.html', {'error': 'Usuario o contraseña incorrectos'})
    return render(request, 'elecciones/login.html')

@login_required
def votacion_view(request):
    if request.method == 'POST':
        form = VotoForm(request.POST)
        if form.is_valid():
            voto = form.save(commit=False)
            voto.usuario = request.user
            voto.save()
            return redirect('gracias')  
    else:
        form = VotoForm()
    
    candidatos = Candidato.objects.all()
    return render(request, 'elecciones/votacion.html', {'form': form, 'candidatos': candidatos})

def gracias_view(request):
    return render(request, 'elecciones/gracias.html')

def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.set_password(form.cleaned_data['password'])  
            usuario.save()
            return redirect('login')  
    else:
        form = RegistroForm()
    return render(request, 'elecciones/registro.html', {'form': form})

def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin)
def añadir_candidato_view(request):
    if request.method == 'POST':
        form = CandidatoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True})
            return redirect('añadir_candidato')
            #return redirect('inicio')  
    else:
        form = CandidatoForm()
    return render(request, 'elecciones/añadir_candidato.html', {'form': form})

def resultados_view(request):
    candidatos = Candidato.objects.all()

    resultados = []
    for candidato in candidatos:
        votos = candidato.voto_set.count()
        resultados.append({
            'candidato': candidato,
            'votos': votos
        })
    
    return render(request, 'elecciones/resultados.html', {'resultados': resultados})

def exportar_resultados_pdf(request):
    candidatos = Candidato.objects.all()
    
    resultados = []
    for candidato in candidatos:
        votos = candidato.voto_set.count()
        resultados.append({
            'candidato': candidato,
            'votos': votos
        })
    
    html_string = render_to_string('resultados_pdf.html', {'resultados': resultados})

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resultados_votacion.pdf"'

    pisa_status = pisa.CreatePDF(html_string, dest=response)

    if pisa_status.err:
        return HttpResponse("Error al generar el PDF.")

    return response