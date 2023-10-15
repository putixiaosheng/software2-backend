from rest_framework import serializers

from user.models import User,MathematicalFormula,Deposit,Loan


class UserSerialzer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class MFormulaSerialzer(serializers.ModelSerializer):
    class Meta:
        model = MathematicalFormula
        fields = '__all__'


class DepositSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = '__all__'


class LoanSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'