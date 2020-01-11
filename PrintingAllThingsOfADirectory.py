import os

'''
def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isfile(path):
            print(path)
        else:
            walk(path)
'''

def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isfile(path):
            print(path)
        else:
            walk(path)

'''
def walk2(dirname2):
    for name2 in os.listdir(dirname):
        cwd = os.getcwd()
        if os.path.isfile(cwd):
            print(cwd)
        else:
            walk2(cwd)
            '''

def walk2(dirname):
    """Prints the names of all files in dirname and its subdirectories.

    This is the exercise solution, which uses os.walk.

    dirname: string name of directory
    """
    for root, dirs, files in os.walk(dirname):
        for filename in files:
            print(os.path.join(root, filename))

            
