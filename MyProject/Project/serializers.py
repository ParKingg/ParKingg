from rest_framework import serializers
from Project.models import Account, ParkingLot, ReserveParking, CheckoutTicket, ReservationFee, TransactionHistory
from django.db import models


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('User_id', 'Username', 'Password', 'Verify_Password', 'Fname', 'Lname', 'Email', 'Address', 'Contactno', 'Profile_Pic')


class ParkingLotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingLot
        fields = '__all__'

class ReserveParkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReserveParking
        fields = '__all__'

class CheckoutTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckoutTicket
        fields = '__all__'

class ReservationFeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservationFee
        fields = '__all__'
class TransactionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionHistory
        fields = '__all__'