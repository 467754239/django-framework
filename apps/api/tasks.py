#-*-coding:utf-8-*-


from celery import task, platforms
from celery.utils.log import get_task_logger

platforms.C_FORCE_ROOT = True

logger = get_task_logger(__name__)


@task
def add(*args, **kwargs):
    import time
    time.sleep(10)
    logger.debug("sleep 10")
    return 1 + 2
