# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1422090314.053742
_enable_loop = True
_template_filename = 'themes/bootstrap3/templates/base_helper.tmpl'
_template_uri = 'base_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_translations', 'html_navigation_links', 'html_feedlinks', 'html_headstart', 'html_stylesheets', 'late_load_js']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _link = context.get('_link', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        for langname in translations.keys():
            if langname != lang:
                __M_writer('            <li><a href="')
                __M_writer(str(_link("index", None, langname)))
                __M_writer('" rel="alternate" hreflang="')
                __M_writer(str(langname))
                __M_writer('">')
                __M_writer(str(messages("LANGUAGE", langname)))
                __M_writer('</a></li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_navigation_links(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        tuple = context.get('tuple', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        rel_link = context.get('rel_link', UNDEFINED)
        isinstance = context.get('isinstance', UNDEFINED)
        navigation_links = context.get('navigation_links', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        for url, text in navigation_links[lang]:
            if isinstance(url, tuple):
                __M_writer('            <li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown">')
                __M_writer(str(text))
                __M_writer('<b class="caret"></b></a>\n            <ul class="dropdown-menu">\n')
                for suburl, text in url:
                    if rel_link(permalink, suburl) == "#":
                        __M_writer('                    <li class="active"><a href="')
                        __M_writer(str(permalink))
                        __M_writer('">')
                        __M_writer(str(text))
                        __M_writer('</a>\n')
                    else:
                        __M_writer('                    <li><a href="')
                        __M_writer(str(suburl))
                        __M_writer('">')
                        __M_writer(str(text))
                        __M_writer('</a>\n')
                __M_writer('            </ul>\n')
            else:
                if rel_link(permalink, url) == "#":
                    __M_writer('                <li class="active"><a href="')
                    __M_writer(str(permalink))
                    __M_writer('">')
                    __M_writer(str(text))
                    __M_writer('</a>\n')
                else:
                    __M_writer('                <li><a href="')
                    __M_writer(str(url))
                    __M_writer('">')
                    __M_writer(str(text))
                    __M_writer('</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_feedlinks(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        generate_rss = context.get('generate_rss', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        rss_link = context.get('rss_link', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if rss_link:
            __M_writer('        ')
            __M_writer(str(rss_link))
            __M_writer('\n')
        elif generate_rss:
            if len(translations) > 1:
                for language in translations:
                    __M_writer('                <link rel="alternate" type="application/rss+xml" title="RSS (')
                    __M_writer(str(language))
                    __M_writer(')" href="')
                    __M_writer(str(_link('rss', None, language)))
                    __M_writer('">\n')
            else:
                __M_writer('            <link rel="alternate" type="application/rss+xml" title="RSS" href="')
                __M_writer(str(_link('rss', None)))
                __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_headstart(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        def html_stylesheets():
            return render_html_stylesheets(context)
        title = context.get('title', UNDEFINED)
        def html_feedlinks():
            return render_html_feedlinks(context)
        blog_title = context.get('blog_title', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
        extra_head_data = context.get('extra_head_data', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        striphtml = context.get('striphtml', UNDEFINED)
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        url_replacer = context.get('url_replacer', UNDEFINED)
        mathjax_config = context.get('mathjax_config', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        prevlink = context.get('prevlink', UNDEFINED)
        description = context.get('description', UNDEFINED)
        comment_system = context.get('comment_system', UNDEFINED)
        favicons = context.get('favicons', UNDEFINED)
        use_open_graph = context.get('use_open_graph', UNDEFINED)
        is_rtl = context.get('is_rtl', UNDEFINED)
        twitter_card = context.get('twitter_card', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<!DOCTYPE html>\n<html\n')
        if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']) or (comment_system == 'facebook'):
            __M_writer("prefix='")
            if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']):
                __M_writer('og: http://ogp.me/ns# ')
            if use_open_graph:
                __M_writer('article: http://ogp.me/ns/article# ')
            if comment_system == 'facebook':
                __M_writer('fb: http://ogp.me/ns/fb# ')
            __M_writer("'")
        if is_rtl:
            __M_writer('dir="rtl" ')
        __M_writer('lang="')
        __M_writer(str(lang))
        __M_writer('">\n    <head>\n    <meta charset="utf-8">\n')
        if description:
            __M_writer('    <meta name="description" content="')
            __M_writer(str(description))
            __M_writer('">\n')
        __M_writer('    <meta name="viewport" content="width=device-width, initial-scale=1">\n    <title>')
        __M_writer(striphtml(str(title)))
        __M_writer(' | ')
        __M_writer(striphtml(str(blog_title)))
        __M_writer('</title>\n\n    ')
        __M_writer(str(html_stylesheets()))
        __M_writer('\n    ')
        __M_writer(str(html_feedlinks()))
        __M_writer('\n')
        if permalink:
            __M_writer('      <link rel="canonical" href="')
            __M_writer(str(abs_link(permalink)))
            __M_writer('">\n')
        __M_writer('\n')
        if favicons:
            for name, file, size in favicons:
                __M_writer('            <link rel="')
                __M_writer(str(name))
                __M_writer('" href="')
                __M_writer(str(file))
                __M_writer('" sizes="')
                __M_writer(str(size))
                __M_writer('"/>\n')
        __M_writer('\n')
        if comment_system == 'facebook':
            __M_writer('        <meta property="fb:app_id" content="')
            __M_writer(str(comment_system_id))
            __M_writer('">\n')
        __M_writer('\n')
        if prevlink:
            __M_writer('        <link rel="prev" href="')
            __M_writer(str(prevlink))
            __M_writer('" type="text/html">\n')
        if nextlink:
            __M_writer('        <link rel="next" href="')
            __M_writer(str(nextlink))
            __M_writer('" type="text/html">\n')
        __M_writer('\n    ')
        __M_writer(str(mathjax_config))
        __M_writer('\n')
        if use_cdn:
            __M_writer('        <!--[if lt IE 9]><script src="//html5shim.googlecode.com/svn/trunk/html5.js"></script><![endif]-->\n')
        else:
            __M_writer('        <!--[if lt IE 9]><script src="')
            __M_writer(str(url_replacer(permalink, '/assets/js/html5.js', lang)))
            __M_writer('"></script><![endif]-->\n')
        __M_writer('\n    ')
        __M_writer(str(extra_head_data))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        use_cdn = context.get('use_cdn', UNDEFINED)
        annotations = context.get('annotations', UNDEFINED)
        has_custom_css = context.get('has_custom_css', UNDEFINED)
        use_bundles = context.get('use_bundles', UNDEFINED)
        notes = context.get('notes', UNDEFINED)
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if use_bundles:
            if use_cdn:
                __M_writer('            <link href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.0/css/bootstrap.min.css" rel="stylesheet">\n            <link href="/assets/css/all.css" rel="stylesheet" type="text/css">\n')
            else:
                __M_writer('            <link href="/assets/css/all-nocdn.css" rel="stylesheet" type="text/css">\n')
        else:
            if use_cdn:
                __M_writer('            <link href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.0/css/bootstrap.min.css" rel="stylesheet">\n')
            else:
                __M_writer('            <link href="/assets/css/bootstrap.min.css" rel="stylesheet" type="text/css">\n')
            __M_writer('        <link href="/assets/css/rst.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/code.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/colorbox.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/theme.css" rel="stylesheet" type="text/css">\n')
            if has_custom_css:
                __M_writer('            <link href="/assets/css/custom.css" rel="stylesheet" type="text/css">\n')
        if annotations and post and not post.meta('noannotations'):
            __M_writer('        ')
            __M_writer(str(notes.css()))
            __M_writer('\n')
        elif not annotations and post and post.meta('annotations'):
            __M_writer('        ')
            __M_writer(str(notes.css()))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_load_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        use_cdn = context.get('use_cdn', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        use_bundles = context.get('use_bundles', UNDEFINED)
        colorbox_locales = context.get('colorbox_locales', UNDEFINED)
        social_buttons_code = context.get('social_buttons_code', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if use_bundles:
            if use_cdn:
                __M_writer('            <script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>\n            <script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.0/js/bootstrap.min.js"></script>\n            <script src="/assets/js/all.js"></script>\n')
            else:
                __M_writer('            <script src="/assets/js/all-nocdn.js"></script>\n')
        else:
            if use_cdn:
                __M_writer('            <script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>\n            <script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.0/js/bootstrap.min.js"></script>\n')
            else:
                __M_writer('            <script src="/assets/js/jquery.min.js"></script>\n            <script src="/assets/js/bootstrap.min.js"></script>\n            <script src="/assets/js/moment-with-locales.min.js"></script>\n            <script src="/assets/js/fancydates.js"></script>\n')
            __M_writer('        <script src="/assets/js/jquery.colorbox-min.js"></script>\n')
        if colorbox_locales[lang]:
            __M_writer('        <script src="/assets/js/colorbox-i18n/jquery.colorbox-')
            __M_writer(str(colorbox_locales[lang]))
            __M_writer('.js"></script>\n')
        __M_writer('    ')
        __M_writer(str(social_buttons_code))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"15": 0, "20": 2, "21": 65, "22": 92, "23": 122, "24": 145, "25": 159, "26": 167, "32": 161, "40": 161, "41": 162, "42": 163, "43": 164, "44": 164, "45": 164, "46": 164, "47": 164, "48": 164, "49": 164, "55": 124, "65": 124, "66": 125, "67": 126, "68": 127, "69": 127, "70": 127, "71": 129, "72": 130, "73": 131, "74": 131, "75": 131, "76": 131, "77": 131, "78": 132, "79": 133, "80": 133, "81": 133, "82": 133, "83": 133, "84": 136, "85": 137, "86": 138, "87": 139, "88": 139, "89": 139, "90": 139, "91": 139, "92": 140, "93": 141, "94": 141, "95": 141, "96": 141, "97": 141, "103": 147, "112": 147, "113": 148, "114": 149, "115": 149, "116": 149, "117": 150, "118": 151, "119": 152, "120": 153, "121": 153, "122": 153, "123": 153, "124": 153, "125": 155, "126": 156, "127": 156, "128": 156, "134": 3, "161": 3, "162": 7, "163": 8, "164": 9, "165": 10, "166": 12, "167": 13, "168": 15, "169": 16, "170": 18, "171": 21, "172": 22, "173": 25, "174": 25, "175": 25, "176": 28, "177": 29, "178": 29, "179": 29, "180": 31, "181": 32, "182": 32, "183": 32, "184": 32, "185": 34, "186": 34, "187": 35, "188": 35, "189": 36, "190": 37, "191": 37, "192": 37, "193": 39, "194": 40, "195": 41, "196": 42, "197": 42, "198": 42, "199": 42, "200": 42, "201": 42, "202": 42, "203": 45, "204": 46, "205": 47, "206": 47, "207": 47, "208": 49, "209": 50, "210": 51, "211": 51, "212": 51, "213": 53, "214": 54, "215": 54, "216": 54, "217": 56, "218": 57, "219": 57, "220": 58, "221": 59, "222": 60, "223": 61, "224": 61, "225": 61, "226": 63, "227": 64, "228": 64, "234": 95, "244": 95, "245": 96, "246": 97, "247": 98, "248": 100, "249": 101, "250": 103, "251": 104, "252": 105, "253": 106, "254": 107, "255": 109, "256": 113, "257": 114, "258": 117, "259": 118, "260": 118, "261": 118, "262": 119, "263": 120, "264": 120, "265": 120, "271": 67, "280": 67, "281": 68, "282": 69, "283": 70, "284": 73, "285": 74, "286": 76, "287": 77, "288": 78, "289": 80, "290": 81, "291": 86, "292": 88, "293": 89, "294": 89, "295": 89, "296": 91, "297": 91, "298": 91, "304": 298}, "uri": "base_helper.tmpl", "source_encoding": "utf-8", "filename": "themes/bootstrap3/templates/base_helper.tmpl"}
__M_END_METADATA
"""
