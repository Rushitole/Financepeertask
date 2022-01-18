from django.db import models
import json
# Create your models here.
class PostData(models.Model):
    id = models.AutoField(primary_key=True)
    userId =  models.IntegerField(default=0)
    title = models.CharField(max_length=200)
    body = models.TextField()

    def _str_(self):
        return self.title


class FileModel(models.Model):
    uploaded_file = models.FileField(upload_to='uploads/')

    def _str_(self):
        return self.uploaded_file.name
    
    def save(self, *args, **kwargs):
        super(FileModel, self).save(*args, **kwargs)
        with open(self.uploaded_file.path) as json_file:
            try:
                data = json.load(json_file)
                for p in data:
                    if p.get('id') and p.get('userId') and p.get('title') and p.get('body'): # check if all the fields are present
                        try:
                            PostData.objects.update_or_create( id=p['id'], userId=p['userId'], title=p['title'], body=p['body'])
                        except Exception as e:
                            print("EXCEPTION OCCURED WHILE INSERTING DATA: ", e)
            except Exception as e:
                print(e)  # We can utilize this place for post validation
                pass
        return self        