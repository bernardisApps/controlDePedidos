import tkinter as tk
import tkinter.simpledialog as sd
from tkinter import ttk,messagebox
from database.modelo import Clientes,Pedidos

class AcercaDe(sd.Dialog):
    def body(self, master):
        tk.Label(master, text='''
        Acerca de Bernardis Apps y nuestro Gestor de Pedidos:
        Bernardis Apps es una empresa de desarrollo de software
        fundada por Matias Bernardis. Nuestro objetivo es crear 
        aplicaciones innovadoras y útiles para mejorar la vida 
        de las personas.
        Nuestro Gestor de Pedidos es una herramienta fácil de 
        usar que te permite agregar clientes y registrar pedidos 
        en base a esos clientes. Con esta aplicación, puedes 
        mantener un registro organizado de tus clientes y sus 
        pedidos, lo que te permitirá gestionar mejor tu negocio.
        Características principales:
        Agregar clientes y sus datos de contacto
        Registrar y ver los pedidos realizados por cada cliente
        Generar informes de ventas y estadísticas
        Configurar recordatorios para realizar seguimiento a 
        pedidos pendientes
        Política de privacidad:
        La privacidad de nuestros usuarios es una de nuestras 
        principales preocupaciones. Por eso, nos comprometemos 
        a proteger y respetar tus datos personales de acuerdo 
        con las leyes de protección de datos aplicables. 
        Puedes encontrar más información en nuestra política 
        de privacidad en nuestro sitio web.
        Contáctanos:
        Si tienes alguna pregunta o sugerencia, 
        no dudes en contactarnos. Puedes enviar un correo electrónico 
        a matias.bernardis@hotmail.com y te responderemos 
        lo antes posible.
        ''',justify='center').grid(row=0)

    
    def apply(self):
        super().cancel()
    
    def cancel(self, event=None):
        super().cancel()