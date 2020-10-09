from django.db import models

class Attackinfo(models.Model):

    mobile_n = models.CharField(max_length=100)
    frequency_n = models.CharField(max_length=100)


    def __str__(self):
        return self.mobile_n + "-" + self.frequency_n

class Userinfo(models.Model):

    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    api_token = models.CharField(max_length=100)


    def __str__(self):
        return self.username + "-" + self.password + "-" +self.api_token

class Workerinfo(models.Model):

    workername = models.CharField(max_length=100)
    workerctime = models.CharField(max_length=100)
    workerrtime = models.CharField(max_length=100)
    status = models.CharField(max_length=100)


    def __str__(self):
        return (self.workername + "-" +  self.workerrtime + "-"+ self.workerctime + "-" +self.status)