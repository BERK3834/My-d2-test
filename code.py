import tkinter as tk  
import random
import time
from tkinter import messagebox

class D2AttentionTest:
    def __init__(self, root):
        self.root = root
        self.root.title("D2 Dikkat Testi")
        self.root.geometry("1000x700")
        self.root.configure(bg="black")

        self.test_running = False
        self.correct_answers = 0
        self.false_positives = 0
        self.row_time = 20  
        self.current_row = 0
        self.timer_running = False 
        self.total_rows = 14
        
        self.header_frame = tk.Frame(self.root, bg="black")
        self.header_frame.pack(fill=tk.X, padx=10, pady=10)

        self.result_label = tk.Label(self.header_frame, text="Doğru: 0 | Yanlış: 0", font=("Arial", 14), fg="white", bg="black")
        self.result_label.pack(side=tk.RIGHT, padx=20)
        
        self.timer_label = tk.Label(self.root, text=f"Kalan Süre: {self.row_time} saniye", font=("Arial", 14), fg="white", bg="black")
        self.timer_label.pack(pady=10)

        self.start_screen()

    def start_screen(self):
        self.clear_widgets()

        tk.Label(self.root, text="Dikkat Testi Kuralları", font=("Arial", 16, "bold"), fg="white", bg="black").pack(pady=20)

        tk.Label(self.root, text="Bu test, görsel dikkat seviyenizi ölçmek için tasarlanmıştır.\n"
                                 "- 'd' harfi ve yanında 2 adet '-' çizgisi olanları seçin.\n"
                                 "- Yanlış seçim yapmamaya dikkat edin!\n"
                                 "- Her satır için 20 saniyeniz var.\n"
                                 "- Test sonunda hata oranınız ve başarı puanınız hesaplanacaktır.\n"
                                 "Hazır olduğunuzda 'Başla' butonuna tıklayın.", 
                 font=("Arial", 12), fg="white", bg="black", justify="left").pack(pady=10)

        tk.Button(self.root, text="Başla", font=("Arial", 14, "bold"), bg="gray", fg="white", command=self.start_test).pack(pady=20)

    def start_test(self):
        self.test_running = True
        self.correct_answers = 0
        self.false_positives = 0
        self.current_row = 0
        self.timer_running = True  

        self.clear_widgets()
        self.timer_label = tk.Label(self.root, text=f"Kalan Süre: {self.row_time} saniye", font=("Arial", 14), fg="white", bg="black")
        self.timer_label.pack(pady=10)

        self.canvas = tk.Canvas(self.root, bg="black")
        self.scrollbar = tk.Scrollbar(self.root, orient=tk.HORIZONTAL, command=self.canvas.xview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="black")
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )
        
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(xscrollcommand=self.scrollbar.set)
        
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.scrollbar.pack(fill=tk.X)

        self.grid_frame = tk.Frame(self.scrollable_frame, bg="black")
        self.grid_frame.pack(pady=20)

        self.letters = self.generate_letters()
        self.buttons = []

        self.create_row(self.current_row)
        self.update_timer()

    def generate_letters(self):
        letters = []
        for _ in range(self.total_rows):
            row = []
            target_count = random.randint(4, 7)  # Her satırda 4-7 arasında 'd--' olacak
            target_positions = random.sample(range(47), target_count)
            
            for j in range(47):
                if j in target_positions:
                    row.append("d--")
                else:
                    row.append(random.choice(["b-", "b", "p", "d", "--p", "-p", "d-", "p-", "p--"]))
            letters.append(row)
        return letters

    def create_row(self, row_index):
        for widget in self.grid_frame.winfo_children():
            widget.destroy()
        
        self.buttons = []
        for j in range(47): 
            btn = tk.Button(self.grid_frame, text=self.letters[row_index][j], font=("Arial", 12), bg="black", fg="white", width=3, height=1,
                            command=lambda c=j: self.check_selection(row_index, c))
            btn.grid(row=0, column=j, padx=3, pady=3)
            self.buttons.append(btn)

    def check_selection(self, row, col):
        if not self.test_running:
            return  

        btn = self.buttons[col]
        selected = btn.cget("text")
        if selected == "d--":
            self.correct_answers += 1
            btn.configure(bg="green", state=tk.DISABLED)
        else:
            self.false_positives += 1
            btn.configure(bg="red", state=tk.DISABLED)

        self.result_label.config(text=f"Doğru: {self.correct_answers} | Yanlış: {self.false_positives}")
    
    def update_timer(self):
        if self.row_time > 0 and self.timer_running:
            self.row_time -= 1
            self.timer_label.config(text=f"Kalan Süre: {self.row_time} saniye")
            self.root.after(1000, self.update_timer)  
        else:
            self.next_row()

    def next_row(self):
        if self.current_row < self.total_rows - 1:
            self.current_row += 1
            self.row_time = 20
            self.create_row(self.current_row)
            self.update_timer()
        else:
            self.finish_test()

    def finish_test(self):
        self.test_running = False
        self.timer_running = False  
        self.clear_widgets()

        hata_orani = round((self.false_positives / max(1, self.correct_answers + self.false_positives)) * 100, 2)
        basari_puani = max(0, self.correct_answers * 10 - self.false_positives * 5)
        
        tk.Label(self.root, text="Test Tamamlandı!", font=("Arial", 14, "bold"), fg="white", bg="black").pack(pady=10)
        tk.Label(self.root, text=f"Doğru: {self.correct_answers} | Yanlış: {self.false_positives}\nHata Oranı: %{hata_orani} | Başarı Puanı: {basari_puani}", font=("Arial", 12), fg="white", bg="black").pack(pady=10)
        tk.Button(self.root, text="Yeniden Başla", font=("Arial", 14), bg="gray", fg="white", command=self.start_screen).pack(pady=20)

    def clear_widgets(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = D2AttentionTest(root)
    root.mainloop()
