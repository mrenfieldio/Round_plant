from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('base/<int:p>',views.base,name='base'),
    path('about/',views.about,name='about'),
    path('packages/',views.packages,name='packages'),
    path('events/',views.events1,name='events'),
    path('gallery/',views.gallery,name='gallery'),
    path('contact/',views.contact,name='contact'),
    path('event1/<int:p>',views.eventsin,name='event1'),
    path('package1/<int:p>',views.package1,name='package1'),
]