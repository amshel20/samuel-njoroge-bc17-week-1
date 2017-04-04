def data_type(a):
	type0f =type(a)
	if type0f == str:
		return len(a) #return length
	elif type0f == bool:
		return a      #return the boolean value
	elif type0f == int:  #return different conditiongs if value is < or > or = 100
		if a == 100:
			return 'equal to 100'
		elif a < 100:
			return 'less than 100'
		else:
			return 'more than 100'

	elif type0f ==list:
		try:
			if a[2]:
				return a[2] #return 3rd item
		except(IndexError):
			return None  #return 'none' if doesnt exist
	else:
		return 'no value'   #return no value if nothing is supplied
