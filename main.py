import sys,os
import ConfigParser

configPath = sys.argv[1]
if configPath == "":
    print "need config path"
    exit()

rootPath = os.getcwd() + "/"

cf = ConfigParser.ConfigParser()
cf.read(configPath)

libName = cf.get("proto", "group_name")
protoFile = cf.get("proto", "proto_list");
tmpDir = rootPath + cf.get("dir", "tmp_dir");
outputDir = rootPath + cf.get("dir", "output_dir");
protoDir = rootPath + cf.get("dir", "proto_dir");

os.system("rm " + tmpDir + "/* -rf")
os.system("rm " + outputDir + "/* -rf")

protocCmd = "cd " + protoDir + " && protoc *.proto" + " --cpp_out=" + tmpDir
makeCmd = "cd " + tmpDir + " && gcc -c *.cc -I../include -O2 -fPIC -g -Wall && ar rcs " + outputDir +  "/lib" + libName + ".a *.o"
copyCmd = "cp " + tmpDir + "/*.h " + outputDir

protocRet = os.system(protocCmd)

if (protocRet != 0):
    print "error in protoc"

makeRet = os.system(makeCmd)
makeRet = os.system(copyCmd)

# print makeCmd
