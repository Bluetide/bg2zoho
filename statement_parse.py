import csv

with open('data/MovimientoEst.txt', newline='',encoding='latin-1') as csvfile:
  with open('data/bgzoho.csv', 'w+') as csvout:
    writer = csv.writer(csvout, lineterminator='\n')
    cs = csv.reader(csvfile, delimiter=';', quotechar='"')
    next(cs, None)  # skip the first row from the reader, the old header
    writer.writerow(['Date-dd/MM/YYYY', 'Withdrawals', 'Deposits', 'Payee', 'Description', 'Reference Number']) # write new header
    for line in cs:
        writer.writerow((line[0],line[3].replace(",", ""),line[4].replace(",", ""),'',line[2].replace(",", ""),line[1].replace(",", "")))
