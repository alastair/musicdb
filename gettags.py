import subprocess
import sys
import os
import json

def processdir(source, target, root, files):
    tree = root[len(source):]
    t = os.path.join(target, tree)
    os.makedirs(t)
    for f in files:
        p = ['/home/pi/taglib/build/examples/tagreader', os.path.join(root, f)]
        proc = subprocess.Popen(p, stdout=subprocess.PIPE)
        out, err = proc.communicate()
        res = {}
        if not out:
            continue
        for l in out.split(chr(30)):
            parts = l.split(chr(29))
            k = parts[0]
            if not k: # might be blank
                continue
            v = "\t".join(parts[1:])
            if k in res and not isinstance(res[k], list):
                res[k] = [res[k]]
                res[k].append(v)
            elif k in res:
                res[k].append(v)
            else:
                res[k] = v
            fpart, fext = os.path.splitext(f)
            outname = os.path.join(t, "%s.json" % fpart)
            json.dump(res, open(outname, "wb"))

def main(source, target):
    for root, dirs, files in os.walk(source):
        if len(files):
            print os.path.basename(root)
            processdir(source, target, root, files)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
