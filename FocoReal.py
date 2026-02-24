import tkinter as tk
import random

# ------------------ CONFIG ------------------
MENSAJES = [
    "Volvé al objetivo",
    "Pequeños pasos = grandes logros",
    "No abandones ahora",
    "Tu yo futuro te lo va a agradecer",
    "Concentrate 5 minutos más",
    "La disciplina gana a la motivación"
]

INTERVALO_CHEQUEO = (60000, 90000)  # entre 15 y 30 segundos
INTERVALO_MENSAJES = 5000  # 5 segundos

# ------------------ FUNCIONES ------------------

def chequeo_concentracion():
    ventana = tk.Toplevel(root)
    ventana.title("Chequeo de foco")
    ventana.geometry("300x150")
    ventana.attributes("-topmost", True)

    tk.Label(ventana, text="¿Seguís concentrado?", font=("Arial", 12)).pack(pady=10)

    def concentrado():
        ventana.destroy()

    def distraido():
        historial.insert(tk.END, "Se distrajo\n")
        ventana.destroy()

    tk.Button(ventana, text="Sí", width=10, command=concentrado).pack(pady=5)
    tk.Button(ventana, text="No", width=10, command=distraido).pack()

    # programar próximo chequeo aleatorio
    proximo = random.randint(*INTERVALO_CHEQUEO)
    root.after(proximo, chequeo_concentracion)


def cambiar_mensaje():
    mensaje_var.set(random.choice(MENSAJES))
    root.after(INTERVALO_MENSAJES, cambiar_mensaje)

# ------------------ INTERFAZ ------------------

root = tk.Tk()
root.title("Control de Foco")
root.geometry("400x300")

tk.Label(root, text="Tarea actual:", font=("Arial", 12)).pack(pady=5)

tarea_entry = tk.Entry(root, width=40)
tarea_entry.pack(pady=5)

tk.Label(root, text="Historial de distracciones:").pack(pady=5)
historial = tk.Text(root, height=6, width=40)
historial.pack()

# Mensaje motivacional
mensaje_var = tk.StringVar()
mensaje_label = tk.Label(root, textvariable=mensaje_var,
                         font=("Arial", 12, "bold"),
                         fg="blue")
mensaje_label.pack(pady=15)

# Iniciar sistema
root.after(3000, chequeo_concentracion)
cambiar_mensaje()

root.mainloop()