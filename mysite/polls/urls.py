from django.urls import path

from . import views

urlpatterns = [
    # routeとpathは必須
    # pollsで登録しているからpollsのトップを呼び出すとindexを呼び出す
    # nameは今は分からん。でも便利らしい
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]