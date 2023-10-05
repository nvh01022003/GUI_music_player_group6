from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageDraw
import pygame

class main_player_music:
    def __init__(self,root) :
        self.root = root
        self.root.title("GUI Music Player")
        self.root.geometry("375x667")
        self.root.resizable(False, False)
        self.root.attributes("-topmost",True)
       
       # Tạo hình nền gradient
        self.gradient_width = 1000
        self.gradient_height = 1000
        self.gradient_image = Image.new("RGB", (self.gradient_width, self.gradient_height))
        # Màu nền gradient - sử dụng color1 và color2
        self.color1 = "#1A4644"  # Màu xanh, màu phía dưới
        self.color2 = "#40E9DF"  # Màu xanh , màu phía trên
        self.draw = ImageDraw.Draw(self.gradient_image)
        for i in range( self.gradient_height):
            r = int((( self.gradient_height - i) /  self.gradient_height) * (int(self.color2[1:3], 16) - int(self.color1[1:3], 16)) + int(self.color1[1:3], 16))
            g = int((( self.gradient_height - i) /  self.gradient_height) * (int(self.color2[3:5], 16) - int(self.color1[3:5], 16)) + int(self.color1[3:5], 16))
            b = int((( self.gradient_height - i) /  self.gradient_height) * (int(self.color2[5:7], 16) - int(self.color1[5:7], 16)) + int(self.color1[5:7], 16))
            color = "#{:02X}{:02X}{:02X}".format(r, g, b)
            self.draw.line([(0, i), (self.gradient_width, i)], fill=color)
        # Chuyển hình nền gradient thành PhotoImage
        self.gradient_photo = ImageTk.PhotoImage(self.gradient_image)
        # Tạo một Label và đặt hình nền gradient
        self.background_label = ttk.Label(self.root, image=self.gradient_photo)
        self.background_label.place(relwidth=1, relheight=1)


        # Tạo khung main điều khiển (ảnh bài đang phát)
        self.image_main = ImageTk.PhotoImage(Image.open("E:/python/lactroi.jpg"))
        self.lable_main = Label(root,image=self.image_main)
        self.lable_main.place(x=30,y=94)
        # Tạo một Label chứa văn bản "Lạc Trôi"
        self.label_tenbaihat = tk.Label(self.root, text="Lạc Trôi", font=("Arrus-Black", 14),bg="#3F8F8A",relief="flat")
        self.label_tenbaihat.place(x=13,y=415)

        # Tạo một Label chứa văn bản "Sơn Tùng MTP"
        self.label_sangtac = tk.Label(self.root, text="Sơn Tùng MTP", font=("Arrus-Black", 11),bg="#3F8F8A",relief="flat")
        self.label_sangtac.place(x=13,y=442)

        #tạo nút phát ngẫu nhiên
        self.image_shuffle = ImageTk.PhotoImage(Image.open("E:/python/shuffle.png"))
        self.button_shuffle = Button(root,image=self.image_shuffle,bg="#3F8F8A",relief="flat")
        self.button_shuffle.place(x=13,y=531)
        #tạo nút phát nhạc phía trước
        self.image_previous = ImageTk.PhotoImage(Image.open("E:/python/previous.png"))
        self.button_previous = Button(root,image=self.image_previous,bg="#3F8F8A",relief="flat")
        self.button_previous.place(x=81,y=526)
        #tạo nút phát bài tiếp theo
        self.image_next = ImageTk.PhotoImage(Image.open("E:/python/next.png"))
        self.button_next = Button(root,image=self.image_next,bg="#3F8F8A",relief="flat")
        self.button_next.place(x=247,y=526)
        #tạo nút phát lại liên tục bài đang phát
        self.image_repeat = ImageTk.PhotoImage(Image.open("E:/python/repeat.png"))
        self.button_repeat = Button(root,image=self.image_repeat,bg="#3F8F8A",relief="flat")
        self.button_repeat.place(x=325,y=531)
        #tạo nút playlist để truy cập 
        self.image_playlist = ImageTk.PhotoImage(Image.open("E:/python/playlist.png"))
        self.button_playlist = Button(root,image=self.image_playlist,relief="flat")
        self.button_playlist.place(x=315,y=27)
        
       
        # Khởi tạo pygame
        pygame.init()
        # Tạo thanh thời gian (progressbar) ở chế độ xem trước
        self.progress_bar = ttk.Scale(self.root, from_=0, to=250, orient="horizontal",length=350)
        self.progress_bar.pack(pady=300,padx=50)
        self.progress_bar.place(x=13,y=465)

        # Tạo Label để hiển thị thời gian
        self.time_label = ttk.Label(self.root, text="0:00")
        self.time_label.place(x=13,y=492)

        # Tạo biến cho biểu tượng Pause và Play
        self.pause_icon = None
        self.play_icon = None

        # Tạo nút Pause/Play sử dụng biểu tượng
        def toggle_music():
            global is_playing
            if self.is_playing:
                pygame.mixer.music.pause()
                self.play_pause_button.config(image=self.play_icon)
            else:
                pygame.mixer.music.unpause()
                self.play_pause_button.config(image=self.pause_icon)
            self.is_playing = not self.is_playing

        self.play_pause_button = tk.Button(self.root,bg="#3F8F8A", command=toggle_music,relief="flat")
        self.play_pause_button.place(x=159,y=521)

        
      


#lactroi
        # Bắt đầu chạy nhạc
        self.music_file = "E:/python/lactroi.mp3"  # Đặt tên file nhạc ở đây
        pygame.mixer.music.load(self.music_file)
        pygame.mixer.music.play()

        # Khởi tạo biến thời gian chạy
        self.is_playing = True
        self.current_time = 0

        def update_progress_bar():
            global current_time
            if pygame.mixer.music.get_busy() and self.is_playing:
                # Lấy thời gian hiện tại của nhạc
                self.current_time = pygame.mixer.music.get_pos() / 1000  # Đổi thành giây

                # Định dạng thời gian thành phút:giây
                self.minutes = int(self.current_time // 60)
                self.seconds = int(self.current_time % 60)
                self.time_str = f"{self.minutes}:{self.seconds:02d}"

               # Cập nhật giá trị thanh thời gian và Label thời gian
                self.progress_bar.set(self.current_time)
                self.time_label.config(text=self.time_str)
                self.time_label.config(background="#3F8F8A")
            

            # Gọi lại hàm sau 1 giây
            root.after(1000, update_progress_bar)

        # Bắt đầu cập nhật giá trị thanh thời gian
        update_progress_bar()
        

        # Load hình ảnh Pause và Play từ file
        self.pause_image = Image.open("E:/python/pause.png")
        self.play_image = Image.open("E:/python/play.png")

        # Chuyển hình ảnh thành biểu tượng (icon) cho nút
        self.pause_icon = ImageTk.PhotoImage(self.pause_image)
        self.play_icon = ImageTk.PhotoImage(self.play_image)

        # Thiết lập biểu tượng ban đầu cho nút
        self.play_pause_button.config(image=self.pause_icon)
        self.play_pause_button.image = self.pause_icon  # Bổ sung để giữ biểu tượng hiển thị đúng

        # Xử lý khi kéo thanh thời gian đến một vị trí
        def seek_music(value):
            if self.is_playing:
                self.new_time = float(self.progress_bar.get())
                pygame.mixer.music.set_pos(new_time)
        self.progress_bar.bind("<Button-1>", seek_music)



        

       
   
    
   



root = Tk()
obj = main_player_music(root)
root.mainloop()

''' # Tạo biến để theo dõi trạng thái của nút
        self.is_paused = False
        # Định nghĩa hàm callback để chuyển đổi trạng thái và hình ảnh của nút
        def toggle_pause():
#            global is_paused
            if self.is_paused:
            # Nếu đang ở trạng thái tạm dừng, chuyển về trạng thái phát và thay đổi hình ảnh
                self.button_play.config(image=self.image_play)
                self.is_paused = False
            else:
                # Nếu đang ở trạng thái phát, chuyển về trạng thái tạm dừng và thay đổi hình ảnh
                self.button_play.config(image=self.image_pause)
                self.is_paused = True

        self.image_play = ImageTk.PhotoImage(Image.open("E:/python/play.png"))
        self.button_play = Button(root,image=self.image_play,command=toggle_pause)
        self.button_play.pack(side=LEFT)

        self.image_pause = ImageTk.PhotoImage(Image.open("E:/python/pause.png"))
        self.button_pause = Button(root,image=self.image_pause)
        #button_pause.pack(side=LEFT)'''


''' 
       # Tạo một Scale để hiển thị thanh thời gian
        #option 1 làm scale()
        time_scale = Scale(root, from_=0, to=100, orient="horizontal", length=300)
        time_scale.pack(pady=10)
        #option 2 làm progressbar()
        self.prog = ttk.Progressbar(self.root,orient="horizontal",length=424,mode="determinate")
        self.prog.place(x=0,y=392,height=7)


        # Tạo một Label để hiển thị thời gian đã chạy được nhạc dưới định dạng phút:giây
        self.lable_start = Label(self.root, text="00:00",font=("times new roman",12),bg="#262626",fg="lightgray")
        self.lable_start.place(x=10,y=360)

        self.lable_end = Label(self.root, text="00:00",font=("times new roman",12),bg="#262626",fg="lightgray")
        self.lable_end.place(x=370,y=360)'''
