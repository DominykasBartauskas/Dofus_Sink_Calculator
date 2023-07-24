import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sink Calculator")
        # self.geometry("300x300")

        self.label = tk.Label(self, text="Sink Calculator")
        self.label.grid(row=0, column=0, columnspan=2)


        # # Buttons
        #
        #
        # self.button13 = tk.Button(self, text="Crit")
        # self.button14 = tk.Button(self, text="Heals")
        # self.button15 = tk.Button(self, text="Reflect")
        # self.button16 = tk.Button(self, text="Hunting Weapon")
        #
        # self.button17 = tk.Button(self, text="AP.Red")
        # self.button18 = tk.Button(self, text="MP.Red")
        # self.button19 = tk.Button(self, text="AP.Parry")
        # self.button20 = tk.Button(self, text="MP.Parry")
        #
        # self.button21 = tk.Button(self, text="%Neutral")
        # self.button22 = tk.Button(self, text="%Earth")
        # self.button23 = tk.Button(self, text="%Fire")
        # self.button24 = tk.Button(self, text="%Water")
        # self.button25 = tk.Button(self, text="%Air")
        #

        # self.button31 = tk.Button(self, text="Critical.Dam")
        # self.button32 = tk.Button(self, text="Pushback.Dam")
        # self.button33 = tk.Button(self, text="Trap.Dam")
        #
        # self.button34 = tk.Button(self, text="Lock")
        # self.button35 = tk.Button(self, text="Dodge")
        # self.button36 = tk.Button(self, text="Prospecting")
        #
        # self.button37 = tk.Button(self, text="%Power")
        # self.button38 = tk.Button(self, text="%Trap.Power")
        #
        # self.button39 = tk.Button(self, text="Neutral.Res")
        # self.button40 = tk.Button(self, text="Earth.Res")
        # self.button41 = tk.Button(self, text="Fire.Res")
        # self.button42 = tk.Button(self, text="Water.Res")
        # self.button43 = tk.Button(self, text="Air.Res")
        # self.button44 = tk.Button(self, text="Crit.Res")
        # self.button45 = tk.Button(self, text="Pushback.Res")
        #
        #
        #
        # self.button52 = tk.Button(self, text="Pod")
        # self.button53 = tk.Button(self, text="Initiative")



        # Column 1 - Wisdom, Strength, Intelligence, Chance, Agility, Vitality
        self.button1 = tk.Button(self, text="Vitality")
        self.button2 = tk.Button(self, text="Wisdom")
        self.button3 = tk.Button(self, text="Strength")
        self.button4 = tk.Button(self, text="Intelligence")
        self.button5 = tk.Button(self, text="Chance")
        self.button6 = tk.Button(self, text="Agility")
        # ---------------------------------------------------------------------
        self.button1.grid(row=1, column=0, sticky="ew")
        self.button2.grid(row=2, column=0, sticky="ew")
        self.button3.grid(row=3, column=0, sticky="ew")
        self.button4.grid(row=4, column=0, sticky="ew")
        self.button5.grid(row=5, column=0, sticky="ew")
        self.button6.grid(row=6, column=0, sticky="ew")

        # Column 2 - AP, MP, Range, Summon
        self.button7 = tk.Button(self, text="AP")
        self.button8 = tk.Button(self, text="MP")
        self.button9 = tk.Button(self, text="Range")
        self.button10 = tk.Button(self, text="Summon")
        # ---------------------------------------------------------------------
        self.button7.grid(row=1, column=1, sticky="ew")
        self.button8.grid(row=2, column=1, sticky="ew")
        self.button9.grid(row=3, column=1, sticky="ew")
        self.button10.grid(row=4, column=1, sticky="ew")

        # Column 3 - Damage, Neutral, Earth, Fire, Water, Air
        self.button11 = tk.Button(self, text="Damage")
        self.button12 = tk.Button(self, text="Neutral")
        self.button13 = tk.Button(self, text="Earth")
        self.button14 = tk.Button(self, text="Fire")
        self.button15 = tk.Button(self, text="Water")
        self.button16 = tk.Button(self, text="Air")
        # ---------------------------------------------------------------------
        self.button11.grid(row=1, column=2, sticky="ew")
        self.button12.grid(row=2, column=2, sticky="ew")
        self.button13.grid(row=3, column=2, sticky="ew")
        self.button14.grid(row=4, column=2, sticky="ew")
        self.button15.grid(row=5, column=2, sticky="ew")
        self.button16.grid(row=6, column=2, sticky="ew")

        # Column 4 - %Damage & %Resistance - Melee, % Ranged, % Spell, % Weapon
        self.button17 = tk.Button(self, text="Melee Damage")
        self.button18 = tk.Button(self, text="Ranged Damage")
        self.button19 = tk.Button(self, text="Spell Damage")
        self.button20 = tk.Button(self, text="Weapon Damage")
        self.button21 = tk.Button(self, text="Melee Resistance")
        self.button22 = tk.Button(self, text="Ranged Resistance")
        self.button23 = tk.Button(self, text="Spell Resistance")
        # ---------------------------------------------------------------------
        self.button17.grid(row=1, column=3, sticky="ew")
        self.button18.grid(row=2, column=3, sticky="ew")
        self.button19.grid(row=3, column=3, sticky="ew")
        self.button20.grid(row=4, column=3, sticky="ew")
        self.button21.grid(row=5, column=3, sticky="ew")
        self.button22.grid(row=6, column=3, sticky="ew")
        self.button23.grid(row=7, column=3, sticky="ew")




    def say_hello(self):
        print("Hello World")

if __name__ == "__main__":
    app = App()
    app.mainloop()
