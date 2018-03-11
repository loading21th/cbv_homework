from django.db import  models
import os

def get_file_path(instance,filename):
    file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),'uploadfile',instance.schoolname,instance.classname,filename)
    print(instance.schoolname)
    print(instance.classname)
    print(file_path)
    return file_path
class Homewore_Courseware(models.Model):
    schoolname = models.CharField(max_length=40)
    classname = models.CharField(max_length=40)
    homework = models.FileField(upload_to=get_file_path)
    class Meta:
        app_label = "fileup"

