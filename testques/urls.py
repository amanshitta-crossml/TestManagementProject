from django.urls import path
from . import views


"""
url defination file for test app /test/<---->/
"""

urlpatterns=[
	# path('', views.index, name="index"),
	path('', views.IndexView.as_view(), name="index"),
	path('<int:pk>/', views.DetailView.as_view(), name="detail"),
	path('create/', views.create, name="create"),
]