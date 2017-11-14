import requests, xlsxwriter, urllib2
import numpy as np
from bs4 import BeautifulSoup
from datetime import date


def getSlopeArr(_movement, _dates):
	slopes_arr = []
	for i in range(len(_movement)):
		if i>0: 
			slopes_arr.append( float(_movement[i]-_movement[i-1]) / float((_dates[i]-_dates[i-1]).days) );
	return slopes_arr

def reject_outliers(data, m=2):
	data = np.array(data);
	return data[abs(data - np.mean(data)) < (m * np.std(data))];


workbook = xlsxwriter.Workbook('tectonicPlates.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write(0,0, "Site Name")
worksheet.write(0,1, "Velocity N")
worksheet.write(0,2, "Velocity E")
worksheet.write(0,3, "Velocity S")
worksheet.write(0,4, "Velocity")

row = 1;
sites = ['P566', 'P300', 'P294', 'P284', 'CRBT', 'P535', 'P513', 'ORES', 'COPR', 'P551', 'VDCY', 'PBPP', 'P588', 'WOMT', 'CCCC', 'P615', 'P595', 'P620', 'P611', 'OPRD', 'OPBL', 'BEMT', 'HNPS', 'P480', 'SBCC', 'CARH', 'P543', 'MIG1', 'CAND', 'P502'];
for site in sites:
	url = "ftp://data-out.unavco.org/pub/products/position/"+site+"/"+site+".pbo.nam08.csv"
	req = urllib2.Request(url);
	response = urllib2.urlopen(req);
	page = response.read();
	sentences = page.split('\n')[:-1]
	data = sentences[12:]
	site_n, site_e, site_v, site_dates = [], [] ,[], []
	for data_entry in data:
		try:
			[rawdate, n, e, v, nstd, estd, vstd, qual] = data_entry[:-1].split(',');
		except:
			print("data_entry", data_entry);
			print("data_entry[:-1] is: ", data_entry[:-1]);
			print('data_entry[:-1].split(,) is: ', data_entry[:-1].split(','));
		y,m,d = map(lambda(x): int(x), rawdate.split('-'));
		_date = date(y,m,d);
		n,e,v= float(n.strip()), float(e.strip()), float(v.strip());
		site_n.append(n);
		site_e.append(e);
		site_v.append(v);
		site_dates.append(_date);
	slopes_n, slopes_e, slopes_v = getSlopeArr(site_n, site_dates), getSlopeArr(site_e, site_dates), getSlopeArr(site_v, site_dates);
	rej_outl_slopes_n, rej_outl_slopes_e, rej_outl_slopes_v =  reject_outliers(slopes_n), reject_outliers(slopes_e), reject_outliers(slopes_v)
	avg_vel_n, avg_vel_e, avg_vel_v = np.mean(rej_outl_slopes_n)*365, np.mean(rej_outl_slopes_e)*365, np.mean(rej_outl_slopes_v)*365

	worksheet.write(row,0,site)
	worksheet.write(row,1,avg_vel_n)
	worksheet.write(row,2,avg_vel_e)
	worksheet.write(row,3,avg_vel_v)
	worksheet.write(row,4,np.sqrt(avg_vel_n**2+avg_vel_e**2+avg_vel_v**2));
	row+=1;

workbook.close()



