import re

regex = r"[a-zA-Z]:/((?:.*?\\)*)*.*ma"
xx = '		 -op "v=0;" "Y:/prod/webisodes/103/Lit/pwp_web103_sc0100/ref/pwp_web103_sc0100_sec_v01.ma";'
r1 = re.findall(r"[a-zA-Z]:/((?:.*?\\)*)*.*ma",xx)

#print(r1.group(0))
for r in r1:
    print(r)

matches = re.finditer(regex, xx)
for matchNum, match in enumerate(matches, start=1):
    match1 = match.group()
    print match1
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
