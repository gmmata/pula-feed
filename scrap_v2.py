from bs4 import BeautifulSoup
import urllib.request 

BASE_URL = "www.pula.hr/"

def clear_list(lista):
	nova_lista=[]
	for l in lista:
		if l not in nova_lista:
			nova_lista.append(l)
	return nova_lista

def get_doc_links (url):
	file = urllib.request.urlopen(url)
	html = file.read()
	soup = BeautifulSoup(html, "lxml")
	links = []
	section = soup.find(id='content')
	sub_section_links = section.findAll("a")
#	print(sub_section_links)
	for sub_section in sub_section_links:
		print (sub_section.string)
		l = sub_section.get("href")
		if l != None:
			links += [BASE_URL + str(sub_section.get("href"))]
	links = clear_list(links)
	return links
'''	sub_section_lists = section.findAll("li")
	sub_section_files = section.findAll("div","filelinks filelinks_layout_0")
	print(type(section),type(sub_section_lists), "\n", type(sub_section_files))
	print ("Skupa u listama:", len(sub_section_lists)+len(sub_section_files))  
	for sub_section in sub_section_lists:
		links += [BASE_URL + l.a["href"] for l in sub_section.findAll("li")]
	for sub_sect in sub_section_files:
		links += [BASE_URL + l.a["href"] for l in sub_sect.findAll("span","name")]'''
#	print (sub_section_lists, "\n", sub_section_files)
#	print ("Skupa u listama:", len(sub_section_lists)+len(sub_section_files))
#	return links

links = get_doc_links("http://www.pula.hr/uprava/uprava/upravni-odjeli-i-sluzbe/upravni-odjel-za-drustvene-djelatnosti/dokumenti-i-izvjesca/")
#http://www.pula.hr/uprava/uprava/upravni-odjeli-i-sluzbe/upravni-odjel-za-prostorno-uredenje-komunalni-sustav-i-imovinu/dokumenti-i-izvjesca/")
#http://www.pula.hr/uprava/uprava/upravni-odjeli-i-sluzbe/ured-grada/dokumenti-i-izvjesca/")
#http://www.pula.hr/uprava/uprava/upravni-odjeli-i-sluzbe/upravni-odjel-za-financije-i-opcu-upravu/dokumenti-i-izvjesca/")
#http://www.pula.hr/uprava/amministrazione-locale/assessorati-e-servizi/assessorato-alle-attivita-sociali/dokumenti-i-izvjesca/")
for l in links:
	print (l)
print (len(links), links[0])
#vidit šta s ovima koji nisu class="files"
