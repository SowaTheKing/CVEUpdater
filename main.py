import requests

from Config import Config
from Logger import Logger
from model.Entry import Entry

logger = Logger(7)


def populate_objects(data):
    logger.info('Populating objects from data dump...')
    returned_objects = []
    for part in data:
        entry = Entry(part['Modified'], part['Published'], part['cvss'], part['cwe'], part['id'], part['last-modified'],
                      part['summary'], part['vulnerable_configuration'])
        returned_objects.append(entry)
        logger.info('Added {0} to collection'.format(entry.id))
    return returned_objects


def main():
    url = 'http://cve.circl.lu/api/last'
    resp = requests.get(url=url)

    try:
        data = resp.json()
        objects = populate_objects(data)
    except ValueError:
        logger.error("Error retriving JSON response!")

    config = Config("last_run.txt")

    for entry in objects:
        if entry.get_last_modified() > config.last_run:
            logger.info("Found new CVS!")
            entry.display()
    config.save_last_run()


if __name__ == "__main__":
    main()
