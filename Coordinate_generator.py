from pylab import *

def Points(Xpos, Ypos, L, Color):
	xbump = L*cos(pi*(1.0/3.0))
	ybump = L*sin(pi*(1.0/3.0))
	xref = [0,xbump, L+xbump, L+2*xbump, L+xbump, xbump]
	yref = [ybump,2*ybump,2*ybump,ybump,0,0]
	x = [(Xpos + i) for i in xref]
	y = [(Ypos + i) for i in yref]
	points = []
	for i in range(len(x)):
		points.append(str(x[i]) + ',' + str(y[i]))
	print  '\t <path \n \t \t d = \"M ' + ' '.join(points) + ' z\" \n \t \t id = \"path5\" \n \t \t style=\"fill:#%s;fill-opacity:1;stroke:#000000;stroke-opacity:1\" />' % Color

