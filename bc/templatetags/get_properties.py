from django import templateregister = template.Library()import syssys.path.append("/home/root2/mptt/readtags")from config_project import *@register.simple_tagdef properties(report, x, y):	try:		return r.hgetall(report+str(x)+str(y))['color']	except:		return "transparent"