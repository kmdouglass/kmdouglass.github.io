# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1421051029.1495743
_enable_loop = True
_template_filename = '/usr/lib/python3.4/site-packages/nikola/data/themes/base/templates/comments_helper.tmpl'
_template_uri = 'comments_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['comment_form', 'comment_link_script', 'comment_link']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('muut', context._clean_inheritance_tokens(), templateuri='comments_helper_muut.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'muut')] = ns

    ns = runtime.TemplateNamespace('disqus', context._clean_inheritance_tokens(), templateuri='comments_helper_disqus.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'disqus')] = ns

    ns = runtime.TemplateNamespace('intensedebate', context._clean_inheritance_tokens(), templateuri='comments_helper_intensedebate.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'intensedebate')] = ns

    ns = runtime.TemplateNamespace('livefyre', context._clean_inheritance_tokens(), templateuri='comments_helper_livefyre.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'livefyre')] = ns

    ns = runtime.TemplateNamespace('facebook', context._clean_inheritance_tokens(), templateuri='comments_helper_facebook.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'facebook')] = ns

    ns = runtime.TemplateNamespace('isso', context._clean_inheritance_tokens(), templateuri='comments_helper_isso.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'isso')] = ns

    ns = runtime.TemplateNamespace('googleplus', context._clean_inheritance_tokens(), templateuri='comments_helper_googleplus.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'googleplus')] = ns

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


def render_comment_form(context,url,title,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        muut = _mako_get_namespace(context, 'muut')
        disqus = _mako_get_namespace(context, 'disqus')
        intensedebate = _mako_get_namespace(context, 'intensedebate')
        facebook = _mako_get_namespace(context, 'facebook')
        googleplus = _mako_get_namespace(context, 'googleplus')
        comment_system = context.get('comment_system', UNDEFINED)
        livefyre = _mako_get_namespace(context, 'livefyre')
        isso = _mako_get_namespace(context, 'isso')
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


def render_comment_link_script(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        muut = _mako_get_namespace(context, 'muut')
        disqus = _mako_get_namespace(context, 'disqus')
        intensedebate = _mako_get_namespace(context, 'intensedebate')
        facebook = _mako_get_namespace(context, 'facebook')
        googleplus = _mako_get_namespace(context, 'googleplus')
        comment_system = context.get('comment_system', UNDEFINED)
        livefyre = _mako_get_namespace(context, 'livefyre')
        isso = _mako_get_namespace(context, 'isso')
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


def render_comment_link(context,link,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        muut = _mako_get_namespace(context, 'muut')
        disqus = _mako_get_namespace(context, 'disqus')
        intensedebate = _mako_get_namespace(context, 'intensedebate')
        facebook = _mako_get_namespace(context, 'facebook')
        googleplus = _mako_get_namespace(context, 'googleplus')
        comment_system = context.get('comment_system', UNDEFINED)
        livefyre = _mako_get_namespace(context, 'livefyre')
        isso = _mako_get_namespace(context, 'isso')
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
{"uri": "comments_helper.tmpl", "line_map": {"22": 6, "25": 3, "28": 5, "31": 4, "34": 8, "37": 9, "40": 7, "43": 0, "48": 2, "49": 3, "50": 4, "51": 5, "52": 6, "53": 7, "54": 8, "55": 9, "56": 27, "57": 45, "58": 63, "64": 11, "76": 11, "77": 12, "78": 13, "79": 13, "80": 13, "81": 14, "82": 15, "83": 15, "84": 15, "85": 16, "86": 17, "87": 17, "88": 17, "89": 18, "90": 19, "91": 19, "92": 19, "93": 20, "94": 21, "95": 21, "96": 21, "97": 22, "98": 23, "99": 23, "100": 23, "101": 24, "102": 25, "103": 25, "104": 25, "110": 47, "122": 47, "123": 48, "124": 49, "125": 49, "126": 49, "127": 50, "128": 51, "129": 51, "130": 51, "131": 52, "132": 53, "133": 53, "134": 53, "135": 54, "136": 55, "137": 55, "138": 55, "139": 56, "140": 57, "141": 57, "142": 57, "143": 58, "144": 59, "145": 59, "146": 59, "147": 60, "148": 61, "149": 61, "150": 61, "156": 29, "168": 29, "169": 30, "170": 31, "171": 31, "172": 31, "173": 32, "174": 33, "175": 33, "176": 33, "177": 34, "178": 35, "179": 35, "180": 35, "181": 36, "182": 37, "183": 37, "184": 37, "185": 38, "186": 39, "187": 39, "188": 39, "189": 40, "190": 41, "191": 41, "192": 41, "193": 42, "194": 43, "195": 43, "196": 43, "202": 196}, "source_encoding": "utf-8", "filename": "/usr/lib/python3.4/site-packages/nikola/data/themes/base/templates/comments_helper.tmpl"}
__M_END_METADATA
"""
