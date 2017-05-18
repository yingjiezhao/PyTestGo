import copy
import threading
import time

from com.pytestgo.utils import CommUtils
from com.pytestgo.utils import ExcelUtils
from com.pytestgo.utils import LogUtils
from com.pytestgo.utils import RequestUtils
from com.pytestgo.utils.TestReporterUtils import TestReporter


class runner():
    def __init__(self):
        self.test_sum = 0;
        self.test_success = 0;
        self.test_failed = 0;
        self.t_detail_data = {};
        self.t_detail = []
        
    def get_testcase(self):   
        return ExcelUtils.readExcel(CommUtils.get_testcase_path() + "zt_testcase.xls", "测试用例")
    
    
    def run(self, testcase):
        
        # 设置循环次数,默认执行1次
        loop_time = 1
        if (isinstance(testcase[9], float)):
            loop_time = int(testcase[9])


        # 执行测试报告
        while(loop_time > 0):
            now_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
            #log_file = "c:\\zt-"+ time.strftime("%Y-%m-%d",time.localtime(time.time())) + ".log"
            log_file = CommUtils.get_logs_path() + time.strftime("%Y-%m-%d",time.localtime(time.time())) + ".log"
            print(now_time+": 开始执行用例"+testcase[1])
    
            # 请求接口
            test_result= RequestUtils.post(testcase[5], testcase[6])
            #test_result = -100
         
            # 添加log内容
            logs = []
            logs.append(("======================================\n"))
            logs.append("执行时间:"+now_time+"\n")
            logs.append("用例ID:"+testcase[0]+"\n")
            logs.append("用例名称:"+testcase[1]+"\n")
            logs.append("所属模块:"+testcase[2]+"\n")
            logs.append("接口名称:"+testcase[3]+"\n")
            logs.append("接口协议:"+testcase[4]+"\n")
            logs.append("请求链接:"+testcase[5]+"\n")
            logs.append("请求数据:"+testcase[6]+"\n")
            logs.append("预期结果:"+testcase[7]+"\n")
            
            
            
            # 收集测试结果
            testcase_tmp = {}
            testcase_tmp["t_id"] = testcase[0]
            testcase_tmp["t_name"] = testcase[1]
            testcase_tmp["t_interfname"] = testcase[3]
            testcase_tmp["t_proto"] = testcase[4]
            testcase_tmp["t_url"] = testcase[5]
            testcase_tmp["t_param"] = testcase[6]
            testcase_tmp["t_expect"] = testcase[7]
            testcase_tmp["t_time"] = now_time
            
            
            # 判断测试是否通过          
            if (isinstance(test_result,int)==False and testcase[7] in test_result):
                logs.append("实际结果:"+test_result+"\n")
                logs.append("测试结论:PASS\n")
                testcase_tmp["t_actual"] = test_result
                testcase_tmp["t_result"] = "PASS"
                self.test_success = self.test_success + 1;
            else:
                logs.append("实际结果:"+str(test_result)+"\n")
                logs.append("测试结论:FAILED\n")
                testcase_tmp["t_actual"] = str(test_result)
                testcase_tmp["t_result"] = "FAILED"
                self.test_failed = self.test_failed + 1;
            
            
            # 生成日志
            LogUtils.logger(log_file, logs)
            # 生成测试结果集
            self.t_detail.append(copy.copy(testcase_tmp))
            
            print(now_time+": 结束执行用例"+testcase[1])
            
            loop_time = loop_time - 1

        return
    
    def testReport(self):
        
        #testReport_path = "c:\\zt-" + time.strftime("%Y-%m-%d %H-%M-%S",time.localtime(time.time())) + ".xls";
        testReport_path = CommUtils.get_testreport_path() + time.strftime("%Y-%m-%d %H-%M-%S",time.localtime(time.time())) + ".xls";
        t_init_data = {"test_name": "四川移动掌厅", "test_version": "v3.3.2", "test_pl": "python34", "test_net": "wifi",
            "test_sum": self.test_success + self.test_failed, "test_success": self.test_success, "test_failed": self.test_failed, "test_date": time.strftime("%Y-%m-%d %H:%M",time.localtime(time.time()))}  
        
        self.t_detail.reverse()
        self.t_detail_data["info"] = self.t_detail
       
#        t_detail_data = {"info":[{"t_id":"1001", "t_name":"test_login", "t_interfname":"test","t_proto":"post","t_url":"www.baidu.com","t_param":"user_name=test\npassword=test", "t_expect":"True", "t_actual":"False", "t_result":"失败", "t_time":"2012-12-12 12:22"},
#                    {"t_id":"1002", "t_name":"test_login","t_interfname":"test", "t_proto":"post","t_url":"www.baidu.com","t_param":"user_name=test\npassword=TEst1", "t_expect":"True", "t_actual":"True", "t_result":"成功", "t_time":"2012-12-12 12:22"}]}
        TestReporter(testReport_path, t_init_data, self.t_detail_data)


        
        
if __name__ == "__main__":
      
    runner = runner()
    runner_threads = []
    test_suites = runner.get_testcase()
 
    for testcase in test_suites:
        runner_thread = threading.Thread(target=runner.run, args=((testcase,)))
        runner_threads.append(runner_thread)
           
    for thread in runner_threads:
        thread.start()
        thread.join()
 
    runner.testReport()
