from django.urls import path
from .views import AuthorREST
from .views import AuthorGenericAPIView


urlpatterns = [
    path('author/', AuthorREST.as_view()),
    path('author/<int:id>/', AuthorREST.as_view()),
    path('authors_generic', AuthorGenericAPIView.as_view())
]