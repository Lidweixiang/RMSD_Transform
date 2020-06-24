Linux or Unix system

# 1.What RMSD_Transform is used for ？ 
Transform a PDB B-factor to RMSD value

# 2.Download RMSD_Transform
website: https://github.com/Lidweixiang/RMSD_Transform
Click Clone and choose Download ZIP

# 3.Uncompress ZIP package and Install RMSD_Transform
unzip RMSD_Transform-master.zip
cd RMSD_Transform-master/RMSD_Transform-1.0.0
python3 setup.py install

# 4.copy TransformRMSD to /usr/bin and add Authority
cp RMSD_Transform-master/TransformRMSD /usr/bin/ 
chmod u+x /usr/bin/TransformRMSD

# 5.Renew and Uninstall
When the RMSD_Transform need be debugged and has some patches to renew，you need delete old package.
Run:
pip3 uninstall RMSD_Transform
rm -rvf RMSD_Transform-master
rm -rvf /usr/bin/TransformRMSD
Then:
Download and install again

# 6.How to use TransformRMSD？
The TransformRMSD is consisted of four modules.
These modules' names are 
A.alignment:This module is used for structure alignment
B.getrmsd:This module is used for outputting RMSD JSON format file
C.changepdb:This module is used for changing PDB B-factor to RMSD according to RMSD JSON file
D.bfactor_to_rmsd:This module include module A,B,C so you can get your RMSD PDB file directly

You can use module A、B、C in turn to get your RMSD PDB result or you can use module D to get your RMSD PDB result directly.

usage: TransformRMSD module [options]

# 7.Modules options
A.Module alignment options

  -h, --help            show this help message and exit
  -c CHANGED_PDB, --changed_pdb CHANGED_PDB
                        -c /../changed.pdb: The PDB will be changed from
                        b-factor to RMSD
  -u UNCHANGED_PDB, --unchanged_pdb UNCHANGED_PDB
                        -u /../unchanged.pdb: The PDB will stay the same
  -s SELECTED_PARAMETER, --selected_parameter SELECTED_PARAMETER
                        -s selected element names,default:CA[C]
  -o OUTPUT_PDB, --output_pdb OUTPUT_PDB
                        -o /../output.pdb: The PDB will only be changed x、y、z
                        location from unchanged_pdb,default:null
  -l LOG_FILE, --log_file LOG_FILE
                        -l /../result.log: The path of result
                        log,default:result.log

Note:result.log includes structure alignment information.

B.Module getrmsd options

  -h, --help            show this help message and exit
  -l LOG_FILE, --log_file LOG_FILE
                        -l /../result.log: The path of result
                        log,default:result.log
  -j RMSD_JSON, --rmsd_json RMSD_JSON
                        -j /../rmsd.json: The path of rmsd
                        json,default:rmsd.json

Note:-l result.log is from Module alignment result,and -j rmsd.json output is extracted from result.log 

C.Module changepdb options

  -h, --help            show this help message and exit
  -j RMSD_JSON, --rmsd_json RMSD_JSON
                        -j /../rmsd.json: The path of rmsd
                        json,default:rmsd.json
  -t TIMES, --times TIMES
                        -t times: The times you want to mutiple
                        RMSD,default:40
  -p PLUS_VALUE, --plus_value PLUS_VALUE
                        -p plus_value:plus value to max RMSD,default:10
  -d DEFAULT_PDB, --default_pdb DEFAULT_PDB
                        -d /../default.pdb: The initial PDB
  -f RMSD_PDB, --rmsd_pdb RMSD_PDB
                        -f /../rmsd.pdb: The path of final rmsd
                        pdb,default:rmsd.pdb

Note:-j rmsd.json is from Module getrmsd result,and -f rmsd.pdb output is the final result. 

D.Module bfactor_to_rmsd options
  
  -h, --help            show this help message and exit
  -t TIMES, --times TIMES
                        -t times: The times you want to mutiple
                        RMSD,default:40
  -p PLUS_VALUE, --plus_value PLUS_VALUE
                        -p plus_value:plus value to max RMSD,default:10
  -d DEFAULT_PDB, --default_pdb DEFAULT_PDB
                        -d /../default.pdb: The initial PDB
  -f RMSD_PDB, --rmsd_pdb RMSD_PDB
                        -f /../rmsd.pdb: The path of final rmsd
                        pdb,default:rmsd.pdb
  -u UNCHANGED_PDB, --unchanged_pdb UNCHANGED_PDB
                        -u /../unchanged.pdb: The PDB will stay the same
  -s SELECTED_PARAMETER, --selected_parameter SELECTED_PARAMETER
                        -s selected element names,default:CA[C]
  -o OUTPUT_PDB, --output_pdb OUTPUT_PDB
                        -o /../output.pdb: The PDB will only be changed x、y、z
                        location from unchanged_pdb,default:null
  -l LOG_FILE, --log_file LOG_FILE
                        -l /../result.log: The path of result
                        log,default:result.log
  -j RMSD_JSON, --rmsd_json RMSD_JSON
                        -j /../rmsd.json: The path of rmsd
                        json,default:rmsd.json

# 8.Examples
A.get help 
a.TransformRMSD -h
b.TransformRMSD module_name -h

B.alignemt 
[Lth@spgpu Desktop]$ TransformRMSD alignment -c 5gxj.pdb -u 5lc0.pdb -s CA[C] -o change_loc.pdb -l result.log
Use CCP4i superpose to run structure alignment...
Run：superpose 5gxj.pdb -s CA[C] 5lc0.pdb -o change_loc.pdb >result.log 2>&1
Finish structure alignment!

C.getrmsd
[Lth@spgpu Desktop]$ TransformRMSD getrmsd -l result.log -j result.json
Get RMSD !
Save RMSD to result.json

D.changepdb
~/Desktop/Lid/帮他人处理的数据/JXY/RMSD_Transform_Final_Version/RMSD_Transform-master » ./TransformRMSD changepdb -j rmsd_btr.json -t 35 -p 10 -d 2yol.pdb -f 2yol_change_rmsd.pdb
Multiple a number to RMSD...
Add a number to Max RMSD...
change pdb B-factor to RMSD...
set the max rmsd plus a value aa number is 48
set the mutiple rmsd aa number is 164
Finish Mission !

F.bfactor_to_rmsd
[Lth@spgpu demo]$ TransformRMSD bfactor_to_rmsd -t 35 -p 10 -d 2yol.pdb -f 2yol_rmsd_btr.pdb -u 3l6p.pdb -s CA[C] -o change_loc_btr.pdb -l result_btr.log -j rmsd_btr.json
Use CCP4i superpose to run structure alignment...
Run：superpose 2yol.pdb -s CA[C] 3l6p.pdb -o change_loc_btr.pdb >result_btr.log 2>&1
Finish structure alignment!
Get RMSD !
Save RMSD to rmsd_btr.json
Multiple a number to RMSD...
Add a number to Max RMSD...
change pdb B-factor to RMSD...
set the max rmsd plus a value aa number is 48
set the mutiple rmsd aa number is 164
Finish Mission !

# 9.Verify result
You can check whether result.log,rmsd.json and changepdb/bfactor_to_rmsd print info are correspondence to judge TransformRMSD running status.
