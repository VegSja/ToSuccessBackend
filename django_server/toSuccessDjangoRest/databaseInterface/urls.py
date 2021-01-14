from django.urls import path
from databaseInterface import views
from rest_framework_simplejwt import views as jwt_views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('activities/', views.activity_list_view.as_view(), name='activities'),
    path('activities/<int:activity_id>/', views.activity_detail.as_view(), name='activities_detailes'),
    path('categories/', views.category_view.as_view(), name='categories'),
    path('categories/<int:category_id>/', views.category_detail.as_view(), name='categories_detail'),
    path('google/', views.GoogleView.as_view(), name='google'),
    path('refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('date/', views.date_view.as_view(), name='date'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
