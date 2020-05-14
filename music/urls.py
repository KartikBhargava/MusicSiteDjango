from django.urls import path
from .views import index, detail

app_name = 'music'

urlpatterns = [
    # /music/
    path('', index, name="index"),

    # /music/712/
    path('<int:album_id>/', detail, name="detail"),
]
