PYTHON ?= python
FILE1 ?= palabras.txt
FILE2 ?= otro.txt
.PHONY: run words

run:
	$(PYTHON) -m uvicorn app.main:app --reload

words:
	$(PYTHON) -c "import pathlib,sys; p=pathlib.Path(sys.argv[1]); print('Archivo:', p); print('Palabras:'); [print('-', line.strip()) for line in p.read_text(encoding='utf-8').splitlines() if line.strip()]" "$(FILE)