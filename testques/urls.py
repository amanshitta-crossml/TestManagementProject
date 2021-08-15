from django.urls import path
from . import views

"""
url defination file for test app /test/<---->/
"""

urlpatterns=[
	path('', views.index, name="index"),
	path('<int:test_id>/', views.detail, name="detail"),
]