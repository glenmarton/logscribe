CHANGELOG_PATH=$(shell pwd)/data
PROJ='logscribe'

all: changelog.conf
	ls -rt ../*.yml | ./yaml2changelog.py 5.0.0-rc.11 >output.md
	diff reference.md output.md && echo 'PASS'

changelog.conf:
	echo "YAML_PATH=$(CHANGELOG_PATH)" > changelog.conf
	echo "CHANGELOG=$(CHANGELOG_PATH).md" >> changelog.conf
#
#    P H O N Y
#   T A R G E T S
#
.PHONY: clean
clean:
	rm -rf build $(PROJ).egg-info dist

.PHONY: distclean
distclean:
	$(MAKE) clean
	rm -rf .mypy_cache venv

.PHONY: dist
dist:
	python -m build .

.PHONY: flags
flags:
	# CHANGELOG_PATH = $(CHANGELOG_PATH)

.PHONY: lint
lint:
	./venv/bin/python -m mypy ./$(PROJ)
	./venv/bin/python -m flake8 --max-line-length=83 ./$(PROJ)/*.py

.PHONY: long
long:
	ls -rt ../*.yml | ./yaml2changelog.py >output.md
	diff long_reference.md output.md && echo 'PASS'

.PHONY: test
test:
	./venv/bin/python3 -m unittest discover

.PHONY: tst
tst:
	./venv/bin/python3 -m unittest discover -v

.PHONY: vars
vars:
	# PATH=$(PATH)
	# PROJ=$(PROJ)

.PHONY: venv
venv:
	python3 -m venv venv
	venv/bin/python3 -m pip install --upgrade pip
	venv/bin/python3 -m pip install --upgrade setuptools wheel
	venv/bin/python3 -m pip install -r requirements.txt

.PHONY: yml
yml:
	./changes_in_merged_order.sh > list.txt
	diff yaml_reference.txt list.txt && echo PASS

