# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1421827171.4473293
_enable_loop = True
_template_filename = '/usr/lib/python3.4/site-packages/nikola/data/themes/base/templates/comments_helper_disqus.tmpl'
_template_uri = 'comments_helper_disqus.tmpl'
_source_encoding = 'utf-8'
_exports = ['comment_link_script', 'comment_form', 'comment_link']


import json 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link_script(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if comment_system_id:
            __M_writer('       <script>var disqus_shortname="')
            __M_writer(str(comment_system_id))
            __M_writer('";(function(){var a=document.createElement("script");a.async=true;a.src="//"+disqus_shortname+".disqus.com/count.js";(document.getElementsByTagName("head")[0]||document.getElementsByTagName("body")[0]).appendChild(a)}());</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_form(context,url,title,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if comment_system_id:
            __M_writer('        <div id="disqus_thread"></div>\n        <script>\n        var disqus_shortname ="')
            __M_writer(str(comment_system_id))
            __M_writer('",\n')
            if url:
                __M_writer('            disqus_url="')
                __M_writer(str(url))
                __M_writer('",\n')
            __M_writer('        disqus_title=')
            __M_writer(str(json.dumps(title)))
            __M_writer(',\n        disqus_identifier="')
            __M_writer(str(identifier))
            __M_writer('",\n        disqus_config = function () {\n')
            if lang == 'es':
                __M_writer('            this.language = "es_ES";\n')
            else:
                __M_writer('            this.language = "')
                __M_writer(str(lang))
                __M_writer('";\n')
            __M_writer('        };\n        (function() {\n            var dsq = document.createElement(\'script\'); dsq.async = true;\n            dsq.src = \'//\' + disqus_shortname + \'.disqus.com/embed.js\';\n            (document.getElementsByTagName(\'head\')[0] || document.getElementsByTagName(\'body\')[0]).appendChild(dsq);\n        })();\n    </script>\n    <noscript>Please enable JavaScript to view the <a href="//disqus.com/?ref_noscript" rel="nofollow">comments powered by Disqus.</a></noscript>\n    <a href="//disqus.com" class="dsq-brlink" rel="nofollow">Comments powered by <span class="logo-disqus">Disqus</span></a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link(context,link,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if comment_system_id:
            __M_writer('    <a href="')
            __M_writer(str(link))
            __M_writer('#disqus_thread" data-disqus-identifier="')
            __M_writer(str(identifier))
            __M_writer('">Comments</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"15": 3, "17": 0, "22": 2, "23": 3, "24": 31, "25": 37, "26": 44, "32": 40, "37": 40, "38": 41, "39": 42, "40": 42, "41": 42, "47": 5, "53": 5, "54": 6, "55": 7, "56": 9, "57": 9, "58": 10, "59": 11, "60": 11, "61": 11, "62": 13, "63": 13, "64": 13, "65": 14, "66": 14, "67": 16, "68": 17, "69": 18, "70": 19, "71": 19, "72": 19, "73": 21, "79": 33, "84": 33, "85": 34, "86": 35, "87": 35, "88": 35, "89": 35, "90": 35, "96": 90}, "uri": "comments_helper_disqus.tmpl", "filename": "/usr/lib/python3.4/site-packages/nikola/data/themes/base/templates/comments_helper_disqus.tmpl", "source_encoding": "utf-8"}
__M_END_METADATA
"""
