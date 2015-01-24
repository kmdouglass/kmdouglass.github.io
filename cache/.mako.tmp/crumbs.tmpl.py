# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1422090314.2121396
_enable_loop = True
_template_filename = '/usr/lib/python3.4/site-packages/nikola/data/themes/base/templates/crumbs.tmpl'
_template_uri = 'crumbs.tmpl'
_source_encoding = 'utf-8'
_exports = ['bar']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bar(context,crumbs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('\n')
        if crumbs:
            __M_writer('<nav class="breadcrumbs">\n<ul class="breadcrumb">\n')
            for link, text in crumbs:
                __M_writer('        <li><a href="')
                __M_writer(str(link))
                __M_writer('">')
                __M_writer(str(text))
                __M_writer('</a></li>\n')
            __M_writer('</ul>\n</nav>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"32": 4, "33": 5, "34": 7, "35": 8, "36": 8, "37": 8, "38": 8, "39": 8, "40": 10, "46": 40, "15": 0, "20": 2, "21": 13, "27": 3, "31": 3}, "uri": "crumbs.tmpl", "source_encoding": "utf-8", "filename": "/usr/lib/python3.4/site-packages/nikola/data/themes/base/templates/crumbs.tmpl"}
__M_END_METADATA
"""
