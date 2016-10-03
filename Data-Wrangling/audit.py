"""
Your task in this exercise has two steps:
- audit the OSMFILE and change the variable 'mapping' to reflect the changes needed to fix
    the unexpected street types to the appropriate ones in the expected list.
    You have to add mappings only for the actual problems you find in this OSMFILE,
    not a generalized solution, since that may and will depend on the particular area you are auditing.
- write the update_name function, to actually fix the street name.
    The function takes a string with street name as an argument and should return the fixed name
    We have provided a simple test so that you see what exactly is expected
"""
import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

OSMFILE = '/Users/Baid/Desktop/denver.osm'
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)


expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road",
            "Trail", "Parkway", "Commons", "Close", "Circle", "Lorong", "Crescent", "Hill", "Highway", "Heights", "Link", "Loop", "Park", "Terrace", "View", "Walk", "Way"]

# UPDATE THIS VARIABLE
mapping = { "E": "East",
            "W": "West",
            "N": "North",
            "S": "South",
            "Rd": "Road",
            "Rd.": "Road",
            "ln": "Lane",
            "ln.": "Lane",
            "Ln": "Lane",
            "Ln.": "Lane",
            "Dr": "Drive",
            "Dr.": "Drive",
            "St": "Street",
            "Ste": "Suite",
            "Ste.": "Suite",
            "Cir": "Circle",
            "Ave": "Avenue",
            "Ave.": "Avenue",
            "Hwy": "Highway",
            "Hwy.": "Highway",
            "Pky": "Parkway",
            "Pky.": "Parkway",
            "Fwy": "Freeway",
            "Fwy.": "Freeway",
            "Blvd": "Boulevard",
            "Blvd.": "Boulevard"
            }


def audit_street_type(street_types, street_name):
    """
    Adds potentially problematic street names to
    list 'street_types'.
    """
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)


def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")

def is_zipcode(elem):
    return (elem.attrib['k'] == "addr:postcode")

def audit_zipcode(v):
    """
       Reduces postcodes to 5 digit strings. Some zips take the form
    'CO-12345' or '12345-6789'. It transforms them to 5 digit zip codes only
    """
    postcode = ''
    for char in v:
        if char.isdigit():
            postcode += char
        if len(postcode) == 5:
            break
    return postcode



def audit(osmfile):
    """
    Returns a list of problematic street type values
    for use with the update() name mapping.
    """
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    
    for event, elem in ET.iterparse(osm_file, events=("start",)):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])
                if (is_zipcode(tag)) & (len(tag.attrib['v']) > 5):
                    #print(tag.attrib['v'])
                    tag.attrib['v']=audit_zipcode(tag.attrib['v'])
                    #print(tag.attrib['v'])
    osm_file.close()
    return street_types


def update_name(name, mapping):
    """
    If the last substring of string 'name' is an int,
    updates all substrings in 'name', else updates
    only the last substring.
    """
    # YOUR CODE HERE
    m = street_type_re.search(name)
    m = m.group()
    # Fix all substrings in an address ending with a number.
    # Example: 'S Tryon St Ste 105' to 'South Tryon Street Suite 105'
    try:
        __ = int(m)
        words = name.split()[:-1]
        for w in range(len(words)):
            if words[w] in mapping:
                words[w] = mapping[words[w]]
        words.append(m)
        address = " ".join(words)
        return address
    # Otherwise, fix only the last substring in the address
    # Example: 'This St.' to 'This Street'
    except ValueError:        
        i = name.index(m)
        if m in mapping:
            name = name[:i] + mapping[m]
    return name

def test():
    st_types = audit(OSMFILE)
    pprint.pprint(dict(st_types))

    for st_type, ways in st_types.items():
        for name in ways:
            better_name = update_name(name, mapping)
            print (name, "=>", better_name)


if __name__ == '__main__':
    test()