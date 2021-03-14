# this is the program that holds the widgets within the main tabs 
# that inheritance from the core module
import tkinter as tk
from tkinter import ttk, filedialog as fd, messagebox as msg
import datetime

"""
		WIDGETS CONTAINS:

	1. Alamat Penerima ( Entry )
	2. Tanggal ( MenuOption )
	3. Nomor ( Entry )
	4. Perihal (Text)



"""

## CONST

x_axis = tk.X
y_axis = tk.Y
BOTH = tk.BOTH
TOP = tk.TOP
LEFT = tk.LEFT
VERTICAL = tk.VERTICAL
HORIZONTAL = tk.HORIZONTAL
END = tk.END

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

		tgl = tk.StringVar()
		bln = tk.StringVar()
		thn = tk.StringVar()

		center_frame = tk.Frame(self.main_frame)
		center_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

		center_node = tk.LabelFrame(center_frame, padx=10, pady=10)
		center_node.pack(side=TOP, fill=BOTH, anchor='n', expand=1)

		center_node_upper = tk.Frame(center_node)
		center_node_upper.pack(fill=BOTH, expand=1)

		tk.Label(center_node_upper, text="Alamat Penerima:").grid(row=0, column=0, padx=5, sticky='w', pady=5)
		self.alamat_penerima = tk.Entry(center_node_upper, width=30)
		self.alamat_penerima.grid(row=0, column=1, padx=5, pady=5, sticky='w')
		self._val.append(self.alamat_penerima)

		tgl_frame = tk.LabelFrame(center_node_upper, text="Tanggal Dikirim", padx=10, pady=10)
		tgl_frame.grid(row=1, column=0, columnspan=2, pady=10, sticky='w')

		tgl.set(datetime.datetime.now().day)
		bln.set(datetime.datetime.now().month)
		thn.set(datetime.datetime.now().year)

		self._val.append([tgl, bln, thn])

		tk.OptionMenu(tgl_frame, tgl, *tgl_list).pack(side=LEFT)
		tk.OptionMenu(tgl_frame, bln, *bln_list).pack(side=LEFT)
		tk.OptionMenu(tgl_frame, thn, *thn_list).pack(side=LEFT)

		tk.Label(center_node_upper, text="Nomor Surat:").grid(row=3, column=0, sticky='w', pady=10, padx=5)

		nomor_surat = tk.Entry(center_node_upper, width=30)
		nomor_surat.grid(row=3, column=1, pady=10, padx=5)
		self._val.append(nomor_surat)


		text_frame = tk.Frame(center_node)
		text_frame.pack()

		tk.Label(text_frame, text="Perihal", justify='left').pack(fill=x_axis, anchor='w', expand=True)

		upper_frame = tk.Frame(text_frame)
		upper_frame.pack(fill=BOTH, expand=1, pady=10)

		text_w = tk.Text(upper_frame, wrap=tk.NONE)
		text_w.pack(side=LEFT, fill=BOTH, expand=1)
		self._val.append(text_w)

		y_scroll = ttk.Scrollbar(upper_frame, orient=VERTICAL, command=text_w.yview)
		y_scroll.pack(side=LEFT, fill=y_axis)
		text_w.config(yscrollcommand=y_scroll.set)

		x_scroll = ttk.Scrollbar(text_frame, orient=HORIZONTAL, command=text_w.xview)
		x_scroll.pack(fill=x_axis, expand=1)
		text_w.config(xscrollcommand=x_scroll.set)






