from django.shortcuts import render
from django.urls import path
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from user.models import User,MathematicalFormula,Deposit,Loan
from user.serializers import UserSerialzer,MFormulaSerialzer,DepositSerialzer,LoanSerialzer
import math
from sympy import *
# import sympy as sy

import json
# Create your views here.
stack = []
stack_total = []
num_and_op = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', '(', ')', ',','.']
tri_op = ['sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'sqrt']
def calt_final(the_cal):
    final_cal = ''
    flag = 0
    i = 0
    flag1 = 0
    flag2 = 0
    while True:
        try:
            if the_cal[i] == '(':
                stack_total.append('(')
            elif the_cal[i] == ')':
                stack_total.pop()
        except:
            return 'error2'
        try:
            if the_cal[i] == '0' and i > 0 and the_cal[i - 1] == '/':
                return "error1"
            if the_cal[i] not in num_and_op:
                if the_cal[i:i + 3] == 'log':
                    i += 3
                    continue
                if the_cal[i] == '^':
                    p = 0
                    k = i
                    the_new = ''
                    while True:
                        k -= 1
                        if (k == -1 or the_cal[k].isdigit() == False) and the_cal[k] != '.':
                            break
                        else:
                            the_new = the_cal[k] + the_new
                    p = k + 1
                    k = i
                    the_new1 = ''
                    while True:
                        k += 1
                        if k == len(the_cal) or (the_cal[k].isdigit() == False and the_cal[k] != '.'):
                            break
                        else:
                            the_new1 = the_cal[k] + the_new1
                    t = pow(float(the_new), float(the_new1))
                    t = str(t)
                    final_cal += the_cal[flag:p] + t
                    i = k - 1
                    flag = k

                for j in range(i + 3, len(the_cal)):
                    if the_cal[j] == '(' and flag2 == 0:
                        flag1 = j
                        flag2 = 1
                        stack.append('(')
                    elif the_cal[j] == '(':
                        stack.append('(')
                    elif the_cal[j] == ')':
                        stack.pop()
                        if len(stack) == 0:
                            flag2 = 0
                            the_new_cal = the_cal[flag1 + 1:j]
                            t = calt_final(the_new_cal)
                            if the_cal[i] != 'a':
                                if the_cal[i + 1] != 'q':  # tri and sqrt\
                                    t = math.radians(t)
                                if the_cal[i:i + 3] == tri_op[0]:
                                    t = sin(t)
                                elif the_cal[i:i + 3] == tri_op[1]:
                                    t = cos(t)
                                elif the_cal[i:i + 3] == tri_op[2]:
                                    t = tan(t)
                                elif the_cal[i:i + 4] == tri_op[6]:
                                    print(1)
                                    t = math.sqrt(t)
                            else:
                                if the_cal[i:i + 4] == tri_op[3]:
                                    t = asin(t)
                                elif the_cal[i:i + 4] == tri_op[4]:
                                    t = acos(t)
                                elif the_cal[i:i + 4] == tri_op[5]:
                                    t = atan(t)
                                t = math.degrees(t)
                                t = math.radians(t)
                            t = str(t)
                            final_cal += the_cal[flag:i] + t
                            i = j
                            flag = j + 1
                            break

        except:
            return 'error'
        i += 1
        if i >= len(the_cal):
            break

    if len(stack_total) != 0:
        return 'error2'
    try:
        final_cal += the_cal[flag:len(the_cal)]
        return eval(final_cal)
    except:
        return 'error'
class FirstView(GenericAPIView):
    queryset = MathematicalFormula.objects.all()
    serializer_class = MFormulaSerialzer
    def get(self,request):
        # all = MathematicalFormula.objects.all()
        # data = MFormulaSerialzer(data=all,many=True)
        # if data.is_valid():
        #     data_len = len(data.validated_data())
        #     if data_len >= 10:
        #         data = data.data[data_len-9:data_len-1]
        #     return Response({"code":200,"data":data.data})
        # return Response({"code":400,"data":"error"})
        list = self.get_queryset()
        ser = self.get_serializer(list, many=True) ## 反序列化不要data =
        len_data = len(ser.data)
        data = ser.data
        if len_data >= 10:
            data = data[len_data-10:len_data]
        return Response({"code":200,"data":data})

    def post(self,request):
        data = request.data.copy()
        formula = data["mathematical_formula"]
        result = calt_final(formula)
        result = str(result)
        if result == 'error':
            code = 400
            return Response({"code": code, "result": result})
        elif result == 'error1':
            code = 401
            return Response({"code": code, "result": result})
        elif result == 'error2':
            code = 402
            return Response({"code": code, "result": result})
        print(data)
        data.update({"result":result})
        ser = MFormulaSerialzer(data=data)
        if ser.is_valid():
            ser.save()
            code = 200
        return Response({"code":code,"result":result})


class SecondView(GenericAPIView):
    queryset = Deposit.objects.all()
    serializer_class = DepositSerialzer
    def get(self,request):
        list = self.get_queryset()
        ser = self.get_serializer(list, many=True)
        data = ser.data
        Cquery = request.query_params.get("data")
        lenght = len(data)
        result = data[lenght - 1]
        if Cquery == None:
            return Response({"code":200,"data":result})
        print(result[Cquery])
        return Response({"code":200,"data":result[Cquery]}) #getattr(result,Cquery)

    def post(self,request):
        data = request.data.copy()
        ser = self.get_serializer(data=data)
        if ser.is_valid():
            ser.save()
            code = 200
        else:
            code = 400
        return Response({"code": code, "result": 'ok'})


class ThreeView(GenericAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerialzer
    def get(self,request):
        list = self.get_queryset()
        ser = self.get_serializer(list, many=True)
        data = ser.data
        Cquery = request.query_params.get("data")
        lenght = len(data)
        result = data[lenght - 1]
        if Cquery == None:
            return Response({"code": 200, "data": result})
        print(result[Cquery])
        return Response({"code": 200, "data": result[Cquery]})  # getattr(result,Cquery)

    def post(self, request):
        data = request.data.copy()
        ser = self.get_serializer(data=data)
        if ser.is_valid():
            ser.save()
            code = 200
        else:
            code = 400
        return Response({"code": code, "result": 'ok'})