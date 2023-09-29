#!/usr/bin/env python

from user import User

class Student(User):
    
    def learn(self, knowledge_string):
        self.knowledge.append(knowledge_string)

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []

        pass