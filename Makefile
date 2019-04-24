PY = pipenv run python
OUTFILE = things3.html
TEMPLATES_DIR = templates
SCP = scp -rp

-include Makefile-Config.mk

.PHONY: all upload clean install uninstall

all: $(OUTFILE) upload

$(OUTFILE): parse.py $(TEMPLATES_DIR)/*
	$(PY) $< $(TEMPLATES_DIR) $@

upload: $(OUTFILE)
ifdef SSH_DIR
	$(SCP) $< $(SSH_DIR)
endif

clean:
	rm -f $(OUTFILE)

install: Pipfile
	pipenv install

uninstall:
	pipenv --rm
