=======================
Jak toto vše rozchodit?
=======================

Stačí stáhnout web2py (klidně jenom zdrojáky) a umístit do této složky (takže
zde bude složka web2py, která obsahuje applications, gluon atd.)


Jak pustit server?
==================

Stačí překopírovat (nebo nasymlinkovat) složku webservices do web2py/applications
a pak pustyt web2py přes skriptík startweb2py.sh. (funguje na Unixu) Pozor,
startovací skriptík nastaví administrátorské heslo na "veslo".

 * pak stačí otevřít adresu http://localhost:8000/webservices/chatroom/call/soap


Jak na Python klienty?
======================

Ty stačí pouze pustit. Pozor, klienti používají python klinovnu pysimplesoap,
která je obsažena ve web2py. (ve složce klienti-python je symlink, pokud váš
systém symlinky neumí, tak tam adresář pysimplesoap překopírujte)
