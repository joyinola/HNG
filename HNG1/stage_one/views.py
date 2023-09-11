
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import SlackTrackSerializer
# Create your views here.

'''
1 endpoint, 2 query param-- slack name and track, return json
'''
class SlackTrackView(APIView):
   
    def get(self,request):
        obj={
            "slack_name":request.query_params['slack_name'],
            "track":request.query_params['track']
        }
        serializer=SlackTrackSerializer(obj)

        return Response(serializer.data, status=status.HTTP_200_OK)
