# RMSD_Transform
 Transform B-factor to RMSD
 
# Software requirement：
 
 Python3
 
 CCP4i Superpose must be added $PATH

# install package:

 Python3 /../RMSD_Transform-1.0.0/setup.py install

# add Executable Authority
 
 chmod u+x TransformRMSD
 
 TransformRMSD should be added $PATH

# TransformRMSD usage:
 
 Divided into four modules

 alignment
 
 getrmsd
 
 changepdb
 
 bfactor_to_rmsd

# Example:
 
 TransformRMSD alignment -h ：for help
 
 TransformRMSD bfactor_to_rmsd -d default.pdb -f rmsd.pdb -u unchanged_pdb -l result.log -j rmsd_json  ：You can get the pdb file changed to rmsd in rmsd.pdb, for other parameters please use -h for details

If a bug occurs during use, please contact me at 17626048270 without hesitation.  ---Lid

