from django.urls import path
from .views import SubmitData

urlpatterns = [
    path('submit-data/', SubmitData.as_view(), name='submit_data'),
]
