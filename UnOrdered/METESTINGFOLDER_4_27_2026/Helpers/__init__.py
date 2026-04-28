def setin(*inputs):
    """
    A helper function to set test inputs for the input() function.
    Usage:
    setin("input1", "input2", "input3")
    This will set up the input() function to return "input1" on the first call,
    "input2" on the second call, and so on.
    To reset to normal input behavior, call setin() with no arguments or None:
    setin()
    """
    if inputs:
        input_iter = iter(inputs)
        def mock_input(prompt=""):
            try:
                value = next(input_iter)
                print(f"{prompt}{value}")
                return value
            except StopIteration:
                raise EOFError("No more inputs for testing")
        builtins.input = mock_input
    else:
        builtins.input = builtins._original_input_backup