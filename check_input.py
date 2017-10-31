def check_input(condition, res=lambda x: x, prompt=None, prompt2=None):
    if prompt is not None and prompt2 is None:
        prompt2 = prompt
    param = input(prompt)
    while not condition(param):
        param = input(prompt2)
    return res(param)
