#! /usr/bin/env python3
import argparse
import json
import collections

def get_rmsd_value(result_log,rmsd_json):
    rmsd_dic = collections.OrderedDict()
    with open(result_log) as rl:
        for line in rl:
            if line.count("|") == 4:
                chunk_info = line.split("|")
                if (chunk_info[1].strip() and chunk_info[2].strip() and
                        chunk_info[3].strip() and chunk_info[1].strip() != "Query"):
                    aa_number = "_".join(chunk_info[1].strip().split(":")[1].split())
                    aa_rmsd = chunk_info[2].strip().split()[1][0:4]
                    rmsd_dic[aa_number] = aa_rmsd
    with open(rmsd_json,"w") as rmsd_js:
        rmsd_js.write(json.dumps(rmsd_dic, ensure_ascii=False, indent=4, separators=(',', ':')))
    print("Get RMSD !")
    print("Save RMSD to " + rmsd_json)
    return rmsd_dic

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This module is for get rmsd value")
    parser.add_argument("-l", "--log_file", help="-l /../result.log: The path of result log,"
                                                 "default:result.log",default="result.log")
    parser.add_argument("-j", "--rmsd_json", help="-j /../rmsd.json: The path of rmsd json,"
                                                  "default:rmsd.json",default="rmsd.json")
    options = parser.parse_args()
    result_log = options.log_file
    rmsd_json = options.rmsd_json
    rmsd_result = get_rmsd_value(result_log, rmsd_json)