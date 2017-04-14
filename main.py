#Author: Debkanya Mazumder <dmazum2@uic.edu> 
import webbrowser

#import tkinter
#if tkinter not present pip install tkinter and then import 
def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)

install_and_import('tkinter')

lib = ''
def callback():
    lib = v.get()
    print(lib)
    url = "https://www.google.co.in/search?q=" +(str(lib))+ "&oq="+(str(lib))+"&gs_l=serp.12..0i71l8.0.0.0.6391.0.0.0.0.0.0.0.0..0.0....0...1c..64.serp..0.0.0.UiQhpfaBsuU"
    webbrowser.open_new(url)
    #print("Search button clicked!")

def close_window():
    #print("Cancel button clicked!")
    window.destroy()
    
window = tkinter.Tk()
window.title("Shortcut-Google-Search")

v = tkinter.StringVar()
#creating the interface
lbl = tkinter.Label(window, text="GOOGLE SEARCH")
ent = tkinter.Entry(window, textvariable=v)
btn = tkinter.Button(window, text="Search", command=callback)
cancelbtn = tkinter.Button(window, text="Cancel", command=close_window)

#pack to add the widgets into the window 
lbl.pack()
ent.pack()
btn.pack()
cancelbtn.pack()
window.mainloop()

