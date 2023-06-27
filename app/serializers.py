from rest_framework import serializers
from .models import Hackathon, Submission, UserSubmissions

class HackathonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hackathon
        fields = '__all__'

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = '__all__'

  #validating a submission making sure submission type is followed.
    def validate(self, attrs):
        submission_type = attrs.get('submission_type')
        submission_file = attrs.get('submission_file')
        submission_link = attrs.get('submission_link')
        submission_image = attrs.get('submission_image')

        if submission_type == 'Image' and not submission_image:
            raise serializers.ValidationError("An image submission requires 'submission_image' field.")

        if submission_type == 'File' and not submission_file:
            raise serializers.ValidationError("A file submission requires 'submission_file' field.")

        if submission_type == 'Link' and not submission_link:
            raise serializers.ValidationError("A link submission requires 'submission_link' field.")

        return attrs


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSubmissions
        fields = '__all__'

class UserSubmissionsSerializer(serializers.ModelSerializer):
    hackathon = HackathonSerializer()
    class Meta:
        model = UserSubmissions
        fields = ['hackathon', 'user']

