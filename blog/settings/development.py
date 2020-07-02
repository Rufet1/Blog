from blog.settings.base import * 

DEBUG = True

STATICFILES_DIRS= [
    os.path.join(BASE_DIR,'static')
    ]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles/')


CKEDITOR_BASEPATH = "/statlicfiles/ckeditor/ckeditor/"