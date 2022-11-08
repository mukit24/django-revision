from django.urls import path
from .views import IndexView, DetailView, vote, ResultView

app_name = 'polls'
urlpatterns = [
    path('',IndexView.as_view(), name='poll_index'),
    path('<int:pk>/',DetailView.as_view(),name='detail'),
    path('<int:question_id>/vote/',vote,name='vote'),
    path('<int:pk>/results/',ResultView.as_view(), name='results'),
]
