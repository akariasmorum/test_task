from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
import os, subprocess
import json
import re
# Create your views here.
def get_processes(request):

	#processes = os.popen('ps -aux').read()
	processes, err = subprocess.Popen( 'ps axo pid,user,command | tr -s "\t" ', stdout=subprocess.PIPE, shell=True).communicate()
	processes = processes.splitlines()

	headers = ['PID', 'USER', 'COMMAND']
	process_list = []
	for proc in processes[1:]:
		proc_splitted = proc.decode().split(None,2)
		process_list.append(dict(zip(headers, proc_splitted)))

	print(len(process_list))

	parse_params(request, process_list)


	print(len(process_list))

	if request.method=='GET':
		return HttpResponse(json.dumps(process_list))

def parse_params(request, proc_list):
	if 'proc_range' in request.GET:
		proc_list[:] = proc_range(request.GET.get('proc_range'), proc_list)
	if 	'cmd_start' in request.GET:
		proc_list[:] = cmd_start(request.GET.get('cmd_start'), proc_list)
	if 'cmd_reg' in request.GET:
		proc_list[:] = cmd_reg(request.GET.get('cmd_reg'), proc_list)



def proc_range(srange, proc_list):
	rs = str(srange).split('-')	
	start=int(rs[0])
	print(start)
	end=int(rs[1])
	print(end)
	
	new_list = []
	for proc in proc_list:
		if start<=int(proc['PID'])<=end:
			
			new_list.append(proc)

	return new_list		

def cmd_start(start, proc_list):
	
	new_list = []
	for proc in proc_list:
		if proc['COMMAND'].startswith(start):
			new_list.append(proc)

	return new_list		

def cmd_reg(reg, proc_list):
	
	'''
		Arguments:
			reg - string, регулярное выражение дял поиска в command
			proc_list - [], list процессов
	'''

	new_list = []
	for proc in proc_list:
		if bool(re.search(reg, proc['COMMAND'])):
			new_list.append(proc)

	return new_list	



