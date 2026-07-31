'''
演示文件读写
'''
import csv


def read_csv_example(filename):
    with open(filename, 'r',encoding='utf-8') as f:
        header_line = f.readline()
        print(f'表头信息：{header_line}')
        index = 1
        for line in f:
            new_str = line.rstrip('\r\n')
            data_list = new_str.split(',')
            print(f'第{index}行数据为{data_list}')

# 写csv
def write_csv(filename,students):
    '''

    :param filename: 文件路径
    :param name: 学生列表
    :return: None
    '''
    with open(filename,'w',encoding='utf-8') as f:
        # 表头
        f.write('name,age,score\n')
        # 循环写数据体
        for student in students:
            line = f"{student['name']},{student['age']},{student['score']}\n"
            f.write(line)


def read_csv(filename):
    students = []
    with open(filename,'r',encoding='utf-8') as f:
        #略过表头
        f.readline()

        for line in f:
            # line = line.rstrip('\r\n')
            # data = line.split(',')
            data_list = line.rstrip('\r\n').split(',')
            data_dict= {
                'name':data_list[0],
                'age':data_list[1],
                'score':data_list[2]
            }
            students.append(data_dict)
    return students

if __name__ == '__main__':
    #read_csv_example('./male_file.csv')
    students = [{'name':'licha','age':'23','score':99},{'name':'dage','age':'23','score':80}]
    write_csv('students.csv',students)
    print(read_csv('students.csv'))