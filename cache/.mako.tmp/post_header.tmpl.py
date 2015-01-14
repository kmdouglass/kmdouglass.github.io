# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1421221926.2846823
_enable_loop = True
_template_filename = '/usr/lib/python3.4/site-packages/nikola/data/themes/base/templates/post_header.tmpl'
_template_uri = 'post_header.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_translations', 'html_sourcelink', 'html_post_header', 'html_title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        messages = context.get('messages', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        len = context.get('len', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if len(translations) > 1:
            __M_writer('        <div class="metadata posttranslations translations">\n            <h3 class="posttranslations-intro">')
            __M_writer(str(messages("Also available in:")))
            __M_writer('</h3>\n')
            for langname in translations.keys():
                if langname != lang and post.is_translation_available(langname):
                    __M_writer('                <p><a href="')
                    __M_writer(str(post.permalink(langname)))
                    __M_writer('" rel="alternate" hreflang="')
                    __M_writer(str(langname))
                    __M_writer('">')
                    __M_writer(str(messages("LANGUAGE", langname)))
                    __M_writer('</a></p>\n')
            __M_writer('        </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_sourcelink(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        messages = context.get('messages', UNDEFINED)
        post = context.get('post', UNDEFINED)
        show_sourcelink = context.get('show_sourcelink', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if show_sourcelink:
            __M_writer('        <p class="sourceline"><a href="')
            __M_writer(str(post.source_link()))
            __M_writer('" id="sourcelink">')
            __M_writer(str(messages("Source")))
            __M_writer('</a></p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_post_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        def html_translations(post):
            return render_html_translations(context,post)
        date_format = context.get('date_format', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        def html_sourcelink():
            return render_html_sourcelink(context)
        def html_title():
            return render_html_title(context)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <header>\n        ')
        __M_writer(str(html_title()))
        __M_writer('\n        <div class="metadata">\n            <p class="byline author vcard"><span class="byline-name fn">')
        __M_writer(str(post.author()))
        __M_writer('</span></p>\n            <p class="dateline"><a href="')
        __M_writer(str(post.permalink()))
        __M_writer('" rel="bookmark"><time class="published dt-published" datetime="')
        __M_writer(str(post.date.isoformat()))
        __M_writer('" itemprop="datePublished" title="')
        __M_writer(str(post.formatted_date(date_format)))
        __M_writer('">')
        __M_writer(str(post.formatted_date(date_format)))
        __M_writer('</time></a></p>\n')
        if not post.meta('nocomments') and site_has_comments:
            __M_writer('                <p class="commentline">')
            __M_writer(str(comments.comment_link(post.permalink(), post._base_path)))
            __M_writer('\n')
        __M_writer('            ')
        __M_writer(str(html_sourcelink()))
        __M_writer('\n')
        if post.meta('link'):
            __M_writer("                    <p><a href='")
            __M_writer(str(post.meta('link')))
            __M_writer("'>")
            __M_writer(str(messages("Original site")))
            __M_writer('</a></p>\n')
        if post.description():
            __M_writer('                <meta name="description" itemprop="description" content="')
            __M_writer(str(post.description()))
            __M_writer('">\n')
        __M_writer('        </div>\n        ')
        __M_writer(str(html_translations(post)))
        __M_writer('\n    </header>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        post = context.get('post', UNDEFINED)
        title = context.get('title', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if title and not post.meta('hidetitle'):
            __M_writer('    <h1 class="p-name entry-title" itemprop="headline name"><a href="')
            __M_writer(str(post.permalink()))
            __M_writer('" class="u-url">')
            __M_writer(filters.html_escape(str(title)))
            __M_writer('</a></h1>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "post_header.tmpl", "filename": "/usr/lib/python3.4/site-packages/nikola/data/themes/base/templates/post_header.tmpl", "line_map": {"128": 41, "129": 41, "130": 41, "131": 41, "132": 43, "133": 44, "134": 44, "135": 44, "136": 46, "137": 47, "138": 47, "144": 5, "22": 2, "151": 6, "152": 7, "25": 3, "154": 7, "155": 7, "28": 0, "150": 5, "33": 2, "34": 3, "35": 9, "36": 22, "37": 28, "38": 49, "156": 7, "44": 11, "52": 11, "53": 12, "54": 13, "55": 14, "56": 14, "57": 15, "58": 16, "59": 17, "60": 17, "61": 17, "62": 17, "63": 17, "64": 17, "65": 17, "66": 20, "72": 24, "162": 156, "79": 24, "80": 25, "81": 26, "82": 26, "83": 26, "84": 26, "85": 26, "153": 7, "91": 30, "106": 30, "107": 32, "108": 32, "109": 34, "110": 34, "111": 35, "112": 35, "113": 35, "114": 35, "115": 35, "116": 35, "117": 35, "118": 35, "119": 36, "120": 37, "121": 37, "122": 37, "123": 39, "124": 39, "125": 39, "126": 40, "127": 41}, "source_encoding": "utf-8"}
__M_END_METADATA
"""
