subKey =  "zmgtceixl?nuworpsjyqfav?b?"
alphabet ="abcdefghijklmnopqrstuvwxyz"

txt="GQEy (yxrjq erj gzpqfjc qxc euzi) zjc z qbpc re grwpfqcj ycgfjlqb grwpcqlqlro. Groqcyqzoqy zjc pjcycoqct vlqx z ycq re gxzuucoicy vxlgx qcyq qxclj gjczqlalqb, qcgxolgzu (zot irriuloi) ynluuy, zot pjrmucw-yrualoi zmlulqb. Gxzuucoicy fyfzuub gracj z ofwmcj re gzqcirjlcy, zot vxco yruact, czgx blcuty z yqjloi (gzuuct z euzi) vxlgx ly yfmwlqqct qr zo rouloc ygrjloi ycjalgc. GQEy zjc z ijczq vzb qr uczjo z vltc zjjzb re grwpfqcj ycgfjlqb ynluuy lo z yzec, ucizu coaljrowcoq, zot zjc xryqct zot puzbct mb wzob ycgfjlqb ijrfpy zjrfot qxc vrjut erj efo zot pjzgqlgc. Erj qxly pjrmucw, qxc euzi ly: plgrGQE{EJ3SF3OGB_4774GN5_4J3_G001_C5M0GGTM}".lower()

outText = ''
for x in txt:
 if(x in subKey):
  outText += alphabet[subKey.index(x)]
 else:
  outText += x
  
print(outText)