import xml.etree.ElementTree as ET
import pprint
import re
import codecs
import json
"""
Your task is to wrangle the data and transform the shape of the data
into the model we mentioned earlier. The output should be a list of dictionaries
that look like this:
{
"id": "2406124091",
"type: "node",
"visible":"true",
"created": {
          "version":"2",
          "changeset":"17206049",
          "timestamp":"2013-08-03T16:43:42Z",
          "user":"linuxUser16",
          "uid":"1219059"
        },
"pos": [41.9757030, -87.6921867],
"address": {
          "housenumber": "5157",
          "postcode": "60625",
          "street": "North Lincoln Ave"
        },
"amenity": "restaurant",
"cuisine": "mexican",
"name": "La Cabana De Don Luis",
"phone": "1 (773)-271-5176"
}
You have to complete the function 'shape_element'.
We have provided a function that will parse the map file, and call the function with the element
as an argument. You should return a dictionary, containing the shaped data for that element.
We have also provided a way to save the data in a file, so that you could use
mongoimport later on to import the shaped data into MongoDB. You could also do some cleaning
before doing that, like in the previous exercise, but for this exercise you just have to
shape the structure.
In particular the following things should be done:
- you should process only 2 types of top level tags: "node" and "way"
- all attributes of "node" and "way" should be turned into regular key/value pairs, except:
    - attributes in the CREATED array should be added under a key "created"
    - attributes for latitude and longitude should be added to a "pos" array,
      for use in geospacial indexing. Make sure the values inside "pos" array are floats
      and not strings. 
- if second level tag "k" value contains problematic characters, it should be ignored
- if second level tag "k" value starts with "addr:", it should be added to a dictionary "address"
- if second level tag "k" value does not start with "addr:", but contains ":", you can process it
  same as any other tag.
- if there is a second ":" that separates the type/direction of a street,
  the tag should be ignored, for example:
<tag k="addr:housenumber" v="5158"/>
<tag k="addr:street" v="North Lincoln Avenue"/>
<tag k="addr:street:name" v="Lincoln"/>
<tag k="addr:street:prefix" v="North"/>
<tag k="addr:street:type" v="Avenue"/>
<tag k="amenity" v="pharmacy"/>
  should be turned into:
{...
"address": {
    "housenumber": 5158,
    "street": "North Lincoln Avenue"
}
"amenity": "pharmacy",
...
}
- for "way" specifically:
  <nd ref="305896090"/>
  <nd ref="1719825889"/>
should be turned into
"node_refs": ["305896090", "1719825889"]
"""


lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

CREATED = [ "version", "changeset", "timestamp", "user", "uid"]


def shape_element(element):
    """
    Takes an XML tag as input and returns a cleaned and reshaped
    dictionary for JSON ouput. If the element contains an abbreviated
    street name, it returns with an updated full street name.
    """
    node = {}

    if element.tag == "node" or element.tag == "way" :

      node['type'] = element.tag

      # Parse attributes
      for a in element.attrib:
        if a in CREATED:
          if 'created' not in node:
            node['created'] = {}
          node['created'][a] = element.attrib[a]

        elif a in ['lat', 'lon']:
          if 'pos' not in node:
            node['pos'] = [None, None]

          if a == 'lat':
            node['pos'][0] = float(element.attrib[a])
          else:
            node['pos'][1] = float(element.attrib[a])

        else:
          node[a] = element.attrib[a]

      # Iterate tag children
      for tag in element.iter("tag"):
        if not problemchars.search(tag.attrib['k']):
          # Tags with single colon
          if lower_colon.search(tag.attrib['k']):

            # Single colon beginning with addr
            if tag.attrib['k'].find('addr') == 0:
              if 'address' not in node:
                node['address'] = {}

              sub_attr = tag.attrib['k'].split(':', 1)
              node['address'][sub_attr[1]] = tag.attrib['v']

            # All other single colons processed normally
            else:
              node[tag.attrib['k']] = tag.attrib['v']

          # Tags with no colon
          elif tag.attrib['k'].find(':') == -1:
            node[tag.attrib['k']] = tag.attrib['v']

      # Iterate nd children
      for nd in element.iter("nd"):
        if 'node_refs' not in node:
          node['node_refs'] = []
        node['node_refs'].append(nd.attrib['ref'])

      return node
    else:
      return None


def process_map(file_in, pretty = False):
    """
    Outputs a JSON file with the above structure.
    Returns the data as a list of dictionaries.
    """
    file_out = "{0}.json".format(file_in)
    data = []
    with codecs.open(file_out, "w") as fo:
        for _, element in ET.iterparse(file_in):
            el = shape_element(element)
            if el:
                data.append(el)
                if pretty:
                    fo.write(json.dumps(el, indent=2)+"\n")
                else:
                    fo.write(json.dumps(el) + "\n")
    return data

def test():
    # NOTE: if you are running this code on your computer, with a larger dataset, 
    # call the process_map procedure with pretty=False. The pretty=True option adds 
    # additional spaces to the output, making it significantly larger.
    data = process_map('/Users/Baid/Desktop/denver.osm', True)
    pprint.pprint(data)

if __name__ == "__main__":
    test()