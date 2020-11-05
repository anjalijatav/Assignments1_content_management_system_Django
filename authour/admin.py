from django.contrib import admin
#todo user name - authour
#todo paswword - admin123456
# Register your models here.
from django.contrib import admin
from authour.userfield import UserfieldManager,Userfield
from authour.contentfield  import Contentfield,ContentfieldManager
admin.site.register(Userfield)
admin.site.register(Contentfield)
# admin.site.register(UserfieldManager)
# admin.site.register(ContentfieldManager)