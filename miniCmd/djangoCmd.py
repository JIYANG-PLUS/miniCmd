import os, re
from .settings import BASE_DIR

__all__ = [
    'startapp',
]

PATT_CHARS = re.compile(r'^[a-zA-Z].*$')
PATT_REPLACE = re.compile(r'[$][{](.*?)[}]')

def new_file(name, content=None):
    with open(name, 'w', encoding='utf-8') as f:
        if content: f.writelines(content)

def read_file_lists(name, *args, path=BASE_DIR, **kwargs):
    f_path = os.path.dirname(path)
    r_path = os.path.join(f_path, 'djangoTemplates', name)
    with open(r_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    if 'replace' in kwargs and kwargs['replace']:
        lines = [PATT_REPLACE.sub(lambda x:kwargs[x.group(1)], _) for _ in lines]
    return lines

def startapp():
    app_name = input('请输入您要创建的app名：').strip()
    if PATT_CHARS.match(app_name) and not os.path.exists(os.path.join(BASE_DIR, app_name)):
        """""""""main"""
        """"""
        os.mkdir(app_name)
        APP_DIR = os.path.join(BASE_DIR, app_name)
        new_file(os.path.join(APP_DIR, '__init__.py'))
        new_file(os.path.join(APP_DIR, 'admin.py'), content=read_file_lists('admin.django'))
        new_file(os.path.join(APP_DIR, 'apps.py'), content=read_file_lists('apps.django'
            , replace=True
            , app_name=app_name))
        new_file(os.path.join(APP_DIR, 'forms.py'), content=read_file_lists('forms.django'))
        new_file(os.path.join(APP_DIR, 'models.py'), content=read_file_lists('models.django'))
        new_file(os.path.join(APP_DIR, 'tests.py'), content=read_file_lists('tests.django'))
        new_file(os.path.join(APP_DIR, 'urls.py'), content=read_file_lists('urls.django'
            , replace=True
            , app_name=app_name))
        new_file(os.path.join(APP_DIR, 'views.py'), content=read_file_lists('views.django'))
        """"""
        """""""""templates"""
        """"""
        os.mkdir(os.path.join(APP_DIR, 'templates'))
        os.mkdir(os.path.join(APP_DIR, 'templates', app_name))
        os.mkdir(os.path.join(APP_DIR, 'templates', app_name, 'includes'))
        TEMP_DIR = os.path.join(APP_DIR, 'templates', app_name)
        new_file(os.path.join(TEMP_DIR, 'base.html'), content=read_file_lists('baseHtml.django'))
        new_file(os.path.join(TEMP_DIR, 'includes', 'paginator.html'), content=read_file_lists('paginator.django'))
        """"""
        """""""""static"""
        """"""
        os.mkdir(os.path.join(APP_DIR, 'static'))
        os.mkdir(os.path.join(APP_DIR, 'static', app_name))
        os.mkdir(os.path.join(APP_DIR, 'static', app_name, 'js'))
        os.mkdir(os.path.join(APP_DIR, 'static', app_name, 'img'))
        os.mkdir(os.path.join(APP_DIR, 'static', app_name, 'css'))
        """"""
        """""""""templatetags"""
        """"""
        os.mkdir(os.path.join(APP_DIR, 'templatetags'))
        new_file(os.path.join(APP_DIR, 'templatetags', '__init__.py'))
        new_file(os.path.join(APP_DIR, 'templatetags', 'filter.py'), content=read_file_lists('filter.django'))
        """"""
        """""""""migrations"""
        """"""
        os.mkdir(os.path.join(APP_DIR, 'migrations'))
        new_file(os.path.join(APP_DIR, 'migrations', '__init__.py'))
        """"""
