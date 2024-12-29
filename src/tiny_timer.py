#!/usr/bin/python
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


# Globals ------------------------------------------------------------ #
C_TIME = int(30)  # minutes


class TinyTimer(tk.Frame):
    """ Implements the GUI of the application. """

    def __init__(self, master: tk.Tk=None):
        super().__init__(master)

        master.title('Tiny Timer')
        master.resizable(False, False)

        self._time_string = tk.StringVar(self)
        self._time_string.set('00:00')

        self._seconds_remain = C_TIME * 60
        self._paused = True
        self._finised = False

        self._update_time_string()

        self.pack()
        self._create_widgets()

    # ---------------------------------------------------------------- #
    # PRIVATE METHODS
    # ---------------------------------------------------------------- #
    def _create_widgets(self) -> None:
        """ Creates the GUI. """

        self._time_label = tk.Label(self, textvariable=self._time_string,
            justify=tk.CENTER)

        start_button = tk.Button(self, text='Start',
            command=self._start)
        pause_button = tk.Button(self, text='Pause',
            command=self._pause)
        reset_button = tk.Button(self, text='Reset',
            command=self._reset)

        self._time_label.grid(row=0, column=0, columnspan=3, sticky='nsew')
        start_button.grid(row=1, column=0, sticky='nsew')
        pause_button.grid(row=1, column=1, sticky='nsew')
        reset_button.grid(row=1, column=2, sticky='nsew')

    def _start(self) -> None:
        """ Prints 'Hello'. """

        self._paused = False
        self._update_time()

    def _pause(self) -> None:
        """ """

        self._paused = True

    def _reset(self) -> None:
        """ """

        self._paused = True
        self._seconds_remain = C_TIME * 60
        self._update_time_string()

    def _update_time(self) -> None:
        """ """
        if not self._paused:
            self._seconds_remain -= 1

            if self._seconds_remain <= 0:
                messagebox.showinfo('Time is over!', 'Time is over!')
                self._reset()

            self._update_time_string()
            self.master.after(1000, self._update_time)

    def _update_time_string(self) -> None:
        minutes = self._seconds_remain // 60
        seconds = self._seconds_remain % 60

        self._time_string.set('{:02d}:{:02d}'.format(minutes, seconds))

if __name__ == '__main__':

    root = tk.Tk()
    app = TinyTimer(master=root)
    app.mainloop()
    root.quit()

