During my research to compare four modern web frameworks in their security protections, I was unable to find
a django extension that provides context-based escaping for XSS protection in templates.

This is a proof-of-concept of how something like this could look like. Similar tools exist for other frameworks,
such as escape (https://github.com/laravelgems/escape) and blade-escape (https://github.com/laravelgems/blade-escape)
for Laravel. On the one hand, this is an implementation of the escaping based on important page contexts, and also an
extension to Django's templating system to allow for easy integration of escaping in templates.

The xss_escape can be added to existing project by doing the following:
1. Add the "templatetags"-folder if it does not exist. Create an "__init__.py" file inside.
2. Copy the xss_escape into this folder.
3. In the setting.py file of the project, add under TEMPLATES -> "libraries" as
'xss_escape': 'YOUR_APP_NAME.templatetags.xss_escape'

This is the sourcecode of a simple Django-App, that once launched by "py manage.py runserver"
can be accessed under http://127.0.0.1:8000/xss_sample/ to display the index.html template with proper escaping.

The most important files:
- xss_sample/templatetags/xss_escape.py -> new template tags for Django to escape based on context
- templates/xss_sample/index.html -> A sample template that uses those template tags
- xss_sample/views.py -> Defines the variables passed to the template
- fullprojects/settings.py -> Showing how to properly add templatetags/xss_escape.py to any Django Project

The escaping is based on OWASP rules for XSS Prevention:
https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html
