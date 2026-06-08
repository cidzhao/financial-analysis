import openpyxl

wb = openpyxl.load_workbook('financial-anaylisis.xlsx')
for sheetname in wb.sheetnames:
    ws = wb[sheetname]
    print(f"Sheet: {sheetname}, Max row: {ws.max_row}")
    # check if there are non-empty rows after row 52
    non_empty = 0
    for r in range(53, ws.max_row + 1):
        if any(ws.cell(row=r, column=col).value is not None for col in range(1, 10)):
            non_empty += 1
    print(f"  Non-empty rows after row 52: {non_empty}")
    if non_empty > 0:
        # print first few non-empty rows
        for r in range(53, ws.max_row + 1):
            row_vals = [ws.cell(row=r, column=col).value for col in range(1, 10)]
            if any(val is not None for val in row_vals):
                print(f"    Row {r:03d}: {row_vals}")
                break
