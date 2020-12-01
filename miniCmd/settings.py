import os, sys

LANGUAGE = 'C' # 当前语言环境（C中文，E英文）

if 'miniCmd.py' not in os.listdir('.'):
    BASE_DIR = os.path.join(os.getcwd(), 'minicmd') # 追踪到miniCmd.py所在路径
    os.chdir(BASE_DIR) # 若运行出错，请检查项目路径是否正确
else: BASE_DIR = os.getcwd()

HELLO = f"""MINICMD [Version 1.0.0.0]
(c) 2020 HAPPY.（欢迎来到逗逼的 CMD ）
{sys.version}
"""

platform_name = os.name
if 'nt' == platform_name: CLS = 'cls'
elif 'posix' == platform_name: CLS = 'clear'
else: CLS = 'clear'

SUPPORT_UNPACK = (
    '.tar.bz2', '.tbz2', '.tar.gz', '.tgz', '.tar'
    , '.tar.xz', '.txz', '.zip',
)

SUPPORT_LS = (
    '.docx', '.py', '.txt', '.zip', '.rar'
    , '.xlsx', '.xls', '.rtf', '.ppt', '.pptx'
    , '.doc', '.exe', '.dll', '.png', '.jpg'
    , '.sql', '.bmp', '.css', '.less', '.js'
    , '.vue', '.c', '.java', '.cpp', '.cs'
    , '.sln', '.xml', '.json', 
)

