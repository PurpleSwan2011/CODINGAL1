class Employee:
    def __init__(self):
        print('employee created')
    def __del__(self):
        print("del called")
def Create_obj():
    print('making obj....')
    obj=Employee()
    print('function end....')
    del obj
print('Calling Create_obj() function....')
obj=Create_obj()
print('proram end............')