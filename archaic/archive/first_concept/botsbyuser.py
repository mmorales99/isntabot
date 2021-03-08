#!/usr/bin/env python3

import os
import sys
import array
from isntabot import pyBot
from validate import Validator

class Database:
	workspace_name = "mydatabase/"
	config_file_name = "users.config"
	users_table = "users_table.dat"
	users = []
	validador = ""
	last_id = 0 # id de los bots

	def __init__(self):
		if(os.path.isdir(self.workspace_name) is False):
			self.create_default()
		elif(os.path.isfile(self.workspace_name+self.config_file_name) is False):
			self.create_default("onlyconfig")
		else:
			config_file = open(self.workspace_name+self.config_file_name,"r")
			if(config_file.mode == "r"):
				self.last_id = config_file.readline() # last bot id
				user = config_file.readline() # reads admin user
				while user:
					self.users.append(user)
					user = config_file.readline() # reads next user	
				config_file.close()
		self.validador = Validator(self.workspace_name)

	def getWorkspace(self):
		return self.workspace_name

	def getConfig_file(self):
		return self.workspace_name + self.config_file_name

	def getValidador(self):
		return self.validador

	def _getLastId(self):
		lid = int(self.last_id)
		lid = lid + 1
		self.last_id = lid
		return self.last_id

	def add_user(self, user_name, user_pword): # falta implementarlo en la web, mas adelante
		user_id = self.validador.createUser(user_name, user_pword)
		if(user_id==-1):
			return "Existing user"
		else:
			config_file = open(self.workspace_name+self.config_file_name, "a")
			config_file.write(user_id+"\n")
			config_file.close()
			os.mkdir(os.path.join(self.workspace_name+user_id))
			return "User added"

	def add_bot(self, user_id, toFollow=None, user_email="<YOUR BOT EMAIL>"):
		if toFollow is None:
			toFollow = []
		user_path = self.workspace_name + str(user_id)+"/"
		nbot = pyBot().create(user_email, self._getLastId(), toFollow, user_path)
		f = open(user_path+str(user_id)+".config", "a+")
		f.write(nbot.getId()+"\n")

	def create_default(self, conf=""): # genera la sesion root, id 0
		if(conf==""):
			os.mkdir(os.path.join("./"+self.workspace_name))
		config_file = open(self.workspace_name+self.config_file_name, "w+")
		config_file.write("0\n")
		config_file.write("0\n")
		config_file.close()
		if(os.path.isdir(self.workspace_name+"0") is False):
			adminpath = os.path.join("./"+self.workspace_name+"0")
			os.mkdir(adminpath)
			testbot = open(adminpath+"/"+"0.config","w+")
			testbot.write("0")
			testbot.close()
			botpath = adminpath+"/"+"0"+".bot"
			f = open(botpath, "w+")
			f.write("0"+"\n")
			f.write("<ADMINs EMAIL>"+"\n")
			f.write("<ADMIN ACCOUNT>"+"\n")
			f.write("<ADMIN PASSWORD>"+"\n")
			f.write("@wazime.es")

def get_bots(UserId, db):
	if(os.path.isdir(db.getWorkspace()+UserId) is True):
		userpath = db.getWorkspace()+UserId+'/'
		userconfig = userpath+UserId+".config"
		if(os.path.isfile(userconfig) is True):
			f = open(userconfig,"r") # en este archivo se guardan los identificadores de los bots
			if(f.mode=="r"):
				bots_from_file = f.readlines()
				bots_saved = ""
				f.close()
				for x in bots_from_file:
					botpath = userpath+x+".bot"
					if(os.path.isfile(botpath) is True):
						fbot = open(botpath,"r") # en este archivo se guardan los identificadores de los bots
						if(fbot.mode=="r"):
							bot_info = fbot.readlines()
							fbot.close()
							bot_infos = iter(bot_info)
							bot_str=next(bot_infos)[:-1]+'/'+next(bot_infos)[:-1]+'/'+next(bot_infos)[:-1]+'/'+next(bot_infos)[:-1]+'/'+'{'
							for x in bot_infos:
								bot_str = bot_str + x[:-1] + '|'
							bot_str = bot_str +'},'
							
					bots_saved = bots_saved + bot_str
				return bots_saved
# id;correo;nombreCuenta;contrasena;{usuario1|usuario2|usuario3|...},siguienteBot


def set_bots(db, UserId, total_bots, toFollow=""):
	toFollowArr = toFollow[1:len(toFollow)-1].split(',')
	for i in range(int(total_bots)):
		db.add_bot(UserId,toFollowArr)

def main():
	db = Database()
	if(len(sys.argv)>1):
		if(sys.argv[1] == "get_bots"):
			print(get_bots(sys.argv[2], db))
		elif(sys.argv[1] == "set_bots"):
			set_bots(db, sys.argv[2], sys.argv[3], sys.argv[4])
		elif(sys.argv[1] == "validate"):
			if(len(sys.argv) < 4):
				print("BT") # Error con el usuario y la contraseña
			else:
				print(db.getValidador().validar(str(sys.argv[2]), str(sys.argv[3])))
		elif(sys.argv[1] == "new_user"):
			if(len(sys.argv) < 4):
				print("No good info")
			else:
				print(db.add_user(sys.argv[2], sys.argv[3]))
	else:
		print("NO ARGUMENTS GIVEN")

main()
