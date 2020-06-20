#! /usr/bin/env python3
import collections
import argparse
import json


def get_value_list_location(my_value, my_list):
    my_loc = []
    for item in enumerate(my_list):
        if item[1] == my_value:
            my_loc.append(item[0])
    return my_loc[-1]


def change_rmsd_dic_range(rmsd_dic, times):
    rmsd_mutiple_dic = collections.OrderedDict()
    for aa_number in rmsd_dic.keys():
        rmsd_value = float(rmsd_dic[aa_number])
        rmsd_mutiple_dic[aa_number] = round(int(times) * rmsd_value, 2)
    print("Multiple a number to RMSD...")
    return rmsd_mutiple_dic


def get_max_rmsd(rmsd_dic, times, plus_value=10):
    rmsd_list = [float(i) * int(times) for i in list(rmsd_dic.values())]
    rmsd_max = max(rmsd_list)
    rmsd_max_plus_value = round(rmsd_max + plus_value, 2)
    print("Add a number to Max RMSD...")
    return rmsd_max_plus_value


def change_pdb(
        default_pdb_path,
        rmsd_mutiple_dic,
        rmsd_max_plus_value,
        rmsd_pdb_path):
    with open(rmsd_pdb_path, "w") as rpp:
        with open(default_pdb_path) as dpp:
            for line in dpp:
                if (line[0:4] == "ATOM" and len(line.split()) > 6):
                    aa_number = line[21] + "_" + \
                        line[17:20] + line[22:26].strip()
                    if aa_number in rmsd_mutiple_dic.keys():
                        rmsd_len = len(str(rmsd_mutiple_dic[aa_number]))
                        mid_line = (6 - rmsd_len) * " " + \
                            str(rmsd_mutiple_dic[aa_number])
                        new_line = line[0:60] + mid_line + line[66:]
                    else:
                        rmsd_len = len(str(rmsd_max_plus_value))
                        mid_line = (6 - rmsd_len) * " " + \
                            str(rmsd_max_plus_value)
                        new_line = line[0:60] + mid_line + line[66:]
                    rpp.write(new_line)
                elif line[0:6] == "ANISOU":
                    pass
                else:
                    rpp.write(line)
    print("change pdb B-factor to RMSD...")
    print("Finish Mission !")


def change_pdb_all(
        rmsd_dic,
        times,
        default_pdb_path,
        rmsd_pdb_path,
        plus_value=10):
    rmsd_mutiple_dic = change_rmsd_dic_range(rmsd_dic, times)
    rmsd_max_plus_value = get_max_rmsd(rmsd_dic, times, plus_value)
    change_pdb(
        default_pdb_path,
        rmsd_mutiple_dic,
        rmsd_max_plus_value,
        rmsd_pdb_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="This module is for change pdb b-factor to RMSD")
    parser.add_argument(
        "-j",
        "--rmsd_json",
        help="-j /../rmsd.json: The path of rmsd json,default:rmsd.json",
        default="rmsd.json")
    parser.add_argument(
        "-t",
        "--times",
        help="-t times: The times you want to mutiple RMSD,default:40",
        default=40,
        type=int)
    parser.add_argument(
        "-p",
        "--plus_value",
        help="-p plus_value:plus value to max RMSD,default:10",
        default=10,
        type=int)
    parser.add_argument(
        "-d",
        "--default_pdb",
        help="-d /../default.pdb: The initial PDB",
        required=True)
    parser.add_argument(
        "-f",
        "--rmsd_pdb",
        help="-f /../rmsd.pdb: The path of final rmsd pdb,default:rmsd.pdb",
        default="rmsd.pdb")
    options = parser.parse_args()
    rmsd_json = options.rmsd_json
    js = open(rmsd_json)
    rmsd_dic = json.load(js)
    times = options.times
    plus_value = options.plus_value
    default_pdb_path = options.default_pdb
    rmsd_pdb_path = options.rmsd_pdb
    rmsd_mutiple_dic = change_rmsd_dic_range(rmsd_dic, times)
    rmsd_max_plus_value = get_max_rmsd(rmsd_dic, times, plus_value)
    change_pdb(
        default_pdb_path,
        rmsd_mutiple_dic,
        rmsd_max_plus_value,
        rmsd_pdb_path)
