import xml.etree.ElementTree as etree

urls1 = []
names1 = []
urls2 = []
names2 = []

def get_url(xml1_path, xml2_path) :

    tree1 = etree.parse(xml1_path)
    tree2 = etree.parse(xml2_path)
    root1 = tree1.getroot()
    root2 = tree2.getroot()

    for child1,child2 in root1,root2:
        urls1.append(child1.find('URL').text)
        names1.append(child1.find('UniqueId').text)
        urls2.append(child2.find('URL').text)
        names2.append(child2.find('UniqueId').text)

    print("Total Urls :", len(urls1))
    return urls1, urls2, names1, names2
