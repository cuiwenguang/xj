"""
Definition of models.
"""
from django.db import models
from django.utils import timezone

# Create your models here.
class PersonnelProfile(models.Model):
    input_location = models.CharField(max_length=200)       # 录入地
    input_user = models.IntegerField(default=0)           # 录入人
    create_date = models.DateTimeField(default=timezone.now)           # 创建日期／登记时间
    name = models.CharField(max_length=200)                 # 姓名
    gender = models.BooleanField(default=True)                # 性别
    ID_number = models.IntegerField(default=0)             # 身份证号
    is_own_house = models.BooleanField(default=False)          # 是自住房／否租房
    is_minimum_security = models.BooleanField(default=False)   # 是否有低保
    family_members = models.IntegerField(default=0)        # 流入地家庭人口
    is_medical_security = models.BooleanField(default=False)      # 是否有医保
    job_source = models.CharField(max_length=50)           # 经济收入来源
    annual_earnings = models.IntegerField(default=0)       # 年收入
    is_corps = models.BooleanField(default=False)              # 是兵团／否地方
    is_leader = models.BooleanField(default=False)             # 是否带头人
    ID_address = models.CharField(max_length=200)           # 身份证地址
    phone_number = models.CharField(max_length=200)         # 联系电话
    is_three_personnel = models.BooleanField(default=False)   # 是否三员
    present_address = models.CharField(max_length=500)      # 现住地址
    passport_number = models.CharField(max_length=200)      # 护照号码
    nation = models.CharField(max_length=50)               # 民族
    educational_level = models.CharField(max_length=50)    #文化程度，教育水平
    political_face = models.CharField(max_length=50)       # 政治面貌
    is_married = models.BooleanField(default=False)            # 是否已婚
    health = models.CharField(max_length=500)               # 健康状况

class Family(models.Model):
    family_id = models.IntegerField(default=0)
    personnel_id = models.IntegerField(default=0)
    desc = models.CharField(max_length=500)

class PersonnelMigration(models.Model):
    personnel_id = models.IntegerField(default=0)     # 人员ID
    input_location = models.CharField(max_length=200)  # 录入地
    input_user = models.IntegerField(default=0)  # 录入人
    create_date = models.DateTimeField(default=timezone.now)  # 创建日期

class PersonnelBrowseLog(models.Model):
    user_id = models.IntegerField(default=0)
    personnel_id = models.IntegerField(default=0)
    create_date = models.DateTimeField(default=timezone.now)  # 创建日期
    browse_source = models.CharField(max_length=50)       # 浏览来源：扫描二维码／头像识别