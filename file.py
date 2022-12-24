"//  Write a Python program to swap two string basis odd/even ?"

&gt;&gt;&gt; s = 'badcfe'
&gt;&gt;&gt; ''.join([ s[x:x+2][::-1] for x in range(0, len(s), 2) ])
'abcdef'







