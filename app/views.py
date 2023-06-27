# for bad request
from django.http.response import Http404  
# view set to send data in api form
from rest_framework.views import APIView 
# used to return response of a API class
from rest_framework.response import Response
# for response status
from rest_framework import status  
# for viewsets.read-only viewsets
from rest_framework import viewsets  
# to add filters in a read only viewset
from django_filters.rest_framework import DjangoFilterBackend
# to add search filter in readonly viewset
from rest_framework import filters  
#to access date and time
from datetime import datetime

from .models import *
from .serializers import *


#Create a new Hackathon provding all the data fields in JSON format.
class newHackathon(APIView):
    
    def post(self,request):
        serializer = HackathonSerializer(data = request.data)# data contains all the model fields in dictionary format.

        if serializer.is_valid():# we check for validation of data here
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#update delete and access any hackethon using this API.
class HackathonView(APIView):
    #function to get the hackathon we want to modify/access
    def get_object(self, pk):
        try:
            return Hackathon.objects.get(pk=pk)
        except Hackathon.DoesNotExist():
            raise Http404

    def get(self, requests, pk):
        hackathon = self.get_object(pk)
        serializer = HackathonSerializer(hackathon)
        return Response(serializer.data)

    def put(self, requests, pk):
        hackathon = self.get_object(pk)
        serializer = HackathonSerializer(hackathon, data=requests.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, requests, pk):
        hackathon = self.get_object(pk)
        hackathon.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#List of all Active Hackathons
class HackathonList(viewsets.ReadOnlyModelViewSet):
    model = Hackathon
    serializer_class = HackathonSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    def get_queryset(self):
        hackathon = Hackathon.objects.all()
        return hackathon


#register a user for a hackathon
class RegisterView(APIView):
    
    def post(self,request):
        serializer = RegisterSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#lists all the hackathons particular user are enrolled into
class UserHackathonList(viewsets.ReadOnlyModelViewSet):
    model = UserSubmissions
    serializer_class = UserSubmissionsSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    def get_queryset(self):
        hackathon = UserSubmissions.objects.filter(user = self.request.user.id)
        return hackathon
    
#submit your submission
class newSubmission(APIView):
    
    def post(self,request):
        data = request.data
        print(data)
        hackathon = Hackathon.objects.get(pk = data['hackathon'])
        data['submission_type'] = hackathon.submission_type
      
        serializer = SubmissionSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
#update, delete and access a submission
class SubmissionView(APIView):
    def get_object(self, pk):
        try:
            return Submission.objects.get(pk=pk)
        except Submission.DoesNotExist():
            raise Http404

    def get(self, requests, pk):
        submission = self.get_object(pk)
        serializer = SubmissionSerializer(submission)
        return Response(serializer.data)

    def put(self, requests, pk):
        submission = self.get_object(pk)
        serializer = SubmissionSerializer(submission, data=requests.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, requests, pk):
        submission = self.get_object(pk)
        submission.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# class SubmissionList(viewsets.ReadOnlyModelViewSet):
#     model = Submission
#     serializer_class = SubmissionSerializer
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
#     def get_queryset(self):
#         submissions = Submission.objects.filter(user = self.kwargs['pk'] )
#         return submissions