# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1419975904.3157537
_enable_loop = True
_template_filename = '/usr/lib/python3.4/site-packages/nikola/data/themes/base/templates/comments_helper.tmpl'
_template_uri = 'comments_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['comment_link_script', 'comment_form', 'comment_link']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('intensedebate', context._clean_inheritance_tokens(), templateuri='comments_helper_intensedebate.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'intensedebate')] = ns

    ns = runtime.TemplateNamespace('isso', context._clean_inheritance_tokens(), templateuri='comments_helper_isso.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'isso')] = ns

    ns = runtime.TemplateNamespace('disqus', context._clean_inheritance_tokens(), templateuri='comments_helper_disqus.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'disqus')] = ns

    ns = runtime.TemplateNamespace('facebook', context._clean_inheritance_tokens(), templateuri='comments_helper_facebook.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'facebook')] = ns

    ns = runtime.TemplateNamespace('googleplus', context._clean_inheritance_tokens(), templateuri='comments_helper_googleplus.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'googleplus')] = ns

    ns = runtime.TemplateNamespace('livefyre', context._clean_inheritance_tokens(), templateuri='comments_helper_livefyre.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'livefyre')] = ns

    ns = runtime.TemplateNamespace('muut', context._clean_inheritance_tokens(), templateuri='comments_helper_muut.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'muut')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link_script(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        isso = _mako_get_namespace(context, 'isso')
        livefyre = _mako_get_namespace(context, 'livefyre')
        intensedebate = _mako_get_namespace(context, 'intensedebate')
        disqus = _mako_get_namespace(context, 'disqus')
        comment_system = context.get('comment_system', UNDEFINED)
        facebook = _mako_get_namespace(context, 'facebook')
        googleplus = _mako_get_namespace(context, 'googleplus')
        muut = _mako_get_namespace(context, 'muut')
        __M_writer = context.writer()
        __M_writer('\n')
        if comment_system == 'disqus':
            __M_writer('        ')
            __M_writer(str(disqus.comment_link_script()))
            __M_writer('\n')
        elif comment_system == 'livefyre':
            __M_writer('        ')
            __M_writer(str(livefyre.comment_link_script()))
            __M_writer('\n')
        elif comment_system == 'intensedebate':
            __M_writer('        ')
            __M_writer(str(intensedebate.comment_link_script()))
            __M_writer('\n')
        elif comment_system == 'muut':
            __M_writer('        ')
            __M_writer(str(muut.comment_link_script()))
            __M_writer('\n')
        elif comment_system == 'googleplus':
            __M_writer('        ')
            __M_writer(str(googleplus.comment_link_script()))
            __M_writer('\n')
        elif comment_system == 'facebook':
            __M_writer('        ')
            __M_writer(str(facebook.comment_link_script()))
            __M_writer('\n')
        elif comment_system == 'isso':
            __M_writer('        ')
            __M_writer(str(isso.comment_link_script()))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_form(context,url,title,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        isso = _mako_get_namespace(context, 'isso')
        livefyre = _mako_get_namespace(context, 'livefyre')
        intensedebate = _mako_get_namespace(context, 'intensedebate')
        disqus = _mako_get_namespace(context, 'disqus')
        comment_system = context.get('comment_system', UNDEFINED)
        facebook = _mako_get_namespace(context, 'facebook')
        googleplus = _mako_get_namespace(context, 'googleplus')
        muut = _mako_get_namespace(context, 'muut')
        __M_writer = context.writer()
        __M_writer('\n')
        if comment_system == 'disqus':
            __M_writer('        ')
            __M_writer(str(disqus.comment_form(url, title, identifier)))
            __M_writer('\n')
        elif comment_system == 'livefyre':
            __M_writer('        ')
            __M_writer(str(livefyre.comment_form(url, title, identifier)))
            __M_writer('\n')
        elif comment_system == 'intensedebate':
            __M_writer('        ')
            __M_writer(str(intensedebate.comment_form(url, title, identifier)))
            __M_writer('\n')
        elif comment_system == 'muut':
            __M_writer('        ')
            __M_writer(str(muut.comment_form(url, title, identifier)))
            __M_writer('\n')
        elif comment_system == 'googleplus':
            __M_writer('        ')
            __M_writer(str(googleplus.comment_form(url, title, identifier)))
            __M_writer('\n')
        elif comment_system == 'facebook':
            __M_writer('        ')
            __M_writer(str(facebook.comment_form(url, title, identifier)))
            __M_writer('\n')
        elif comment_system == 'isso':
            __M_writer('        ')
            __M_writer(str(isso.comment_form(url, title, identifier)))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link(context,link,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        isso = _mako_get_namespace(context, 'isso')
        livefyre = _mako_get_namespace(context, 'livefyre')
        intensedebate = _mako_get_namespace(context, 'intensedebate')
        disqus = _mako_get_namespace(context, 'disqus')
        comment_system = context.get('comment_system', UNDEFINED)
        facebook = _mako_get_namespace(context, 'facebook')
        googleplus = _mako_get_namespace(context, 'googleplus')
        muut = _mako_get_namespace(context, 'muut')
        __M_writer = context.writer()
        __M_writer('\n')
        if comment_system == 'disqus':
            __M_writer('        ')
            __M_writer(str(disqus.comment_link(link, identifier)))
            __M_writer('\n')
        elif comment_system == 'livefyre':
            __M_writer('        ')
            __M_writer(str(livefyre.comment_link(link, identifier)))
            __M_writer('\n')
        elif comment_system == 'intensedebate':
            __M_writer('        ')
            __M_writer(str(intensedebate.comment_link(link, identifier)))
            __M_writer('\n')
        elif comment_system == 'muut':
            __M_writer('        ')
            __M_writer(str(muut.comment_link(link, identifier)))
            __M_writer('\n')
        elif comment_system == 'googleplus':
            __M_writer('        ')
            __M_writer(str(googleplus.comment_link(link, identifier)))
            __M_writer('\n')
        elif comment_system == 'facebook':
            __M_writer('        ')
            __M_writer(str(facebook.comment_link(link, identifier)))
            __M_writer('\n')
        elif comment_system == 'isso':
            __M_writer('        ')
            __M_writer(str(isso.comment_link(link, identifier)))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/usr/lib/python3.4/site-packages/nikola/data/themes/base/templates/comments_helper.tmpl", "line_map": {"22": 5, "25": 9, "28": 3, "31": 8, "34": 7, "37": 4, "40": 6, "43": 0, "48": 2, "49": 3, "50": 4, "51": 5, "52": 6, "53": 7, "54": 8, "55": 9, "56": 27, "57": 45, "58": 63, "64": 47, "76": 47, "77": 48, "78": 49, "79": 49, "80": 49, "81": 50, "82": 51, "83": 51, "84": 51, "85": 52, "86": 53, "87": 53, "88": 53, "89": 54, "90": 55, "91": 55, "92": 55, "93": 56, "94": 57, "95": 57, "96": 57, "97": 58, "98": 59, "99": 59, "100": 59, "101": 60, "102": 61, "103": 61, "104": 61, "110": 11, "122": 11, "123": 12, "124": 13, "125": 13, "126": 13, "127": 14, "128": 15, "129": 15, "130": 15, "131": 16, "132": 17, "133": 17, "134": 17, "135": 18, "136": 19, "137": 19, "138": 19, "139": 20, "140": 21, "141": 21, "142": 21, "143": 22, "144": 23, "145": 23, "146": 23, "147": 24, "148": 25, "149": 25, "150": 25, "156": 29, "168": 29, "169": 30, "170": 31, "171": 31, "172": 31, "173": 32, "174": 33, "175": 33, "176": 33, "177": 34, "178": 35, "179": 35, "180": 35, "181": 36, "182": 37, "183": 37, "184": 37, "185": 38, "186": 39, "187": 39, "188": 39, "189": 40, "190": 41, "191": 41, "192": 41, "193": 42, "194": 43, "195": 43, "196": 43, "202": 196}, "source_encoding": "utf-8", "uri": "comments_helper.tmpl"}
__M_END_METADATA
"""