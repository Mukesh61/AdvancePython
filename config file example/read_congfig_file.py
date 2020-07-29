from configparser import ConfigParser

#creating a object of parser

config = ConfigParser()

file = 'config.ini' #name of config file

config.read(file)

#check all the section in config file

print("all the section in config file",config.sections())

#read a element from any  section

print("dev database name",config['dev']['database'])

print("dev database name",config['dev']['password'])
