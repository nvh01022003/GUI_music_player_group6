import tkinter as tk
from tkinter import PhotoImage, Canvas, Scrollbar

class PlayList:
    def __init__(self, root):
        self.root = root
        self.root.title("Danh sách phát nhạc")
        self.root.geometry("375x422")
        self.root.resizable(False, False)

        # Create a frame for the main content
        self.frame = tk.Frame(root)
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Create a canvas for the song list with a vertical scrollbar
        self.canvas = Canvas(self.frame, bg="white")  # Set canvas background color
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create a scrollbar and associate it with the canvas
        self.scrollbar = Scrollbar(self.frame, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Create a frame to contain the song buttons
        self.song_frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.song_frame, anchor=tk.NW)

        # Create a list of songs
        self.songs = [
            {"title": "Ánh Nắng Của Anh", "color": "#CCFFFF", "image_path": "anca.png", "artist": "Đức Phúc"},
            {"title": "Bùa Yêu", "color": "#CCFFFF", "image_path": "by.png", "artist": "Bích Phương"},
            {"title": "Mặt Trời Của Em", "color": "#CCFFFF", "image_path": "mtce.png", "artist": "Phương Ly, JustaTee"},
            {"title": "Hẹn Yêu", "color": "#CCFFFF", "image_path": "hy.png", "artist": "Vũ Cát Tường"},
            {"title": "Yêu Được Không", "color": "#CCFFFF", "image_path": "ydk.png", "artist": "Đức Phúc"},
            {"title": "Tình Yêu Màu Nắng", "color": "#CCFFFF", "image_path": "tymn.png",
             "artist": "Đoàn Thuý Trang, BigDaddy"},
            {"title": "Tớ Thích Cậu", "color": "#CCFFFF", "image_path": "ttc.png", "artist": "Han Sara"},
            {"title": "Trót Yêu", "color": "#CCFFFF", "image_path": "ty.png", "artist": "Trung Quân"},
            {"title": "Mình Hẹn Hò Nhau Đi", "color": "#CCFFFF", "image_path": "mhhnd.png", "artist": "Han Sara"},
            {"title": "Thích Rồi Đấy", "color": "#CCFFFF", "image_path": "trd.png", "artist": "Suni Hạ Linh"},
            {"title": "Ta Đã Yêu Chưa Vậy", "color": "#CCFFFF", "image_path": "tdycv.png",
             "artist": "Issac, BigDaddy"},
            {"title": "Mình Yêu Nhau Đi", "color": "#CCFFFF", "image_path": "mynd.png", "artist": "Bích Phương"},
            {"title": "Cô Gái Nhà Bên", "color": "#CCFFFF", "image_path": "cgnb.png", "artist": "Jun Phạm"},
            {"title": "Muốn Yêu Ai Đó Cả Cuộc Đời", "color": "#CCFFFF", "image_path": "myadccd.png",
             "artist": "Hoàng Yến Chibi, Tino"},
        ]  # Your list of songs here

        # Create buttons for each song with images and text on the song_frame
        self.song_buttons = []  # Keep references to song buttons
        for i, song in enumerate(self.songs):
            image = PhotoImage(file=song["image_path"])
            # Resize the image using the subsample method
            image = image.subsample(3, 3)  # You can adjust the subsample values as needed
            song_frame = tk.Frame(self.song_frame, bg=song["color"])
            song_frame.pack(fill=tk.X)
            # Create a button for the image and text
            song_button = tk.Button(
                song_frame,
                image=image,
                text=f"{i + 1}. {song['title']}\n{song['artist']}",  # Display artist name below title
                compound=tk.LEFT,  # Show image and text together
                font=("Helvetica", 12, "bold"),  # Use a bold font for both title and artist
                relief=tk.FLAT,
                padx=10,
                pady=5,
                anchor="w"  # Align text to the left
            )
            song_button.image = image  # Keep a reference to the image
            song_button.pack(fill=tk.X, expand=True, padx=27, pady=0, ipadx=20)

            # Customize the font style for the artist
            song_button.configure(font=("Helvetica", 10, "normal"), anchor="w", justify="left")

            # Bind the button to a function that plays the song
            song_button.config(command=lambda title=song["title"]: self.play_song(title))

            self.song_buttons.append(song_frame)  # Append to the list of song buttons

        # Update the canvas to fit the content
        self.song_frame.update_idletasks()
        canvas_width = self.song_frame.winfo_reqwidth()
        canvas_height = self.song_frame.winfo_reqheight()
        self.canvas.config(scrollregion=(0, 0, canvas_width, canvas_height))

        # Load an image to use as the button background
        button_image = PhotoImage(file="playlist.png")  # Replace "button_image.png" with your image file
        self.button = tk.Button(self.canvas, image=button_image)
        self.button.image = button_image  # Keep a reference to the image
        self.canvas.create_window((360, 0), window=self.button, anchor=tk.NE)



    def play_song(self, title):
        # Add logic to play the selected song here
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = PlayList(root)

    root.mainloop()
