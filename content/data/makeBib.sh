#!/bin/bash
#
# Make bibliography...
#



# Run bib2bib first to extract stuff I want.  Added fields JMKPubtype
# and pdf to bibtex entries of my papers, i.e.:
#
# @Article{klymaketal06a,
#   author = {Jody M. Klymak and Robert Pinkel
#       and Cho-Teng Liu and Anthony K. Liu and Laura David},
#   title = 	 {Prototypical solitons in the {South} {China} {Sea}},
#   journal = 	 grl,
#   year = 	 {2006},
#   volume = 	 33,
#   pages = 	 {doi:10.1029/2006GL025932},
#   pdf = {http://web.uvic.ca/~jklymak/pdfs/KlymakEtAl06a.pdf},
#   JMKPubtype = {refereed}
# }

BIBLOC=/Users/jklymak/texmf/bibtex/bib/main.bib
# Make separate bibs for each "type" of publication...
./bib2bib $BIBLOC -ob refbib.bib  -c 'JMKPubtype : "refereed"'
./bib2bib $BIBLOC -ob inreviewbib.bib  -c 'JMKPubtype : "inreview"'
./bib2bib $BIBLOC -ob inprepbib.bib  -c 'JMKPubtype : "inprep"'
./bib2bib $BIBLOC -ob otherbib.bib  -c 'JMKPubtype : "other"'
./bib2bib $BIBLOC -ob booksbib.bib  -c 'JMKPubtype : "inbook"'

# cat them together
cat refbib.bib inreviewbib.bib inprepbib.bib otherbib.bib booksbib.bib > all.bib
