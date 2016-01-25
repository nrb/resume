install:
	pip install -U rst2pdf

spellcheck:
	aspell --add-extra-dicts=./aspell.en.pws -c resume.rst

resume: spellcheck
	rst2pdf -s cv.pdfstyle resume.rst

view: resume
	./opener.sh resume.pdf
