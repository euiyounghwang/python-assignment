
from pydantic import BaseModel

class Lookup(BaseModel):
    first_input_array: list = ['test', 'abc']
    second_input_array: list = ['abc', 'xyz']
    
    def to_json(self):
        return {
            'first_input_array' : self.first_input_array,
            'second_input_array' : self.second_input_array,
        }
        
class Response_Lookup(BaseModel):
    result: dict = {
        'result' : 
        {
            'first_input_array_lookup': [], 
            'second_input_array_lookup' : []
        }
    }
