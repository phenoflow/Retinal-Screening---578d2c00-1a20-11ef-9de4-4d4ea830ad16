# Evangelos Kontopantelis, David Springate, David Reeves, Darren M Ashcroft, Jose M Valderas, Tim Doran, 2024.

import sys, csv, re

codes = [{"code":"2BBF.00","system":"readv2"},{"code":"3128200","system":"readv2"},{"code":"2BBG.00","system":"readv2"},{"code":"2BBE.00","system":"readv2"},{"code":"2BB1.00","system":"readv2"},{"code":"2BBD.00","system":"readv2"},{"code":"3128000","system":"readv2"},{"code":"3128100","system":"readv2"},{"code":"X962 AB","system":"readv2"},{"code":"X962 NM","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('retinal-screening-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["abnormal-retinal-screening---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["abnormal-retinal-screening---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["abnormal-retinal-screening---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
