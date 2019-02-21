import xml.etree.ElementTree as etree

urls1 = []
urls2 = []
names1 = []
names2 = []
type = ""

def get_urls(xml1_path, xml2_path) :

    try :
        tree1 = etree.parse(xml1_path)
        root1 = tree1.getroot()
        tree2 = etree.parse(xml2_path)
        root2 = tree2.getroot()

        type = root1[0].find('ReportType').text

        for child1 in root1 :
            urls1.append(child1.find('URL').text)
            names1.append(child1.find('UniqueId').text)

        for child2 in root2 :
            urls2.append(child2.find('URL').text)
            names2.append(child2.find('UniqueId').text)

        if len(urls1) != len(urls2) :
            raise Exception ("Number of Urls in both Xmls did'nt match")

    except Exception as e :
        print("Parsing Xml :",e)

    print("Total Input URLs :", len(urls1)+len(urls2))
    return urls1, urls2, names1, names2, type
