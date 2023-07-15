#!/usr/bin/env python3

import logging
from logging import handlers

# BOILERPLATE do log
# TODO: usar função
# TODO: usar lib (loguru)
# instancia do logger
log = logging.Logger("logs.py", logging.DEBUG)

# level
# ch = logging.StreamHandler() # Console/terminal/stderr (ch = console handler)
# ch.setLevel(logging.DEBUG)
fh = handlers.RotatingFileHandler(
    "meulog.log", #nome do arquivo de log a ser salvo
    maxBytes=300, #100 bytes para efeitos de exemplo, mas em prod se usa 10**6 que é = 1 megabyte
    backupCount=10, # quantidade de arquivos de log a serem guardados
)

# formatação
fmt = logging.Formatter('%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s')
#ch.setFormatter(fmt)
fh.setFormatter(fmt)

#destino
# log.addHandler(ch)
log.addHandler(fh)

"""
log.debug("Mensagem para o dev, QA, sysadmin") 
log.info("ensagem geral para usuarios") 
log.warning("Aviso que nao causa erro") 
log.error("Erro que afeta uma unica execucao") 
log.critical("Erro geral! Ex: banco de dados sumiu!") 
"""

try:
    1 / 0
except ZeroDivisionError as e:
    log.error("Deu erro %s", str(e))
    
