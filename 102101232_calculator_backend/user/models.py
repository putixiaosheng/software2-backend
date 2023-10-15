from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=20)
    class Meta:
        db_table = "user_table"

class MathematicalFormula(models.Model):
    mathematical_formula = models.CharField(max_length=100)
    result = models.CharField(max_length=20,default=0)
    class Meta:
        db_table = "formula_table"

class Deposit(models.Model):
    live = models.CharField(max_length=100)
    three_month = models.CharField(max_length=100)
    half_year = models.CharField(max_length=100)
    one_year = models.CharField(max_length=100)
    two_year = models.CharField(max_length=100)
    three_year = models.CharField(max_length=100)
    five_year = models.CharField(max_length=100)


class Loan(models.Model):
    half_year = models.CharField(max_length=100)
    one_year = models.CharField(max_length=100)
    one_to_three_year = models.CharField(max_length=100)
    three_to_five_year = models.CharField(max_length=100)
    five_year = models.CharField(max_length=100)