square_values = {"e4": 2, "e5": 2, "d4": 2, "d5": 2, "c6": 1, "d6": 1, "e6": 1, "f6": 1,
                 "c3": 1, "d3": 1, "e3": 1, "f3": 1, "c4": 1, "c5": 1, "f4": 1, "f5": 1}
piece_score = {'0': 100, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

COLUMN = 9
ROW = 11

ranks_to_rows = {"1": 10, "2": 9, "3": 8, "4": 7, "5": 6, "6": 5,
                 "7": 4, "8": 3, "9": 2, "10": 1, "11": 0}
rows_to_ranks = {v: k for k, v in ranks_to_rows.items()}
files_to_cols = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4,
                 "f": 5, "g": 6, "h": 7, "i": 8}
cols_to_files = {v: k for k, v in files_to_cols.items()}