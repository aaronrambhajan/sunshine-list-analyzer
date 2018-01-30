import tkinter.filedialog
import os

"""
    Written in 2017 by Aaron Rambhajan for CUPE 3902.
"""

SIXTEEN = ['PARHAM AARABI,174300.97\n', \
           'JONATHAN ABBATT,221176.44\n', \
           'TAREK ABDELRAHMAN,213677.93\n', \
           'BAHER ABDULHAI,181358.94\n', \
           'SEMERE AB ABIYO,126449.51\n', \
           'CHRISTIAN ABIZAID,116845.02\n', \
           'MOUNIR ABOUHAIDAR,178107.48\n', \
           'ROBERTO ABRAHAM,181070.09\n', \
           'CAROLINE ABRAHAMS,134249.05\n', \
           'LUSINE ABRAHAMYAN,102693.64\n', \
           'IZZELDIN ABUELAISH,347633.46\n', \
           'ALAN ACKERMAN,156819.73\n', \
           'EDGAR JOEL ACOSTA,162093.42\n', \
           'JENNIFER ADAMS PEFFER,116493.75\n', \
           'EMANUEL ADLER,231667.76\n', \
           'RAVIRAJ ADVE,194513.74\n', \
           'PHILIPP AFECHE,246285.49\n', \
           'PANKAJ AGGARWAL,411989.70\n', \
           'ALEXANDRA AGOSTINO,113716.88\n', \
           'AJAY AGRAWAL,401553.48']

FIFTEEN = ['PARHAM AARABI,156586.16\n', \
           'JONATHAN ABBATT,203291.52\n', \
           'TAREK ABDELRAHMAN,191869.60\n', \
           'BAHER ABDULHAI,166699.50\n', \
           'SEMERE AB ABIYO,122114.48\n', \
           'CHRISTIAN ABIZAID,105798.48\n', \
           'MOUNIR ABOUHAIDAR,164069.46\n', \
           'ROBERTO ABRAHAM,165213.96\n', \
           'CAROLINE ABRAHAMS,126921.46\n', \
           'IZZELDIN ABUELAISH,332414.52\n', \
           'ALAN ACKERMAN,142480.50\n', \
           'EDGAR JOEL ACOSTA,147133.02\n', \
           'JENNIFER ADAMS PEFFER,110151.49\n', \
           'EMANUEL ADLER,108385.50\n', \
           'RAVIRAJ ADVE,163632.85\n', \
           'PHILIPP AFECHE,295512.46\n', \
           'PANKAJ AGGARWAL,327826.50\n', \
           'ALEXANDRA AGOSTINO,109176.06\n', \
           'AJAY AGRAWAL,322544.52\n', \
           'ANEIL AGRAWAL,154248.00']
    
################################################################################
############### This is the program that runs all programs... ##################
################################################################################

def main_program(year_one, year_two):
    """ (int, int) -> str

    Takes the input for two user-given years. Returns a comprehensive string
    describing percent change, dollar amount, dollar rate/change, sample size,
    the salary average for year_one and year_two, and the number of unused
    people from the list.

    >>> main_program(2006, 2016)
    The average total salary increase for UofT Sunshine-Listed employees
    between the years of 2006 and 2016 was 45.92%, or $64436.57 in total
    growth and $6443.66 per year. The average salary for 2006 was $140326.26,
    and for 2016 was $204762.84. This search tracked 2156 employees over
    10 years. There were 3344 employees not included in this calculation
    because they were not employed in both years.
    """

    # Converts user str input to int.
    start_year = int(year_one)
    end_year = int(year_two)

    # Create the str location of the corresponding salary data by year.
    local_dir = os.getcwd()
    start_name = local_dir + '/data/' + str(start_year) + '.txt'
    end_name = local_dir + '/data/' + str(end_year) + '.txt'

    # Open the files.
    start_file = open(start_name, 'r')
    end_file = open(end_name, 'r')
                   
    # Make the respective dictionaries.
    early = make_dicts(start_file)
    later = make_dicts(end_file)
    unused = prepare_dicts(early, later, 'count')
    sample_size = len(early) + len(later)
        
    # Creates main variables.
    yr_one_avg = round(dict_crunch(early), 2)
    yr_two_avg = round(dict_crunch(later), 2)
    yr_diff = end_year - start_year
    percent = compare_percent(early, later)
    dollar_amt = compare_dollar_amt(early, later)
    dollar_rate = compare_dollar_rate(dollar_amt, start_year, end_year)
    avg_change = average_change(start_year, end_year)

    # Print statement.
    main_return = "\nThe average total salary increase for UofT Sunshine-Listed \
employees between the years of {0} and {1} was {2}%, changing at an average rate \
of {3}% per year. There was ${4} in overall growth at an average rate of ${5} \
per year. The average salary for {0} was ${6}, and for {1} was ${7}. This \
search tracked {8} employees over {9} years. There were {10} employees not \
included in this calculation because they were not employed in both given \
years.".format(start_year, end_year, percent, avg_change, \
               dollar_amt, dollar_rate, yr_one_avg, yr_two_avg, \
               sample_size, yr_diff, unused)

    print(main_return)

################################################################################
############# Functions that create and prepare the dictionary. ################
################################################################################
    
def make_dicts(year_file):
    """ (file open for reading) -> dict

    Takes the NEW_FORMAT data from .txt file and converts to dictionary.

    >>> make_dicts_two(SIXTEEN)
    {'CAROLINE ABRAHAMS': '134249.05', 'PARHAM AARABI': '174300.97', \
    'JONATHAN ABBATT': '221176.44', 'AJAY AGRAWAL': '401553.48', \
    'MOUNIR ABOUHAIDAR': '178107.48', 'IZZELDIN ABUELAISH': '347633.46', \
    'RAVIRAJ ADVE': '194513.74', 'SEMERE AB ABIYO': '126449.51', \
    'BAHER ABDULHAI': '181358.94', 'CHRISTIAN ABIZAID': '116845.02', \
    'ROBERTO ABRAHAM': '181070.09', 'EMANUEL ADLER': '231667.76', \
    'LUSINE ABRAHAMYAN': '102693.64', 'TAREK ABDELRAHMAN': '213677.93', \
    'PANKAJ AGGARWAL': '411989.70', 'EDGAR JOEL ACOSTA': '162093.42', \
    'ALEXANDRA AGOSTINO': '113716.88', 'ALAN ACKERMAN': '156819.73', \
    'PHILIPP AFECHE': '246285.49', 'JENNIFER ADAMS PEFFER': '116493.75'}
    """
    
    year_dict = {}

    for line in year_file:

        marker = line.index(',')
        name = line[:marker]
        salary = line[marker + 1:].strip()

        year_dict[name] = salary

    return year_dict


def prepare_dicts(start_dict, end_dict, request = ''):
    """ (dict, dict, str) -> list of list of str

    NOTE: request can be either 'COUNT', 'LIST', or blank.
    
    Updates the keys in each dictionary so they do not calculate names not in
    both dictionaries. IOW, asserts that data from both years are being
    calculated using equivalent information (tracking the same people).
    Additionally, returns the number of unused instances from each dict.

    Ex.: If someone is in 2015 but not in 2016, deletes from 2015 dict. If
    someone is in 2016 but not in 2015, deletes from 2016 dict.

    start = {'aaron': 1, 'victoria': 2, 'irwan': 3, 'alex': 4}
    end = {'aaron': 1, 'victoria': 2, 'te': 5, 'alex': 4}
    >>> prepare_two_dicts(start, end, 'count')
    2
    >>> start.keys() == end.keys()
    True
    """
    
    # Retrieves all the keys in a list-like object.
    year_one = start_dict.keys()
    year_two = end_dict.keys()

    # Deleted list accumulators.
    del_start_list = []
    del_end_list = []
    
    # If in START_YEAR but not in END_YEAR, delete from START_YEAR dict.
    for name in year_one:
        if name not in year_two:
            del_start_list.append(name)

    # If in END_YEAR but not in START_YEAR, delete from END_YEAR dict.
    for name in year_two:
        if name not in year_one:
            del_end_list.append(name)

    # Modify the original dictionaries.
    for name in del_start_list:
        del start_dict[name]
    for name in del_end_list:
        del end_dict[name]

    # Return the entries exempted.
    if request.upper() == 'COUNT':
        return len(del_start_list) + len(del_end_list)
    elif request.upper() == 'LIST':
        return [del_start_list, del_end_list]
    else:
        return None


def dict_crunch(year_dict):
    """ (dict of str to int) -> float

    Precondition: Dictionary must already be prepared (as per prepare_dict).

    Calculates the average salary for a given year, rounded to two decimals.
    
    >>> dict_crunch(
    {'IZZELDIN ABUELAISH': '347633.46', 'CHRISTIAN ABIZAID': '116845.02', \
    'TAREK ABDELRAHMAN': '213677.93', 'CAROLINE ABRAHAMS': '134249.05', \
    'ROBERTO ABRAHAM': '181070.09', 'EMANUEL ADLER': '231667.76', \
    'PARHAM AARABI': '174300.97', 'ALAN ACKERMAN': '156819.73', \
    'JONATHAN ABBATT': '221176.44', 'BAHER ABDULHAI': '181358.94', \
    'RAVIRAJ ADVE': '194513.74', 'PANKAJ AGGARWAL': '411989.70', \
    'ALEXANDRA AGOSTINO': '113716.88', 'EDGAR JOEL ACOSTA': '162093.42', \
    'JENNIFER ADAMS PEFFER': '116493.75', 'SEMERE AB ABIYO': '126449.51', \
    'AJAY AGRAWAL': '401553.48', 'MOUNIR ABOUHAIDAR': '178107.48', \
    'PHILIPP AFECHE': '246285.49'})
    205789.6231578947
    >>> dict_crunch(
    {'IZZELDIN ABUELAISH': '332414.52', 'CHRISTIAN ABIZAID': '105798.48', \
    'TAREK ABDELRAHMAN': '191869.60', 'CAROLINE ABRAHAMS': '126921.46', \
    'ROBERTO ABRAHAM': '165213.96', 'PARHAM AARABI': '156586.16', \
    'ALAN ACKERMAN': '142480.50', 'JONATHAN ABBATT': '203291.52', \
    'BAHER ABDULHAI': '166699.50', 'RAVIRAJ ADVE': '163632.85', \
    'PANKAJ AGGARWAL': '327826.50', 'ALEXANDRA AGOSTINO': '109176.06', \
    'EMANUEL ADLER': '108385.50', 'EDGAR JOEL ACOSTA': '147133.02', \
    'JENNIFER ADAMS PEFFER': '110151.49', 'SEMERE AB ABIYO': '122114.48', \
    'AJAY AGRAWAL': '322544.52', 'MOUNIR ABOUHAIDAR': '164069.46', \
    'PHILIPP AFECHE': '295512.46'})
    182801.16
    """

    all_keys = year_dict.keys()
    total = 0

    # Goes through all keys and totals the salaries.
    for name in all_keys:

    # In case of a blank line.
        if name != ' ':
            total += float(year_dict[name])

    return total / len(year_dict)

################################################################################
########################### Mathematical functions. ############################
################################################################################

def compare_percent(early_dict, later_dict):
    """ (dict, dict) -> float

    Returns the percent change between later_dict and early_dict.

    >>> compare_percent(FIFTEEN, SIXTEEN)
    12.58
    >>> compare_percent(/2006, /2016)
    45.92
    """

    early_avg = dict_crunch(early_dict)
    later_avg = dict_crunch(later_dict)
    
    return round((((later_avg / early_avg) - 1) * 100), 2)


def compare_dollar_amt(early_dict, later_dict):
    """ (dict, dict) -> float

    Returns the difference in average salary between two years.
    
    >>> compare_dollar_amt(/2006, /2016)
    64436.57
    >>> compare_dollar_amt(/2014, /2016)
    15245.92    
    """
    
    early_avg = dict_crunch(early_dict)
    later_avg = dict_crunch(later_dict)
    
    return round((later_avg - early_avg), 2)


def compare_dollar_rate(dollar_amt, start_year, end_year):
    """ (float, int, int) -> float

    Returns the average rate of change between two years.
    
    >>> compare_dollar_rate(/2006, /2016)
    6443.66
    >>> compare_dollar_rate(/2014, /2016)
    7622.96
    """

    return round((dollar_amt / (end_year - start_year)), 2)


def average_change(first_year, second_year):
    """ (int, int) -> float

    This function calculates the average change between each individual
    year between start_year and end_year, and returns the overall avg.
    increase.

    >>> average_increase(2014, 2016)
    ...
    >>> average_increase(2006, 2016)
    ...
    """

    file_list = []
    avg_percent = 0
    local_dir = os.getcwd()
    years_to_cover = second_year - first_year

    for year in range(years_to_cover + 1):
        new_year = first_year + year
        new_line = local_dir + '/data/' + str(new_year) + '.txt'
        file_list.append(new_line)
    
    for i in range(len(file_list) - 1):
        file_one = open(file_list[i], 'r')
        file_two = open(file_list[i + 1], 'r')

        early = make_dicts(file_one)
        later = make_dicts(file_two)
        prepare_dicts(early, later)
        
        yearly_percent = compare_percent(early, later)
        avg_percent += yearly_percent
	
    return round((avg_percent / years_to_cover), 2)

################################################################################
################# Testing functions, only for internal use. ####################
################################################################################

def elimination_error(early_year, later_year):
    """ (int, int) -> bool
    
    Adds names to error_list if a name in early_prep dict is in the list
    of erased names from the year of late_prep, or if a name in late_prep
    dict is in the list of erased names from the year of early_prep.
    Returns True if there were items, False if empty (desired).  
    """

    # Get the files.
    start_file = tkinter.filedialog.askopenfile()
    end_file = tkinter.filedialog.askopenfile()
                   
    # Make the respective dictionaries.
    early_dict = make_dicts(start_file)
    later_dict = make_dicts(end_file)
    unused = prepare_dicts(early_dict, later_dict, 'list')
    early_errors = unused[0]
    later_errors = unused[1] 

    # Creates the entire list of errors.
    early_error_count = []
    later_error_count = []

    for name_key in later_dict:
        if name_key in early_errors: 
            early_error_count.append(name_key) 

    for name_key in early_dict:
        if name_key in later_errors:
            later_error_count.append(name_key)

    error_count = [early_error_count, later_error_count]
    decision_numbers = (len(error_count[0]) + len(error_count[1]))

    # If error_count contains incorrect names, display errors.
    if decision_numbers != 0:
        return decision_numbers, error_count
    else:
        print("No errors! Your algorithm doesn't totally suck.")

              
################################################################################
########## One-time scripts for modifying and formatting file data. ############
################################################################################

def rewrite_data(year_file, text_file):
    """ (file open for reading, file open for writing) -> NoneType

    Rewrites data to a .txt file in a format easier for parsing.

    >>> rewrite_data(SIXTEEN)
    >>> SIXTEEN == SIXTEEN_UPDATE
    True
    >>> rewrite_data(FIFTEEN)
    >>> FIFTEEN == FIFTEEN_UPDATE
    True
    """

    for line in year_file:

    # Create the name.
        start = line.index(',')
        end = line.index(',', start + 1)
        first_name = line[start + 1:end]
        last_name = line[:start]
        name_key = first_name + ' ' + last_name

    # Create the salary.
        salary = ''
        for char in line[end:]:
            if char.isnumeric() or char == '.':
                salary += char

    # Write the new line.
        new_line = name_key + ',' + salary + '\n'
        text_file.write(new_line)

    text_file.close()


def rewrite_all(year):
    """ (int) -> NoneType

    Uses year and rewrites .csv file to corresponding .txt.
    """

    # Locate the file.
    old_file = tkinter.filedialog.askopenfile()
    nuu = tkinter.filedialog.askdirectory()
    nuu_file = open(nuu, 'w')

    # Rewrite the file.
    rewrite_data(old_file, nuu_file)


def formatting_magic(year):
    """ (int) -> NoneType

    Reformats file: all caps, no hyphens, punctuation, or double spacing.

    >>> formatting_magic('Ajay  Agrawal,322544.52\n')
    'AJAY AGRAWAL,322544.52\n'
    >>> formatting_magic('Jennifer Adams-Peffer,116493.75\n')
    'JENNIFER ADAMS PEFFER,116493.75\n'
    >>> formatting_magic('J. Stewart Aitchison,252314.64\n')
    'J STEWART AITCHISON,252314.64\n'
    """

    # Prepare files.
    pre = tkinter.filedialog.askopenfile() 
    reformat = tkinter.filedialog.askdirectory()
    post = open(reformat, 'w')

    # Reformat files.
    for line in pre:
        marker = line.index(',')
        temp_new = ''

        # Name reformatting.
        for i in range(len(line[:marker])):
            if line[i] == '-':
                temp_new += ' '
            elif line[i] in '()':
                temp_new += ''
            elif line[i] == '.':
                temp_new += ''
            elif line[i] == ' ' and line[i + 1] == ' ':
                temp_new += ''
            else:
                temp_new += line[i]

        # Add salary.
        temp_new += line[marker:]

        # Writing file.
        post.write(temp_new.upper())
        
    post.close()


def kill_same_name(year_file):
    """ (file open for reading) -> NoneType

    Eliminates all name duplicates within a given datafile.
    """

    list_of_names = []

    for line in year_file:
        
        start = line.index(',')
        end = line.index(',', start + 1)
        first_name = line[start + 1:end]
        last_name = line[:start]
        name_key = first_name + ' ' + last_name

        if name_key not in list_of_names:
            list_of_names.append(name_key)

    return list_of_names
