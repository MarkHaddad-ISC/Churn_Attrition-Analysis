from Functions.CommonKeyMaker import *

file_path = '/Users/haddadm/CursorXopenPYXL/Outputs/LLM ANALYSIS - SFDC TIMELINE.xlsx'
sheet_name = 'CleanedData'
col1 = 'Q'
col2 = 'P'
start_row = 2
save_path = '/Users/haddadm/CursorXopenPYXL/Outputs/LLM ANALYSIS - SFDC TIMELINE.xlsx'

#concatenate_columns_and_insert_to_column_a(file_path=file_path, sheet_name=sheet_name, col1=col1, col2=col2, start_row=start_row, save_path=save_path)

mapToSlideCategories(file_path=file_path, sheet_name=sheet_name, col1=col1, col2=col2, start_row=start_row, save_path=save_path)

