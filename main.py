from tkinter import *
from tkinter import ttk
import requests
from districts import india_states
from PIL import Image, ImageTk

def get_temp(url, state):
    
    response = requests.get(url) 
    if response.status_code == 200:
        data = response.json()
        Cit_info = data["main"]
        return Cit_info
    else:
        print("Failed to fetch data")

def update_districts(event):
    selected_state = StateChosen.get()
    districtChosen["values"] = india_states[selected_state]
    districtChosen.set('')

def done_click():
    state = StateChosen.get()
    city = districtChosen.get()
    api_key = "YOUR_API_KEY_HERE"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{state},IN&appid={api_key}&units=metric"
    state_wea = get_temp(url, state);
    state_label = Label(win, text=f"========{city.capitalize()}'s Weather========", font= ("Inter", 12, "bold"), bg="white", fg="black", width=30)
    temp_label = Label(win, text=f"temperature: {state_wea['temp']}", font= ("Inter", 12, "bold"), bg="white", fg="black", width=30)
    act_label = Label(win, text=f"but feels like: {state_wea['feels_like']}", font= ("Inter", 12, "bold"), bg="white", fg="black", width=30)
    max_label = Label(win, text=f"Maximum tempereture today: {state_wea['temp_max']}", font= ("Inter", 12, "bold"), bg="white", fg="black", width=30)
    min_label = Label(win, text=f"Minimum temperature today: {state_wea['temp_min']}", font= ("Inter", 12, "bold"), bg="white", fg="black", width=30)
    end_label = Label(win, text="===============================", font= ("Inter", 12, "bold"), bg="white", fg="black", width=30)
    state_label.pack()
    temp_label.pack()
    act_label.pack()
    max_label.pack()
    min_label.pack()
    end_label.pack()

win = Tk()
win.title("The Weather App")



win.geometry("800x600")
win["bg"] = "green"

pil_img = Image.open(r"hamburger.jpg")
pil_img = pil_img.resize((800, 600), Image.Resampling.LANCZOS)
img = ImageTk.PhotoImage(pil_img)
bg_label = Label(win, image=img)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
bg_label.image = img
# Label(win, text="Content Here").pack(pady=50)


name_label = Label(win, text="Spy Weather App", font= ("Inter", 30, "bold"), bg="white", fg="black", width=17)
name_label.pack(pady=30)


frame = Frame(win, bg="green")
frame.pack()


StateLabel = Label(frame, text="Select state: ", font= ("Inter", 10, "bold"), bg="white", fg="black", width=15)
StateLabel.grid(row=0, column=0, padx=5)




n = StringVar()
StateChosen = ttk.Combobox(frame, width=25, textvariable=n, font=("Inter", 10))
StateChosen["values"] = ("Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", 
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir", 
    "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", 
    "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", 
    "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", 
    "Uttar Pradesh", "Uttarakhand", "West Bengal",
    "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli and Daman and Diu", 
    "Delhi", "Ladakh", "Lakshadweep", "Puducherry")
StateChosen.grid(row=0, column=1, padx=5)

StateChosen.bind("<<ComboboxSelected>>", update_districts)


districtLabel = Label(frame, text="Select district: ", font= ("Inter", 10, "bold"), bg="white", fg="black", width=15)
districtLabel.grid(row=1, column=0, padx=5)

ds = StringVar()
districtChosen = ttk.Combobox(frame, width=25, textvariable=ds, font=("Inter", 10))
districtChosen.grid(row=1, column=1, padx=5, pady=5)

done_but = Button(win, text="Done", command=done_click, activebackground="blue", activeforeground="white", anchor="center", font=("Inter", 14))
done_but.pack(padx=20, pady=25)
win.mainloop()