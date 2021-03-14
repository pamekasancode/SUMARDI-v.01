# import necessary module
# main_window, DMS are defined here

import os, sys, logging, tkinter as tk, time, sqlite3
from tkinter import ttk, filedialog as fd, messagebox as msgbox
import traceback, shutil as util, datetime, threading, widget_feature as wf
from surat_keluar import Main as main1 
from surat_masuk import Main as main2

# CONST
BOTH = tk.BOTH
END = tk.END
x_axis = tk.X
LEFT = tk.LEFT


class Module_1(main1):
	def __init__(self, master, parent):
		super().__init__(master, parent)
		self.nodes()


class Module_2(main2):
	def __init__(self, master, parent):
		super().__init__(master, parent)
		self.nodes()


class _Core:
	class Database:
		def __init__(self, date):
			self.fname = date + ".db"
			self.connection = sqlite3.connect(self.fname)
			self.cursor = self.connection.cursor()

		def load_data(self, table_name):
			try:
			 	data, cursor = self.cursor.execute(f"SELECT *, oid FROM {table_name}").fetchall(), self.cursor
			except:
			 	return False, False
			return data, cursor

		def exec(self, sql, extra=False):			# this will execute the sql with no return value
			if extra:
				self.cursor.execute(sql, extra)
			else:
				self.cursor.execute(sql)
			self.connection.commit()

		def exit(self):
			self.connection.commit()
			self.cursor.close()
			self.connection.close()
			return self.fname.split(".")[0]


	#-----------------------------------------------

	def __enter__(self):
		# init section
		self.db_manager = self.Database(self.get_datetime())
		self.configure_log()

		# write activity to the logs file
		self.loggers.debug("Database Filename is " + self.get_datetime() + ".db")

		self.parent_window = tk.Tk()
		self.parent_window.title("Aplikasi Surat Keluar-Masuk (SUMARDI)")
		self.parent_window.geometry("1000x900")
		self.parent_window.iconbitmap("image2.ico")
		self.parent_window.bind("<Control-s>", lambda x: self.check_data())

		# self.parent_window.iconify()
		# self.parent_window.update()
		# self.parent_window.deiconify()

		self.menus()

		self.main_tabs = ttk.Notebook(self.parent_window)
		self.main_tabs.pack(fill=BOTH, expand=True)

		self.w1 = Module_1(self.parent_window, self.main_tabs)
		self.w2 = Module_2(self.parent_window, self.main_tabs)

		self.main_tabs.add(self.w1.main_frame, text="Surat Keluar")
		self.main_tabs.add(self.w2.main_frame, text="Surat Masuk")

		self.info_w = tk.Label(self.parent_window, text="")
		self.info_w.pack(fill=x_axis, side=tk.RIGHT)

		self.parent_window.mainloop()

	def set_info(self, msg, widget=False, color="red", wcolor="red", type_info_box=False):
		def ret_():
			if widget:
				widget.config(bg='white')
				self.info_w.config(text="")
				widget.unbind("<FocusOut>")
			else:
				time.sleep(1)
				self.info_w.config(text="", fg="black")

			if type_info_box == "info":
				msgbox.showinfo("Information", msg)
			elif type_info_box == "warning":
				msgbox.showwarning("Warning", msg)
			elif type_info_box == "error":
				msgbox.showerror("Error", msg)

		if widget:
			widget.config(bg=wcolor)
			self.info_w.config(text=msg, fg=color)
			self.info_w.bell()
			widget.bind("<Button-1>", lambda x: ret_())
		else:
			self.info_w.config(text=msg, fg=color)
			threading.Thread(target=ret_).start()


	def __exit__(self, types, values, traceback_):
		if types:
			msgbox.showerror("Traceback", traceback.format_exc())
			self.loggers.exception(traceback.format_tb(traceback_)[0])
			self.loggers.info("Program Halted!")
			self.save_current_logs()
			return True
		self.loggers.info("Program Halted!")
		self.archive_database()
		self.save_current_logs()

	def call_edit(self):
		edit_ = wf.Main(self.parent_window, self.db_manager, self.loggers)

		edit_.main(self.main_tabs.index(self.main_tabs.select()))

	def get_datetime(self):
		return str(datetime.datetime.now().date())


	def archive_database(self):
		cur_dname = self.db_manager.exit()
		cur_date = self.get_datetime()
		old_file = [x for x in os.listdir() if x.endswith(".db")]
		c = 0

		if not old_file:
			self.loggers.debug("No old Database detected!")
			return

		if not os.path.isdir("storage"):
			os.mkdir("storage")

		for x in old_file:
			if x.split(".")[0] != cur_date:
				util.move(x, "storage/"+x)
				c += 1
		self.loggers.debug(f"Moved {c} old Database Into archive")


	def save_current_logs(self):
		self.logs_fhandler.close()		
		self.loggers.removeHandler(self.logs_fhandler)
		if not os.path.isdir("logs"):
			os.mkdir("logs")
		os.rename("logs.log", self.get_datetime()+".log")
		util.move(self.get_datetime()+".log", f"logs/{self.get_datetime()}.log")

	def configure_log(self):
		self.loggers = logging.getLogger(__name__)
		self.loggers.setLevel(logging.DEBUG)
		self.Fformat = logging.Formatter('%(asctime)s : %(name)s : %(levelname)s : %(message)s')
		self.logs_fhandler = logging.FileHandler("logs.log", mode="w+")	
		self.logs_fhandler.setLevel(logging.DEBUG)	# write a log file and create a handler that can reuse later
		self.logs_fhandler.setFormatter(self.Fformat)
		self.loggers.addHandler(self.logs_fhandler)

	def check_data(self):		# function to check all widgets within the selected tabs is empty or not
		if str(self.main_tabs.select()) == str(self.w1.main_frame):
			for x in range(len(self.w1._val)):
				if x == 1:
					continue
				elif x == len(self.w1._val) - 1:
					if not self.w1._val[x].get("1.0", END) or self.w1._val[x].get("1.0", END) == "\n":
						self.set_info("Perihal Tidak boleh kosong!", widget=self.w1._val[x], color='red', wcolor='red')
						return
				else:
					if not self.w1._val[x].get():
						self.set_info("Harap Diisi!", widget=self.w1._val[x])
						return
			self.save_data()


		elif str(self.main_tabs.select()) == str(self.w2.main_frame):
			for x in range(len(self.w2._val)):
				if x == 1 or x == 0:
					continue
				elif x == len(self.w2._val) - 1:
					if not self.w2._val[x].get("1.0", END) or self.w2._val[x].get("1.0", END) == "\n":
						self.set_info("Perihal Tidak boleh kosong!", widget=self.w2._val[x], color='red', wcolor='red')
						return
				else:
					if not self.w2._val[x].get():
						self.set_info("Harap Diisi!", widget=self.w2._val[x])
						return
			self.save_data()

	def save_data(self):
		if str(self.main_tabs.select()) == str(self.w1.main_frame):
			data = []
			for x in range(len(self.w1._val)):
				if x == 1:
					data.append("-".join([x.get() for x in self.w1._val[x]]))
				elif x == len(self.w1._val) - 1:
					data.append(self.w1._val[x].get("1.0", "end-1c"))
				else:
					data.append(self.w1._val[x].get())

			try:
				self.db_manager.exec("CREATE TABLE IF NOT EXISTS Surat_Keluar (ALAMAT_PENERIMA TEXT, TANGGAL TEXT, NOMOR TEXT, PERIHAL TEXT)")
				self.db_manager.exec("INSERT INTO Surat_Keluar VALUES (?, ?, ?, ?)", extra=tuple(data))
			except:
				self.set_info(traceback.format_exc, type_info_box="error")

				self.loggers.warning(traceback.format_exc())
				return True

			self.set_info("Berhasil Menyimpan Ke database", color="green", type_info_box="info")
			self.loggers.info("Added value to a Database")
			self.clear_widget()

		elif str(self.main_tabs.select()) == str(self.w2.main_frame):
			data = []
			for x in range(len(self.w2._val)):
				if x == 0 or x == 1:
					data.append("-".join([x.get() for x in self.w2._val[x]]))
				elif x == len(self.w2._val) - 1:
					data.append(self.w2._val[x].get("1.0", "end-1c"))
				else:
					data.append(self.w2._val[x].get())

			try:
				self.db_manager.exec("CREATE TABLE IF NOT EXISTS Surat_Masuk (TANGGAL_SURAT TEXT, TANGGAL_DITERIMA TEXT, ALAMAT_PENGIRIM TEXT, NOMOR_SURAT TEXT, PERIHAL TEXT)")
				self.db_manager.exec("INSERT INTO Surat_Masuk VALUES (?, ?, ?, ?, ?)", extra=tuple(data))

			except:
				self.set_info(traceback.format_exc, type_info_box="error")
				self.loggers.warning(traceback.format_exc())				
				return True
			self.set_info("Berhasil Menyimpan Ke database", color="green", type_info_box="info")
			self.loggers.info("Added value to a Database")
			self.clear_widget()

	def clear_widget(self):		# function to clear all widgets i.e the it successfully added to a database
		if str(self.main_tabs.select()) == str(self.w1.main_frame):
			for x in range(len(self.w1._val)):
				if x == 1:
					continue
				elif x == len(self.w1._val) - 1:
					self.w1._val[x].delete("1.0", END)
				else:
					self.w1._val[x].delete(0, END)

		elif str(self.main_tabs.select()) == str(self.w2.main_frame):
			for x in range(len(self.w2._val)):
				if x == 1 or x == 0:
					continue
				elif x == len(self.w2._val) - 1:
					self.w2._val[x].delete("1.0", END)
				else:
					self.w2._val[x].delete(0, END)

		else:
			return True


	def menus(self):
		self.main_menus = tk.Menu(self.parent_window)
		self.parent_window.config(menu=self.main_menus)
		self.file_menu = tk.Menu(self.main_menus, tearoff=0)
		self.main_menus.add_cascade(label="File", menu=self.file_menu)
		self.file_menu.add_command(label="Simpan Database    Ctrl+s", command=self.check_data)
		self.file_menu.add_command(label="Edit/View Database   Ctrl+o", command=lambda: self.call_edit())

		self.loggers.info("Program Started!")



class _Main:
	def __init__(self):
		with _Core() as c:
			pass

if __name__ == '__main__':
	_Main()