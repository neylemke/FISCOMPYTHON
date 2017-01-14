#!/usr/bin/python
import os
lisdata=!gcloud compute instances list
comand="open http://"+lisdata[1].split()[4]+":8888"
os.system(comand)
