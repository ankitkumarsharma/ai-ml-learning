#Python Match - The match statement is used to match patterns in Python. It is similar to switch-case statements in other programming languages. The match statement evaluates an expression and compares it against a series of patterns defined in case clauses. When a match is found, the corresponding block of code is executed.
#Basic Syntax of match statement
""" 
match subject:
    case pattern1:
        # code block for pattern1
    case pattern2:
        # code block for pattern2
    case _:
        # default code block
"""
#Example of match statement
def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status"
print(http_status(200))  # Output: OK

#Combine Values in a Case
def http_status_combined(status):
    match status:
        case 200 | 201 | 202:
            return "Success"
        case 400 | 401 | 403:
            return "Client Error"
        case 500 | 501 | 502:
            return "Server Error"
        case _:
            return "Unknown Status"

#If Statements as Guards in Cases for extra conditions
def http_status_guarded(status):
    match status:
        case code if 200 <= code < 300:
            return "Success"
        case code if 400 <= code < 500:
            return "Client Error"
        case code if 500 <= code < 600:
            return "Server Error"
        case _:
            return "Unknown Status"
        
