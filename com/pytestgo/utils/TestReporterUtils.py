# -*- coding: utf-8 -*-
import xlsxwriter



class TestReporter():
    def get_format(self, wd, option={}):
        return wd.add_format(option)
    
    # 设置居中
    def get_format_center(self, wd,num=1):
        return wd.add_format({'align': 'center','valign': 'vcenter','border':num})
    def set_border_(self, wd, num=1):
        return wd.add_format({}).set_border(num)
    
    # 写数据
    def _write_center(self, worksheet, cl, data, wd):
        return worksheet.write(cl, data, self.get_format_center(wd))
    
    
    
    def __init__(self, excel_path, init_data, detail_data):
        self.workbook = xlsxwriter.Workbook(excel_path)
        self.init_worksheet = self.workbook.add_worksheet("测试总况")
        self.detail_worksheet = self.workbook.add_worksheet("测试详情")
        self.init_data = init_data
        self.detail_data = detail_data
        
        """生成测试报告"""
        self.test_summer()
        self.test_detail()
        
        self.workbook.close()
      
    
    def test_summer(self):
        self.init_worksheet.set_column("A:A", 16)
        self.init_worksheet.set_column("B:B", 16)
        self.init_worksheet.set_column("C:C", 15)
        self.init_worksheet.set_column("D:D", 16)
        self.init_worksheet.set_column("E:E", 18)
        self.init_worksheet.set_column("F:F", 18)
    
#         self.init_worksheet.set_row(1, 30)
        self.init_worksheet.set_row(2, 24)
        self.init_worksheet.set_row(3, 24)
        self.init_worksheet.set_row(4, 24)
        self.init_worksheet.set_row(5, 24)
    
    
        define_format_H1 = self.get_format(self.workbook, {'bold': True, 'font_size': 16})
        define_format_H2 = self.get_format(self.workbook, {'bold': True, 'font_size': 12})
        define_format_H1.set_border(1)
    
        define_format_H2.set_border(1)
        define_format_H1.set_align("center")
        define_format_H2.set_align("center")
        define_format_H2.set_bg_color("#538DD5")
        define_format_H2.set_color("#ffffff")
        # Create a new Chart object.
    
        self.init_worksheet.merge_range('A1:F1', '测试报告总概况', define_format_H1)
        self.init_worksheet.merge_range('A2:F2', '测试概括', define_format_H2)
        self.init_worksheet.merge_range('A3:A6', '这里放图片', self.get_format_center(self.workbook))
    
        self._write_center(self.init_worksheet, "B3", '项目名称', self.workbook)
        self._write_center(self.init_worksheet, "B4", '项目版本', self.workbook)
        self._write_center(self.init_worksheet, "B5", '脚本语言', self.workbook)
        self._write_center(self.init_worksheet, "B6", '测试网络', self.workbook)
    
    
        
        self._write_center(self.init_worksheet, "C3", self.init_data['test_name'], self.workbook)
        self._write_center(self.init_worksheet, "C4", self.init_data['test_version'], self.workbook)
        self._write_center(self.init_worksheet, "C5", self.init_data['test_pl'], self.workbook)
        self._write_center(self.init_worksheet, "C6", self.init_data['test_net'], self.workbook)
    
        self._write_center(self.init_worksheet, "D3", "用例执行总数", self.workbook)
        self._write_center(self.init_worksheet, "D4", "通过总数", self.workbook)
        self._write_center(self.init_worksheet, "D5", "失败总数", self.workbook)
        self._write_center(self.init_worksheet, "D6", "测试日期", self.workbook)
    
    
    
       
        self._write_center(self.init_worksheet, "E3", self.init_data['test_sum'], self.workbook)
        self._write_center(self.init_worksheet, "E4", self.init_data['test_success'], self.workbook)
        self._write_center(self.init_worksheet, "E5", self.init_data['test_failed'], self.workbook)
        self._write_center(self.init_worksheet, "E6", self.init_data['test_date'], self.workbook)
    
        self._write_center(self.init_worksheet, "F3", "通过率", self.workbook)
        
        self.init_worksheet.merge_range('F4:F6', str((self.init_data['test_success']/self.init_data['test_sum'])*100)+"%", self.get_format_center(self.workbook))

        self.pie(self.workbook, self.init_worksheet)
    
    
    def pie(self, workbook, worksheet):
        chart1 = workbook.add_chart({'type': 'pie'})
        chart1.add_series({
        'name':       '测试结果统计',
        'categories':'=测试总况!$D$4:$D$5',
       'values':    '=测试总况!$E$4:$E$5',
        })
        chart1.set_title({'name': '测试结果统计'})
        chart1.set_style(10)
        worksheet.insert_chart('A8', chart1, {'x_offset': 25, 'y_offset': 10})
    
    def test_detail(self):
    
        # 设置列行的宽高
        self.detail_worksheet.set_column("A:A", 8)
        self.detail_worksheet.set_column("B:B", 15)
        self.detail_worksheet.set_column("C:C", 15)
        self.detail_worksheet.set_column("D:D", 8)
        self.detail_worksheet.set_column("E:E", 15)
        self.detail_worksheet.set_column("F:F", 30)
        self.detail_worksheet.set_column("G:G", 20)
        self.detail_worksheet.set_column("H:H", 10)
        self.detail_worksheet.set_column("I:I", 10)
        self.detail_worksheet.set_column("J:J", 20)
    
        self.detail_worksheet.set_row(1, 20)
        self.detail_worksheet.set_row(2, 15)

    
    
    
        self.detail_worksheet.merge_range('A1:J1', '测试详情', self.get_format(self.workbook, {'bold': True, 'font_size': 12 ,'align': 'center','valign': 'vcenter','bg_color': '#538DD5', 'font_color': '#ffffff'}))
        self._write_center(self.detail_worksheet, "A2", '用例ID', self.workbook)
        self._write_center(self.detail_worksheet, "B2", '用例名称', self.workbook)
        self._write_center(self.detail_worksheet, "C2", '接口名称', self.workbook)
        self._write_center(self.detail_worksheet, "D2", '接口协议', self.workbook)
        self._write_center(self.detail_worksheet, "E2", 'url', self.workbook)
        self._write_center(self.detail_worksheet, "F2", '请求数据', self.workbook)
        self._write_center(self.detail_worksheet, "G2", '预期结果', self.workbook)
        self._write_center(self.detail_worksheet, "H2", '实际结果', self.workbook)
        self._write_center(self.detail_worksheet, "I2", '测试结果', self.workbook)
        self._write_center(self.detail_worksheet, "J2", '测试时间', self.workbook)
    
    
    #     data = {"info": [{"t_id": "1001", "t_name": "登陆", "t_method": "post", "t_url": "http://XXX?login", "t_param": "{user_name:test,pwd:111111}",
    #                       "t_hope": "{code:1,msg:登陆成功}", "t_actual": "{code:0,msg:密码错误}", "t_result": "失败"}, {"t_id": "1002", "t_name": "商品列表", "t_method": "get", "t_url": "http://XXX?getFoodList", "t_param": "{}",
    #                       "t_hope": "{code:1,msg:成功,info:[{name:123,detal:dfadfa,img:product/1.png},{name:456,detal:dfadfa,img:product/1.png}]}", "t_actual": "{code:1,msg:成功,info:[{name:123,detal:dfadfa,img:product/1.png},{name:456,detal:dfadfa,img:product/1.png}]}", "t_result": "成功"}],
    #             "test_sum": 100,"test_success": 20, "test_failed": 80}
        temp = len(self.detail_data["info"]) + 2
        for item in self.detail_data["info"]:
            self._write_center(self.detail_worksheet, "A"+str(temp), item["t_id"], self.workbook)
            self._write_center(self.detail_worksheet, "B"+str(temp), item["t_name"], self.workbook)
            self._write_center(self.detail_worksheet, "C"+str(temp), item["t_interfname"], self.workbook)
            self._write_center(self.detail_worksheet, "D"+str(temp), item["t_proto"], self.workbook)
            self._write_center(self.detail_worksheet, "E"+str(temp), item["t_url"], self.workbook)
            self._write_center(self.detail_worksheet, "F"+str(temp), item["t_param"], self.workbook)
            self._write_center(self.detail_worksheet, "G"+str(temp), item["t_expect"], self.workbook)
            self._write_center(self.detail_worksheet, "H"+str(temp), item["t_actual"], self.workbook)
            self._write_center(self.detail_worksheet, "I"+str(temp), item["t_result"], self.workbook)
            self._write_center(self.detail_worksheet, "J"+str(temp), item["t_time"], self.workbook)
            temp = temp -1

    
"""
1. 测试饼图样式

"""



if __name__ =="__main__":
    
    path = "C:\\Users\\Administrator\\Desktop\\report.xlsx"
    t_init_data = {"test_name": "智商", "test_version": "v2.0.8", "test_pl": "android", "test_net": "wifi",
            "test_sum": 100, "test_success": 80, "test_failed": 20, "test_date": "2018-10-10 12:10"}  
    t_detail_data = {"info":[{"t_id":"1001", "t_name":"test_login", "t_interfname":"test","t_proto":"post","t_url":"www.baidu.com","t_param":"user_name=test\npassword=test", "t_expect":"True", "t_actual":"False", "t_result":"失败", "t_time":"2012-12-12 12:22"},
                    {"t_id":"1002", "t_name":"test_login","t_interfname":"test", "t_proto":"post","t_url":"www.baidu.com","t_param":"user_name=test\npassword=TEst1", "t_expect":"True", "t_actual":"True", "t_result":"成功", "t_time":"2012-12-12 12:22"}]}
    
    TestReporter(path, t_init_data, t_detail_data)