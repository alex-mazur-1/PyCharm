import script1
import delete_key_pair


#describe instances
ec2 = boto3.client('ec2')
response = ec2.describe_instances(
    Filters=[
        {
            'key-name': 'EC2',
        },
    ],
    InstanceIds=[
        'string',
    ],
    DryRun=True,
    MaxResults=123,
    NextToken='string'
)

if DryRun == True:
    print(delete-key-pair)


for i in range(whatever):
    script1.some_function(i)

# Визвати на пряму
# modulename.main()

import subprocess
subprocess.Popen("script2.py 1", shell=True)


import subprocess
cmd = 'python script.py'

p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
out, err = p.communicate()
result = out.split('\n')
for lin in result:
    if not lin.startswith('#'):
        print(lin)

print ("Please, enter time in seconds:")
waitime=input()
cmd = 'shutdown -s -t ' +str(waitime)
import subprocess
PIPE = subprocess.PIPE
p = subprocess.Popen(cmd, shell = True)











def main(arg1, arg2, etc):
    # do whatever the script does


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])