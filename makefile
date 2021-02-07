#all processes result in a pdf scatterplot
all: scatterplot.pdf

#all intermediate files
clean:
	rm EMS2019.gz EMS2020.gz calls2019 calls2020 results scatterplot.pdf

#section of EMS data containing only March-July 2019
EMS2019.gz: EMSdata.gz makeEMSfiles.awk
	gawk -f makeEMSfiles.awk

#section of EMS data containing only March-July 2020
EMS2020.gz: EMSdata.gz makeEMSfiles.awk
	gawk -f makeEMSfiles.awk

#file for 2019 records of ZIP|non-severe calls
calls2019: EMS2019.gz makeZIPcalls.py
	zcat EMS2019.gz | python3 makeZIPcalls.py > calls2019

#file for 2020 records of ZIP|non-severe calls
calls2020: EMS2020.gz makeZIPcalls.py
	zcat EMS2020.gz | python3 makeZIPcalls.py > calls2020

#results from combining covid rates and non-severe EMS calls by zip code
#used to produce scatterplot
results: calls2019 calls2020 covidByZIP.csv getResults.py
	python3 getResults.py

#final plot: COVID rates vs. ratio of non-severe EMS calls (2020/2019)
scatterplot.pdf: makePlot.py results
	python3 makePlot.py
