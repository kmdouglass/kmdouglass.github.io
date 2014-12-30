# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1419976170.3986995
_enable_loop = True
_template_filename = '/usr/lib/python3.4/site-packages/nikola/data/themes/base/templates/comments_helper_facebook.tmpl'
_template_uri = 'comments_helper_facebook.tmpl'
_source_encoding = 'utf-8'
_exports = ['comment_link', 'comment_form', 'comment_link_script']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link(context,link,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('\n<span class="fb-comments-count" data-url="')
        __M_writer(str(link))
        __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_form(context,url,title,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<div id="fb-root"></div>\n<script>\n  window.fbAsyncInit = function() {\n    // init the FB JS SDK\n    FB.init({\n      appId      : \'')
        __M_writer(str(comment_system_id))
        __M_writer('\',\n      status     : true,\n      xfbml      : true\n    });\n\n  };\n\n  // Load the SDK asynchronously\n  (function(d, s, id){\n     var js, fjs = d.getElementsByTagName(s)[0];\n     if (d.getElementById(id)) {return;}\n     js = d.createElement(s); js.id = id;\n     js.src = "//connect.facebook.net/en_US/all.js";\n     fjs.parentNode.insertBefore(js, fjs);\n   }(document, \'script\', \'facebook-jssdk\'));\n</script>\n\n<div class="fb-comments" data-href="')
        __M_writer(str(url))
        __M_writer('" data-width="470"></div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link_script(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<div id="fb-root"></div>\n<script>\n    // thank lxml for this\n    $(\'.fb-comments-count\').each(function(i, obj) {\n        var url = obj.attributes[\'data-url\'].value;\n        // change here if you dislike the default way of displaying\n        // this\n        obj.innerHTML = \'<fb:comments-count href="\' + url + \'"></fb:comments-count> comments\';\n    });\n\n  window.fbAsyncInit = function() {\n    // init the FB JS SDK\n    FB.init({\n      appId      : \'')
        __M_writer(str(comment_system_id))
        __M_writer('\',\n      status     : true,\n      xfbml      : true\n    });\n\n  };\n\n  // Load the SDK asynchronously\n  (function(d, s, id){\n     var js, fjs = d.getElementsByTagName(s)[0];\n     if (d.getElementById(id)) {return;}\n     js = d.createElement(s); js.id = id;\n     js.src = "//connect.facebook.net/en_US/all.js";\n     fjs.parentNode.insertBefore(js, fjs);\n   }(document, \'script\', \'facebook-jssdk\'));\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "comments_helper_facebook.tmpl", "line_map": {"32": 28, "33": 29, "34": 29, "68": 62, "40": 2, "60": 32, "45": 2, "46": 8, "15": 0, "48": 25, "49": 25, "20": 26, "21": 30, "22": 62, "55": 32, "47": 8, "28": 28, "61": 46, "62": 46}, "source_encoding": "utf-8", "filename": "/usr/lib/python3.4/site-packages/nikola/data/themes/base/templates/comments_helper_facebook.tmpl"}
__M_END_METADATA
"""
