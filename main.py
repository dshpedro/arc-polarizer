import re

def read_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

def write_file(filename, data):
    with open(filename, 'w') as file:
        for line in data:
            file.write(line + '\n')

def assign_arcs_polarity(arcs, truth_table_map):
    polarized_arcs = []

    for arc in arcs:
        polarity = get_arc_polarity(arc, truth_table_map)
        polarized_arcs.append(arc + polarity)

    return polarized_arcs

def create_truth_table_map(truth_table):
    """
    This function creates a look up table with a dictionary
    the inputs of the truth table are the key, 
    the result from each input is going to the the correspondant value
    """
    truth_table_map = {}
    for row in truth_table:
        input = row[:-1] # everything apart from the last digit
        output = row[-1] # the last digit
        truth_table_map[input] = output
    return truth_table_map

def get_arc_polarity(arc, truth_table_map):
    literal = re.search(r"\D", arc).group()
    input = re.sub(r"\D", "1", arc) # replace non digits with '1'
    row_result = truth_table_map.get(input, "Unknown")
    if row_result == "1":
        polarity = literal # direct
    else:
        polarity = f"!{literal}" # reverse

    return polarity


def main():
    arcs = read_file('arcs.txt')
    truth_table = read_file('truth_table.txt')
    truth_table_map = create_truth_table_map(truth_table)
    
    polarized_arcs = assign_arcs_polarity(arcs, truth_table_map)
    write_file('polarized_arcs.txt', polarized_arcs)

if __name__ == "__main__":
    main()
