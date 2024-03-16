from django.urls import path,include
from rest_framework import routers
from api import views

router=routers.DefaultRouter()
router.register(r'programmers',views.ProgrammerViewSet)#la r para que se interprete de manera correcta porque podria estar programmers/n y lo tomaria como un salto de linea
router.register(r'persons',views.PersonViewSet)#la r para que se interprete de manera correcta porque podria estar programmers/n y lo tomaria como un salto de linea

urlpatterns = [
    path('', include(router.urls))
]
