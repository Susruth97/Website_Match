import json
import delete
import urls
import screens
import compare

if __name__ == "__main__" :

    with open('./config.json', 'r') as f :
        path_data = json.load(f)

    source1 = path_data['source1']
    source2 = path_data['source2']
    destination = path_data['destination']
    xml1_path = path_data['xml1_path']
    xml2_path = path_data['xml2_path']
    username = path_data['username']
    password = path_data['password']

    delete.empty_folders(source1, source2, destination)
    urls1, urls2, names1, names2 = urls.get_urls(xml1_path, xml2_path)
    screens.get_screenShots(urls1, urls2, names1, names2, source1, source2, username, password)
    compare.match_images(source1, source2, destination)




