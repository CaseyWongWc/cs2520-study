
import builtins
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

# Store the original input function once, globally, to avoid re-capturing a mocked input
if not hasattr(builtins, '_original_input_backup'):
    builtins._original_input_backup = builtins.input

def set_test_inputs(inputs_list):
    """
    Sets up a mock input function that draws from a list of inputs.
    If inputs_list is None or empty, restores the original input function.
    """
    if inputs_list:
        input_iter = iter(inputs_list)
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

# Define test_inputs, this is where you can change your desired inputs
test_inputs = [1]  # <--- Change this list to provide your test inputs

# Apply the test inputs automatically when this cell is run
set_test_inputs(test_inputs)

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
              