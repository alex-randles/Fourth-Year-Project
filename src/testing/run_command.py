## Script to run a command without speaking text
## Command is passed as a command line argument 
import sys, os 
commandScripts = {"$HOME/projectSourceCode/commandScripts/jokeCommand/jokes.py" : (["joke"],"Telling a joke   ") , ##script : (keywords for command, prompt to user)
                   "$HOME/projectSourceCode/commandScripts/weatherCommand/getWeather.sh" : (["weather"],"Telling the weather   "),
                   "$HOME/projectSourceCode/commandScripts/timeCommand/time.py" : (["time"], "Telling the time  "),
                   "$HOME/projectSourceCode/commandScripts/translationCommand/translateV2.py" : (["translate"], ""),
                   "$HOME/projectSourceCode/commandScripts/newsCommand/getNewsV2.py" : (["news"],"The news headlines for today are   "),
                   "$HOME/projectSourceCode/commandScripts/sportsCommand/getSportsV2.py" : (["sport","sports"], "Telling the sports headlines for today are  "),
                   "$HOME/projectSourceCode/commandScripts/tvCommand/turn_On.py" : (["tv","on"],"Turning the tv on   "),
                   "$HOME/projectSourceCode/commandScripts/musicCommand/playMusicV2.py dj dove illusion" : (["music"], ""),

                }
                
def runCommand(userKeyWords):
   for script in commandScripts.keys():
       commandKeyWords = commandScripts[script][0] 
       if (set(userKeyWords).issubset(commandKeyWords)) == True:
           os.system("python3 " + script) 

       
if __name__ == "__main__":
    keywords = sys.argv[1:] 
    print(keywords) 
    runCommand(keywords) 
       
    
