#! /usr/bin/env python3
import os
import argparse


def structure_alignment(
        changed_pdb,
        unchanged_pdb,
        select_para,
        log_file,
        out_pdb=""):
    if not out_pdb:
        superpose = "superpose " + changed_pdb + " -s " + select_para + " " + \
                    unchanged_pdb + " >" + log_file + " 2>&1"
    else:
        superpose = "superpose " + changed_pdb + " -s " + select_para + " " + \
                    unchanged_pdb + " -o " + out_pdb + " >" + log_file + " 2>&1"
    print("Use CCP4i superpose to run structure alignment...")
    print("Run：" + superpose)
    os.system(superpose)
    print("Finish structure alignment!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="This module is for structure alignment")
    parser.add_argument(
        "-c",
        "--changed_pdb",
        help="-c /../changed.pdb: The PDB will be changed"
        " from b-factor to RMSD",
        required=True)
    parser.add_argument(
        "-u",
        "--unchanged_pdb",
        help="-u /../unchanged.pdb: The PDB "
        "will stay the same",
        required=True)
    parser.add_argument(
        "-s",
        "--selected_parameter",
        help="-s selected element names,"
        "default:CA[C]",
        default="CA[C]",
        type=str)
    parser.add_argument(
        "-o",
        "--output_pdb",
        help="-o /../output.pdb: The PDB will only be changed "
        "x、y、z location from unchanged_pdb,default:null",
        default="",
        type=str)
    parser.add_argument(
        "-l",
        "--log_file",
        help="-l /../result.log: The path of result log,"
        "default:result.log",
        default="result.log",
        type=str)
    options = parser.parse_args()
    changed_pdb = options.changed_pdb
    unchanged_pdb = options.unchangend_pdb
    select_para = options.selected_parameter
    log_file = options.log_file
    out_pdb = options.output_pdb
    structure_alignment(
        changed_pdb,
        unchanged_pdb,
        select_para,
        log_file,
        out_pdb)
