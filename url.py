import xml.etree.ElementTree as etree

urls = []
names = []
def get_url() :

    tree = etree.parse('test.xml')  # change to input.xml
    root = tree.getroot()

    for child in root:
        urls.append(child.find('URL').text)
        names.append(child.find('UniqueId').text)

get_url()
print(urls)
print(len(urls))
print(names)
print(len(names))

