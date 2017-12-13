from flask import Flask
from flask_restful import Resource, Api, reqparse
import os, sys, subprocess

# if (len(sys.argv) < 2):
#     print("Server usage: python Server.py [PORT]")
#     sys.exit(0)

app = Flask(__name__)
api = Api(app)


class serverFileList(Resource):
    def get(self):
        return files_list

    def post(self):
        r = reqparse.RequestParser()
        r.add_argument('fileName', type=str, location='json')
        r.add_argument('data', type=str, location='json')
        print(r.parse_args()['fileName'], "to add.")
        filename = r.parse_args()['fileName']
        files_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "files")
        f = [f for f in files_list if f == filename]
        if len(f) != 0:
            return False
        files_list.append(filename)
        addFilePath = os.path.join(files_path, filename)
        print(addFilePath)
        addFile = open(addFilePath, 'w')
        addFile.write(r.parse_args()['data'])
        addFile.close()
        with open(os.path.join(files_path, filename)) as f:
            data = f.readlines()
        return data


class serverfile(Resource):
    def get(self, filename):
        files_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "files")
        f = [f for f in files_list if f == filename]
        if len(f) == 0:
            return False
        with open(os.path.join(files_path, filename)) as f:
            data = f.readlines()
        return data

    def put(self, filename):
        r = reqparse.RequestParser()
        r.add_argument('data', type=str, location='json')
        files_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "files")
        f = [f for f in files_list if f == filename]
        if len(f) == 0:
            return False
        editFilePath = os.path.join(files_path, filename)
        print(editFilePath)
        currentFile = open(editFilePath, 'w')
        currentFile.write(r.parse_args()['data'])
        currentFile.close()
        with open(os.path.join(files_path, filename)) as f:
            data = f.readlines()
        return data

    def delete(self, filename):
        files_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "files")
        f = [f for f in files_list if f == filename]
        if len(f) == 0:
            return False
        deleteFilePath = os.path.join(files_path, filename)
        print(deleteFilePath)
        os.remove(deleteFilePath)
        files_list.remove(files_list.index(filename))
        return True

class folder(Resource):
    def get(self):
        return dir_list

    def post(self):
        r = reqparse.RequestParser()
        r.add_argument('folderName', type=str, location='json')
        newdir = r.parse_args()['folderName']
        print(newdir, "to add.")
        # print(dir_list)
        d = [d for d in dir_list if d == newdir]
        if len(d) != 0:
            return False
        os.makedirs(os.path.join(files_path,newdir))
        dir_list.append(newdir)
        return True

    def put(self):
        pass

    def delete(self):
        pass

# def joinPathAndFile(file):
#     fileGet = []
#     for f in files_list:
#         f_dir = str(f.split('@\./@')[0])
#         f_file = str(f.split('@\./@')[1])
#         if f_file == file:
#             fileGet.append(os.path.join(f_dir,f_file))
#     return fileGet


api.add_resource(serverFileList, '/fileList')
api.add_resource(serverfile, '/file/<string:filename>')
api.add_resource(folder, '/folder')

if __name__ == '__main__':
    root_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "files")
    files_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "files")
    print(files_path)
    dir_list = []
    files_list = []

    for dirName, subdirList, fileList in os.walk(files_path):
        print('Dir: root{}'.format(dirName[dirName.rfind(files_path) + len(files_path):]))
        dir_list.append(dirName[dirName.rfind(files_path) + len(files_path)+1:])
        for fname in fileList:
            print('\t{}'.format(fname))
            # files_list.append('{}@\./@{}'.format(dirName[dirName.rfind(files_path) + len(files_path):], fname))
            files_list.append(os.path.join(dirName,fname)[os.path.join(files_path,fname).rfind(root_path)+len(root_path)+1:])
        print()
    # print(len(files_list))

    name = 'hat.txt'
    # print(joinPathAndFile(name))
    # for d in dir_list:
    #     print(d)
    #
    for f in files_list:
        print(f)
        # if f.split('@\./@')[1] == name:
        #     print('!!')
    app.run(host="0.0.0.0", port=int(5555))
