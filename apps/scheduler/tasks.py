#-*-coding:utf-8-*-

from celery import task, platforms
from celery.utils.log import get_task_logger

from celery.task.schedules import crontab
from celery.decorators import periodic_task

platforms.C_FORCE_ROOT = True

logger = get_task_logger(__name__)


@periodic_task(run_every=crontab(hour="*", minute="*", day_of_week="*"))
def sync():
    logger.debug("sync ldap user")
