from Screens.Screen import Screen
from Screens.MessageBox import MessageBox
from Components.ActionMap import ActionMap
from Components.Label import Label
from Components.Pixmap import Pixmap
from Components.ConfigList import ConfigListScreen
from Components.config import getConfigListEntry, config, ConfigYesNo, ConfigText, ConfigSelection, ConfigClock
from Components.Sources.List import List
from Components.Network import iNetwork
from Tools.LoadPixmap import LoadPixmap
from Tools.Directories import fileExists, pathExists, resolveFilename, SCOPE_CURRENT_SKIN
from os import system, remove as os_remove, rename as os_rename, popen, getcwd, chdir
from Screens.Setup import Setup
from Screens.NetworkSetup import *
from Plugins.SystemPlugins.NetworkBrowser.MountManager import AutoMountManager
from Plugins.SystemPlugins.NetworkBrowser.NetworkBrowser import NetworkBrowser
from Plugins.SystemPlugins.NetworkWizard.NetworkWizard import NetworkWizard



class LDServices(Screen):
	skin = """
<screen name="LDServices" position="70,35" size="1150,650">
<ePixmap position="700,10" zPosition="1" size="450,700" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/LDteam/images/menu/fondo.png" alphatest="blend" transparent="1" />
<widget source="list" render="Listbox" position="15,10" size="660,650" scrollbarMode="showOnDemand">
<convert type="TemplatedMultiContent">
{"template": [
MultiContentEntryText(pos = (60, 1), size = (300, 40), flags = RT_HALIGN_LEFT|RT_VALIGN_CENTER, text = 0),
MultiContentEntryPixmapAlphaTest(pos = (4, 2), size = (40, 40), png = 1),
],
"fonts": [gFont("Regular", 24)],
"itemHeight": 40
}
	</convert>
	</widget>
</screen>"""
	
	def __init__(self, session):
		Screen.__init__(self, session)
		
		self.list = []
		self["list"] = List(self.list)
		self.updateList()
		
		
		self["actions"] = ActionMap(["WizardActions", "ColorActions"],
		{
			"ok": self.KeyOk,
			"back": self.close

		})
		
	def KeyOk(self):
		self.sel = self["list"].getCurrent()
		self.sel = self.sel[2]
		
		if self.sel == 0:
			from Plugins.Extensions.LDteam.LdNetworkSetup import NetworkSamba
			self.session.open(NetworkSamba)
		elif self.sel == 1:
			from Plugins.Extensions.LDteam.LdNetworkSetup import NetworkNfs
			self.session.open(NetworkNfs)
		elif self.sel == 2:
			from Plugins.Extensions.LDteam.LdNetworkSetup import NetworkOpenvpn
			self.session.open(NetworkOpenvpn)
		elif self.sel == 3:
			from Plugins.Extensions.LDteam.LdNetworkSetup import NetworkInadyn
			self.session.open(NetworkInadyn)
		elif self.sel == 4:
			from Plugins.Extensions.LDteam.LdNetworkSetup import NetworkMiniDLNA
			self.session.open(NetworkMiniDLNA)
		elif self.sel == 5:
			from Plugins.Extensions.LDteam.LdNetworkSetup import NetworkFtp
			self.session.open(NetworkFtp)
		elif self.sel == 6:
			from Plugins.Extensions.LDteam.LdNetworkSetup import NetworkAfp
			self.session.open(NetworkAfp)
		elif self.sel == 7:
			from Plugins.Extensions.LDteam.LdNetworkSetup import NetworkuShare
			self.session.open(NetworkuShare)
		elif self.sel == 8:
			from Plugins.Extensions.LDteam.LdNetworkSetup import NetworkTelnet
			self.session.open(NetworkTelnet)
		else:
			self.noYet()
			
	def noYet(self):
		nobox = self.session.open(MessageBox, "Funcion Todavia no disponible", MessageBox.TYPE_INFO)
		nobox.setTitle(_("Info"))
	
		
	def updateList(self):
		self.list = [ ]
		mypath = "/usr/lib/enigma2/python/Plugins/Extensions/LDteam/images/icons/"

		mypixmap = mypath + "Mounts.png"
		png = LoadPixmap(mypixmap)
		name = "Samba"
		idx = 0
		res = (name, png, idx)
		self.list.append(res)

		mypixmap = mypath + "MountManager.png"
		png = LoadPixmap(mypixmap)
		name = "NFS"
		idx = 1
		res = (name, png, idx)
		self.list.append(res)

		mypixmap = mypath + "Vpn.png"
		png = LoadPixmap(mypixmap)
		name = "OpenVPN"
		idx = 2
		res = (name, png, idx)
		self.list.append(res)

		mypixmap = mypath + "Inadyn.png"
		png = LoadPixmap(mypixmap)
		name = "Inadyn"
		idx = 3
		res = (name, png, idx)
		self.list.append(res)

		mypixmap = mypath + "Dlna.png"
		png = LoadPixmap(mypixmap)
		name = "MiniDLNA"
		idx = 4
		res = (name, png, idx)
		self.list.append(res)

		mypixmap = mypath + "Ftp.png"
		png = LoadPixmap(mypixmap)
		name = "FTP"
		idx = 5
		res = (name, png, idx)
		self.list.append(res)
		
		mypixmap = mypath + "Afp.png"
		png = LoadPixmap(mypixmap)
		name = "AFP"
		idx = 6
		res = (name, png, idx)
		self.list.append(res)
		
		mypixmap = mypath + "Ushare.png"
		png = LoadPixmap(mypixmap)
		name = "uShare"
		idx = 7
		res = (name, png, idx)
		self.list.append(res)	
		
		mypixmap = mypath + "Telnet.png"
		png = LoadPixmap(mypixmap)
		name = "Telnet"
		idx = 8
		res = (name, png, idx)
		self.list.append(res)	

		
		self["list"].list = self.list
		
		

