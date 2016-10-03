def ratiosPOI(data_dict, features_list):
    fields = ['to_messages', 'from_messages',
              'from_poi_to_this_person', 'from_this_person_to_poi']
    for record in data_dict:
        person = data_dict[record]
        is_valid = True
        for field in fields:
            if person[field] == 'NaN':
                is_valid = False
        if is_valid:
            total_messages = person['to_messages'] +\
                             person['from_messages']
            poi_messages = person['from_poi_to_this_person'] +\
                           person['from_this_person_to_poi']
            person['ratios_poi'] = float(poi_messages) / total_messages
        else:
            person['ratios_poi'] = 'NaN'
    features_list += ['ratios_poi']

def totalFinance(data_dict, features_list):
    fields = ['total_stock_value', 'exercised_stock_options', 'salary']
    for record in data_dict:
        person = data_dict[record]
        is_valid = True
        for field in fields:
            if person[field] == 'NaN':
                is_valid = False
        if is_valid:
            person['total_finance'] = sum([person[field] for field in fields])
        else:
            person['total_finance'] = 'NaN'
    features_list += ['total_finance']