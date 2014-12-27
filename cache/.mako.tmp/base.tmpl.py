# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1419693714.370077
_enable_loop = True
_template_filename = 'themes/oldfashioned/templates/base.tmpl'
_template_uri = 'base.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'extra_js', 'content', 'belowtitle']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('base', context._clean_inheritance_tokens(), templateuri='base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'base')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        content_footer = _import_ns.get('content_footer', context.get('content_footer', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        def extra_js():
            return render_extra_js(context._locals(__M_locals))
        def belowtitle():
            return render_belowtitle(context._locals(__M_locals))
        set_locale = _import_ns.get('set_locale', context.get('set_locale', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        body_end = _import_ns.get('body_end', context.get('body_end', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        search_form = _import_ns.get('search_form', context.get('search_form', UNDEFINED))
        notes = _import_ns.get('notes', context.get('notes', UNDEFINED))
        annotations = _import_ns.get('annotations', context.get('annotations', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        base = _mako_get_namespace(context, 'base')
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        license = _import_ns.get('license', context.get('license', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer(str(set_locale(lang)))
        __M_writer('\n')
        __M_writer(str(base.html_headstart()))
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n')
        __M_writer(str(template_hooks['extra_head']()))
        __M_writer('\n</head>\n<body style="padding-top: 10px;">\n<div class="container-fluid" id="container" style="margin: 0 auto;">\n    <div class="row-fluid" id="titlerow">\n    <div class="span12" id="titlecolumn">\n    <!-- Banner-like substance -->\n        <div class="titlebox" style="text-align: right;">\n        <h1 id="blog-title" style="margin: 0; padding: 0;">\n            <a href="')
        __M_writer(str(abs_link('/')))
        __M_writer('" title="')
        __M_writer(str(blog_title))
        __M_writer('">')
        __M_writer(str(blog_title))
        __M_writer('</a>\n        </h1>\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'belowtitle'):
            context['self'].belowtitle(**pageargs)
        

        __M_writer('\n        <hr>\n        </div>\n    <!-- End of banner-like substance !-->\n    <div class="row-fluid" id="contentrow">\n        <div class="span10" id="contentcolumn">\n            <!--Body content-->\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n            <!--End of body content-->\n            <hr>\n            <div class="footerbox">\n                ')
        __M_writer(str(content_footer))
        __M_writer('\n                ')
        __M_writer(str(template_hooks['page_footer']()))
        __M_writer('\n            </div>\n        </div>\n        <div class="span2" id="sidebar">\n            <!--Sidebar content-->\n            <ul class="unstyled">\n            <li>')
        __M_writer(str(license))
        __M_writer('</li>\n            ')
        __M_writer(str(base.html_navigation_links()))
        __M_writer('\n            <li>')
        __M_writer(str(search_form))
        __M_writer('</li>\n            ')
        __M_writer(str(template_hooks['menu']()))
        __M_writer('\n            ')
        __M_writer(str(template_hooks['menu_alt']()))
        __M_writer('\n            </ul>\n            <!--End of sidebar content-->\n        </div>\n    </div>\n    </div>\n    </div>\n</div>\n')
        __M_writer(str(base.late_load_js()))
        __M_writer('\n    <script>jQuery("a.image-reference").colorbox({rel:"gal",maxWidth:"100%",maxHeight:"100%",scalePhotos:true});</script>\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_js'):
            context['self'].extra_js(**pageargs)
        

        __M_writer('\n')
        if annotations and post and not post.meta('noannotations'):
            __M_writer('        ')
            __M_writer(str(notes.code()))
            __M_writer('\n')
        elif not annotations and post and post.meta('annotations'):
            __M_writer('        ')
            __M_writer(str(notes.code()))
            __M_writer('\n')
        __M_writer(str(body_end))
        __M_writer('\n')
        __M_writer(str(template_hooks['body_end']()))
        __M_writer('\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        __M_writer('\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_js(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        def extra_js():
            return render_extra_js(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        def content():
            return render_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_belowtitle(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        base = _mako_get_namespace(context, 'base')
        def belowtitle():
            return render_belowtitle(context)
        __M_writer = context.writer()
        __M_writer('\n')
        if len(translations) > 1:
            __M_writer('        <small>\n            ')
            __M_writer(str(messages("Also available in:")))
            __M_writer('&nbsp;\n            ')
            __M_writer(str(base.html_translations()))
            __M_writer('\n        </small>\n')
        __M_writer('        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "uri": "base.tmpl", "filename": "themes/oldfashioned/templates/base.tmpl", "line_map": {"130": 5, "136": 59, "149": 34, "22": 2, "25": 0, "162": 20, "174": 20, "175": 21, "176": 22, "177": 23, "178": 23, "179": 24, "180": 24, "181": 27, "56": 2, "57": 3, "58": 3, "59": 4, "60": 4, "65": 8, "66": 9, "67": 9, "68": 18, "69": 18, "70": 18, "71": 18, "72": 18, "73": 18, "78": 27, "83": 34, "84": 38, "85": 38, "86": 39, "87": 39, "88": 45, "89": 45, "90": 46, "91": 46, "92": 47, "93": 47, "94": 48, "95": 48, "96": 49, "97": 49, "98": 57, "99": 57, "104": 59, "105": 60, "106": 61, "107": 61, "108": 61, "109": 62, "110": 63, "111": 63, "112": 63, "113": 65, "114": 65, "115": 66, "116": 66, "187": 181, "122": 5}}
__M_END_METADATA
"""
