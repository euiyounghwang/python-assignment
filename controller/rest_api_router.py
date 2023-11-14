
from fastapi import APIRouter
from repository.schema import Lookup, Response_Lookup
from inject.injector import (logger, util)
import datetime
import asyncio
import json

app = APIRouter(
    prefix="/v1",
)


@app.post("/process_lookup", 
          response_model=Response_Lookup,
          description="Lookup the different keys via REST-API", 
          summary="Lookup the different keys via REST-API")
async def processing(request: Lookup):
    ''' processing via REST-API '''
    StartTime, EndTime, Delay_Time = 0, 0, 0
    
    try:
        StartTime = datetime.datetime.now()
     
        request_json = request.to_json()
        logger.info("processing : {}".format(json.dumps(request_json, indent=2)))
        
        ''' parallel extract the result from different jsons '''
        '''
        {
            "first_input_array": [
                "test",
                "abc"
            ],
            "second_input_array": [
                "abc",
                "xyz"
            ]
        }
        '''
        
        result = await asyncio.gather(
            util.lookup_difference(
                source=util.sort_str_dict(request_json.get("first_input_array", {})),
                dest=util.sort_str_dict(request_json.get("second_input_array", {}))),
            util.lookup_difference(
                source=util.sort_str_dict(request_json.get("second_input_array", {})),
                dest=util.sort_str_dict(request_json.get("first_input_array", {}))),
        )
        
        response_json = {
            'result' : {
                'first_input_array_lookup' : [
                    result[0]
                ],
                'second_input_array_lookup' : [
                    result[1]
                ]
            }
        }
               
        EndTime = datetime.datetime.now()

        Delay_Time = str((EndTime - StartTime).seconds) + '.' + str((EndTime - StartTime).microseconds).zfill(6)[:2]
        
        logger.info(f'Delay Time : {Delay_Time}')
        logger.info(f'response - {json.dumps(response_json, indent=2)}')
        
        return response_json
        
    except Exception as e:
        logger.error(e)