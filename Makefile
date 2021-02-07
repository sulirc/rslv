###############################################################################
# Simple Makefile of workflow
###############################################################################

RSLV_DIR="$(shell pwd)"
RSLV="./rslv.sh"
BIN_DIR="/usr/local/bin/rslv"
DATABASE="~/.rslv.db"
H1="\n\n\033[0;32m\#\#\# "
H1END=" \#\#\# \033[0m\n"

setenv:
	@echo $(H1)Setup rslv env$(H1END)
	@ENV_RSLV_DIR=$(RSLV_DIR) ./setenv.sh

uninstall:
	@echo $(H1)Uninstalling rslv$(H1END)
	rm -f $(BIN_DIR)

install: uninstall setenv
	@echo $(H1)Installing rslv$(H1END)
	ln $(RSLV) $(BIN_DIR)
	@echo

clean:
	@echo $(H1)Cleaning up$(H1END)
	rm -f rslv.*.log
	rm -f cliresolve/*.pyc
