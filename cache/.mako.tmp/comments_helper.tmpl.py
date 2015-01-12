# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1421050835.0859177
_enable_loop = True
_template_filename = '/usr/lib/python3.4/site-packages/nikola/data/themes/base/templates/comments_helper.tmpl'
_template_uri = 'comments_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['comment_form', 'comment_link', 'comment_link_script']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('isso', context._clean_inheritance_tokens(), templateuri='comments_helper_isso.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'isso')] = ns

    ns = runtime.TemplateNamespace('intensedebate', context._clean_inheritance_tokens(), templateuri='comments_helper_intensedebate.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'intensedebate')] = ns

    ns = runtime.TemplateNamespace('livefyre', context._clean_inheritance_tokens(), templateuri='comments_helper_livefyre.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'livefyre')] = ns

    ns = runtime.TemplateNamespace('muut', context._clean_inheritance_tokens(), templateuri='comments_helper_muut.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'muut')] = ns

    ns = runtime.TemplateNamespace('googleplus', context._clean_inheritance_tokens(), templateuri='comments_helper_googleplus.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'googleplus')] = ns

    ns = runtime.TemplateNamespace('facebook', context._clean_inheritance_tokens(), templateuri='comments_helper_facebook.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'facebook')] = ns

    ns = runtime.TemplateNamespace('disqus', context._clean_inheritance_tokens(), templateuri='comments_helper_disqus.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'disqus')] = ns

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
        intensedebate = _mako_get_namespace(context, 'intensedebate')
        livefyre = _mako_get_namespace(context, 'livefyre')
        googleplus = _mako_get_namespace(context, 'googleplus')
        facebook = _mako_get_namespace(context, 'facebook')
        disqus = _mako_get_namespace(context, 'disqus')
        isso = _mako_get_namespace(context, 'isso')
        muut = _mako_get_namespace(context, 'muut')
        comment_system = context.get('comment_system', UNDEFINED)
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
        intensedebate = _mako_get_namespace(context, 'intensedebate')
        livefyre = _mako_get_namespace(context, 'livefyre')
        googleplus = _mako_get_namespace(context, 'googleplus')
        facebook = _mako_get_namespace(context, 'facebook')
        disqus = _mako_get_namespace(context, 'disqus')
        isso = _mako_get_namespace(context, 'isso')
        muut = _mako_get_namespace(context, 'muut')
        comment_system = context.get('comment_system', UNDEFINED)
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


def render_comment_link_script(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        intensedebate = _mako_get_namespace(context, 'intensedebate')
        livefyre = _mako_get_namespace(context, 'livefyre')
        googleplus = _mako_get_namespace(context, 'googleplus')
        facebook = _mako_get_namespace(context, 'facebook')
        disqus = _mako_get_namespace(context, 'disqus')
        isso = _mako_get_namespace(context, 'isso')
        muut = _mako_get_namespace(context, 'muut')
        comment_system = context.get('comment_system', UNDEFINED)
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


"""
__M_BEGIN_METADATA
{"uri": "comments_helper.tmpl", "source_encoding": "utf-8", "filename": "/usr/lib/python3.4/site-packages/nikola/data/themes/base/templates/comments_helper.tmpl", "line_map": {"22": 9, "25": 5, "28": 4, "31": 6, "34": 7, "37": 8, "40": 3, "43": 0, "48": 2, "49": 3, "50": 4, "51": 5, "52": 6, "53": 7, "54": 8, "55": 9, "56": 27, "57": 45, "58": 63, "64": 11, "76": 11, "77": 12, "78": 13, "79": 13, "80": 13, "81": 14, "82": 15, "83": 15, "84": 15, "85": 16, "86": 17, "87": 17, "88": 17, "89": 18, "90": 19, "91": 19, "92": 19, "93": 20, "94": 21, "95": 21, "96": 21, "97": 22, "98": 23, "99": 23, "100": 23, "101": 24, "102": 25, "103": 25, "104": 25, "110": 29, "122": 29, "123": 30, "124": 31, "125": 31, "126": 31, "127": 32, "128": 33, "129": 33, "130": 33, "131": 34, "132": 35, "133": 35, "134": 35, "135": 36, "136": 37, "137": 37, "138": 37, "139": 38, "140": 39, "141": 39, "142": 39, "143": 40, "144": 41, "145": 41, "146": 41, "147": 42, "148": 43, "149": 43, "150": 43, "156": 47, "168": 47, "169": 48, "170": 49, "171": 49, "172": 49, "173": 50, "174": 51, "175": 51, "176": 51, "177": 52, "178": 53, "179": 53, "180": 53, "181": 54, "182": 55, "183": 55, "184": 55, "185": 56, "186": 57, "187": 57, "188": 57, "189": 58, "190": 59, "191": 59, "192": 59, "193": 60, "194": 61, "195": 61, "196": 61, "202": 196}}
__M_END_METADATA
"""
