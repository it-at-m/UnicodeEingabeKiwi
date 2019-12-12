#!/usr/bin/python3

import re
import sys
import logging
import xml.etree.ElementTree


ns = {
    'sl': 'http://muenchen.de/stringlatin/'
}


def getCase(c):
    if c.islower():
        return 'L'
    elif c.isupper():
        return 'U'
    else :
        return None


def main():
    logging.basicConfig(level=logging.DEBUG)

    xmlFile = sys.argv[1]
    logging.debug("Parsing model file {}".format(xmlFile));
    xmlDoc = xml.etree.ElementTree.parse(xmlFile)
    root = xmlDoc.getroot()

    # xsdFile = sys.argv[2]
    # schemaDoc = xml.etree.ElementTree.parse(xsdFile)
    # xmlSchema = etree.XMLSchema(schemaDoc)
    # if xmlschema.validate(xml_doc):
    #     logging.info("xml model document is valid")
    # else:
    #     logging.error("xml model document is invalid")


    for c in root.findall('.//sl:char', ns):
        name = c.get('name')
        logging.info('==================== {} ===================='.format(name))

        if not name.isalpha():
            logging.info('Not a char -- skipping.')
            continue

        for bc in c.findall('.//sl:basechar', ns):
            bcnameci = bc.get('name-ci')
            if not bcnameci.islower():
                logging.error("name-ci is not lower-case")

            bcname = bc.get('name')
            if getCase(name) != getCase(bcname):
                logging.error("name does not match case of char.")


if __name__ == "__main__":
    main()
