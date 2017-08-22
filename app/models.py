"""
Definition of models.
"""
from django.db import models
from django.utils import timezone
import uuid
# Create your models here.
class PersonnelProfile(models.Model):
    personnel_uuid = models.CharField(max_length=500)                 # 唯一标识
    input_location = models.CharField(max_length=255)       # 录入地
    input_user_id = models.IntegerField(default=0)           # 录入人
    input_user_name = models.CharField(max_length=255)  # 录入人
    create_date = models.DateTimeField(default=timezone.now)           # 创建日期／登记时间
    name = models.CharField(max_length=255)                 # 姓名
    gender = models.BooleanField(default=True)                # 性别
    ID_number = models.CharField(max_length=255)             # 身份证号
    own_house = models.CharField(max_length=50)          # 是自住房／否租房
    is_minimum_security = models.BooleanField(default=False)   # 是否有低保
    family_members = models.CharField(max_length=50)        # 流入地家庭人口
    is_medical_security = models.BooleanField(default=False)      # 是否有医保
    work_source = models.CharField(max_length=255)           # 经济收入来源
    work_address = models.CharField(max_length=255)          # 工作地址
    work_desc = models.CharField(max_length=255)             # 工作内容／工作性质
    annual_earnings = models.CharField(max_length=255)       # 年收入
    is_corps = models.BooleanField(default=False)              # 是兵团／否地方
    is_leader = models.BooleanField(default=False)             # 是否带头人
    ID_address = models.CharField(max_length=255)           # 身份证地址
    phone_number = models.CharField(max_length=255)         # 联系电话
    is_three_personnel = models.BooleanField(default=False)   # 是否三员
    present_address = models.CharField(max_length=500)      # 现住地址
    passport_number = models.CharField(max_length=255)      # 护照号码
    nation = models.CharField(max_length=50)               # 民族
    educational_level = models.CharField(max_length=50)    #文化程度，教育水平
    political_face = models.CharField(max_length=50)       # 政治面貌
    marriage = models.CharField(max_length=50)            # 是否已婚
    health = models.CharField(max_length=500)               # 健康状况
    note = models.CharField(max_length=255)

class Family(models.Model):
    family_master_uuid = models.CharField(max_length=500)    # 家庭户主ID＝personnel_uuid唯一标识
    personnel_uuid = models.CharField(max_length=500)        # 家庭成员ID＝personnel_uuid唯一标识
    family_relation = models.CharField(max_length=50)  # 家庭关系
    desc = models.CharField(max_length=200)

class PersonnelMigration(models.Model):
    personnel_uuid = models.CharField(max_length=500)     # 人员ID
    input_location = models.CharField(max_length=255)  # 录入地
    input_user_id = models.IntegerField(default=0)  # 录入人
    input_user_name = models.CharField(max_length=255)  # 录入人
    create_date = models.DateTimeField(default=timezone.now)  # 创建日期

class PersonnelBrowseLog(models.Model):
    user_id = models.IntegerField(default=0)
    personnel_uuid = models.CharField(max_length=500)
    create_date = models.DateTimeField(default=timezone.now)  # 创建日期
    browse_source = models.CharField(max_length=50)       # 浏览来源：扫描二维码／头像识别

class UserToken(models.Model):
    user_id = models.IntegerField(default=0)
    token = models.CharField(max_length=500)
    create_date = models.DateTimeField(default=timezone.now)  # 创建日期
    expires = models.DateTimeField(default=timezone.now)
