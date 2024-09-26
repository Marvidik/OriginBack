from django.db import models

# Create your models here.



class Token(models.Model):

    key=models.CharField(max_length=100)


class State(models.Model):
    state=models.CharField(max_length=100)

    def __str__(self):

        return self.state


class StateCode(models.Model):
    name=models.CharField(max_length=100)
    code=models.IntegerField()


    def __str__(self) -> str:
        code=f'{self.code}'
        return code


class Phrases(models.Model):
    origin=models.ForeignKey(StateCode,on_delete=models.CASCADE )
    name=models.CharField(max_length=100)
    code=models.IntegerField()    

    def __str__(self) -> str:
        code=f'{self.code}'
        return code




