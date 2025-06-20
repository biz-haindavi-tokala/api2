from pydantic import BaseModel
from datetime import datetime
class Todo(BaseModel):
    
    title: str
    description: str 
    is_completed: bool = False
    is_deleted: bool = False
    creation:int = int(datetime.timestamp(datetime.now())) # Use str for date representation, or use datetime if preferred
    updated_at:int = int(datetime.timestamp(datetime.now())) # Use str for date representation, or use datetime if preferred
