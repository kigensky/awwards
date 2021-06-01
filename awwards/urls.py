from django.urls import path
from . import views
from .views import (ProjectListView,ProjectDetailView,ProjectCreateView,ProjectDeleteView,ProjectUpdateView,RatingCreateView,RatingUpdateView,RatingDeleteView)


urlpatterns = [
    path('', ProjectListView.as_view(), name='awwards-home'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='awwards-detail'),
    path('awwards/new', ProjectCreateView.as_view(), name='awwards-create'),
    path('awwards/<int:pk>/update/',ProjectUpdateView.as_view(), name='awwards-update'),
    path('awwards/<int:pk>/delete/',ProjectDeleteView.as_view(), name='awwards-delete'),
    path('awwards/<int:pk>/rate/',RatingCreateView.as_view(), name='add_rating'),
    path('comment/<int:pk>/update/',RatingUpdateView.as_view(), name='rating-update'),
    path('comment/<int:pk>/delete/',RatingDeleteView.as_view(), name='rating-delete'),
]
