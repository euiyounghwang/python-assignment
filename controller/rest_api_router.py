
from fastapi import APIRouter
from repository.schema import Lookup
from inject.injector import logger
import datetime
import json

app = APIRouter(
    prefix="/v1",
)


@app.post("/process_lookup", 
          description="Lookup the different keys via REST-API", 
          summary="Lookup the different keys via REST-API")
async def processing(request: Lookup):
    ''' processing via REST-API '''
    StartTime, EndTime, Delay_Time = 0, 0, 0
    
    try:
        StartTime = datetime.datetime.now()
     
        request_json = request.to_json()
        logger.info("processing : {}".format(json.dumps(request_json, indent=2)))
        
        EndTime = datetime.datetime.now()

        Delay_Time = str((EndTime - StartTime).seconds) + '.' + str((EndTime - StartTime).microseconds).zfill(6)[:2]
        
        # result = await service_cal_inject.excute_cal(arg1=request_json.get('args1'), 
        #                                     arg2=request_json.get('args2'), 
        #                                     operator=request_json.get('operator')
        #                                     )
        # print('response - {}'.format(result))
        return {'result' : request_json}
        
    except Exception as e:
        logger.error(e)