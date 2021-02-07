#produces file containing final results to be plotted:
#zip, cases, ratio of 2020:2019 calls

def main():

    #collect data into dictionaries
    dict19 = collect("calls2019")
    dict20 = collect("calls2020")

    #open input (covid data) and output (results) files
    fin = open("covidByZIP.csv")
    fout = open("results","w")

    #process covid data
    line = fin.readline()
    while line:
        fields = line.split(",")
        zipcode = fields[0] #zip code
        cases = fields[4] #cases per 100,000

        #for each zip in covid data,
        #if in both data sets, add data to results
        #ZIP|cases|2020/2019 ratio
        if (zipcode in dict19) and (zipcode in dict20):
            #ratio = 2020 data/2019 data
            ratio = int(dict20[zipcode])/int(dict19[zipcode])
            print(zipcode + "|" + cases + "|" + str(ratio), file=fout)


        line = fin.readline()

    fin.close()
    fout.close()

#get data from file and store in dictionary
def collect(filename):
    dict = {}
    
    f = open(filename)
    line = f.readline()

    while line:
        fields = line.split("|")
        zipcode = fields[0]
        calls = fields[1]
        #key=zip, data=calls     
        dict[zipcode] = calls

        line = f.readline()
    f.close()

    return dict

main()
