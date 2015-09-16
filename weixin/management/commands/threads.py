# -*-coding:utf-8 -*-
"""
Created on 2015-09-10
@author: 汤晓川

"""

import time

from django.core.management.base import BaseCommand
from django.conf import settings

from ...threads import AsyncEventHandler

CHECKING_LOOP_PERIOD = 30


class Command(BaseCommand):
    threads = {}

    def handle(self, *args, **options):
        print 'settings.ASYNC_MSG_HANDLER_THREADS_CONFIG:%s ' % settings.ASYNC_MSG_HANDLER_THREADS_CONFIG

        for pool, amount in settings.ASYNC_MSG_HANDLER_THREADS_CONFIG:
            for i in range(amount):
                t = AsyncEventHandler(pool, str(i))
                t.setDaemon(True)
                t.start()

                tl = self.threads.get(pool, [])
                tl.append(t)
                self.threads[pool] = tl

        while True:
            self.stdout.write('Checking threads status...')
            for pool, ts in self.threads.iteritems():
                self.stdout.write('--- POOL {0} ---'.format(pool))
                for t in ts:
                    self.stdout.write('{0}: {1}'.format(t, t.is_alive()))

            time.sleep(CHECKING_LOOP_PERIOD)
