from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('cakes/', views.cakes_list, name='cakes'),
    path('cakes/<int:cake_id>/', views.cake_detail, name='cake_detail'),
    path('menu/',views.menu,name='menu'),
    path('reservation/',views.reservation,name='reservation'),
    path('contact/',views.contact,name='contact'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)