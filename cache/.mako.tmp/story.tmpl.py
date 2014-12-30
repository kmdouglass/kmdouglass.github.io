# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1419977094.2107399
_enable_loop = True
_template_filename = '/usr/lib/python3.4/site-packages/nikola/data/themes/base/templates/story.tmpl'
_template_uri = 'story.tmpl'
_source_encoding = 'utf-8'
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('pheader', context._clean_inheritance_tokens(), templateuri='post_header.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'pheader')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'post.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        post = context.get('post', UNDEFINED)
        pheader = _mako_get_namespace(context, 'pheader')
        def content():
            return render_content(context._locals(__M_locals))
        comments = _mako_get_namespace(context, 'comments')
        helper = _mako_get_namespace(context, 'helper')
        enable_comments = context.get('enable_comments', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
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
        post = context.get('post', UNDEFINED)
        pheader = _mako_get_namespace(context, 'pheader')
        def content():
            return render_content(context)
        comments = _mako_get_namespace(context, 'comments')
        helper = _mako_get_namespace(context, 'helper')
        enable_comments = context.get('enable_comments', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<article class="storypage" itemscope="itemscope" itemtype="http://schema.org/Article">\n    <header>\n        ')
        __M_writer(str(pheader.html_title()))
        __M_writer('\n        ')
        __M_writer(str(pheader.html_translations(post)))
        __M_writer('\n    </header>\n    <div class="e-content entry-content" itemprop="articleBody text">\n    ')
        __M_writer(str(post.text()))
        __M_writer('\n    </div>\n')
        if site_has_comments and enable_comments and not post.meta('nocomments'):
            __M_writer('        <section class="comments">\n        <h2>')
            __M_writer(str(messages("Comments")))
            __M_writer('</h2>\n        ')
            __M_writer(str(comments.comment_form(post.permalink(absolute=True), post.title(), post.base_path)))
            __M_writer('\n        </section>\n')
        __M_writer('    ')
        __M_writer(str(helper.mathjax_script(post)))
        __M_writer('\n</article>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/usr/lib/python3.4/site-packages/nikola/data/themes/base/templates/story.tmpl", "uri": "story.tmpl", "source_encoding": "utf-8", "line_map": {"86": 19, "75": 7, "76": 10, "77": 10, "78": 11, "79": 11, "80": 14, "81": 14, "82": 16, "83": 17, "84": 18, "85": 18, "22": 4, "87": 19, "88": 22, "25": 2, "90": 22, "28": 3, "96": 90, "34": 0, "48": 2, "49": 3, "50": 4, "51": 5, "89": 22, "56": 24, "62": 7}}
__M_END_METADATA
"""
