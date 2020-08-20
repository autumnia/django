import logging.config

logging.config.dictConfig({
    'version': 1,
    'formatters': {
        'sampleFormatter': {
            'format': '%(asctime)s [%(levelname)-7s] \n 경로:\t %(pathname)s   %(funcName)s  %(lineno)s \n 설명:\t %(message)s \n ----------------------------------------------------------------------'
        }
    },
    'handlers': {
        'sampleHandlers': {
            'class': 'logging.StreamHandler',
            'formatter': 'sampleFormatter',
            'level': logging.DEBUG
        }
    },
    'root': {
        'handlers': ['sampleHandlers'],
        'level': logging.WARNING
    },
    'loggers': {
        'simpleExample': {
            'handlers': ['sampleHandlers'],
            'level': logging.DEBUG,
            'propagate': 0
        }
    }
})


<!-- 사용방법 -->
# -*- coding: utf-8 -*-

import logging.config

from config import loggingCfg

logger = logging.getLogger('simpleExample')

if __name__ == '__main__':

    logger.debug({
        'date'          : '2020-08-20 19:41:01',
        'api_id'        : 'OP_IF_0001',
        'api_desc'      : '실시간 고객 주문 데이터',
        'action'        : '수신',
        'status'        : 'fail',
        'return_code'   : '9002',
        'return_msg'    : 'Api call is failed',
        'error_code'    : '5002',
        'error_msg'     : 'StackOverflow 설문에서 나타난 가장 원하는 데이터 베이스 기술 MongoDB! NoSQL 데이터베이스중 가장 유명한 MongoDB! "return_code":"90" 왜 이토록 많은 사람이 원하는 데이터베이스가 되어버렸을까요? SQL을 배우지 않은 웹 개발자들에게 친숙한 Javascript로 되어있기 때문에 많은 사람들이 관심을 갖게 되었습니다. 또한 MongoDB는 속도가 매우 뛰어납니다! 이런 장점 때문에 빅데이터 처리가 필요한 분야에서 MongoDB가 요구되고 있습니다. 본 강좌는 MongoDB의 가장 기본적인 부분 부터 실제적인 부분까지를 이용해서 개념을 설명할 것입니다.'
    })
