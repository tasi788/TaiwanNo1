a = {
	'1':'ㄅ',
	'2':'ㄉ',
	'3':'ˇ',
	'4':'ˋ',
	'5':'ㄓ',
	'6':'ˊ',
	'7':'˙',
	'8':'ㄚ',
	'9':'ㄞ',
	'0':'ㄢ',
	'-':'ㄦ',
	'q':'ㄆ',
	'w':'ㄊ',
	'e':'ㄍ',
	'r':'ㄐ',
	't':'ㄔ',
	'y':'ㄗ',
	'u':'ㄧ',
	'i':'ㄛ',
	'o':'ㄟ',
	'p':'ㄣ',
	'a':'ㄇ',
	's':'ㄋ',
	'd':'ㄎ',
	'f':'ㄑ',
	'g':'ㄕ',
	'h':'ㄘ',
	'j':'ㄨ',
	'k':'ㄜ',
	'l':'ㄠ',
	';':'ㄤ',
	'z':'ㄈ',
	'x':'ㄌ',
	'c':'ㄏ',
	'v':'ㄒ',
	'b':'ㄖ',
	'n':'ㄙ',
	'm':'ㄩ',
	',':'ㄝ',
	'.':'ㄡ',
	'/':'ㄥ',
	' ':' ',
	'\n':'\n'
	}
b = input('輸入亂碼文～：')
c = ''
for x in b:
	c = c + a[x]
print (c)
