'''
YYYY-MM-DD HH:MM:SS+05:30 --> YYYYMMDD HHhMMmSSs
'''
import pandas as pd
import os
import shutil  
  
def format_date(ip):

	index, date = ip.split(",")
	ip = date
	temp_list = ip.split(" ")

	# YYYY-MM-DD -> YYYYMMDD
	temp = temp_list[0].split("-")
	op1 = ""
	for i in temp:
		op1 = op1 + i

	# HH:MM:SS+05:30 -> HHhMMmSSs
	temp = temp_list[1][:-6].split(":")
	t = ["h", "m", "s"]
	op2 = ""
	for i in range(3):
		op2 = op2 + temp[i] + t[i]

	return op1 + " " + op2


def load_images(formated_dates, profiles):
    # input directory
	IMAGE_DIR = r"C:\Users\91976\Desktop\instagram-scraper-master\images"
	images = []
	for id in formated_dates:
		for profile in profiles:
			image = os.path.join(IMAGE_DIR, profile)
			image = os.path.join(image, id)
			if (os.path.isfile(image)): 
				images.append(image)
				break

	return images

#load profile_names
profile_names = pd.read_csv("C:/Users/91976/Desktop/instagram-scraper-master/proflies.csv")
profiles = profile_names['proflie_name'].tolist()


#Load date csv
datetime = pd.read_csv("C:/Users/91976/Desktop/instagram-scraper-master/datetime.csv", "r")
dates = datetime[',datetimelist'].tolist()


formated_dates = [format_date(date) + ".jpg" for date in dates]
#Get paths 
images = load_images(formated_dates, profiles)

destination = r"C:/Users/91976/Desktop/dataset/"

#Search directory
for image in images:
	print(image)
	shutil.copy(image, destination)  
	







