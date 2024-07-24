# 1. Import necessary functionality
import tkinter as tk
from tkinter import filedialog
from tkinter import Tk, Text, Frame, Button


# 2. Create a class
class SimpleNotepad:
    # 3. Initialize the class with all the UI
    def __init__(self, root: Tk) -> None:
        self.root = root
        self.root.title('Bob\'s Notepad')

        # Create a text widget for entering the content
        self.text_area: Text = Text(self.root, wrap='word')
        self.text_area.pack(expand=True, fill='both')

        # Create a frame to hold the buttons
        self.button_frame: Frame = Frame(self.root)
        self.button_frame.pack()

        # Create and pack the save button
        self.save_button: Button = Button(self.button_frame, text='Save', command=self.save_file)
        self.save_button.pack(side=tk.LEFT)

        # Create and pack the load button
        self.load_button: Button = Button(self.button_frame, text='Load', command=self.load_file)
        self.load_button.pack(side=tk.LEFT)

    # 4. Create a function that saves files
    def save_file(self) -> None:
        file_path: str = filedialog.asksaveasfilename(defaultextension='.txt',
                                                      filetypes=[('Text files', '*.txt')])
        # 4.5 Save the file
        with open(file_path, 'w') as file:
            file.write(self.text_area.get(1.0, tk.END))

        print(f'File saved to: {file_path}')

    # 5. Create a function that loads files
    def load_file(self) -> None:
        file_path: str = filedialog.askopenfilename(defaultextension='.txt',
                                                    filetypes=[('Text files', '*.txt')])
        # 5.5 Load the file
        with open(file_path, 'r') as file:
            content: str = file.read()
            self.text_area.delete(1.0, tk.END)  # Clear existing content
            self.text_area.insert(tk.INSERT, content)  # Insert new content

        print(f'File loaded from: {file_path}')

    # 6. Create a function that runs the program
    def run(self) -> None:
        self.root.mainloop()


# 7. Create the main entry point
def main() -> None:
    root: Tk = tk.Tk()
    app: SimpleNotepad = SimpleNotepad(root=root)
    app.run()


# 8. Run the script
if __name__ == '__main__':
    main()


"""
Homework:
1. Make it so that the save button saves the text to the current file if it already exists, instead
of asking the user to create a new file each time.

"""
