import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry  # Libreria per il calendario delle scadenze
import sqlite3
from datetime import datetime, timedelta

# Database setup
conn = sqlite3.connect('shopping_list.db')
c = conn.cursor()

# Creiamo la tabella se non esiste già
c.execute('''CREATE TABLE IF NOT EXISTS shopping_list
             (id INTEGER PRIMARY KEY, product TEXT, quantity TEXT, in_stock INTEGER, expiration_date TEXT)''')
conn.commit()

class ShoppingListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista della Spesa")
        self.root.geometry("600x500")
        self.root.configure(bg="#000000")  # Sfondo nero

        # Frame per la lista
        self.list_frame = tk.Frame(root, bg="#000000")
        self.list_frame.pack(pady=20)

        # Titolo
        self.title_label = tk.Label(self.list_frame, text="Lista della Spesa", font=("Arial", 24, "bold"), fg="#FFFFFF", bg="#000000")
        self.title_label.pack(pady=10)

        # Dividere in due sezioni: Acquisti e Prodotti in casa
        self.notebook = ttk.Notebook(self.list_frame)
        self.notebook.pack(pady=10)

        # Tab per Acquisti
        self.shopping_tab = tk.Frame(self.notebook, bg="#000000")
        self.notebook.add(self.shopping_tab, text="Acquisti da fare")
        self.shopping_listbox = tk.Listbox(self.shopping_tab, height=10, width=50, font=("Arial", 14), bg="#1C1C1C", fg="#FFFFFF", selectbackground="#FF5722", selectforeground="#000000")
        self.shopping_listbox.pack(pady=5)

        # Tab per Prodotti in casa
        self.in_stock_tab = tk.Frame(self.notebook, bg="#000000")
        self.notebook.add(self.in_stock_tab, text="Prodotti in casa")
        self.in_stock_listbox = tk.Listbox(self.in_stock_tab, height=10, width=50, font=("Arial", 14), bg="#1C1C1C", fg="#FFFFFF", selectbackground="#FF5722", selectforeground="#000000")
        self.in_stock_listbox.pack(pady=5)

        # Pulsanti
        button_style = {
            "font": ("Arial", 14, "bold"), 
            "bg": "#FF5722", 
            "fg": "white", 
            "activebackground": "#E64A19",
            "relief": tk.FLAT,
            "borderwidth": 0,
            "padx": 10,
            "pady": 5
        }

        self.add_button = self.create_styled_button(root, "Aggiungi prodotto", self.add_product_window, **button_style)
        self.remove_button = self.create_styled_button(root, "Rimuovi selezionato", self.remove_product, **button_style)
        self.summary_button = self.create_styled_button(root, "Riepilogo settimanale", self.show_summary, **button_style)

        self.load_products()

    def create_styled_button(self, parent, text, command, **kwargs):
        button = tk.Button(parent, text=text, command=command, **kwargs)
        button.pack(pady=10)
        button.bind("<Enter>", lambda e: button.configure(bg="#E64A19"))  # Cambia colore al passaggio del mouse
        button.bind("<Leave>", lambda e: button.configure(bg="#FF5722"))  # Ripristina colore quando il mouse esce
        return button

    def load_products(self):
        self.shopping_listbox.delete(0, tk.END)
        self.in_stock_listbox.delete(0, tk.END)

        c.execute("SELECT * FROM shopping_list ORDER BY expiration_date")
        products = c.fetchall()

        for product in products:
            product_info = f"{product[1]} ({product[2]}) - Scadenza: {product[4]}" if product[4] else f"{product[1]} ({product[2]})"
            if product[3] == 1:
                self.in_stock_listbox.insert(tk.END, product_info)
            else:
                self.shopping_listbox.insert(tk.END, product_info)

    def add_product_window(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Aggiungi Prodotto")
        self.new_window.configure(bg="#000000")

        self.product_label = tk.Label(self.new_window, text="Prodotto:", font=("Arial", 14), fg="#FFFFFF", bg="#000000")
        self.product_label.pack(pady=5)
        self.product_entry = tk.Entry(self.new_window, font=("Arial", 14), bg="#1C1C1C", fg="#FFFFFF")
        self.product_entry.pack(pady=5)

        self.quantity_label = tk.Label(self.new_window, text="Quantità:", font=("Arial", 14), fg="#FFFFFF", bg="#000000")
        self.quantity_label.pack(pady=5)
        self.quantity_entry = tk.Entry(self.new_window, font=("Arial", 14), bg="#1C1C1C", fg="#FFFFFF")
        self.quantity_entry.pack(pady=5)

        self.in_stock_var = tk.IntVar()
        self.in_stock_check = tk.Checkbutton(self.new_window, text="Disponibile in casa", variable=self.in_stock_var, font=("Arial", 14), fg="#FFFFFF", bg="#000000", activebackground="#000000", activeforeground="#FFFFFF")
        self.in_stock_check.pack(pady=5)

        self.expiration_label = tk.Label(self.new_window, text="Scadenza (facoltativa):", font=("Arial", 14), fg="#FFFFFF", bg="#000000")
        self.expiration_label.pack(pady=5)
        self.expiration_entry = DateEntry(self.new_window, font=("Arial", 14), bg="#1C1C1C", fg="#FFFFFF")
        self.expiration_entry.pack(pady=5)

        self.add_product_button = tk.Button(self.new_window, text="Aggiungi", command=self.add_product_to_list, font=("Arial", 14), bg="#FF5722", fg="white", activebackground="#E64A19")
        self.add_product_button.pack(pady=10)

    def add_product_to_list(self):
        product_name = self.product_entry.get()
        quantity = self.quantity_entry.get()
        in_stock = self.in_stock_var.get()
        expiration_date = self.expiration_entry.get_date().strftime('%Y-%m-%d') if self.expiration_entry.get() else None

        if product_name and quantity:
            c.execute("INSERT INTO shopping_list (product, quantity, in_stock, expiration_date) VALUES (?, ?, ?, ?)", 
                      (product_name, quantity, in_stock, expiration_date))
            conn.commit()
            self.new_window.destroy()
            self.load_products()
        else:
            messagebox.showwarning("Input non valido", "Inserisci sia il nome del prodotto che la quantità.")

    def remove_product(self):
        selected_index = self.shopping_listbox.curselection() or self.in_stock_listbox.curselection()
        if selected_index:
            if selected_index == self.shopping_listbox.curselection():
                product = self.shopping_listbox.get(selected_index)
            else:
                product = self.in_stock_listbox.get(selected_index)
            
            product_name = product.split(" (")[0]
            
            c.execute("DELETE FROM shopping_list WHERE product=?", (product_name,))
            conn.commit()
            self.load_products()
        else:
            messagebox.showwarning("Nessuna selezione", "Seleziona un prodotto da rimuovere.")

    def show_summary(self):
        self.summary_window = tk.Toplevel(self.root)
        self.summary_window.title("Riepilogo settimanale")
        self.summary_window.configure(bg="#000000")

        summary_label = tk.Label(self.summary_window, text="Prodotti in scadenza nei prossimi 7 giorni:", font=("Arial", 14), fg="#FFFFFF", bg="#000000")
        summary_label.pack(pady=10)

        summary_listbox = tk.Listbox(self.summary_window, height=10, width=50, font=("Arial", 14), bg="#1C1C1C", fg="#FFFFFF", selectbackground="#FF5722", selectforeground="#000000")
        summary_listbox.pack(pady=5)

        today = datetime.today()
        next_week = today + timedelta(days=7)

        c.execute("SELECT * FROM shopping_list WHERE expiration_date BETWEEN ? AND ? ORDER BY expiration_date", 
                  (today.strftime('%Y-%m-%d'), next_week.strftime('%Y-%m-%d')))
        products = c.fetchall()

        if products:
            for product in products:
                summary_listbox.insert(tk.END, f"{product[1]} - Scadenza: {product[4]}")
        else:
            summary_listbox.insert(tk.END, "Nessun prodotto in scadenza!")

# Main loop
if __name__ == "__main__":
    root = tk.Tk()
    app = ShoppingListApp(root)
    root.mainloop()
