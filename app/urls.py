from django.urls import path

from .views import *

urlpatterns = [
  #create a new hackathon
  path('api/hackathon/create/', newHackathon.as_view()),

  #update,delete and access any hackathon through Primary key.
  path('api/hackathon/<int:pk>/',HackathonView.as_view()),
  
  #lists of a active hackathons
  path('api/hackathon/',HackathonList.as_view({'get':'list'}), name=''),

  # register for a hackathon where
  path('api/hackathon/register/',RegisterView.as_view(), name=''),

  # list all the hackathons a user is registered for
  path('api/dashboard/hackathons/',UserHackathonList.as_view({'get':'list'}), name=''),

  #Submission of solution
  path('api/hackathon/submit/',newSubmission.as_view(), name=''),
   
  #update,delete and access any submission through its primary key.
  path('api/hackathon/submission/<int:pk>/',SubmissionView.as_view(), name=''),

]