from django.urls import path
from polls import views as polls_views

app_name = 'polls'
urlpatterns = [
    path("", polls_views.IndexView.as_view(), name="polls-home"),
    path("<int:question_id>", polls_views.DetailView.as_view(), name="polls-detail"),
    path("<int:question_id>/results", polls_views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote", polls_views.vote, name="vote")
]