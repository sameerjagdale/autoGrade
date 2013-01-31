import subprocess
import glob

def executeFile(fileName) :
        p=subprocess.Popen("./"+fileName.split(".")[0], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        #for lines in p.stdout.readlines() :
        #        print lines
	return p.stdout.readlines()
#end of executeFile 

	
def extractName(fileName):
	return fileName.split("_")[0]
	
	
def hasError(output,word):
	for line in output:
		if line.lower().find(word) >=0:
			return True
	return False
#end of hasError
def parseOutput(output,keywordFile) :
	try:
		fin=open(keywordFile,"r")
		count=0
		for keyword in fin.readlines():
			
			for line in output:
				
				if line.lower().strip().find(keyword.strip())>=0:
					count=count+1
					print keyword
					break
		fin.close()
		print "count="+str(count)
	except IOError:
		print "keyword file not found"
		return 0
	return count	
			
	
def assignScore(numKeys):
	if numKeys==0:
		return 80
	elif numKeys ==1:
		return 95
	elif numKeys ==2:
		return 95
	else:
		return 100
def writeToFile(student, score):
	fout=open("score.csv","a")
	fout.write(student+","+str(score)+"\n")
	
#start of script
i=1
listOfFiles=list()
listOfFiles=glob.glob("*.c");

for fileName  in listOfFiles:
	numKeys=0
	p=subprocess.Popen("gcc -o"+fileName.split('.')[0]+" "+fileName, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	output=p.stdout.readlines()	
	if not hasError(output,"error"):
		print "Successful compilation for "+ fileName 
		print "output: "
		output=executeFile(fileName)
		numKeys= parseOutput(output,"keyword.txt")
		print numKeys
		
	else :
		print "error in compilation for:"+fileName
	name=extractName(fileName)
	score=assignScore(numKeys)
	writeToFile(name,score)
		
retval = p.wait()
 # end of script

