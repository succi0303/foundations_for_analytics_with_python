#!/usr/bin/env python3
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, sheetname=None, index_col=None)
row_output = []
for worksheet_name, data in data_frame.items():
    row_output.append(data['Sale Amount'].replace('$', '')\
            .replace(',', '').astype(float) > 2000.0)
filterd_rows = pd.concat(row_output, axis=0, ignore_index=True)
writer = pd.ExcelWriter(row_output, sheet_name='sale_amount_gt2000', index=False)
writer.save()
