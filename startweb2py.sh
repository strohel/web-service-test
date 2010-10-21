#!/bin/bash

# cesta k instalaci web2py:
WEB2PY_PATH="${HOME}/škola/4. ročník/OOP/projekt/web2py"

# nastartovat server, ktery posloucha vsude, nezobrazi gui, heslo nastavit na veslo, a nestartuje cron
cd "${WEB2PY_PATH}"
./web2py.py -i 0.0.0.0 --nogui -a veslo -N
