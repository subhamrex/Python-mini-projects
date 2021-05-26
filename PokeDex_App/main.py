# Imports
import pypokedex as pk
import PIL.Image , PIL.ImageTk
import tkinter as tk
import urllib3
from io import BytesIO

# Tkinter Initialization and setting geometry and title
root = tk.Tk()
root.geometry("600x500")
root.title("PokeDex")
root.config(padx=10,pady=10)

# Title label
title_label = tk.Label(root,text = "Ash's Pokedex")
title_label.config(font=("Arial",32))
title_label.pack(padx=10,pady=10)

# Pokemon image label
pokemon_image = tk.Label(root)
pokemon_image.config(font=("Arial",20))
pokemon_image.pack(padx=10,pady=10)

# Pokemon information label
pokemon_information = tk.Label(root)
pokemon_information.config(font=("Arial",20))
pokemon_information.pack(padx=10,pady=10)

# Pokemon types label
pokemon_types = tk.Label(root)
pokemon_types.config(font=("Arial",20))
pokemon_types.pack(padx=10,pady=10)

def load_pokemon():
    pokemon = pk.get(name=text_id_name.get(1.0,"end-1c"))

    http = urllib3.PoolManager()
    response = http.request('GET',pokemon.sprites.front.get('default'))
    image = PIL.Image.open(BytesIO(response.data))

    # Load image
    img = PIL.ImageTk.PhotoImage(image)
    pokemon_image.config(image=img)
    pokemon_image.image = img

    # Load pokemon information
    pokemon_information.config(text=f"{pokemon.dex} - {pokemon.name}".title())

    # Load pokemon types
    pokemon_types.config(text=" - ".join([t for t in pokemon.types]).title())



# ID or Name label
label_id_name = tk.Label(root,text="ID or Name")
label_id_name.config(font=("Arial",20))
label_id_name.pack(padx=10,pady=10)

# Text label
text_id_name = tk.Text(root,height=1)
text_id_name.config(font=("Arial",20))
text_id_name.pack(padx=10,pady=10)

# Button 
btn_load = tk.Button(root, text="Load Pokemon",command=load_pokemon)
btn_load.config(font=("Arial,20"))
btn_load.pack(padx=10,pady=10)






root.mainloop()

