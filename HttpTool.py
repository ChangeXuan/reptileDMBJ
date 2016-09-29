import re
class Html_tool:
	BgnCharToNoneRex = re.compile("(\t|\n| |<a.*?>|<img.*?>|&(.*?);)") 
	EndCharToNoneRex = re.compile("<.*?>") 
	BgnPartRex = re.compile("<p.*?>")
	CharToNewLineRex = re.compile("(<br>|</p>|<tr>|<div>|</div>)")
	CharToNextTabRex = re.compile("<td>") 
	replaceTab = [("<","<"),(">",">"),("&","&"),("&","\""),(" "," ")] 

	def replace_char(self,x):
		x = self.BgnCharToNoneRex.sub("",x)
		x = self.BgnPartRex.sub("\n    ",x)
		x = self.CharToNewLineRex.sub("\n",x)
		x = self.CharToNextTabRex.sub("\t",x)
		x = self.EndCharToNoneRex.sub("",x)

		for i in self.replaceTab:
			x = x.replace(i[0],i[1])
		return x