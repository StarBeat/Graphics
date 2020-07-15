# -*- coding: UTF-8 -*-
import os
import sys
import re
import subprocess
import pickle

#config
config_file = "tools/config.cfg"
class Config(object):
    def __init__(self):
        super(Config, self).__init__()
        self.is_first = True

current_encoding = 'GBK'
#cmd
build_3rd = "cd 3rd&&build.bat"
def build(parameter_list = None):
    commane = parameter_list or build_3rd
    print("------build start...")
    cmd = subprocess.Popen(commane, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True)
    try:
        # 重定向标准输出
        while cmd.poll() is None:         # None表示正在执行中
            r = cmd.stdout.readline().decode(current_encoding)
            sys.stdout.write(r)                    # 可修改输出方式，比如控制台、文件等
        # 重定向错误输出
        if cmd.poll() != 0:                      # 不为0表示执行错误
            err = cmd.stderr.read().decode(current_encoding)
            sys.stdout.write(err)                 # 可修改输出方式，比如控制台、文件等
    except AttributeError as e:
        pass
    print("------build complete! {}".format(cmd.wait()))

def replace(file, regex, repl):
    with open(file, 'r') as f:
            s = re.sub(regex, repl, f.read())
            with open(file, 'w') as w:
                w.write(s)

def prepare():
    dir='3rd/'
    r = re.compile(r"/WX") #关闭警告变错误
    sub = re.compile(r"ADD_SUBDIRECTORY\((.+)\)")
    repl = "/WX-" 
    ls = os.listdir(dir)
    for i in ls:
        if os.path.isdir(dir + i) and os.path.exists(dir + i + "/CMakeLists.txt"):
                replace(dir + i + "/CMakeLists.txt", r, repl)
                with open(dir + i + "/CMakeLists.txt", 'r') as f:
                    subls = sub.findall(f.read())
                    for j in subls:
                        file = (dir + i + "/" + j+ "/CMakeLists.txt").replace(" ", "").replace("//", "/").replace("\\", "/")
                        if os.path.exists(file):
                            replace(file, r, repl)

if __name__ == "__main__":
    if os.path.exists(config_file):
        with open(config_file , "rb") as f:
            cfg = pickle.load(f) 
    else:
        cfg = Config()
    print(cfg.is_first)
    if cfg.is_first:
        cfg.is_first = False
        prepare()
    build()
    with open(config_file , "wb") as f:
        pickle.dump(cfg, f)