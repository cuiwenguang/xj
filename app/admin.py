from app.models import *
from django.shortcuts import HttpResponse
import uuid
import logging

def import_excel():
    import xlrd
    from pprint import pprint
    file = 'app/xj.xls'
    wb = xlrd.open_workbook(filename=file)
    wsh = wb.sheet_by_name('Sheet1')

    # 获取行数
    nrows = wsh.nrows
    # 获取列数
    ncols = wsh.ncols
    print("nrows %d, ncols %d" % (nrows, ncols))
    # 获取第一行第一列数据
    cell_value = wsh.cell_value(1, 0) #wsh.cell(1, 0).value
    a = wsh.row_values(28)
    c = 1
    # 获取各行数据
    for i in range(1, nrows):
        row_data = wsh.row_values(i)
        try:
            if row_data[15] != '':
                pp = PersonnelProfile()
                pp.personnel_uuid = str(uuid.uuid1())  # 唯一标识
                pp.input_location = row_data[0]  # 录入地
                pp.input_user_id = 1  # 录入人
                pp.input_user_name = row_data[1]  # 录入人
                pp.name = row_data[3]  # 姓名
                if row_data[4] != '男':
                    pp.gender = False  # 性别
                pp.ID_number = row_data[15]  # 身份证号
                pp.own_house = row_data[16]  # 是自住房／否租房
                if row_data[17] == '是':
                    pp.is_minimum_security = True  # 是否有低保
                pp.family_members = row_data[18]  # 流入地家庭人口
                if row_data[19] == ' 是':
                    pp.is_medical_security = True  # 是否有医保
                pp.work_source = row_data[20]  # 经济收入来源
                pp.work_address = row_data[28]  # 工作地址
                pp.work_desc = row_data[29]  # 工作内容／工作性质
                pp.annual_earnings = row_data[21]  # 年收入
                if row_data[22] == '兵团':
                    pp.is_corps = True  # 是兵团／否地方
                if row_data[23] == '是':
                    pp.is_leader = True  # 是否带头人
                pp.ID_address = row_data[24]  # 身份证地址
                pp.phone_number = row_data[25]  # 联系电话
                if row_data[26] == '是':
                    pp.is_three_personnel = True  # 是否三员
                pp.present_address = row_data[27]  # 现住地址
                pp.passport_number = row_data[31]  # 护照号码
                pp.nation = row_data[5]  # 民族
                pp.educational_level = row_data[11]  # 文化程度，教育水平
                pp.political_face = row_data[6]  # 政治面貌
                pp.marriage = row_data[7]  # 是否已婚
                pp.health = ''  # 健康状况
                pp.note = row_data[2]
                pp.save()

                if row_data[32] != '':
                    pp1 = PersonnelProfile()
                    pp1.personnel_uuid = str(uuid.uuid1())  # 唯一标识
                    pp1.input_location = row_data[0]  # 录入地
                    pp1.input_user_id = 1  # 录入人
                    pp1.input_user_name = row_data[1]  # 录入人
                    pp1.name = row_data[33]  # 姓名
                    if row_data[4] == '女':
                        pp1.gender = False  # 性别

                    pp1.ID_number = row_data[34]  # 身份证号
                    pp1.own_house = row_data[16]  # 是自住房／否租房
                    if row_data[17] == '是':
                        pp1.is_minimum_security = True  # 是否有低保

                    pp1.family_members = row_data[18]  # 流入地家庭人口
                    if row_data[19] == ' 是':
                        pp1.is_medical_security = True  # 是否有医保
                    pp1.work_source = row_data[20]  # 经济收入来源
                    pp1.work_address = row_data[28]  # 工作地址
                    pp1.work_desc = row_data[29]  # 工作内容／工作性质
                    pp1.annual_earnings = row_data[21]  # 年收入
                    if row_data[22] == '兵团':
                        pp1.is_corps = True  # 是兵团／否地方
                    if row_data[23] == '是':
                        pp1.is_leader = True  # 是否带头人
                    pp1.ID_address = row_data[43]  # 身份证地址
                    pp1.phone_number = row_data[41]  # 联系电话
                    if row_data[26] == '是':
                        pp1.is_three_personnel = True  # 是否三员
                    pp1.present_address = row_data[27]  # 现住地址
                    pp1.passport_number = row_data[31]  # 护照号码
                    pp1.nation = row_data[35]  # 民族
                    pp1.educational_level = row_data[36]  # 文化程度，教育水平
                    pp1.political_face = row_data[37]  # 政治面貌
                    pp1.marriage = row_data[38]  # 是否已婚
                    pp1.health = row_data[39]  # 健康状况
                    pp1.note = row_data[40]
                    pp1.save()

                    family = Family()
                    family.family_master_uuid = pp.personnel_uuid  # 家庭户主ID＝personnel_uuid唯一标识
                    family.personnel_uuid = pp1.personnel_uuid  # 家庭成员ID＝personnel_uuid唯一标识
                    family.family_relation = row_data[32]  # 家庭关系
                    family.desc = ''
                    family.save()

                if row_data[44] != '':
                    pp2 = PersonnelProfile()
                    pp2.personnel_uuid = str(uuid.uuid1())  # 唯一标识
                    pp2.input_location = row_data[0]  # 录入地
                    pp2.input_user_id = 1  # 录入人
                    pp2.input_user_name = row_data[1]  # 录入人
                    pp2.name = row_data[45]  # 姓名
                    if row_data[4] != '男':
                        pp2.gender = False  # 性别
                    pp2.ID_number = row_data[46]  # 身份证号
                    pp2.own_house = row_data[16]  # 是自住房／否租房
                    if row_data[17] == '是':
                        pp2.is_minimum_security = True  # 是否有低保
                    pp2.family_members = row_data[18]  # 流入地家庭人口
                    if row_data[19] == ' 是':
                        pp2.is_medical_security = True  # 是否有医保
                    pp2.work_source = row_data[54]  # 经济收入来源
                    pp2.work_address = row_data[28]  # 工作地址
                    pp2.work_desc = row_data[29]  # 工作内容／工作性质
                    pp2.annual_earnings = row_data[21]  # 年收入
                    if row_data[22] == '兵团':
                        pp2.is_corps = True  # 是兵团／否地方
                    if row_data[23] == '是':
                        pp2.is_leader = True  # 是否带头人
                    pp2.ID_address = row_data[55]  # 身份证地址
                    pp2.phone_number = row_data[53]  # 联系电话
                    if row_data[26] == '是':
                        pp2.is_three_personnel = True  # 是否三员
                    pp2.present_address = row_data[27]  # 现住地址
                    pp2.passport_number = row_data[31]  # 护照号码
                    pp2.nation = row_data[47]  # 民族
                    pp2.educational_level = row_data[48]  # 文化程度，教育水平
                    pp2.political_face = row_data[49]  # 政治面貌
                    pp2.marriage = row_data[50]  # 是否已婚
                    pp2.health = row_data[51]  # 健康状况
                    pp2.note = row_data[52]
                    pp2.save()

                    family = Family()
                    family.family_master_uuid = pp.personnel_uuid  # 家庭户主ID＝personnel_uuid唯一标识
                    family.personnel_uuid = pp2.personnel_uuid  # 家庭成员ID＝personnel_uuid唯一标识
                    family.family_relation = row_data[44]  # 家庭关系
                    family.desc = ''
                    family.save()

                if row_data[56] != '':
                    pp3 = PersonnelProfile()
                    pp3.personnel_uuid = str(uuid.uuid1())  # 唯一标识
                    pp3.input_location = row_data[0]  # 录入地
                    pp3.input_user_id = 1  # 录入人
                    pp3.input_user_name = row_data[1]  # 录入人
                    pp3.name = row_data[57]  # 姓名
                    if row_data[4] != '男':
                        pp3.gender = False  # 性别
                    pp3.ID_number = row_data[58]  # 身份证号
                    pp3.own_house = row_data[16]  # 是自住房／否租房
                    if row_data[17] == '是':
                        pp3.is_minimum_security = True  # 是否有低保
                    pp3.family_members = row_data[18]  # 流入地家庭人口
                    if row_data[19] == ' 是':
                        pp3.is_medical_security = True  # 是否有医保
                    pp3.work_source = row_data[66]  # 经济收入来源
                    pp3.work_address = row_data[28]  # 工作地址
                    pp3.work_desc = row_data[29]  # 工作内容／工作性质
                    pp3.annual_earnings = row_data[21]  # 年收入
                    if row_data[22] == '兵团':
                        pp3.is_corps = True  # 是兵团／否地方
                    if row_data[23] == '是':
                        pp3.is_leader = True  # 是否带头人
                    pp3.ID_address = row_data[67]  # 身份证地址
                    pp3.phone_number = row_data[65]  # 联系电话
                    if row_data[26] == '是':
                        pp3.is_three_personnel = True  # 是否三员
                    pp3.present_address = row_data[27]  # 现住地址
                    pp3.passport_number = row_data[31]  # 护照号码
                    pp3.nation = row_data[59]  # 民族
                    pp3.educational_level = row_data[60]  # 文化程度，教育水平
                    pp3.political_face = row_data[61]  # 政治面貌
                    pp3.marriage = row_data[62]  # 是否已婚
                    pp3.health = row_data[63]  # 健康状况
                    pp3.note = row_data[64]
                    pp3.save()

                    family = Family()
                    family.family_master_uuid = pp.personnel_uuid  # 家庭户主ID＝personnel_uuid唯一标识
                    family.personnel_uuid = pp3.personnel_uuid  # 家庭成员ID＝personnel_uuid唯一标识
                    family.family_relation = row_data[56]  # 家庭关系
                    family.desc = ''
                    family.save()

                if row_data[68] != '':
                    pp4 = PersonnelProfile()
                    pp4.personnel_uuid = str(uuid.uuid1())  # 唯一标识
                    pp4.input_location = row_data[0]  # 录入地
                    pp4.input_user_id = 1  # 录入人
                    pp4.input_user_name = row_data[1]  # 录入人
                    pp4.name = row_data[69]  # 姓名
                    if row_data[4] != '男':
                        pp4.gender = False  # 性别
                    pp4.ID_number = row_data[70]  # 身份证号
                    pp4.own_house = row_data[16]  # 是自住房／否租房
                    if row_data[17] == '是':
                        pp4.is_minimum_security = True  # 是否有低保
                    pp4.family_members = row_data[18]  # 流入地家庭人口
                    if row_data[19] == ' 是':
                        pp4.is_medical_security = True  # 是否有医保
                    pp4.work_source = row_data[78]  # 经济收入来源
                    pp4.work_address = row_data[28]  # 工作地址
                    pp4.work_desc = row_data[78]  # 工作内容／工作性质
                    pp4.annual_earnings = row_data[21]  # 年收入
                    if row_data[22] == '兵团':
                        pp4.is_corps = True  # 是兵团／否地方
                    if row_data[23] == '是':
                        pp4.is_leader = True  # 是否带头人
                    pp4.ID_address = row_data[79]  # 身份证地址
                    pp4.phone_number = row_data[77]  # 联系电话
                    if row_data[26] == '是':
                        pp4.is_three_personnel = True  # 是否三员
                    pp4.present_address = row_data[27]  # 现住地址
                    pp4.passport_number = row_data[31]  # 护照号码
                    pp4.nation = row_data[71]  # 民族
                    pp4.educational_level = row_data[72]  # 文化程度，教育水平
                    pp4.political_face = row_data[73]  # 政治面貌
                    pp4.marriage = row_data[74]  # 是否已婚
                    pp4.health = row_data[75]  # 健康状况
                    pp4.note = row_data[76]
                    pp4.save()

                    family = Family()
                    family.family_master_uuid = pp.personnel_uuid  # 家庭户主ID＝personnel_uuid唯一标识
                    family.personnel_uuid = pp4.personnel_uuid  # 家庭成员ID＝personnel_uuid唯一标识
                    family.family_relation = row_data[68]  # 家庭关系
                    family.desc = ''
                    family.save()

                if row_data[80] != '':
                    pp5 = PersonnelProfile()
                    pp5.personnel_uuid = str(uuid.uuid1())  # 唯一标识
                    pp5.input_location = row_data[0]  # 录入地
                    pp5.input_user_id = 1  # 录入人
                    pp5.input_user_name = row_data[1]  # 录入人
                    pp5.name = row_data[81]  # 姓名
                    if row_data[4] != '男':
                        pp5.gender = False  # 性别
                    pp5.ID_number = row_data[82]  # 身份证号
                    pp5.own_house = row_data[16]  # 是自住房／否租房
                    if row_data[17] == '是':
                        pp5.is_minimum_security = True  # 是否有低保
                    pp5.family_members = row_data[18]  # 流入地家庭人口
                    if row_data[19] == ' 是':
                        pp5.is_medical_security = True  # 是否有医保
                    pp5.work_source = row_data[90]  # 经济收入来源
                    pp5.work_address = row_data[90]  # 工作地址
                    pp5.work_desc = row_data[90]  # 工作内容／工作性质
                    pp5.annual_earnings = row_data[21]  # 年收入
                    if row_data[22] == '兵团':
                        pp5.is_corps = True  # 是兵团／否地方
                    if row_data[23] == '是':
                        pp5.is_leader = True  # 是否带头人
                    pp5.ID_address = row_data[91]  # 身份证地址
                    pp5.phone_number = row_data[89]  # 联系电话
                    if row_data[26] == '是':
                        pp5.is_three_personnel = True  # 是否三员
                    pp5.present_address = row_data[27]  # 现住地址
                    pp5.passport_number = row_data[31]  # 护照号码
                    pp5.nation = row_data[83]  # 民族
                    pp5.educational_level = row_data[84]  # 文化程度，教育水平
                    pp5.political_face = row_data[85]  # 政治面貌
                    pp5.marriage = row_data[86]  # 是否已婚
                    pp5.health = row_data[87]  # 健康状况
                    pp5.note = row_data[88]
                    pp5.save()

                    family = Family()
                    family.family_master_uuid = pp.personnel_uuid  # 家庭户主ID＝personnel_uuid唯一标识
                    family.personnel_uuid = pp5.personnel_uuid  # 家庭成员ID＝personnel_uuid唯一标识
                    family.family_relation = row_data[80]  # 家庭关系
                    family.desc = ''
                    family.save()

        except :
            logging.basicConfig(filename='app/log/xj_error.log', level=logging.INFO)
            logging.info("row num = " + str(i))


#import_excel()

def get_all(request):
    v = 1
    #a = UserToken.objects.create(token="abc")
    c = 1
    import_excel()
    return HttpResponse("ok")

