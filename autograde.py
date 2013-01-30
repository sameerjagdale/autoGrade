import subprocess
import glob

def executeFile(fileName) :
        p=subprocess.Popen("./"+item.split(".")[0], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for lines in p.stdout.readlines() :
                print lines
#end if executeFile 
#def extractName(fileName):
def hasError(output):
	for line in output:
		if line.find("error") >=0:
			return True
	return False

#end of hasError

#start of script
i=1
listOfFiles=list()
listOfFiles=glob.glob("*.c");
  
for item  in listOfFiles:

	p=subprocess.Popen("gcc -o"+item.split('.')[0]+" "+item, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
output=p.stdout.readlines()
if not hasError(output):
	
	executeFile(item)
else :
	print "error in compilation"
retval = p.wait()
 # end of script

