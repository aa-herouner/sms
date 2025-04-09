from django.db import models
from students.models import StudentClassInfo, StudentInfo

# Create your models here.
class MonthsofTheYear(models.Model):
    month_name = models.CharField(max_length=20)


    def __str__(self):
        return self.month_name
    

class AcademicSession(models.Model):
    session_name = models.CharField(max_length=20)


    def __str__(self):
        return self.session_name
    
class PaymentStatus(models.Model):
    status_name = models.CharField(max_length=20)


    def __str__(self):
        return self.status_name

class PaymentsInformation(models.Model):
    name = models.CharField(StudentInfo, max_length=100)
    class_type = models.ForeignKey(StudentClassInfo, on_delete=models.CASCADE, null=True, blank=True)
    month = models.ForeignKey(MonthsofTheYear, on_delete=models.CASCADE)
    session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE)
    status= models.ForeignKey(PaymentStatus,on_delete=models.CASCADE)

    def __str__(self):
        return self.name