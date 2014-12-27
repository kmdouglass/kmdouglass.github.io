# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1419697166.3438528
_enable_loop = True
_template_filename = '/usr/lib/python3.4/site-packages/nikola/data/themes/bootstrap3/templates/listing.tmpl'
_template_uri = 'listing.tmpl'
_source_encoding = 'utf-8'
_exports = ['sourcelink', 'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('ui', context._clean_inheritance_tokens(), templateuri='crumbs.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'ui')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        def content():
            return render_content(context._locals(__M_locals))
        source_link = _import_ns.get('source_link', context.get('source_link', UNDEFINED))
        files = _import_ns.get('files', context.get('files', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        crumbs = _import_ns.get('crumbs', context.get('crumbs', UNDEFINED))
        folders = _import_ns.get('folders', context.get('folders', UNDEFINED))
        ui = _mako_get_namespace(context, 'ui')
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        code = _import_ns.get('code', context.get('code', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
            context['self'].sourcelink(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        def sourcelink():
            return render_sourcelink(context)
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        source_link = _import_ns.get('source_link', context.get('source_link', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        if source_link:
            __M_writer('    <li>\n    <a href="')
            __M_writer(str(source_link))
            __M_writer('" id="sourcelink">')
            __M_writer(str(messages("Source")))
            __M_writer('</a>\n    </li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        def content():
            return render_content(context)
        files = _import_ns.get('files', context.get('files', UNDEFINED))
        crumbs = _import_ns.get('crumbs', context.get('crumbs', UNDEFINED))
        folders = _import_ns.get('folders', context.get('folders', UNDEFINED))
        ui = _mako_get_namespace(context, 'ui')
        code = _import_ns.get('code', context.get('code', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer(str(ui.bar(crumbs)))
        __M_writer('\n')
        if folders or files:
            __M_writer('<ul class="list-unstyled">\n')
            for name in folders:
                __M_writer('    <li><a href="')
                __M_writer(str(name))
                __M_writer('"><i class="glyphicon glyphicon-folder-open"></i> ')
                __M_writer(str(name))
                __M_writer('</a>\n')
            for name in files:
                __M_writer('    <li><a href="')
                __M_writer(str(name))
                __M_writer('.html"><i class="glyphicon glyphicon-file"></i> ')
                __M_writer(str(name))
                __M_writer('</a>\n')
            __M_writer('</ul>\n')
        if code:
            __M_writer('    ')
            __M_writer(str(code))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "listing.tmpl", "source_encoding": "utf-8", "filename": "/usr/lib/python3.4/site-packages/nikola/data/themes/bootstrap3/templates/listing.tmpl", "line_map": {"73": 22, "74": 23, "75": 24, "76": 25, "77": 25, "78": 25, "79": 25, "85": 5, "22": 3, "110": 13, "111": 13, "28": 0, "116": 17, "98": 5, "99": 6, "100": 6, "101": 7, "102": 8, "103": 9, "104": 10, "105": 10, "106": 10, "107": 10, "108": 10, "109": 12, "46": 2, "47": 3, "112": 13, "113": 13, "114": 13, "115": 15, "52": 20, "117": 18, "118": 18, "119": 18, "57": 28, "125": 119, "63": 22}}
__M_END_METADATA
"""
