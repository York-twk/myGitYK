import logging
import os
import sys
import traceback
import datetime
import time
import logging.config
from logging import handlers
from colorama import init, Fore, Back

def _logging(**kwargs):
    level = kwargs.pop('level', None)
    filename = kwargs.pop('filename', None)
    datefmt = kwargs.pop('datefmt', None)
    format = kwargs.pop('formate', None)
    if level is None:
        level = logging.DEBUG
    if filename is None:     
        filename = 'default.log'
    if datefmt is None:
        datefmt = '%Y-%m-%d %H:%M:%S'
    if format is None:
        format = '%(asctime)s [%(module)s %(lineno)d]  %(message)s'

    log = logging.getLogger(filename)
    format_str = logging.Formatter(format, datefmt)

    def namer(filename):
        return filename.spilt('default.')[1]
    
    os.makedirs("./debug/logs", exist_ok=True)
    th_debug = handlers.TimedRotatingFileHandler(filename="./debug/" + filename, when='s', encoding='utf-8')
    th_debug.suffix = "%Y-%m-%d.log"
    th_debug.setFormatter(format_str)
    th_debug.setLevel(logging.DEBUG)
    log.addHandler(th_debug)

    th = handlers.TimedRotatingFileHandler(filename="./debug/" + filename, when='s', encoding='utf-8')
    th.suffix = "%Y-%m-%d.log"
    th.setFormatter(format_str)
    th.setLevel(logging.DEBUG)
    log.addHandler(th)
    log.setLevel(level)
    return log

def Update_DateTime():
    _path = 'logs'
    if not (os.path.exists(_path)):
        os.makedirs(_path)
    
    Set_Info(_path)
    Set_Debug(_path)

    LOGGING_DEBUG_FORMAT = '%(asctime)s [%(module)s %(lineno)d]   %(message)s'
    DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
    tid = datetime.datetime.now().strftime('%Y-%m-%d')
    yesterday_day = datetime.datetime.now() + datetime.timedelta(days=-1)
    yesterday_tid = yesterday_day.strftime('%Y-%m-%d')


def Set_Info(path):
    filename = 'info.log'
    filehandle = handlers.TimedRotatingFileHandler(filename= path + ".\\" + filename, when='midnight', encoding='utf-8', interval=1)
    LOGGING_FORMAT = '%(asctime)s  %(message)s'   
    filehandle.setFormatter(logging.Formatter(LOGGING_FORMAT))
    filehandle.setLevel(logging.INFO)
    filehandle.namer = 'info'
    filehandle.suffix = "%Y-%m-%d.log"
    log_info.addHandler(filehandle)
    log_info.setLevel(logging.INFO)

def Set_Debug(path):
    filename = 'debug.log'
    debughandle = handlers.TimedRotatingFileHandler(filename= path + ".\\" + filename, when='midnight', encoding='utf-8', interval=1)
    LOGGING_DEBUG_FORMAT = '%(asctime)s %(levelname)s %(module)s %(lineno)d   %(message)s'   
    debughandle.setFormatter(logging.Formatter(LOGGING_DEBUG_FORMAT))
    debughandle.setLevel(logging.DEBUG)
    debughandle.namer = 'debug'
    debughandle.suffix = "%Y-%m-%d.log"
    log_debug.addHandler(debughandle)
    log_debug.setLevel(logging.DEBUG)

def Add(msg):
    log_info.info(msg)
    log_debug.info(msg)
    pmsg = "{} {}".format(datetime.datetime.now().strftime('%H:%M:%S.%f')[:-3], msg)
    print(pmsg)

def Add_Exception(e):
    error_class = e.__class__.__name__ #get module name of error 
    detail = e.args[0] #get error detail
    cl, exc, tb = sys.exc_info() #get call back
    lastCallBack = traceback.extract_tb(tb)[-1]
    filename = lastCallBack[0] #get file name of error 
    lineNum = lastCallBack[1]  #get line no of error 
    funName = lastCallBack[2]  #get function of error
    errMsg = "File \"{}\", line {}, in {}: [{}] {}".format(filename, lineNum, funName, error_class, detail)

    log_debug.error(errMsg)
    pmsg = "{} ERROR {}".format(datetime.datetime.now().strftime('%H:%M:%S.%f')[:-3], errMsg)
    print(pmsg)
    return errMsg

def Add_Debug(msg):
    log_debug.debug(msg)



log_info : logging.Logger = logging.getLogger(name='info')
log_debug : logging.Logger = logging.getLogger(name='debug')
Update_DateTime()
