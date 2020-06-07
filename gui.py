from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
from image_utils import *


class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("K-means Visualization Tool")
        self.geometry("2000x700")
        self.imgFrame = ttk.Labelframe(self)
        self.imgFrame.grid(column=0, row=4)
        self.labelFrame = ttk.LabelFrame(self, text="Open File")
        self.labelFrame.grid(column=0, row=1, padx=20, pady=20)

        self.button()

    def button(self):
        self.button = ttk.Button(self.labelFrame, text="Browse A File", command=self.file_dialog)
        self.button.grid(column=1, row=1)

    def file_dialog(self):
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=
        (("JPEG file", "*.jpg, .jpeg"), ("all files", "*.*")))
        self.label = ttk.Label(self.labelFrame, text="")
        self.label.grid(column=1, row=2)
        self.label.configure(text=self.filename)
        self.open_image()

    def open_image(self):
        image = Image.open(self.filename)
        photo = ImageTk.PhotoImage(image)
        self.myvar = Label(self.imgFrame, image=photo)
        self.myvar.image = photo
        self.myvar.grid(row=4, column=1)

        self.textLabel = Label(self, text="K:").grid(row=3, column=3)
        self.enter = Entry(self)
        self.enter.grid(row=3, column=4)

        self.b1 = Button(self, text="Run K-Means", command=self.k_means)
        self.b1.grid(row=4, column=4)

    def k_means(self):
        k = int(self.enter.get())
        image = read_jpg(self.filename)
        new_image = assign_clusters(image, k)
        img = Image.fromarray(new_image.astype('uint8'))
        photo = ImageTk.PhotoImage(img)
        self.new_imgFrame = ttk.Labelframe(self)
        self.new_imgFrame.grid(column=10, row=4, padx=50, pady=20)
        self.new_var = Label(self.new_imgFrame, image=photo)
        self.new_var.image = photo
        self.new_var.grid(row=4, column=10)


root = Root()
root.mainloop()
