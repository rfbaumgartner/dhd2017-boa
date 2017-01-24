#!/usr/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import glob, codecs

in_path = '~/Desktop/dhd2017-boa/input/xml-source'
out_path = '~/Desktop/dhd2017-boa/input/xml'

def process_file(filename):
	notes = {}
	handler = open(filename).read()
	soup = BeautifulSoup(handler, 'xml')
	doc_id = soup.TEI['xml:id']
	print doc_id
	for note in soup.findAll('note'):
		# get informations:
		xml_id = doc_id + note['xml:id']
		number = eval(note['n'])
		try:
			ftn = note.p.extract()
		except:
			# use the note tag for the Notes section
			footnote_text = note
            
            # make a new ref
			note = soup.new_tag('ref')
			footnote_text_idx = footnote_text.parent.contents.index(footnote_text)
			footnote_text.parent.insert(footnote_text_idx + 1, note)
			
			ftn = footnote_text.extract()

			print("Make sure correctness. No p in notes!")
			print "REF: " + str(note)
			print "NOTE: " + str(ftn)
		notes[number] = (xml_id, ftn)
		
		# reformat:
		note.name = 'ref'
		note.string = str(number)
		del note['place']
		del note['xml:id']
		note['type'] = 'note'
		note['target'] = xml_id
		
	if len(notes) > 0:
		back = soup.find('back')
		
		# create note div
		new_div = soup.new_tag('div')
		new_div['type'] = 'Notes'
		
		# add note entries
		for key in sorted(notes.keys()):
			new_note = notes[key][1]
			new_note.name = 'note'
			new_note['n'] = key
			new_note['xml:id'] = notes[key][0]
			
			# add it to footnote list
			new_div.append(new_note)
			
		back.insert(0, new_div)
		
	# write new file
	filename_wo_path = filename.split('/')[-1]
	outfile = codecs.open(out_path + '/' + filename_wo_path, 'w', 'utf-8')
	outfile.write(unicode(soup))
	outfile.close()

		
		

if __name__ == '__main__':
	files = glob.glob(in_path + '/*.xml')
	for f in files:
		print(f)
		process_file(f)
	