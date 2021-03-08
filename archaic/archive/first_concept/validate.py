#!/usr/bin/env python3

import os
import sys

class User:
	def __init__(self):
		super().__init__()
		self._name = ""
		self._pword = ""
		self._id = -1

	def setName(self, name: str):
		self._name = name

	def setPword(self, pword: str):
		self._pword = pword

	def setId(self, id: int): # modify when new users are gonna be created with a static counter
		self._id = id

	def getName(self):
		return self._name

	def getPword(self):
		return self._pword

	def getId(self):
		return self._id

class Validator:
	_filename = "users_table.dat"
	_users_list = []
	def __init__(self, workspace_name=""):
		if(workspace_name==""):
			workspace_name = "./"
		self._filename = workspace_name + self._filename
		file_exists = os.path.isfile(self._filename)
		if(file_exists is False):
			_validated_data_file = open(self._filename, "w+")
			_validated_data_file.write("##\n#\n# Formato de escritura de nuevos usuarios:\n#\n#\n#   [nombre_usuario;password;identificador]\\n\n#\n#\n#\n##\n\n[manuel@wazime.es;wazime1234;0]\n")
			_validated_data_file.close()
			print('NO CONFIG FILES EXISTING... NO USERS')
		
		_validated_data_file = open(self._filename, "r")
		if(_validated_data_file.mode == "r"):
			_file = _validated_data_file.readlines()
			_validated_data_file.close()
			for x in _file:
				if x[0] == "#":
					continue
				if x[0] in (' ','\n'):
					continue
				if x[0] == "[":
					fbl = -1
					sbl = -1
					for i in range(len(x)):
						if x[i] == ";":
							if fbl == -1:
								fbl = i
							elif sbl == -1:
								sbl = i
					user = User()
					user.setName(x[1:fbl])
					user.setPword(x[fbl+1:sbl])
					user.setId(x[sbl+1:len(x)-2])
					self._users_list.append(user)

	def validar(self, userName: str, userPword: str):
		valUser = User()
		valUser.setName(userName)
		valUser.setPword(userPword)
		for x in self._users_list:
			if same(valUser, x) is True:
				if correctPw(valUser, x) is True:
					# send server info
					return x.getId()
				else:
					# send no correct info # Contraseña erronea
					return "PW"
		# no correct info # Usuario erroneo
		return "UW"

	def createUser(self, user_name, user_pword):
		last_id = -1
		existing_user = self.validar(user_name, user_pword)
		if(existing_user!="UW"):
			return -1
		else:
			last_id = self._users_list[-1].getId()
			last_id = int(last_id)
			last_id = last_id + 1
			last_id = str(last_id)
			userstr = "["+user_name+";"+user_pword+";"+last_id+"]\n"
			#[nombre_usuario;password;identificador]\n
			f = open(self._filename, "a")
			f.write(userstr)
			f.close()
		return last_id


def same(u, u1):
	if u.getName() == u1.getName():
		return True
	return False

def correctPw(u, u1):
	if u.getPword() == u1.getPword():
		return True
	return False
