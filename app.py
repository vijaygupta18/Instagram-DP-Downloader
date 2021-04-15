from tkinter import *
import instaloader


class Downloader:
  
  def __init__(self,root):
      
    self.root = root
    self.root.title("Instagram DP Downloader")
    self.root.geometry("580x160")
    self.url = StringVar()
    self.status = StringVar()
    self.status.set("Status : ----")
    download_frame = Frame(self.root,background="grey",width=580,height=160).place(x=0,y=0)
    url_lbl = Label(download_frame,text="Username",compound=LEFT,font=("times new roman",16,"bold"),bg="grey",fg="yellow").grid(row=1,column=0,padx=10,pady=10)
    url_txt = Entry(download_frame,bd=5,width=25,textvariable=self.url,relief=SUNKEN,font=("times new roman",15)).grid(row=1,column=1,padx=10,pady=10)
    # Download button
    dwn_btn = Button(download_frame,text="Download",command=self.download,width=10,font=("times new roman",14,"bold"),bd=10,bg="aqua",fg="navyblue").grid(row=1,column=2,padx=10,pady=10)
    #  Status Label
    status_lbl = Label(download_frame,textvariable=self.status,font=("times new roman",16,"bold"),bg="grey",fg="gold").grid(row=2,column=1)
  # Defining Download
  def download(self):
    if self.url.get()=="":
      self.status.set("Enter UserName")
    else:
      try:
        # Updating Status
        self.status.set("Status : Downloading...")
        self.root.update()
        mod=instaloader.Instaloader(download_videos=False, save_metadata=False, post_metadata_txt_pattern="hello")
        mod.download_profile(self.url.get(),profile_pic_only=True)
        self.status.set("Downloaded")
      
      except:
        self.status.set("Status : Error in Downloading")
root = Tk()
Downloader(root)
root.mainloop()
