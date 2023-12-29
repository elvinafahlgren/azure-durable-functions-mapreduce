import azure.durable_functions as df

def orchestrator_function(context: df.DurableOrchestrationContext):

    input_data = yield context.call_activity("GetInputDataFn", " ")

    mapped = []

    for key, value in input_data:
        mapped.append(context.call_activity("Mapper", (key, value)))

    map_res = yield context.task_all(mapped)

    shuffled = yield context.call_activity("Shuffler", map_res)

    reduced = yield context.call_activity("Reducer", shuffled)

    formatted_output = ", ".join([f"<{key}, {value}>" for key, value in reduced.items()])

    return formatted_output

main = df.Orchestrator.create(orchestrator_function)
