import time

def func_A(context, input_value):
    
    context.logger.info(f"Function A is running with input {input_value}")
    return int(input_value)

def func_B(context):
    
    context.logger.info(f"Function B is running now")        
    return "Function B has been triggered"

def func_C(context):
    
    context.logger.info(f"Function C is running now")        
    return "Function C has been triggered"
