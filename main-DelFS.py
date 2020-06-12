from FN import FN

if __name__ == '__main__':
	c1 = FN(workDir=r'H:\OneDrive - revolutionize B2C bandwidth\视频教程\Adobe\Flash&Animate')
	exe = True
	# exe = False
	c1.analyzeExtensions()
	# print(c1.filesName)

	# 更该文件夹名
	# c1.delDsStr('【更多分享关注微信公众号：互联网架构师】', '', exe)

	# 更改文件名
	c1.delFsStr('. ', '.', exe)
	# print(c1.filesNum)

	# 使用正则表达式更改文件名
	# c1.delFsStrWithRe('(\d+.)\d*-*(.+)\(.+\)', exe)
	pass
