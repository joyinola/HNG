
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
# Create your views here.

'''
1 endpoint, 2 query param-- slack name and track, return json
'''
class SlackTrack(APIView):
   
    def get(self,slack_name,track,request):
        pass
    return Response(serializer.data, status=status.HTTP_200_OK)
