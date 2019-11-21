import subprocess

def main():
    path = 'Programs/'
    while(1):
        instr = input("[L]ist Programs, [R]un program, [C]lear, [E]nd it: ")
        
        if(str.lower(instr) == 'e'):
            return 0

        if(str.lower(instr) == 'c'):
            subprocess.run('clear')
            
        if(str.lower(instr) == 'l'):
            subprocess.run(['ls', 'Programs'])
            
        if(str.lower(instr) == 'r'):
            programName = input("What Program?:")
            programLoc = path + programName
            if '.py' in programName:
                subprocess.run(['python3', programLoc])
                
            if  '.cpp' in programName:
                subprocess.run(['g++', programLoc])
                subprocess.run('./a.out')
                subprocess.run(['rm','a.out'])


main()
