from enum import Enum
from uuid import uuid4, UUID
from datetime import datetime


class TaskStatus(str, Enum):
    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"


class LaundryTask:
    def __init__(self, order_id: UUID, service_type: str, weight_kg: float, duration: int):
        self.task_id = uuid4()
        self.order_id = order_id
        self.service_type = service_type
        self.weight_kg = weight_kg
        self.duration = duration

        self.status = TaskStatus.PENDING
        self.machine_id = None

        self.start_time = None
        self.end_time = None


    # DOMAIN BEHAVIOR
    
    def start(self):
        if self.status != TaskStatus.PENDING:
            raise ValueError("Task can only be started when pending.")
        self.status = TaskStatus.IN_PROGRESS
        self.start_time = datetime.utcnow()

    def complete(self):
        if self.status != TaskStatus.IN_PROGRESS:
            raise ValueError("Task must be in progress to complete.")
        self.status = TaskStatus.DONE
        self.end_time = datetime.utcnow()

    def assign_machine(self, machine_id: str):
        self.machine_id = machine_id

