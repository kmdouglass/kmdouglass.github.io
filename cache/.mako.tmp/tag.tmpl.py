# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1421223072.7445996
_enable_loop = True
_template_filename = '/usr/lib/python3.4/site-packages/nikola/data/themes/base/templates/tag.tmpl'
_template_uri = 'tag.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content']


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
    return runtime._inherit_from(context, 'list_post.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        date_format = context.get('date_format', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        title = context.get('title', UNDEFINED)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        messages = context.get('messages', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        len = context.get('len', UNDEFINED)
        kind = context.get('kind', UNDEFINED)
        tag = context.get('tag', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def extra_head():
            return render_extra_head(context)
        parent = context.get('parent', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        len = context.get('len', UNDEFINED)
        kind = context.get('kind', UNDEFINED)
        tag = context.get('tag', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n')
        if len(translations) > 1 and generate_rss:
            for language in translations:
                __M_writer('            <link rel="alternate" type="application/rss+xml" type="application/rss+xml" title="RSS for ')
                __M_writer(str(kind))
                __M_writer(' ')
                __M_writer(str(tag))
                __M_writer(' (')
                __M_writer(str(language))
                __M_writer(')" href="')
                __M_writer(str(_link(kind + "_rss", tag, language)))
                __M_writer('">\n')
        elif generate_rss:
            __M_writer('        <link rel="alternate" type="application/rss+xml" type="application/rss+xml" title="RSS for ')
            __M_writer(str(kind))
            __M_writer(' ')
            __M_writer(str(tag))
            __M_writer('" href="')
            __M_writer(str(_link(kind + "_rss", tag)))
            __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        date_format = context.get('date_format', UNDEFINED)
        def content():
            return render_content(context)
        title = context.get('title', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        len = context.get('len', UNDEFINED)
        tag = context.get('tag', UNDEFINED)
        kind = context.get('kind', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<article class="tagpage">\n    <header>\n        <h1>')
        __M_writer(str(title))
        __M_writer('</h1>\n        <div class="metadata">\n')
        if len(translations) > 1 and generate_rss:
            for language in translations:
                __M_writer('                <p class="feedlink">\n                    <a href="')
                __M_writer(str(_link(kind + "_rss", tag, language)))
                __M_writer('" hreflang="')
                __M_writer(str(language))
                __M_writer('" type="application/rss+xml">')
                __M_writer(str(messages('RSS feed', language)))
                __M_writer(' (')
                __M_writer(str(language))
                __M_writer(')</a>&nbsp;\n                </p>\n')
        elif generate_rss:
            __M_writer('                <p class="feedlink"><a href="')
            __M_writer(str(_link(kind + "_rss", tag)))
            __M_writer('" type="application/rss+xml">')
            __M_writer(str(messages('RSS feed')))
            __M_writer('</a></p>\n')
        __M_writer('        </div>\n    </header>\n')
        if posts:
            __M_writer('    <ul class="postlist">\n')
            for post in posts:
                __M_writer('        <li><a href="')
                __M_writer(str(post.permalink()))
                __M_writer('" class="listtitle">')
                __M_writer(str(post.title()))
                __M_writer('</a> <time class="listdate" datetime="')
                __M_writer(str(post.date.isoformat()))
                __M_writer('" title="')
                __M_writer(str(post.formatted_date(date_format)))
                __M_writer('">')
                __M_writer(str(post.formatted_date(date_format)))
                __M_writer('</time></li>\n')
            __M_writer('    </ul>\n')
        __M_writer('</article>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/usr/lib/python3.4/site-packages/nikola/data/themes/base/templates/tag.tmpl", "uri": "tag.tmpl", "source_encoding": "utf-8", "line_map": {"128": 24, "129": 24, "130": 24, "131": 24, "132": 27, "133": 28, "134": 28, "135": 28, "136": 28, "137": 28, "138": 30, "139": 32, "140": 33, "141": 34, "142": 35, "143": 35, "144": 35, "145": 35, "146": 35, "147": 35, "148": 35, "149": 35, "150": 35, "151": 35, "152": 35, "153": 37, "26": 0, "154": 39, "160": 154, "46": 2, "51": 13, "56": 40, "62": 4, "75": 4, "76": 5, "77": 5, "78": 6, "79": 7, "80": 8, "81": 8, "82": 8, "83": 8, "84": 8, "85": 8, "86": 8, "87": 8, "88": 8, "89": 10, "90": 11, "91": 11, "92": 11, "93": 11, "94": 11, "95": 11, "96": 11, "102": 16, "118": 16, "119": 19, "120": 19, "121": 21, "122": 22, "123": 23, "124": 24, "125": 24, "126": 24, "127": 24}}
__M_END_METADATA
"""
