# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1421223072.5879214
_enable_loop = True
_template_filename = '/usr/lib/python3.4/site-packages/nikola/data/themes/base/templates/comments_helper_intensedebate.tmpl'
_template_uri = 'comments_helper_intensedebate.tmpl'
_source_encoding = 'utf-8'
_exports = ['comment_form', 'comment_link_script', 'comment_link']


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


def render_comment_form(context,url,title,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer("\n<script>\nvar idcomments_acct = '")
        __M_writer(str(comment_system_id))
        __M_writer('\';\nvar idcomments_post_id = "')
        __M_writer(str(identifier))
        __M_writer('";\nvar idcomments_post_url = "')
        __M_writer(str(url))
        __M_writer('";\n</script>\n<span id="IDCommentsPostTitle" style="display:none"></span>\n<script src=\'http://www.intensedebate.com/js/genericCommentWrapperV2.js\'></script>\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link_script(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link(context,link,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<a href="{link}" onclick="this.href=\'')
        __M_writer(str(link))
        __M_writer('\'; this.target=\'_self\';"><span class=\'IDCommentsReplace\' style=\'display:none\'>')
        __M_writer(str(identifier))
        __M_writer("</span>\n<script>\nvar idcomments_acct = '")
        __M_writer(str(comment_system_id))
        __M_writer('\';\nvar idcomments_post_id = "')
        __M_writer(str(identifier))
        __M_writer('";\nvar idcomments_post_url = "')
        __M_writer(str(link))
        __M_writer('";\n</script>\n<script src="http://www.intensedebate.com/js/genericLinkWrapperV2.js"></script>\n</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/usr/lib/python3.4/site-packages/nikola/data/themes/base/templates/comments_helper_intensedebate.tmpl", "uri": "comments_helper_intensedebate.tmpl", "source_encoding": "utf-8", "line_map": {"64": 14, "65": 16, "66": 16, "67": 17, "68": 17, "69": 18, "70": 18, "76": 70, "15": 0, "20": 11, "21": 22, "22": 25, "28": 2, "33": 2, "34": 4, "35": 4, "36": 5, "37": 5, "38": 6, "39": 6, "45": 24, "49": 24, "55": 13, "60": 13, "61": 14, "62": 14, "63": 14}}
__M_END_METADATA
"""
