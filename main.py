# -*- coding: utf-8 -*-
import os
import logging

if __name__ == '__main__':

    FORMAT = '%(asctime)-15s | docker-cron | %(levelname)-2s | %(message)s'
    logging.basicConfig(level=logging.INFO, format=FORMAT)
    logger = logging.getLogger(__name__)

    # read all the enviornment variable
    ENV_VAR = os.environ['env_var']

    logger.info(ENV_VAR)
