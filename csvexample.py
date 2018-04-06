import csv
#----------------------------------------------------------------------
def csv_reader(file_obj):
    """
    Read a csv file
    """
    reader = csv.reader(file_obj)
    for row in reader:
        print(" ".join(row))
#----------------------------------------------------------------------
if __name__ == "__main__":
    # csv_path = "home/vineet/Documents/vineet/python/class1130/TB_data_dictionary_2014-02-26.csv"
    with open('data2.csv', "r") as f_obj:
        csv_reader(f_obj)