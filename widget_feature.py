import tkinter as tk, os, sqlite3 as sql, datetime
from tkinter import ttk, messagebox as msgbox



year = int(datetime.datetime.now().year)

DAY_LIST = [x for x in range(1, 32)]
MONTH_LIST = [x for x in range(1, 13)]
YEAR_LIST = [x for x in range(year-20, year+21)]


year = 0

class Surat_Keluar:
	def __init__(self, master):
		self.master = master

		self.tgl = tk.StringVar()
		self.bln = tk.StringVar()
		self.thn = tk.StringVar()

	def main(self):
		self.vars = []

		self.vars.append([self.tgl, self.bln, self.thn])

		self.main_frame = tk.Frame(self.master)
		self.main_frame.pack(fill=tk.BOTH, expand=1)

		frame_1 = tk.Frame(self.main_frame)
		frame_1.pack()

		tk.Label(frame_1, text="Alamat Penerima").pack()

		alamat_penerima = tk.Entry(frame_1, width=30)
		alamat_penerima.pack()
		self.vars.append(alamat_penerima)

		frame_2 = tk.Frame(self.main_frame)
		frame_2.pack(pady=10)

		tk.Label(frame_2, text="Nomor Surat").pack()

		no_surat = tk.Entry(frame_2, width=30)
		no_surat.pack()
		self.vars.append(no_surat)

		frame_3 = tk.LabelFrame(self.main_frame, text="Tanggal Dikirim", padx=10, pady=10)
		frame_3.pack(pady=10)

		tk.OptionMenu(frame_3, self.tgl, *DAY_LIST).pack(side=tk.LEFT)
		tk.OptionMenu(frame_3, self.bln, *MONTH_LIST).pack(side=tk.LEFT)
		tk.OptionMenu(frame_3, self.thn, *YEAR_LIST).pack(side=tk.LEFT)

		frame_4 = tk.Frame(self.main_frame)
		frame_4.pack(anchor='w', fill=tk.BOTH, expand=1)

		tk.Label(frame_4, text="Perihal").pack(anchor='w')

		top_frame_1 = tk.Frame(frame_4)
		top_frame_1.pack(fill=tk.BOTH, expand=1)

		top_frame_2 = tk.Frame(top_frame_1)
		top_frame_2.pack(fill=tk.BOTH, expand=1, side=tk.LEFT)

		perihal = tk.Text(top_frame_2, wrap=tk.NONE)
		perihal.pack(fill=tk.BOTH, expand=1)
		self.vars.append(perihal)
		top_frame_2.pack_propagate(0)

		yscroll = ttk.Scrollbar(top_frame_1, orient=tk.VERTICAL, command=perihal.yview)
		yscroll.pack(fill=tk.Y, side=tk.LEFT)
		perihal.config(yscrollcommand=yscroll.set)

		xscroll = ttk.Scrollbar(frame_4, orient=tk.HORIZONTAL, command=perihal.xview)
		xscroll.pack(fill=tk.X)
		perihal.config(xscrollcommand=xscroll.set)

		return self.main_frame, self.vars

class Surat_Masuk:
	def __init__(self, master):
		self.master = master

		self.tgl_s = tk.StringVar()
		self.bln_s = tk.StringVar()
		self.thn_s = tk.StringVar()

		self.tgl_m = tk.StringVar()
		self.bln_m = tk.StringVar()
		self.thn_m = tk.StringVar()


	def main(self):
		self.vars = []

		self.vars.append([self.tgl_s, self.bln_s, self.thn_s])
		self.vars.append([self.tgl_m, self.bln_m, self.thn_m])


		self.main_frame = tk.Frame(self.master)
		self.main_frame.pack(fill=tk.BOTH, expand=1)

		frame_1 = tk.Frame(self.main_frame)
		frame_1.pack(pady=10)

		tk.Label(frame_1, text="Alamat Pengirim").pack(anchor='w')
		alamat_pengirim = tk.Entry(frame_1, width=30)
		alamat_pengirim.pack()
		self.vars.append(alamat_pengirim)

		frame_2 = tk.Frame(self.main_frame)
		frame_2.pack(pady=10)

		tk.Label(frame_2, text="Nomor Surat").pack(anchor='w')
		no_surat = tk.Entry(frame_2, width=30)
		no_surat.pack()
		self.vars.append(no_surat)

		frame_3 = tk.Frame(self.main_frame, padx=5, pady=10)
		frame_3.pack(pady=10)

		date_masuk = tk.LabelFrame(frame_3, text="Tanggal Masuk")
		date_masuk.pack(side=tk.LEFT, padx=5)

		tk.OptionMenu(date_masuk, self.tgl_m, *DAY_LIST).pack(side=tk.LEFT)
		tk.OptionMenu(date_masuk, self.bln_m, *MONTH_LIST).pack(side=tk.LEFT)
		tk.OptionMenu(date_masuk, self.thn_m, *YEAR_LIST).pack(side=tk.LEFT)

		date_surat = tk.LabelFrame(frame_3, text="Tanggal Surat")
		date_surat.pack(side=tk.LEFT, padx=5)

		tk.OptionMenu(date_surat, self.tgl_s, *DAY_LIST).pack(side=tk.LEFT)
		tk.OptionMenu(date_surat, self.bln_s, *MONTH_LIST).pack(side=tk.LEFT)
		tk.OptionMenu(date_surat, self.thn_s, *YEAR_LIST).pack(side=tk.LEFT)


		frame_4 = tk.Frame(self.main_frame)
		frame_4.pack(fill=tk.BOTH, expand=1)

		tk.Label(frame_4, text="Perihal").pack(anchor='w')

		top_frame_1 = tk.Frame(frame_4)
		top_frame_1.pack(fill=tk.BOTH, expand=1)

		top_frame_2 = tk.Frame(top_frame_1)
		top_frame_2.pack(fill=tk.BOTH, expand=1, side=tk.LEFT)

		perihal = tk.Text(top_frame_2, wrap=tk.NONE)
		perihal.pack(fill=tk.BOTH, expand=1)
		self.vars.append(perihal)
		top_frame_2.pack_propagate(0)

		yscroll = ttk.Scrollbar(top_frame_1, orient=tk.VERTICAL, command=perihal.yview)
		yscroll.pack(fill=tk.Y, side=tk.LEFT)
		perihal.config(yscrollcommand=yscroll.set)

		xscroll = ttk.Scrollbar(frame_4, orient=tk.HORIZONTAL, command=perihal.xview)
		xscroll.pack(fill=tk.X)
		perihal.config(xscrollcommand=xscroll.set)

		return self.main_frame, self.vars

class Main:
	def __init__(self, master, cur_fhandle, log_obj):
		self.master = master
		self.db_handler = cur_fhandle
		self.catagories = tk.StringVar()
		self.cur_database = tk.StringVar()
		self.active_db = None
		self.catagories_list = ["Surat_Keluar", "Surat_Masuk"]
		self.mode_state = tk.BooleanVar()
		self.database_list = self.find_databases()
		self.disabled = False
		self.node_main_frames = []
		self.active_w = None
		self.tree_init = False
		self.w_vars = []
		self.log = log_obj

	def main(self, tabs_index):
		self.catagories.set(self.catagories_list[tabs_index])
		self.cur_database.set(self.database_list[0])

		self.window = tk.Toplevel(self.master)
		self.window.geometry("1500x800")
		self.window.iconbitmap("image3.ico")

		self.top_window = tk.Frame(self.window)
		self.top_window.pack(fill=tk.X)
		self.bot_window = tk.Frame(self.window)
		self.bot_window.pack(fill=tk.BOTH, expand=1)

		self.tools_frame = tk.Frame(self.top_window)
		self.tools_frame.pack(fill=tk.X, expand=1)

		self.tree_frame = tk.Frame(self.bot_window)
		self.tree_frame.pack(fill=tk.BOTH, expand=1, side=tk.LEFT)

		self.edit_frame = tk.Frame(self.bot_window)
		self.edit_frame.pack(fill=tk.BOTH, expand=1, side=tk.LEFT)

		self.edit_node_frame = tk.Frame(self.edit_frame)
		self.edit_node_frame.pack(fill=tk.BOTH, expand=1)
		self.edit_node_frame.pack_propagate(0)

		self.feature_1 = Surat_Keluar(self.edit_node_frame)
		self.feature_2 = Surat_Masuk(self.edit_node_frame)


		# tools frame widgets
		frame_1 = tk.LabelFrame(self.tools_frame, text="Katagori")
		frame_1.pack(side=tk.LEFT)

		tk.OptionMenu(frame_1, self.catagories, *self.catagories_list, command=lambda x: self.edit_feature()).pack()

		frame_2 = tk.Frame(self.tools_frame)
		frame_2.pack(side=tk.LEFT, padx=20)

		tk.Radiobutton(frame_2, text="Readonly Mode", variable=self.mode_state, value=False, command=self.enable_disable).pack(side=tk.LEFT)
		tk.Radiobutton(frame_2, text="Edit Mode", variable=self.mode_state, value=True, command=self.enable_disable).pack(side=tk.LEFT)

		frame_3 = tk.LabelFrame(self.tools_frame, text="Using Database")
		frame_3.pack(side=tk.LEFT)

		tk.OptionMenu(frame_3, self.cur_database, *self.database_list, command=lambda x: self.switch_database()).pack()

		frame_4 =tk.Frame(self.tools_frame)
		frame_4.pack(side=tk.LEFT)

		self.update_btn = tk.Button(frame_4, text="Update", state=tk.DISABLED)
		self.update_btn.pack()

		self.delete_btn = tk.Button(frame_4, text="Delete", state=tk.DISABLED)
		self.delete_btn.pack()

		# treeview widgets

		frame_top_1 = tk.Frame(self.tree_frame)
		frame_top_1.pack(fill=tk.BOTH, expand=1)

		frame_top_2 = tk.Frame(frame_top_1)
		frame_top_2.pack(fill=tk.BOTH, expand=1, side=tk.LEFT)

		frame_top_2.pack_propagate(0)

		self.tree_view = ttk.Treeview(frame_top_2, selectmode='browse')
		self.tree_view.pack(fill=tk.BOTH, expand=1)
		self.tree_view.bind("<<TreeviewOpen>>", lambda x: self.selected_invoke())

		yscroll = ttk.Scrollbar(frame_top_1, orient=tk.VERTICAL, command=self.tree_view.yview)
		yscroll.pack(fill=tk.Y, side=tk.LEFT)
		self.tree_view.config(yscrollcommand=yscroll.set)

		xscroll = ttk.Scrollbar(self.tree_frame, orient=tk.HORIZONTAL, command=self.tree_view.xview)
		xscroll.pack(fill=tk.X)
		self.tree_view.config(xscrollcommand=xscroll.set)

		self.enable_disable()
		self.edit_feature()	
		self.switch_database()

	def log_bridge(self, level, msg):
		if level == 0:			# on debug level
			self.log.debug(msg)
		elif level == 1:
			self.log.info(msg)
		elif level == 2:
			self.log.warning(msg)
		elif level == 3:
			self.log.error(msg)
		elif level == 4:
			self.log.critical(msg)
		else:
			return

	def delete_feature(self, selection_id):
		row_id = self.tree_view.item(selection_id)['values'][-1]
		con, cur, stat = self.database_manager(ret_con_only=True)
		cat = self.catagories.get()
		if not con:
			return

		if stat == 0:
			con.exec(f"DELETE FROM {cat} WHERE oid = {row_id}")
		else:
			cur.execute(f"DELETE FROM {cat} WHERE oid = {row_id}")
			con.commit()
		self.log_bridge(0, f"Deleted value with the id = {row_id}")
		self.show_info("1 Data Dihapus Dari Database")				# task!: create a refresh function for refreshing the table and clear all widget in edit region!
		self.refresh_treeview()

	def refresh_treeview(self):
		def clear_edit():
			if self.catagories.get() == "Surat_Keluar":
				w_ = self.w_vars[1:]
				[w_[x].delete("1.0", tk.END) if x == len(w_)-1  else w_[x].delete(0, tk.END) for x in range(len(w_))]
			else:
				w_ = self.w_vars[2:]
				[w_[x].delete("1.0", tk.END) if x == len(w_)-1 else w_[x].delete(0, tk.END) for x in range(len(w_))]
			w_ = 0


		children = self.tree_view.get_children()
		if children:
			self.tree_view.delete(children)
		self.insert_tree_view()
		self.window.lift()
		self.delete_btn.config(state=tk.DISABLED)
		self.update_btn.config(state=tk.DISABLED)
		clear_edit()


	def update_feature(self, selection_id):
		def check_equality(handler, cur=False):
			index = self.tree_view.index(selection_id)
			data, cols_name, desc_ = self.database_manager()
			changed_val = {}

			data = data.pop(index)
			data.pop(0)					# remove number in the treeview
			row_id = data.pop()			# move number from the list to this var
			cols_name.pop(0)
			cols_name.pop()
			cols_name.append("PERIHAL")
			data.append(desc_[index])

			if self.catagories.get() == "Surat_Keluar":
				for x in range(len(data)):
					if "-" in data[x]:
						data.insert(x-1, data.pop(x))
						cols_name.insert(x-1, cols_name.pop(x))

			for x in range(len(data)):
				if type(self.w_vars[x]) == list:
					date = "-".join([y.get() for y in self.w_vars[x]])
					if date != data[x]:
						changed_val[cols_name[x]] = date

				elif x == len(self.w_vars) - 1:
					value = self.w_vars[x].get("1.0", "end-1c")
					if data[x] != value:
						changed_val[cols_name[x]] = value
				else:
					if data[x] != self.w_vars[x].get():
						changed_val[cols_name[x]] = self.w_vars[x].get()

			return changed_val, row_id

		con, cur, _ = self.database_manager(ret_con_only=True)		# if the cursor is zero that mean it refer to old database not the current database

		cat = self.catagories.get()
		if not cur:			# it mean it use current database
			stat, row_id = check_equality(con)
			if not stat:
				self.show_info("Nilai Tidak Berubah") 
				self.log_bridge(2, "Value Not Changed!, Won't Update The Database For Efficiency")
				return
			else:
				[con.exec(f"UPDATE {cat} SET {x} = {stat[x]} WHERE oid={row_id}") for x in stat]
				self.log_bridge(0, f"Updated {len(stat)} Columns in '{cat}' Tables on {self.cur_database.get()}")
				self.show_info(f"Berhasil Mengupdate {len(stat)} kolom!")

		else:				# it mean it use old database
			stat, row_id = check_equality(con, cur=cur)
			if not stat:
				self.show_info("Nilai Tidak Berubah") 
				self.log_bridge(2, "Value Not Changed!, Won't Update The Database For Efficiency")
				return
			else:
				[con.exec(f"UPDATE {cat} SET {x} = {stat[x]} WHERE oid={row_id}") for x in stat]
				self.log_bridge(0, f"Updated {len(stat)} Columns in '{cat}' Tables on {self.cur_database.get()}")			
				self.show_info(f"Berhasil Mengupdate {len(stat)} kolom!")
		self.refresh_treeview()


	def selected_invoke(self):
		index = self.tree_view.index(self.tree_view.selection()[0])
		if self.insert_edit_w(index):
			self.insert_edit_w(index)


		self.delete_btn.config(state=tk.NORMAL, command=lambda: self.delete_feature(self.tree_view.selection()[0]))
		self.update_btn.config(state=tk.NORMAL, command=lambda: self.update_feature(self.tree_view.selection()[0]))

	def switch_database(self):
		if not self.active_db:
			self.active_db = self.cur_database.get()
			return

		if self.active_db == self.cur_database.get():
			return


		self.refresh_treeview()
		self.active_db = self.cur_database.get()

	def insert_edit_w(self, index):
		cat = self.catagories.get()
		data, _, desc_ = self.database_manager()

		data = data[index]
		data.pop(0)					# remove the first items
		data.pop()					# and the last items
		data.append(desc_[index])	# add a values to the last items

		if cat == "Surat_Keluar":
			try:
				for x in range(len(self.w_vars)):
					if x == 0:
						splited_date = data.pop(1).split("-")
						for i in range(len(self.w_vars[x])):
							self.w_vars[x][i].set(splited_date[i])

					elif x == len(self.w_vars) - 1:
						self.w_vars[x].insert("1.0", data.pop())

					else:
						self.w_vars[x].insert(0, data.pop())

			except tk.TclError as e:
				self.log_bridge(4, str(e))
				self.re_add_w()
				return True

		else:
			for x in range(len(self.w_vars)):
				try:
					if x == 0 or x == 1:
						splited_date = data.pop(0).split("-")
						for i in range(len(splited_date)):
							self.w_vars[x][i].set(splited_date[i])

					elif x == len(self.w_vars) - 1:
						self.w_vars[x].insert("1.0", data.pop())

					else:
						self.w_vars[x].insert(0, data.pop())

				except tk.TclError as e:
					self.log_bridge(4, str(e))
					self.re_add_w()
					return True


	def re_add_w(self):
		if self.catagories.get() == "Surat_Keluar":
			main_frame, var = self.feature_1.main()
		else:
			main_frame, var = self.feature_2.main()

		if self.node_main_frames:
			self.node_main_frames.pop().destroy()

		self.node_main_frames.append(main_frame)
		self.add_var(var)


	def add_var(self, vars_):
		if self.w_vars:
			[x.destroy() for x in self.w_vars if type(x) != list]
			self.w_vars = []
		self.w_vars.extend(vars_)


	def edit_feature(self):
		cat = self.catagories.get()
		
		if self.active_w == cat:
			return

		stat = self.insert_tree_view()

		if not stat:
			if len(self.node_main_frames) > 1:
				self.node_main_frames.pop().destroy()
			return

		if cat == "Surat_Keluar":
			main_frame, var = self.feature_1.main()
		else:
			main_frame, var = self.feature_2.main()

		if not self.active_w:
			self.node_main_frames.append(main_frame)
			self.add_var(var)
			self.active_w = cat
			return

		self.add_var(var)
		self.node_main_frames.pop().destroy()
		self.node_main_frames.append(main_frame)
		self.active_w = cat


	def enable_disable(self):
		if not self.mode_state.get():			# if the switch is in disable status
			if self.disabled:
				return
			self.edit_node_frame.pack_forget()
			self.disabled = True

		else:
			if not self.disabled:
				return
			self.edit_node_frame.pack(fill=tk.BOTH, expand=1)
			self.disabled = False


	def database_manager(self, ret_con_only=False):
		if self.cur_database.get() == self.db_handler.fname.split(".")[0]:
			data, cur = self.db_handler.load_data(self.catagories.get())
			if not data:
				return False, False, 0
			elif ret_con_only:
				return self.db_handler, 0, 0

		else:
			fname = "storage/" + self.cur_database.get() + ".db"
			if not os.path.isfile(fname):
				return False, "0xa", 0
			con = sql.connect(fname)
			cur = con.cursor()
			try:
				data = cur.execute(f"SELECT *, oid FROM {self.catagories.get()}").fetchall()
			except:
				return False, False, 0

			if ret_con_only:
				return con, cur, 1

		data = list(map(list, data))
		cols_name = list(cur.description)

		desc_ = [x.pop(-2) for x in data]
		cols_name.pop(-2)
		cols_name = [x[0] for x in cols_name]
		cols_name.insert(0, "No")

		[data[x].insert(0, str(x+1)) for x in range(len(data))]

		return data, cols_name, desc_


	def show_info(self, msg):
		msgbox.showinfo("Info", msg)

	def insert_tree_view(self):
		data, cur, desc = self.database_manager()

		if not data:
			if cur == "0xa":
				self.show_info("Database Tidak Ditemukan!")
			else:
				self.show_info("Database Kosong! harap ubah database di tools bar jika ingin mengakses database yang lama")
			self.window.lift()
			return False

		children = self.tree_view.get_children()

		if children:
			self.tree_view.delete(children)


		self.tree_view['columns'] = [str(x) for x in range(len(cur))]
		self.tree_view['show'] = "headings"
		[self.tree_view.column(str(x), width=120, anchor='c', minwidth=120) if x == 0 else self.tree_view.column(str(x), width=200, anchor='c', minwidth=200) for x in range(len(cur))]
		[self.tree_view.heading(str(x), text=cur[x]) for x in range(len(cur))]
		[self.tree_view.insert("", tk.END, values=x) for x in data]
		self.tree_frame.pack_propagate(0)
		return True

	def find_databases(self):
		db_name = []

		for x in os.listdir(os.getcwd()):
			if x.endswith(".db"):
				db_name.append(x.split(".")[0])
		if os.path.isdir("storage"):
			[db_name.append(x.split(".")[0]) for x in os.listdir("storage")]
		return db_name
