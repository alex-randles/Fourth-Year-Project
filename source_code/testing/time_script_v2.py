## This will time the script passed as a command line argument to it 
## Fixes new directory issue
import os,sys 
from datetime import datetime


def timeScript(scriptName):
      ## run the script all scripts will be in projectSourceCode folder 
      print(scriptName) 
      scriptExtension = scriptName[-2] 
      ## current time 
      startTime = datetime.now()
      if scriptExtension == "sh":
	    os.system("$HOME/2019-ca400-randlea2/src/commandScripts/" + scriptName) 
      else:
	    os.system("python $HOME/2019-ca400-randlea2/src/commandScripts/" + scriptName) 

      ## print result 
      timeTaken  = datetime.now() - startTime
      result = "The script took {} to execute".format(timeTaken)  
      print(result) 
      ## record time in executionTimeResults.txt 
      recordTime(timeTaken,scriptName)
      
def recordTime(timeTaken,scriptName):
      fileName = "executionTimeResults.txt"
      f = open(fileName,"a") 
      f.write("Script: $HOME/2019-ca400-randlea2/src/commandScripts/{} took {} seconds to execute\n".format(scriptName,timeTaken)) 

if __name__ == "__main__":
	userInput = sys.argv[1:] 
	userInput = " ".join(userInput) 
	## change into files directory to access resources 
	#directoryName = userInput.split("/")[0] 
	#path = "$HOME/projectSourceCode/commandScripts/" + directoryName
	#print(path) 
	#os.chdir(path) 
	#os.system("pwd")  
	timeScript(userInput) 
