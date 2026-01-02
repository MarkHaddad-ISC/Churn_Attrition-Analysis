#NEEDS WORK
#functions required for filtering by date

def build_max_value_dict(keys, values):
    """
    Takes two lists: keys and values.
    Returns a dictionary where each unique key maps to the highest value found at matching indices.
    """
    result = {}
    for key, value in zip(keys, values):
        key = key.strip()  # Remove leading/trailing whitespace
        if key in result:
            result[key] = max(result[key], value)
        else:
            result[key] = value
    return result






def filter_rows_by_dict(combined_filtered_data, comparison_dict):
    """
    Removes rows from combined_filtered_data where the dictionary value for the account ID
    is less than the month digit extracted from the date string.
    
    Parameters:
    - combined_filtered_data: List of rows, each containing a date string at index 4 and account ID at index 5.
    - comparison_dict: Dictionary with account ID as key and threshold month digit as value.
    
    Returns:
    - Filtered list of rows.
    """
    for i in range(len(combined_filtered_data) - 1, -1, -1):
        account_id = str(combined_filtered_data[i][5]).strip()
        month_digit = int(str(combined_filtered_data[i][4])[5:7])  # Extract 7th character from date string



        #this if loop isnt scalable, we need to include the year if we want to run this over multiple years logic
        if month_digit > 9:
            month_digit = month_digit - 12
            #print(month_digit)

        if account_id in comparison_dict:
            if int(comparison_dict[account_id]) < month_digit:
                del combined_filtered_data[i]

    return combined_filtered_data
