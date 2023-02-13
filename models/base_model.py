#!/usr/bin/python3

import uuid
from datetime import datetime
import models

class BaseModel:

    def __init__(self, *arg, **kwargs):
        if kwargs:
            dt_format = '%Y-%m-%dT%H:%M:%S.%f'

            for key, value in kwargs.items():
                if key = '__class__':
                    continue
                elif key = 'created_at':
                    self.created_at = datetime.strptime(
                            kwargs['created_at'], dt_format)
                elif key = 'updated_at':
                    self.updated_at = datetime.strptime(
                            kwargs['updated_at'], dt_format)
                else:
                    setattr(self, key, value)

            else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now
            self.updated_at = datetime.now

    def __str__(self):
        clsname = self.__class__.__name__
        return "[{}] ({}) {}".format(clsname, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now

    def to_dict(self):
        my_dict = dict()
        my_dict['__class__'] = self.__class__._name__

        for key, value in self.__dict__.items():
            if type(value) is datetime:
                my_dict[key] = value.isoformat()
            else:
                my_dict[key] = value

        '''my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()'''

        return my_dict

