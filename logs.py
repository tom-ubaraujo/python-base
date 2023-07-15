#!/usr/bin/env python3

import logging

# BOILERPLATE do log
# TODO: usar função
# TODO: usar lib (loguru)
# instancia do logger
log = logging.Logger("logs.py", logging.DEBUG)
# level
ch = logging.StreamHandler() # Console/terminal/stderr
ch.setLevel(logging.DEBUG)
# formatação
fmt = logging.Formatter('%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s')
ch.setFormatter(fmt)
#destino
log.addHandler(ch)



log.debug("Mensagem para o dev, QA, sysadmin") 
log.info("ensagem geral para usuarios") 
log.warning("Aviso que nao causa erro") 
log.error("Erro que afeta uma unica execucao") 
log.critical("Erro geral! Ex: banco de dados sumiu!") 

print("-------")

try:
    1 / 0
except ZeroDivisionError as e:
    logging.error("Deu erro %s", str(e))

