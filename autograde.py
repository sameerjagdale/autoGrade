import subprocess
import glob
import datetime
import os
#start of executeFile . Function executes compiled file and return output
def executeFile(fileName) :
        p=subprocess.Popen("./a.out", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	return p.stdout.readlines()
#end of executeFile 

# start of extract name. Function extracts student name from the file name passed as an argument. 	
def extractName(fileName):
	return fileName.split("-")[0]
#end of extractName 

#start of writeToLog. Writes given message to log after appending date and time 
def writeToLog(message):
	fout=open("log.txt","a")
	fout.write(str(datetime.datetime.now())+":"+message+ "\n")
#end of writeToLog

#start of hasError. Checks for error based on given keyword	
def hasError(output,word):
	for line in output:
		if line.lower().find(word) >=0:
			return True
	return False
#end of hasError
def remSpace(fileName):
	lst=fileName.split(" ")
	newFileName="".join(lst)
	os.rename(fileName,newFileName)
	return newFileName
#start of parseOutput.parses output for keywords present  in the file . 
def parseOutput(output,keywordFile) :
	try:
		fin=open(keywordFile,"r")
		count=0
		for keyword in fin.readlines():
			
			for line in output:
				if line.lower().strip().find(keyword.lower().strip())>=0:
					count=count+1
					
					break
			
		fin.close()
		
	except IOError:
		print "keyword file not found"
		return 0
	return count	
#end of parseOutput		
#start of parseSource
def parseSource(sourceFile,keywordFile):
	try:
		fin=open(sourceFile,"r")
		keyfile=open(keywordFile,"r")
		source=fin.read()
		count=0
		for key in keyfile.readlines():
			if source.strip().lower().find(key.strip().lower())>=0:
				count=count+1
		print "for file"+sourceFile+ str(count)
	except IOError:
		print "file not found"
		return 0
	return count
#start of assignScore. assigns scores on the basis of number of keywords found. 
def assignScore(numKeys):
	if numKeys==0:
		return 80
	#elif numKeys ==1:
	#	return 95
	#elif numKeys ==2:
	#	return 100
	else:
		return 100
#end of assignscore
		
#writes score to file.
def writeToFile(student, score):
	fout=open("score.csv","a")
	fout.write(student+","+str(score)+"\n")
	
#end of writeToFile
#start of script
i=1
listOfFiles=list()
listOfFiles=glob.glob("*.c");


for fileName  in listOfFiles:
	numKeys=0
	print fileName
	newFileName=remSpace(fileName)
	p=subprocess.Popen("gcc" +" "+newFileName.strip(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	output=p.stdout.readlines()	
	if not hasError(output,"error"):
	
		writeToLog("Successful compilation for "+ fileName) 
		output=executeFile(fileName)
		numKeys= parseOutput(output,"keyword.txt")
		#numKeys=parseSource(newFileName,"srcKeyword.txt")
		writeToLog("in file " +fileName+" number of keywords found = "+str(numKeys))
		print numKeys
	else :
		writeToLog("error in compilation for:"+fileName)
		#print output
		#break
	name=extractName(fileName)
	score=assignScore(numKeys)
	print score
	writeToFile(name.strip(),score)
		
retval = p.wait()
 # end of script

