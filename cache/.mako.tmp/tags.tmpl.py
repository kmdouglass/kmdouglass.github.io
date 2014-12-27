# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1419700152.2898545
_enable_loop = True
_template_filename = '/usr/lib/python3.4/site-packages/nikola/data/themes/bootstrap/templates/tags.tmpl'
_template_uri = 'tags.tmpl'
_source_encoding = 'utf-8'
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        items = context.get('items', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        cat_items = context.get('cat_items', UNDEFINED)
        title = context.get('title', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        items = context.get('items', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        cat_items = context.get('cat_items', UNDEFINED)
        title = context.get('title', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<h1>')
        __M_writer(str(title))
        __M_writer('</h1>\n')
        if cat_items:
            __M_writer('    <h2>')
            __M_writer(str(messages("Categories")))
            __M_writer('</h2>\n    <ul class="unstyled">\n')
            for text, link in cat_items:
                if text:
                    __M_writer('            <li><a class="reference badge" href="')
                    __M_writer(str(link))
                    __M_writer('">')
                    __M_writer(str(text))
                    __M_writer('</a></li>\n')
            __M_writer('    </ul>\n')
            if items:
                __M_writer('        <h2>')
                __M_writer(str(messages("Tags")))
                __M_writer('</h2>\n')
        if items:
            __M_writer('    <ul class="list-inline">\n')
            for text, link in items:
                __M_writer('        <li><a class="reference badge" href="')
                __M_writer(str(link))
                __M_writer('">')
                __M_writer(str(text))
                __M_writer('</a></li>\n')
            __M_writer('    </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/usr/lib/python3.4/site-packages/nikola/data/themes/bootstrap/templates/tags.tmpl", "line_map": {"64": 7, "65": 9, "66": 10, "67": 11, "68": 11, "69": 11, "70": 11, "71": 11, "72": 14, "73": 15, "74": 16, "75": 16, "76": 16, "77": 19, "78": 20, "79": 21, "80": 22, "81": 22, "82": 22, "83": 22, "84": 22, "85": 24, "26": 0, "91": 85, "37": 2, "42": 26, "48": 4, "58": 4, "59": 5, "60": 5, "61": 6, "62": 7, "63": 7}, "uri": "tags.tmpl", "source_encoding": "utf-8"}
__M_END_METADATA
"""
