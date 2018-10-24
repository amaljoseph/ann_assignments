def corrections(i, r1, r2, m):
	k = i-r1
	h = i-r2
	j = i+r1+1
	l = i+r2+1
	if k<0:
		k = 0
	if h<0:
		h = 0
	if l>m:
		l = m
	if j>m:
		j = m
	return k, h, j, l
