from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import añadir_candidato_view, exportar_resultados_pdf, inicio_view, login_view, registro_view, resultados_view, votacion_view, gracias_view


urlpatterns = [
    path('', inicio_view, name='inicio'),
    path('login/', login_view, name='login'),
    path('registro/', registro_view, name='registro'),
    path('votacion/', votacion_view, name='votacion'),
    path('resultados/', resultados_view, name='resultados'), 
    path('gracias/', gracias_view, name='gracias'),
    path('añadir_candidato/', añadir_candidato_view, name='añadir_candidato'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('exportar_resultados_pdf/', exportar_resultados_pdf, name='exportar_resultados_pdf'), 


]
