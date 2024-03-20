from django.urls import path
from .views import SubmitData, PerevalDetailView, PerevalByUserEmailView

urlpatterns = [
    path('submit-data/', SubmitData.as_view(), name='submit_data'),
    path('submitData/<int:id>/', PerevalDetailView.as_view(), name='pereval_detail'),
    path('submitData/', PerevalByUserEmailView.as_view(), name='pereval_by_email'),

]
