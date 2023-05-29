from django.urls import path
from dictionary import views

urlpatterns = [
    path('', views.DefinitionListView.as_view(), name='definiton-list'),
    path('create/', views.DefinitionCreateView.as_view(), name="definiton-create"),
    path('<slug:slug>/', views.DefinitionDetailView.as_view(), name="definiton-detail"),
    path('<pk>/update/', views.DefinitionUpdateView.as_view(), name="definiton-update"),
    path('<pk>/delete/', views.DefinitionDeleteView.as_view(), name="definiton-delete")
] 