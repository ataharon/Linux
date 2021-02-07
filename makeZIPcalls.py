#generates file of ZIP|# of non-severe calls
#input: reduced EMS file (2019 or 2020)
#output: results file
import sys

def main():
    #initialize dictionary
    dict  = {}

    #read input file
    line = sys.stdin.readline()

    #for each record in the EMS data
    while line:
        fields = line.split("\t") #split into fields
        zipcode = fields[21] #zip code
        try: severity = int(fields[3]) #severity level code (1-9, 1 being most severe)
        except: severity = 0

        #tally:
        #if the record is a non-severe call
        if severity > 4:
            #if the zip code is not yet in the dictionary,
            #add a new key
            if not(zipcode in dict):
                dict[zipcode] = 1
            #if it is in the dictionary, add 1
            else:
                dict[zipcode]+=1

        #read the next line
        line = sys.stdin.readline()

    #for each ZIP in the dict, output
    #ZIP|# non-severe calls
    for key in dict:
        print(key+"|"+str(dict[key]))

main()

