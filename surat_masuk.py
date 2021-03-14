# this is the program that holds the widgets within the main tabs 
# that inheritance from the core module
import tkinter as tk
from tkinter import ttk, filedialog as fd, messagebox as msg
import datetime

"""		WIDGETS AVAILABLE
	
	1. Tanggal Surat (OptionMenu)
	2. Tanggal Diterima (OptionMenu)
	3. Alamat Pengirim (Entry)
	4. Nomor Surat (Entry)
	5. Perihal (Text)

"""


# defines consts
BOTH = tk.BOTH
LEFT  = tk.LEFT
TOP = tk.TOP
CENTER = tk.CENTER
NONE = tk.NONE
HORIZONTAL = tk.HORIZONTAL
VERTICAL = tk.VERTICAL
x_axis = tk.X
y_axis = tk.Y



class Main:
	def __init__(self, master_, parent_):
		self.root = master_
		self.main_frame = tk.Frame(parent_)
		self._val = []

	def nodes(self):
		local_year = int(datetime.datetime.now().year)

		tgl_list = [x for x in range(1, 31)]
		bln_list = [x for x in range(1, 13)]
		thn_list = [x for x in range(local_year-20, local_year+20)]

		tgl_s = tk.StringVar()
		bln_s = tk.StringVar()
		thn_s = tk.StringVar()

		tgl_m = tk.StringVar()
		bln_m = tk.StringVar()
		thn_m = tk.StringVar()

		self._val.append([tgl_s, bln_s, thn_s])
		self._val.append([tgl_m, bln_m, thn_m])

		center_frame = tk.Frame(self.main_frame)
		center_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

		center_frame_node = tk.LabelFrame(center_frame, padx=10, pady=10)
		center_frame_node.pack(fill=BOTH, expand=True, anchor='n', side=TOP)

		frame_1 = tk.Frame(center_frame_node)
		frame_1.pack(anchor='w')

		tk.Label(frame_1, text="Alamat Pengirim:").pack(side=LEFT, anchor='w')

		alamat_pengirim = tk.Entry(frame_1, width=30)
		alamat_pengirim.pack(side=LEFT, padx=50)
		self._val.append(alamat_pengirim)

		frame_2 = tk.Frame(center_frame_node)
		frame_2.pack(anchor='w')

		tk.Label(frame_2, text="Nomor Surat:").pack(side=LEFT, anchor='w', pady=10)

		nomor_surat = tk.Entry(frame_2, width=30)
		nomor_surat.pack(side=LEFT, padx=75, pady=10)
		self._val.append(nomor_surat)

		date_frame = tk.Frame(center_frame_node, padx=5, pady=5)
		date_frame.pack(pady=5, anchor='w', fill=x_axis, expand=True)

		date_1 = tk.LabelFrame(date_frame, text="Tanggal Surat", padx=5, pady=5)
		date_1.pack(side=LEFT, anchor='w')

		tgl_s.set(datetime.datetime.now().day)
		bln_s.set(datetime.datetime.now().month)
		thn_s.set(datetime.datetime.now().year)

		tk.OptionMenu(date_1, tgl_s, *tgl_list).pack(side=LEFT)
		tk.OptionMenu(date_1, bln_s, *bln_list).pack(side=LEFT, padx=10)
		tk.OptionMenu(date_1, thn_s, *thn_list).pack(side=LEFT)

		date_2 = tk.LabelFrame(date_frame, text="Diterima Tanggal", padx=10, pady=10)
		date_2.pack(side=LEFT, padx=10, anchor='w') 

		tgl_m.set(datetime.datetime.now().day)
		bln_m.set(datetime.datetime.now().month)
		thn_m.set(datetime.datetime.now().year)

		tk.OptionMenu(date_2, tgl_m, *tgl_list).pack(side=LEFT)
		tk.OptionMenu(date_2, bln_m, *bln_list).pack(side=LEFT, padx=10)
		tk.OptionMenu(date_2, thn_m, *thn_list).pack(side=LEFT)

		frame_3 = tk.Frame(center_frame_node)
		frame_3.pack()

		tk.Label(frame_3, text="Perihal", justify='left').pack(anchor='w', fill=x_axis, expand=1)

		text_w_frame = tk.Frame(frame_3)
		text_w_frame.pack()

		text_w = tk.Text(text_w_frame, wrap=NONE)
		text_w.pack(side=LEFT, fill=BOTH, expand=True)
		self._val.append(text_w)

		y_scrollbar = ttk.Scrollbar(text_w_frame, orient=VERTICAL, command=text_w.yview)
		y_scrollbar.pack(side=LEFT, fill=y_axis, expand=1)
		text_w.config(yscrollcommand=y_scrollbar.set)

		x_scrollbar = ttk.Scrollbar(frame_3, orient=HORIZONTAL, command=text_w.xview)
		x_scrollbar.pack(fill=x_axis)
		text_w.config(xscrollcommand=x_scrollbar.set)




