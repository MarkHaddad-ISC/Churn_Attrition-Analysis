from openpyxl import load_workbook
from Functions.GroupByCommonID import *
from Prompts.OppyPrompt import *


file_path = '/Users/haddadm/CursorXopenPYXL/RawInputs/GA_q1_q3.xlsx'
sheet_name = 'RawInput'
GPTModel = 'gpt-4o'



# Batch size for incremental saving, Value should be no less than 50, theoretically shouldnt matter with new error handeling, batch size is inversely proportinal to runtime
starting_row = 2 #change to actual starting row value if it errors out, no offset neccesary, make this number the exact number of the row you want to start anaylsis on, row 1 is the header row no naturally we start at 2



# Load the workbook and select the sheet
workbook = load_workbook(filename=file_path, data_only=True)
sheet = workbook[sheet_name]


length_col_A = sum(1 for cell in sheet['A'] if cell.value is not None)


FinalRowPlus1 = length_col_A+1
#FinalRowPlus1 = 40

grouped_data = group_rows_by_contract_id(
    sheet,
    start_row=starting_row,
    end_row=FinalRowPlus1,
    key_col='A',
    group_col='M',
    data_cols=['AC','AD','AF','AI','AK','AL','AM']
)


batches = create_batches(grouped_data, batch_size=1)


process_batches_and_writeV3(workbook, file_path, sheet, batches ,GPTModel, ContractIDChunkingPrompt,5,40,3)

