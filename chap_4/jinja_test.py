# -*- coding:utf-8 -*-

import os
import jinja2

def render(tpl_path,**kwargs):
    path,filename = os.path.split(tpl_path)
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(path or './')
    ).get_template(filename).render(**kwargs)

def test_simple():
    title = "  Title H    "
    items = [{'href':'a.com','caption':'ACaption'},{'href':'b.com','caption':'BCaption'},
    {'href':'c.com','caption':'CCaption'}]
    content = " This is the content"
    result = render('/mnt/hgfs/shared_files/python_manage/chap_4/templates/simple.html',**locals())
    print(result)

def test_extend():
    result = render('/mnt/hgfs/shared_files/python_manage/chap_4/templates/index.html')
    print(result)

if __name__ == "__main__":
    # test_simple()
    test_extend()
