import ast


def clean_string(input_string):
    # Check if the string starts with ```python and ends with ```
    if input_string.startswith("```python") and input_string.endswith("```"):
        # Remove the ```python at the beginning and ``` at the end
        cleaned_string = input_string[9:-3]
        return cleaned_string.strip()
    else:
        return input_string.strip()

# function to remove any text values outside of brakceted values

def extract_bracketed_value(input_string, numberOfOutputsFromAI):
    start = input_string.find('[')
    end = input_string.find(']') + 1
    if start != -1 and end != -1 and len(ast.literal_eval(input_string[start:end])) == numberOfOutputsFromAI:
        return input_string[start:end]
    else:
        return False



def convert_to_dict(s):
    # Convert the string to a list of lists
    list_of_lists = ast.literal_eval(s)
     
    # Create a dictionary with keys starting from 1
    return {i + 1: lst for i, lst in enumerate(list_of_lists)}

