# Django XSS Escape in Templates

During my research to compare four modern web frameworks in their security protections, I noticed Django does not provide context-based escaping for XSS protection in templates by default. This is a Proof-of-concept how something like this _could_ look like. However, since this has not been extensively tested and validated, use it at your own risk.

Similar tools exist for other frameworks, such as escape (https://github.com/laravelgems/escape) and blade-escape (https://github.com/laravelgems/blade-escape) for Laravel. 
On the one hand, this is an implementation of the escaping based on important page contexts, and also an
extension to Django's templating system to allow for easy integration of escaping in templates.

The most important files:
- ```xss_sample/templatetags/xss_escape.py``` -> new template tags for Django to escape based on context
- ```templates/xss_sample/index.html``` -> A sample template that uses those template tags
- ```xss_sample/views.py``` -> Defines the variables passed to the template
- ```fullproject/settings.py``` -> Showing how to properly add templatetags/xss_escape.py to any Django Project

The xss_escape can be added to existing project by doing the following:
1. Add the "templatetags"-folder if it does not exist. Create an empty ```__init__.py``` file inside.
2. Copy xss_escape.py into this folder.
3. In the setting.py file of the project, add under TEMPLATES -> "libraries" as
```
'xss_escape': 'YOUR_APP_NAME.templatetags.xss_escape'
```
This is the sourcecode of a simple Django-App, that once launched by 
```py manage.py runserver```
can be accessed under http://127.0.0.1:8000/xss_sample/ to display the index.html template with proper escaping.

The escaping is based on OWASP rules for XSS Prevention:
https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html
