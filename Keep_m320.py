"""
This file is used to extract specific devices' info from customer.
198devices are M320 while we have 386 ones in total and each of them
has huge amount of configuration
what this file did is decreasing 11976K -> 5074K
"""

config_file = "SUM-FILE_SHOW-CHASSIS_201710.txt"
cate_file = "category.txt"
category = []
with open(cate_file, 'r') as ctfile:
	for line in ctfile.readlines():
		line = line.replace('\n', '')
		category.append(line)
with open(config_file, 'r+') as cffile:
	finish = False
	# i = 0
	while not finish:
		line = cffile.readline()
		for cate in category:
			if line.startswith('mschae10@' + cate): # from here to </rpc-reply>
				# i += 1
				rpc_fin = False
				with open('M320.txt', "a") as f:
					f.write(line)
					while not rpc_fin:
						line2 = cffile.readline()
						if not line2.startswith('</rpc-reply>'):
							f.write(line2)
						else:
							rpc_fin = True

				category.remove(cate)
		if(line == ''):
			finish = True
# print(i)
