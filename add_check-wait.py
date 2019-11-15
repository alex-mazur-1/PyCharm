import boto
#import boto.ec2
import time



conn.create_tags([instance.id], {"Name":"bogo-instance"})
while instance.state == u'pending':
    print "Instance state: %s" % instance.state
    time.sleep(10)
    instance.update()

print "Instance state: %s" % instance.state
