from django.db import models
from jalali_date import datetime2jalali
from django.contrib.auth.models import User, Group



class Train_Type(models.Model):
    name = models.CharField(max_length=100, verbose_name='نوع')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "نوع تمرین"
        verbose_name_plural = verbose_name


class Train_Target(models.Model):
    name = models.CharField(max_length=100, verbose_name='جامعه هدف')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "مخاطبین"
        verbose_name_plural = verbose_name


class Train_Location(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام مکان')
    
    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "مکان"
        verbose_name_plural = verbose_name



class Train(models.Model):
    date = models.DateTimeField(verbose_name='زمان')
    location = models.ForeignKey(Train_Location, on_delete=models.PROTECT, verbose_name='مکان')
    target = models.ForeignKey(Train_Target, on_delete=models.PROTECT, verbose_name='جامعه هدف')
    category = models.ManyToManyField(Train_Type, verbose_name='دسته‌بندی تمرین')

    def __unicode__(self):
        return datetime2jalali(self.date).strftime('%a , %Y/%m/%d')

    def __str__(self):
        return datetime2jalali(self.date).strftime('%a , %Y/%m/%d')

    class Meta:
        verbose_name = "تمرین"
        verbose_name_plural = verbose_name




class Feature(models.Model):
    name = models.CharField(max_length=100, verbose_name='ویژگی')
    default = models.PositiveIntegerField(default=0,verbose_name='امتیاز پیش‌فرض')
    zarib = models.PositiveIntegerField(default=0,verbose_name='ضریب')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "ویژگی"
        verbose_name_plural = verbose_name




class Point(models.Model):
    train = models.ForeignKey(Train, on_delete=models.PROTECT, verbose_name='تمرین', null=True, blank=True)
    player = models.ManyToManyField(User,  verbose_name='بازیکن')
    feature = models.ManyToManyField(Feature, verbose_name='ویژگی')
    point = models.PositiveIntegerField(default=0,verbose_name='امتیاز')

    def __unicode__(self):
        return str(self.id)

    def __str__(self):
        return str(self.id)


    class Meta:
        verbose_name = "امتیاز"
        verbose_name_plural = verbose_name

