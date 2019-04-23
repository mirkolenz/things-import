PY = pipenv run python
OUTFILE = things3.html
TEMPLATES_DIR = templates

-include Makefile-Config.mk

.PHONY: all

all: $(OUTFILE) upload

$(OUTFILE): parse.py $(TEMPLATES_DIR)/*
	$(PY) $< $(TEMPLATES_DIR) $@

upload: $(OUTFILE)
ifdef SSH_DIR
	scp -rp $< $(SSH_DIR)
endif
