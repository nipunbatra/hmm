colors = ['rgb(31,119,180)',
              'rgb(255,127,14)',
              'rgb(44,160,44)',
              'rgb(214,39,40)',
              'rgb(148,103,189)',
              'rgb(140,86,75)',
              'rgb(227,119,194)',
              'rgb(127,127,127)',
              'rgb(188,189,34)',
              'rgb(158,218,229)']


for cnt,i in enumerate(colors):
	s = i.split('(')[1]
	s = s.split(')')[0]

	print ('\\definecolor{color%s}{RGB}{%s}'%(cnt,s))
	print ("\n")
