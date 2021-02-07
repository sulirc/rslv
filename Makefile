###############################################################################
# Simple Makefile of workflow
###############################################################################

RSLV_DIR="$(shell pwd)"
RSLV="./.rslv.sh"
BIN_DIR="/usr/local/bin/rslv"
DATABASE="~/.rslv.db"
H1="\033[0;32m==> "
H1END=" \033[0m"

setenv:
	@echo $(H1)Setup rslv env$(H1END)
	@ENV_RSLV_DIR=$(RSLV_DIR) ./setenv.sh
	@echo "rslv setenv ok"
	@echo

uninstall:
	@echo $(H1)Uninstalling rslv$(H1END)
	@rm -f $(BIN_DIR)
	@echo "rslv uninstall ok"
	@echo

install: uninstall setenv
	@echo $(H1)Installing rslv$(H1END)
	@ln $(RSLV) $(BIN_DIR)
	@echo "rslv install ok"
	@echo

clean:
	@echo $(H1)Cleaning up$(H1END)
	@rm -f rslv.*.log
	@rm -f cliresolve/*.pyc
	@rm -f .rslv.sh
	@rm -f .rslv.db
	@rm -f .rslv.runtime.log
	@echo "rslv clean ok"
	@echo
