install:
	pip install -U rst2pdf

resume:
	rst2pdf -s cv.pdfstyle resume.rst

view: resume
	open resume.pdf
