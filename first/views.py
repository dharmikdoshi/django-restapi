from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AdvisorSerializer, UserSerializer, BookingSerializer
from rest_framework import status
from .models import AdvisorModel,User,BookingAdvisorModel
from rest_framework.exceptions import AuthenticationFailed
import jwt
from rest_framework.decorators import api_view
import datetime

#Register a User
class RegisterView(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"Message":"Now login to get your JWT Token","Created User":serializer.data})
            #return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


#Login a User
class LoginView(APIView):
    def post(self,request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not Found')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')

        payload = {
            'id':user.id,
            'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat':datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt',value=token,httponly=True)
        response.data = {
            'JWT_Token':token,
            'UserId':user.id
        }

        return response

#add an advisor
@api_view(['POST'])
def addAdvisor(request):
    if request.method == 'POST':
        saveadvisor = AdvisorSerializer(data=request.data)
        if saveadvisor.is_valid():
            saveadvisor.save()
            return Response(saveadvisor.data, status=status.HTTP_200_OK)
            return Response(saveadvisor.data, status=status.HTTP_400_BAD_REQUEST)

#Display all Advisors
@api_view(['GET'])
def showAdvisor(request, userid):
    if request.method == 'GET':
        results = AdvisorModel.objects.all()
        serialize = AdvisorSerializer(results, many=True)
        return Response({"message": "This data was requested by user {}".format(userid), "List of Advisors": serialize.data})
        return Response(serialize.data)


#Book an Advisor
@api_view(['POST'])
def bookAdvisor(request, userid, advisorid):
    if request.method == 'POST':
        test = AdvisorModel.objects.get(id=advisorid)
        bookadv = BookingSerializer(data=request.data)
        b = BookingAdvisorModel(advisor_id=test,booking_time=bookadv)
        if bookadv.is_valid():
            b.booking_time = bookadv.data['booking_time']
            b.save()
            return Response({"Message":"This was booked by advisor {}".format(advisorid)},status=status.HTTP_200_OK)
            return Response(bookadv.data, status=status.HTTP_400_BAD_REQUEST)


#Show all Bookings
@api_view(['GET'])
def showBooking(request):
    bookings = BookingAdvisorModel.objects.all()#.select_related("advisor_id")
    serialize = BookingSerializer(bookings, many=True)
    #return Response({"message": "This data was requested by user {}".format(userid), "List of Advisors": serialize.data})
    return Response(serialize.data, status=status.HTTP_200_OK)

 

