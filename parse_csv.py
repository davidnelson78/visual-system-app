import csv
from collections import defaultdict

incompatable_phrasings = ['Not Compatible']
semicompatable_phrasings = ['May be Compatible','No known issues or dependencies']
compatibale_phrasings = ['Compatible']
outstanding_anomaly_phrasings = ['Known Anomaly']
fixed_anomaly_phrasings = ['Corrected Anomaly']

compatability_category_phrasings = ['Compatibility']
features_services_category_phrasings = ['Rockwell Services', 'Features', 'Virtualization', 'Redundancy']
OS_category_phrasings = ['Operating Systems']
migration_category_phrasing = ['Firmware Migration', 'Module Replacement']
anomaly_category_phrasing = ['Anomaly']

class Category:
    def __init__(self):
        self.types = {
            'incompatabilities': defaultdict(list),
            'semicompatabilities': defaultdict(list),
            'compatabilities': defaultdict(list),
            'outstanding_anomolies': defaultdict(list),
            'fixed_anomolies': defaultdict(list),
            }

class CategoryCollection:
    def __init__(self):
        self.types = {
            'compatability' : Category(),
            'features and services' : Category(),
            'operating systems' : Category(),
            'migration' : Category(),
            'anomaly' : Category()
        }

def print_dictionary(my_dictionary, print_string):
    for key in my_dictionary:
        print("%s %s" % (key, print_string), end ='')
        for item in my_dictionary[key]:
            print('; %s' % (item), end ='')
        print() # prints newline

def simple_compatability_score(my_category):
    score = 1
    incompatabilities_number = 0
    compatabilities_number = 0
    total_possible = 0
    for each in my_category.types['incompatabilities']:
        incompatabilities_number += len(my_category.types['incompatabilities'][each])
    for each in my_category.types['compatabilities']:
        compatabilities_number += len(my_category.types['compatabilities'][each])
    total_possible = incompatabilities_number + compatabilities_number
    
    if total_possible != 0:
        score = compatabilities_number / total_possible
    return score

def populate_dictionary(my_category, item, col_names, col_num, row_name):
    phrase = ''
    if any(phrase in item for phrase in incompatable_phrasings):
        my_category.types['incompatabilities'][col_names[col_num]].append(row_name)
    elif any(phrase in item for phrase in semicompatable_phrasings):
        my_category.types['semicompatabilities'][col_names[col_num]].append(row_name)
    elif any(phrase in item for phrase in compatibale_phrasings):
        my_category.types['compatabilities'][col_names[col_num]].append(row_name)
    elif any(phrase in item for phrase in outstanding_anomaly_phrasings):
        my_category.types['outstanding_anomolies'][col_names[col_num]].append(row_name)
    elif any(phrase in item for phrease in fixed_anomaly_phrasings):
        my_category.types['fixed_anomolies'][col_names[col_num]].append(row_name)

def populate_dictionary_flipped(my_category, item, col_names, col_num, row_name):
    phrase = ''
    if any(phrase in item for phrase in incompatable_phrasings):
        my_category.types['incompatabilities'][row_name].append(col_names[col_num])
    elif any(phrase in item for phrase in semicompatable_phrasings):
        my_category.types['semicompatabilities'][row_name].append(col_names[col_num])
    elif any(phrase in item for phrase in compatibale_phrasings):
        my_category.types['compatabilities'][row_name].append(col_names[col_num])
    elif any(phrase in item for phrase in outstanding_anomaly_phrasings):
        my_category.types['outstanding_anomolies'][row_name].append(col_names[col_num])
    elif any(phrase in item for phrease in fixed_anomaly_phrasings):
        my_category.types['fixed_anomolies'][row_name].append(col_names[col_num])

def select_category(all_categories, item, col_names, col_num, row_name, row_category):
    phrase = ''
    if any(phrase in row_category for phrase in compatability_category_phrasings):
        populate_dictionary(all_categories.types['compatability'], item, col_names, col_num, row_name)
    elif any(phrase in row_category for phrase in features_services_category_phrasings):
        populate_dictionary(all_categories.types['features and services'], item, col_names, col_num, row_name)
    elif any(phrase in row_category for phrase in OS_category_phrasings):
        populate_dictionary_flipped(all_categories.types['operating systems'], item, col_names, col_num, row_name)
    elif any(phrase in row_category for phrase in features_services_category_phrasings):
        populate_dictionary(all_categories.types['features and services'], item, col_names, col_num, row_name)
    elif any(phrase in row_category for phrase in anomaly_category_phrasing):
        populate_dictionary(all_categories.types['anomaly'], item, col_names, col_num, row_name)
    

def parse_csv(csv_filename):
    my_collection = CategoryCollection()
    print('Processing %s' % (csv_filename))
    row_num = 0
    row_size = 0
    col_num = 0
    col_names = []
    col_series = []
    col_version = []
    col_full_name = []

    col_names.append('Category')
    col_names.append('Name')
    col_full_name = col_names
    col_series.append('')
    col_series.append('')
    col_version.append('')
    col_version.append('')

    with open(csv_filename, encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if row_num == 0:
                col_num = 0
                for item in row:
                    if col_num >= len(col_names): # lazy way to tell it to ignore blank columns at the front, while keeping it expandable
                        col_names.append(item)
                        col_full_name.append(item)
                    col_num += 1
            if row_num == 1:
                col_num = 0
                for item in row:
                    if col_num >= len(col_series): # lazy way to tell it to ignore blank columns at the front, while keeping it expandable
                        col_series.append(item)
                    if col_series[col_num] != '':
                        col_full_name[col_num] = col_full_name[col_num] + ' ' + col_series[col_num]
                    col_num += 1
            if row_num == 2:
                col_num = 0
                for item in row:
                    if col_num >= len(col_version): # lazy way to tell it to ignore blank columns at the front, while keeping it expandable
                        col_version.append(item)
                    if col_version[col_num] != '':
                        col_full_name[col_num] = col_full_name[col_num] + ' ' + col_version[col_num]
                    col_num += 1
            if row_num == 3:
                pass
                # lifecycle
            else:
                # print('Line Num: %i' % row_num)
                col_num = 0 # initialize col count
                row_category = ''
                row_name = ''
                phrase = ''
                for item in row:
                    if col_num == 0:
                        row_category = item
                    elif col_num == 1:
                        row_name = item
                    else:
                        select_category(my_collection, item, col_full_name, col_num, row_name, row_category)
                    col_num += 1 # keep track of what col we are in
            row_num += 1
        
        #print_dictionary(test_category.types['incompatabilities'], 'is incompatible with')
        #print_dictionary(test_category.types['outstanding_anomolies'], 'has known anomilies')

        return my_collection



#if __name__ == "__main__":
#    print('Enter File Name: ')
#    csv_filename = input()
#    parsed_dict = parse_csv(csv_filename)
#    
#    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
#    print('Software and Hardware Compatability')
#    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
#    score_compatability = simple_compatability_score(parsed_dict.types['compatability'])
#    print('Compatability score of %.2f %%' % (score_compatability*100))
#    print_dictionary(parsed_dict.types['compatability'].types['incompatabilities'], 'is incompatible with')
#    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
#    print('Features and Services Compatabilty')
#    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
#    score_features = simple_compatability_score(parsed_dict.types['features and services'])
#    print('Compatability score of %.2f %%' % (score_features*100))
#    print_dictionary(parsed_dict.types['features and services'].types['incompatabilities'], 'is incompatible with')
#    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
#    print('Operating Systems')
#    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
#    print_dictionary(parsed_dict.types['operating systems'].types['incompatabilities'], 'is incompatible with')
#    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
#    print('Known Anomilies')
#    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
#    print_dictionary(parsed_dict.types['anomaly'].types['outstanding_anomolies'], 'has known anomaly')

