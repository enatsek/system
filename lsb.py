#!/usr/bin/env python3

def distro_version():
    d = {}
    try:
        with open("/etc/os-release") as f:
            for line in f:
                line = line.replace('"', '')
                line = line.replace('\n', '')
                if line == "":
                    continue
                (key, val) = line.split("=")
                d[(key)] = val
        distro = d["NAME"]
        version = d["VERSION_ID"]
    except:
        distro = "Other"
        version = "Other"
    return distro, version

distro, version = distro_version()
print("---"+distro+"---"+version+"---")
