import os

def empty_folders (source1, source2, destination) :

    try :
        for f in os.listdir(source1):
            if f.endswith(".png"):
                os.remove(os.path.join(source1, f))

        for f in os.listdir(source2):
            if f.endswith(".png"):
                os.remove(os.path.join(source2, f))

        for f in os.listdir(destination):
            if f.endswith(".png"):
                os.remove(os.path.join(destination, f))
    except Exception as e :
        print("Deleting Output Folders :",e)