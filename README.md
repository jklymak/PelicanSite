# PelicanSite
My Pelican Website

Only trick from all the other versions online is a special version of `themes/pelican-bootstrapJMK/templates/publications.html` that makes the publication list.

To run:
```bash
source activate pelican
cd ~/Dropbox/PelicanSite/
make bib # to make the bibliography
make cp_upload # to install on site
```

If we need to use the python environment then run
```bash
conda env create -f pelican.env
```
