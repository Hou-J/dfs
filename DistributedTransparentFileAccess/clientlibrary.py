import requests, json

class clientLibrary():
    def fileLists(self):
        r = requests.get("http://127.0.0.1:8888/fileList")
        # print(json.loads(r.text))
        filelists = json.loads(r.text)

        print("------------action start---------------")
        print("File List:\n")
        for filename in filelists:
            print(filename)
        print("\n-------------action end----------------")

    def readFile(self,fileName):
        r = requests.get("http://127.0.0.1:8888/file/{}".format(fileName))
        data = json.loads(r.text)

        print("--------------file start-----------------")
        for d in data:
            print(d,end='')
        print("\n---------------file end------------------")