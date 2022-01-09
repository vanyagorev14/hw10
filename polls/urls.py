from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

    path('contact', views.contact_form, name='contact_form'),

    path('create_form', views.create_form, name='create_form'),

    path('process_form', views.process_form, name='process_form'),

    path('create_question_form', views.create_question_form, name='create_question_form'),

    path('triangle_form', views.triangle_form, name='triangle_form'),

    path('persons', views.PersonForms, name='name of persons')
]
