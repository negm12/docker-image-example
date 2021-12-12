
message = input('pls inter the massage')
def encode(message):
	encoded_message = ""
	i = 0
	while (i <= len(message)-1):
		count = 1
		ch = message[i]
		j = i
		while (j < len(message)-1):
			if (message[j] == message[j+1]):
				count = count+1
				j = j+1
			else:
				break
		encoded_message=encoded_message+ch+str(count)
		i = j+1
	comprratio = len(message)/len(encoded_message)
	print( f'th compression ratio is {comprratio}')
	return encoded_message

encoded_message=encode(message)
print(encoded_message)


def decode(en_message):
	enmessage = list(en_message)
	decoded_message = ""
	ch = 0
	num = 1
	while ch<len(enmessage) and num<len(enmessage):
		decoded_message = decoded_message + enmessage[ch]*int(enmessage[num])
		ch = ch+2
		num = num+2

	return decoded_message

print(decode(encoded_message))
