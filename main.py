from tkinter import *
import pyscreenshot

class Paint:
    
    def __init__(self: object) -> None:
        self.window: Tk = Tk()
        self.window.title("Paint")
        self.window.minsize(width=1290, height=720)
        self.window.resizable(0, 0)
        
        self.oval_brush: bool = True
        self.line_brush: bool = False
        self.erase_brush: bool = False
        
        self.img_line: PhotoImage = PhotoImage(file="icon/line.png")
        self.img_circle: PhotoImage = PhotoImage(file="icon/circle.png")
        self.img_erase: PhotoImage = PhotoImage(file="icon/erase.png")
        self.img_save: PhotoImage = PhotoImage(file="icon/save.png")
        self.img_square: PhotoImage = PhotoImage(file="icon/square.png")
        self.img_new: PhotoImage = PhotoImage(file="icon/new.png")
        
        self.color: list = ("black", "gray", "white", "red", "green",
                            "blue", "purple", "orange", "yellow",
                            "#783D6C")
        
        self.pick_colors: str = "black"
        
        
        self.bar_menu: Frame = Frame(self.window, bg="#3b3b3b", height=50)
        self.bar_menu.pack(fill="x")
        
        self.text_color: Label = Label(self.bar_menu, text="Colors:", fg="white", bg="#3b3b3b")
        self.text_color.pack(side="left")
        
        for i in self.color:
            self.button_color: Button = Button(self.bar_menu, bg=i, width=2, height=1, command=lambda col=i:self.select_colors(col))
            self.button_color.pack(side="left")
            
        self.label_colors_choose: Label = Label(self.bar_menu, text="  Color Choose:  ", fg="white", bg="#3b3b3b")
        self.label_colors_choose.pack(side="left")
        
        self.colors_choose: Button = Button(self.bar_menu, image=self.img_square, command=None)
        self.colors_choose.pack(side="left")
            
        self.text_pen_size: Label = Label(self.bar_menu, text=" Size: ", fg="white", bg="#3b3b3b")
        self.text_pen_size.pack(side="left")
        
        self.pen_size: Spinbox = Spinbox(self.bar_menu, from_=1, to=50)
        self.pen_size.pack(side="left")
            
        self.text_brushs: Label = Label(self.bar_menu, text=" Brushs: ", fg="white", bg="#3b3b3b")
        self.text_brushs.pack(side="left")
            
        self.button_line: Button = Button(self.bar_menu, image=self.img_line, command=self.brush_line).pack(side="left")
        self.button_circle: Button = Button(self.bar_menu, image=self.img_circle, command=self.brush_oval).pack(side="left")
        self.button_erase: Button = Button(self.bar_menu, image=self.img_erase, command=self.brush_erase).pack(side="left")
        
        self.text_option: Label = Label(self.bar_menu, text=" Options: ", fg="white", bg="#3b3b3b")
        self.text_option.pack(side="left")
        
        self.button_save: Button = Button(self.bar_menu, image=self.img_save, command=self.save)
        self.button_save.pack(side="left")
        self.button_new: Button = Button(self.bar_menu, image=self.img_new, command=self.clean)
        self.button_new.pack(side="left")
        
        self.area_draw: Canvas = Canvas(self.window, height=720, bg="gainsboro")
        self.area_draw.pack(fill="both")
        self.area_draw.bind("<B1-Motion>", self.draw)
        
        self.window.mainloop()
        
    def draw(self: object, event) -> None:
        x1, y1 = event.x, event.y
        x2, y2 = event.x, event.y
        
        if self.oval_brush:
            self.area_draw.create_oval(x1,y1,x2,y2, fill=self.pick_colors, outline=self.pick_colors, width=self.pen_size.get())
        elif self.line_brush:
            self.area_draw.create_line(x1-10,y1-10,x2,y2, fill=self.pick_colors, width=self.pen_size.get())
        else:
            self.area_draw.create_oval(x1,y1,x2,y2, fill="gainsboro", outline="gainsboro", width=self.pen_size.get())
        
    def select_colors(self: object, color) -> None:
        self.pick_colors = color
        
    def brush_oval(self: object) -> None:
        self.oval_brush: bool = True
        self.line_brush: bool = False
        self.erase_brush: bool = False
        
    def brush_line(self: object) -> None:
        self.oval_brush: bool = False
        self.line_brush: bool = True
        self.erase_brush: bool = False
        
    def brush_erase(self: object) -> None:
        self.oval_brush: bool = False
        self.line_brush: bool = False
        self.erase_brush: bool = False
        
    def clean(self: object) -> None:
        self.area_draw.delete("all")
        
    def save(self: object) -> None:
        
        x = self.window.winfo_rootx() + self.area_draw.winfo_x()
        y = self.window.winfo_rooty() + self.area_draw.winfo_y()
        x1 = self.window.winfo_rootx() + self.area_draw.winfo_width()
        y1 = self.window.winfo_rooty() + self.area_draw.winfo_height()
        
        img = pyscreenshot.grab(bbox=(x, y, x1, y1))
        img.save("image.jpeg", "jpeg")
        
    def selected_color(self: object) -> None:
        colorchoose.askcolor
        
Paint()