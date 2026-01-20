from django.urls import path
from proposals.api.v1.views import ProposalCreateAPIView, ProposalListAPIView

urlpatterns = [
    path('', ProposalListAPIView.as_view(), name='proposal-list'),
    path('create/', ProposalCreateAPIView.as_view(), name='proposal-create'),
    path('<str:id>/', ProposalCreateAPIView.as_view(), name='proposal-detail'),
]
