PYTHON := python3
SCRIPT := main.py

VERBOSE ?= 0

# Verbosity
ifeq ($(VERBOSE),0)
AT := @
else
AT :=
endif

all: run

run:
	$(AT)$(PYTHON) $(SCRIPT)

all_tests: test_a test_b test_c test_d

test_a:
	$(AT)printf "%s\n" "a" | $(PYTHON) $(SCRIPT)

test_b:
	$(AT)printf "%s\n" "b" | $(PYTHON) $(SCRIPT)

test_c:
	$(AT)printf "%s\n%s\n" "c" "128"  | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n" "c" "256"  | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n" "c" "512"  | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n" "c" "1024" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n" "c" "2048" | $(PYTHON) $(SCRIPT)

test_d:
	$(AT)printf "%s\n%s\n" "d" "128"  | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n" "d" "256"  | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n" "d" "512"  | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n" "d" "1024" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n" "d" "2048" | $(PYTHON) $(SCRIPT)

