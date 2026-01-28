from kfp import dsl
import os
import sys
import mlrun

@dsl.pipeline(name="Condition pipeline", description="Pipeline that runs a function based on the result of a previous function")
def kfpipeline(input_val):
    project = mlrun.get_current_project()
    
    # Run first function with the input value given to the workflow
    step_1 = mlrun.run_function('func-A', params={"input_value":str(input_val)}, returns=['first_func_res'])    
    step_2 = mlrun.run_function('func-B', returns=['second_func_res']).after(step_1)
    # # Based on func_A result, we run either func_B or func_C
    # step_1_output = step_1.outputs["first_func_res"]
    
    # with dsl.Condition(step_1_output > 5) as condition1:
    #     step_2 = mlrun.run_function('func-B', returns=['second_func_res'])
    # condition1.after(step_1)
        
    # with dsl.Condition(step_1_output <= 5) as condition2:
    #     step_2 = mlrun.run_function('func-C', returns=['second_func_res'])
    # condition2.after(step_1)
