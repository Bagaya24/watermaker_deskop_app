import tkinter
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont
from datetime import datetime as dt

win = tkinter.Tk()
win.minsize(width=600, height=500)
win.config(padx=20, pady=20)

image_draw = None
image_copyright = None
image_path = ""

# TODO: 2 creer les fontions de traiter l'image
def upload_image():
    global image_draw, image_path
    image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    new_pic = Image.open(f"{image_path}")
    size_img = new_pic.size
    new_pic = new_pic.resize(((round(size_img[0]/4)), round(size_img[1]/4)))
    image_draw = new_pic.copy()
    new_pic_lb = ImageTk.PhotoImage(new_pic)
    image_frame.config(width=int(size_img[0] / 4), height=int(size_img[1] / 4))
    lb_pics.config(image=new_pic_lb)
    lb_pics.image = new_pic_lb
    lb_pics.place(x=0, y=0)


def copyright(image, texte, opacity=1.0, font_size=40):
    global image_copyright
    image = image.convert("RGBA")
    texte_image = Image.new("RGBA", image.size, (255, 255, 255, 0))

    font = ImageFont.truetype('./text_font/roboto.ttf', font_size)
    pos = (0, int(image.size[1] / 2))

    d = ImageDraw.Draw(texte_image)
    d.text(pos, texte, fill=(255, 255, 255, round(opacity * 255)), font=font)

    texte_image = texte_image.rotate(45)

    image_copyright = Image.alpha_composite(image, texte_image)
    return image_copyright


def put_watermaker():
    global image_draw
    text_watermaker = etr_watermarker.get()
    opacity = float(etr_opacity.get())
    size = int(etr_font.get())
    image_copyright = copyright(image_draw, text_watermaker, opacity, size)
    new_pic_draw = ImageTk.PhotoImage(image_copyright)
    lb_pics.config(image=new_pic_draw)
    lb_pics.image = new_pic_draw


def save_img():
    global image_copyright, image_path
    time_saved = dt.now().date()

    image_copyright.save(f"./images_saved/image_{time_saved}.png")


# TODO: 1 creer l interface utilisateur
btn_upload_pics = tkinter.Button(text="UPLOAD", command=upload_image)
btn_upload_pics.grid(row=0, column=3)


# label image
image_frame = tkinter.Frame(win, width=550, height=500, bg="#EEEEEE")
image_frame.grid(row=1, column=0, columnspan=4)

lb_pics = tkinter.Label(image_frame, text="Upload a picture", font=("Arial", 20, "underline"), fg="blue", bg="#EEEEEE")

lb_pics.place(x=220, y=200)

lb_watermaker = tkinter.Label(text="Watermaker: ")
lb_watermaker.grid(row=2, column=0)

etr_watermarker = tkinter.Entry(width=35)
etr_watermarker.grid(row=2, column=1, columns=2)

btn_up_watermaker = tkinter.Button(text="Show", command=put_watermaker)
btn_up_watermaker.grid(row=2, column=4)

lb_opacity = tkinter.Label(text="Opacity:")
lb_opacity.grid(row=3, column=0)

etr_opacity = tkinter.Entry(width=10)
etr_opacity.grid(row=3, column=1)

lb_font = tkinter.Label(text="Font size: ")
lb_font.grid(row=3, column=2)

etr_font = tkinter.Entry(width=20)
etr_font.grid(row=3, column=3)

lb_font = tkinter.Label(text="Font size: ")
btn_save = tkinter.Button(text="Save", width=10, command=save_img)
btn_save.grid(row=4, column=1)


win.mainloop()
