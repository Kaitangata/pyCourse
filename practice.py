import inspect
import os
import sys

#source: https://stackoverflow.com/questions/3718657/how-do-you-properly-determine-the-current-script-directory/22881871#22881871
#def get_script_dir(follow_symlinks=True):
#    if getattr(sys, 'frozen', False):
#        path = os.path.abspath(sys.executable)
#    else:
#        path = inspect.getabsfile(get_script_dir)
#    if follow_symlinks:
#        path = os.path.realpath(path)
#    return os.path.dirname(path)

def fileTest():
    filename = inspect.getframeinfo(inspect.currentframe()).filename
    os.chdir(os.path.dirname(os.path.abspath(filename)))

    file = open('test.txt', 'r', encoding="utf-8")
    data = file.read()
    print(data)
    file.close()

def main():
    fileTest()
main()