#!/usr/bin/env python3
# This is based on the awesome work of Dr Spencer Bryngelson (https://github.com/sbryngelson/sbryngelson.github.io)

import yaml
import os

paperdir = 'assets/papers/'

#get .bib for files with arXiv identifier
with open(r'_data/publist.yml') as file:
    pubs = yaml.load(file, Loader=yaml.FullLoader)

    for pub in pubs:
        for k,v in pub.items():
            if (k=='url'):
                url=v
            if (k=='arxiv'):
                print('working on ArXiv file ' + url)
                os.system("./scripts/arxiv2bib.py " + str(v) + " > " + paperdir + url +".bib")
                infile = open(os.path.join(paperdir, url +".bib"),'r')
                tmpfile = os.path.join(paperdir,"tmp.bib")
                newopen = open(tmpfile,'w')
                for line in infile:
                    if 'File' not in line and 'Eprint' not in line and 'PrimaryClass' not in line:
                        newopen.write(line)
                newopen.close()
                os.system("mv " + tmpfile + os.path.join(paperdir,url + ".bib"))

#get .bib for files with DOI 
with open(r'_data/publist.yml') as file:
    pubs = yaml.load(file, Loader=yaml.FullLoader)
    for pub in pubs:
        for k,v in pub.items():
            if (k=='url'):
                url=v
            if (k=='doi'):
                print('working on DOI file ' + url)
                os.system("./scripts/doi2bib.py " + str(v) + " > " + paperdir + url +".bib")
                #remove empty lines that doi2bib gives
                tmpfile = os.path.join(paperdir,"tmp.bib")
                open(tmpfile,'w').write(
                    ''.join(
                        l for l in open(os.path.join(paperdir, url + ".bib")) if l.strip()))
                # os.system("mv papers/tmp.bib papers/" + url + ".txt")
                infile = open(tmpfile,'r')
                newopen = open(os.path.join(paperdir,"tmp2.bib"),'w')
                for line in infile:
                    if 'url' not in line and 'publisher' not in line:
                        newopen.write(line)
                newopen.close()
                os.system("mv " + os.path.join(paperdir,'tmp2.bib ') + os.path.join(paperdir,url + ".bib"))
                
# Clear up
os.system("rm -f " + paperdir + "tmp*.bib")
