PYTHON := python3
SCRIPT := main.py

VERBOSE ?= 0

# Verbosity
ifeq ($(VERBOSE),0)
AT := @
else
AT :=
endif

all: first_task second_task

first_task: 1a_task 1b_task 1c_task

second_task: 2a_task 2b_task 2c_task

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

2a_task:
	$(AT)printf "%s\n%s\n%s\n%s" "2" "a" "e" "10" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "2" "a" "e" "20" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "2" "a" "e" "40" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "2" "a" "e" "80" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "2" "a" "e" "160" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "2" "a" "e" "320" | $(PYTHON) $(SCRIPT)

	$(AT)printf "%s\n%s\n%s\n%s" "2" "a" "c" "10" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "2" "a" "c" "20" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "2" "a" "c" "40" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "2" "a" "c" "80" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "2" "a" "c" "160" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "2" "a" "c" "320" | $(PYTHON) $(SCRIPT)

2b_task:
	$(AT)printf "%s\n%s\n%s\n%s" "2" "b" "e" "10" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "2" "b" "e" "20" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "2" "b" "e" "40" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "2" "b" "e" "80" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "2" "b" "e" "160" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "2" "b" "e" "320" | $(PYTHON) $(SCRIPT)

	$(AT)printf "%s\n%s\n%s\n%s" "2" "b" "c" "10" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "2" "b" "c" "20" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "2" "b" "c" "40" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "2" "b" "c" "80" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "2" "b" "c" "160" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "2" "b" "c" "320" | $(PYTHON) $(SCRIPT)

2c_task:
	$(AT)printf "%s\n%s\n%s\n%s" "2" "c" "e" "10" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "2" "c" "e" "20" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "2" "c" "e" "40" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "2" "c" "e" "80" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "2" "c" "e" "160" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "2" "c" "e" "320" | $(PYTHON) $(SCRIPT)

	$(AT)printf "%s\n%s\n%s\n%s" "2" "c" "c" "10" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "2" "c" "c" "20" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "2" "c" "c" "40" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "2" "c" "c" "80" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "2" "c" "c" "160" | $(PYTHON) $(SCRIPT)
	$(AT)printf "%s\n%s\n%s\n%s" "2" "c" "c" "320" | $(PYTHON) $(SCRIPT)
