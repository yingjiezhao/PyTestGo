'''
Created on 2017年5月17日

@author: Administrator
'''
import threading

def logger(log_file_path, list_of_text_strings):
    file_object = open(log_file_path, 'a')
    try:
        file_object.writelines(list_of_text_strings)
    finally:
        file_object.close( )

    return




if __name__ == "__main__":
    a = []
    log_file_path = "C:\\Users\\Administrator\\workspace\\PyTestGo\\\com\\pytestgo\\logs\\1.txt"
    contents = [["111\n","1111\n", "11111\n"],["222\n","2222\n","22222\n"],["333\n","3333\n","33333\n"],["444\n","4444\n","44444\n"]]
    
    for content in contents:
        thread = threading.Thread(target=logger, args=(log_file_path, content,))
        a.append(thread)
    for c in a:
        c.start()
        

    
