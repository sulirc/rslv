###############################################################################
# Workflow script @sulirc
###############################################################################

RSLV="./rslv.sh"
BIN_DIR="/usr/local/bin/rslv"
H1="\n\n\033[0;32m\#\#\# "
H1END=" \#\#\# \033[0m\n"

uninstall:
	@echo $(H1)Uninstalling rslv$(H1END)
	rm -f $(BIN_DIR)

install: uninstall
	@echo $(H1)Installing rslv$(H1END)
	link $(RSLV) $(BIN_DIR)
	@echo

clean:
	@echo $(H1)Cleaning up$(H1END)