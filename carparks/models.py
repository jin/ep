from django.db import models



class Cluster(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    

    def __unicode__(self):
        return self.name



class Node(models.Model):
    cluster = models.ForeignKey(Cluster) 
    node = models.IntegerField()
    

    def __unicode__(self):
        return str(self.node)



class Measurement(models.Model):
    node = models.ForeignKey(Node)
    raw_reading = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    

    def isTaken(self):
        if self.raw_reading <= 150:
            #return True
            return "Taken"
        else:
            #return False
            return "Empty"


    def __unicode__(self):
        return str(self.node)


    class Meta:
        ordering = ['-created']
