PYTHON := python3
SCRIPT := main.py

VERBOSE ?= 0

# Verbosity
ifeq ($(VERBOSE),0)
AT := @
else
AT :=
endif

all: first_task

first_task: 1a_task 1b_task 1c_task

1a_task:
	$(AT)printf "%s\n%s\n%s\n%s" "1" "a" "10" "0.5" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "1" "a" "20" "0.5" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "1" "a" "40" "0.5" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "1" "a" "80" "0.5" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "1" "a" "160" "0.5" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "1" "a" "320" "0.5" | $(PYTHON) $(SCRIPT)

	$(AT)printf "%s\n%s\n%s\n%s" "1" "a" "10" "0.25" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "1" "a" "20" "0.25" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "1" "a" "40" "0.25" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "1" "a" "80" "0.25" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "1" "a" "160" "0.25" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "1" "a" "320" "0.25" | $(PYTHON) $(SCRIPT)

1b_task:
	$(AT)printf "%s\n%s\n%s\n%s" "1" "b" "10" "0.5" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "1" "b" "20" "0.5" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "1" "b" "40" "0.5" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "1" "b" "80" "0.5" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "1" "b" "160" "0.5" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "1" "b" "320" "0.5" | $(PYTHON) $(SCRIPT)

	$(AT)printf "%s\n%s\n%s\n%s" "1" "b" "10" "0.25" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "1" "b" "20" "0.25" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "1" "b" "40" "0.25" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "1" "b" "80" "0.25" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "1" "b" "160" "0.25" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "1" "b" "320" "0.25" | $(PYTHON) $(SCRIPT)

1c_task:
	$(AT)printf "%s\n%s\n%s\n%s" "1" "c" "10" "0.5" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "1" "c" "20" "0.5" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "1" "c" "40" "0.5" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "1" "c" "80" "0.5" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "1" "c" "160" "0.5" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "1" "c" "320" "0.5" | $(PYTHON) $(SCRIPT)

	$(AT)printf "%s\n%s\n%s\n%s" "1" "c" "10" "0.25" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "1" "c" "20" "0.25" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "1" "c" "40" "0.25" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "1" "c" "80" "0.25" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "1" "c" "160" "0.25" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "1" "c" "320" "0.25" | $(PYTHON) $(SCRIPT)
