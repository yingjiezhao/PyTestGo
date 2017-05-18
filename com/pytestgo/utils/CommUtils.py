'''
Created on 2017年5月16日

@author: Administrator
'''

import os


def get_testcase_path():
    return os.getcwd() + "\\com\\pytestgo\\testcase\\"

def get_logs_path():
    return os.getcwd() + "\\com\\pytestgo\\logs\\"
    
def get_testreport_path():
    return os.getcwd() + "\\com\\pytestgo\\testreport\\"    
    
if __name__ == "__main__":
    get_logs_path()