###############################################################################
# -*- makefile -*- 
#
# Copyright (C) D.G.R.C. Furminieux
#
# $Id$
# Author  : D.G.R.C. Furminieux
# $Revision$
# $Date$
# $State$
# $Name$
#
# Purpose :
#
###############################################################################
#
# ToDo:
#
#

########################### Global Constants ##################################
SRC_DIR=./src

PARSER_DIR=$(SRC_DIR)/taj/parser
ANTLR_PATH=./lib/build/antlr-3.1.3.jar
PYTHONPATH=$(SRC_DIR):lib/antlr_python_runtime-3.1.3-py2.5.egg

JAVA_BIN=/usr/bin/java
ANTLR=$(JAVA_BIN) -cp $(ANTLR_PATH) org.antlr.Tool

PYTHON=PYTHONPATH=$(PYTHONPATH) python


################################ Targets ######################################

################################# Rules #######################################


all: grammar

test:
	@echo TEST src/taj/parser/test.py
	@$(PYTHON) src/taj/parser/test.py
	@echo TEST src/taj/parser/cqlTest.py
	@$(PYTHON) src/taj/parser/cqlTest.py
	@echo TEST src/taj/alu/test.py
	@$(PYTHON) src/taj/alu/test.py
	@echo TEST src/taj/operator/test.py
	@$(PYTHON) src/taj/operator/test.py

loc:
	@(echo MFQL.g src/mforest; find src/ -type f -name "*.py"  | grep -v MFQL) | xargs wc -l | sort -n

grammar: $(PARSER_DIR)/MFQL.py

$(PARSER_DIR)/MFQL.py: MFQL.g
	$(ANTLR) -o $(PARSER_DIR) MFQL.g

# EOF #
