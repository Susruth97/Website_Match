import json
import delete
import screens_threads
import urls
import screens
import compare

if __name__ == "__main__" :

    try :
        with open('./configC.json', 'r') as f1:
            path_data1 = json.load(f1)

        source1 = path_data1['SourceLocation1']
        source2 = path_data1['SourceLocation2']
        destination = path_data1['DestinationLocation']

        with open('./configP.json', 'r') as f2:
            path_data2 = json.load(f2)

        username = path_data2['v_username']
        password = path_data2['v_password']

        xml1_path = 'input1.xml'
        xml2_path = 'input2.xml'

    except Exception as e :
        print('Parsing Json :',e)

    try :
        delete.empty_folders(source1, source2, destination)
        urls1, urls2, names1, names2, type = urls.get_urls(xml1_path, xml2_path)
        screens.get_screenShots(urls1, urls2, names1, names2, type, source1, source2, username, password)
        compare.match_images(source1, source2, destination)

    except Exception as e :
        print('Calling Functions :', e)


