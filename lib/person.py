#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="Name", job="Admin"):
        if (type(name) != int) and 0 < len(name) < 26:
            newName = name.title()
            self.name = newName 
        else:
            print("Name must be string between 1 and 25 characters.")

        if job in APPROVED_JOBS:
            self.job = job
        else:
            print("Job must be in list of approved jobs.")

        name = property(name)
        job = property(job)
