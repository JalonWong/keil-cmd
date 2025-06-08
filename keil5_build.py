import os
import sys
import subprocess

if __name__ == "__main__":
    keil_path = os.path.dirname(os.path.realpath(__file__))
    uv4 = os.path.join(keil_path, "UV4", "UV4.exe")

    prj_path = os.path.dirname(os.path.realpath(sys.argv[2]))
    log_file = os.path.join(prj_path, "build_log.txt")

    print("Building...")

    cmd = [uv4, "-j0", sys.argv[1], sys.argv[2], "-o", "build_log.txt"]
    print(" ".join(cmd))

    if len(sys.argv) > 3:
        out_name = sys.argv[3]
        out_bin = os.path.realpath(out_name + ".bin")
        if os.path.exists(out_bin):
            os.remove(out_bin)
        out_axf = os.path.realpath(out_name + ".axf")
        if os.path.exists(out_axf):
            os.remove(out_axf)

    ret = subprocess.run(cmd)
    with open(log_file, 'r', encoding='utf-8') as f:
        print(f.read())

    print("Done.")
    exit(ret.returncode)
