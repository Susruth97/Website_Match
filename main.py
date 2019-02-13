import json
#import urls
#import screens
import compare

if __name__ == "__main__" :

    with open('./config.json', 'r') as f :
        path_data = json.load(f)

    source1 = path_data['source1'] + '/*.png'
    source2 = path_data['source2'] + '/*.png'
    destination = path_data['destination']
    xml1_path = path_data['xml1_path']
    xml2_path = path_data['xml2_path']

    #urls1, urls2, names1, names2 = urls.get_url(xml1_path, xml2_path)
    #screens.get_screenShots(urls1, urls2)
    compare.match_images(source1, source2)





