all: main.pdf

main.pdf: main.tex
	latexmk main -pdf

clean:
	rm -f *.aux *.log *.pdf *.dvi *.fdb_latexmk *.fls *.out
