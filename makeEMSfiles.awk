#splits EMS data into 2 files, one for 2019 and one for 2020

BEGIN{
    OFS = "|"

    #for each record, if it is from March-July 2019 or 2020,
    #add it to the correct file

    while (("zcat EMSdata.gz" | getline) > 0){
	if ($2 ~ /0[3-7]\/[0-9]{2}\/2019/){
	    print $0 | "gzip > EMS2019.gz"
	}
	else if ($2 ~ /0[3-7]\/[0-9]{2}\/2020/){
	    print $0 | "gzip > EMS2020.gz"
	}
    }
    close("zcat EMSdata.gz")
}
