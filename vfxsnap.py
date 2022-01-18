import wx
import os
import _thread
import time 
from gump1fclass import gumpclass
from python_get_resolve import GetResolve


class MyFrame(wx.Frame):    
    
    def __init__(self, parent, id):

        wx.Frame.__init__(self, parent, id, title="HuHu Davinci API", size=(600, 400))
        self.Center() #Window Centered
     
        # create a panel in the frame
        panel = wx.Panel(self)
        
        ''' create a menu bar'''
        self.makeMenuBar()
        # and a status bar
        self.CreateStatusBar()
        self.SetStatusText("Render VFX Snapshot Settings")

        self.label_user = wx.StaticText(panel, label="Davinci Preset", pos=(50, 50))
        self.text_user = wx.TextCtrl(panel, size=(150, 25), pos=(150, 50), style=wx.TE_LEFT, value = "VFXSnap")
        
        self.label_pwd = wx.StaticText(panel, label="Davinci Timeline", pos=(50, 90))
        self.text_password = wx.TextCtrl(panel, size=(150, 25), pos=(150, 90), style=wx.TE_LEFT, value = "VFXSnap") #TE_PASSWORD
                        
        
        self.BtnPressHere = chooseFolder(panel,
             id=-1,
             path=os.getcwd(),
             message='Choose Folder',
             pos = (50, 130),
             style= wx.DIRP_DEFAULT_STYLE|wx.DIRP_CHANGE_DIR,
             size = (350, 25))

        self.Bind(wx.EVT_DIRPICKER_CHANGED, self.DirChange)      
        
        # Progress Bar
        self.count = 0 
        
        self.label_proc = wx.TextCtrl(panel, size=(150, 25), pos=(50, 170), style=wx.TE_LEFT, value = "Progress")
        
        
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        hbox1 = wx.BoxSizer(wx.HORIZONTAL) 
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        
        
        self.gauge = wx.Gauge(panel, range = 100, size = (250, 25),pos=(50, 190), style =  wx.GA_HORIZONTAL) 
        self.gauge.SetValue(0)
        
        
        hbox1.Add(self.gauge, proportion = 1, flag = wx.ALIGN_CENTRE) 
         
        vbox.Add((0, 30)) 
        vbox.Add(hbox1, flag = wx.ALIGN_CENTRE) 
        vbox.Add((0, 20)) 
        panel.SetSizer(vbox)
      
        
        # Set Submit Btn
        self.bt_confirm = wx.Button(panel, label='Submit', pos=(150, 210))
        self.bt_confirm.Bind(wx.EVT_BUTTON, self.OnclickSubmit)
 

    def on_combobox(self,event):
        print("Choose{0}".format(event.GetString()))

    def on_choice(self,event):
        print("Choose{0}".format(event.GetString()))

    def DirChange(self,event):
       
        print("Dir changed to: ", event.GetPath())
#         print("Checking Current Dir: ",os.getcwd())


    def OnclickSubmit(self, event):      
        _thread.start_new_thread(self.watch,(self,None)) 
        """Submit Onclick"""
       
        
        
            
#         wx.MessageBox("Render Complete")
    def watch(self,dummy,e):
        while True:
            time.sleep(1)
            self.count += 1
            print(self.count)
            self.gauge.SetValue(self.count)
            wx.CallAfter(self.label_proc.SetLabel, str(self.count)+" %")
            message = ""
            username = self.text_user.GetValue()
            password = self.text_password.GetValue()
            render_path = self.BtnPressHere.GetPath()
        
        
            if username == "" or password == "":
                message = 'Input Preset And Timeline Name'
       
            else:            
                if(self.CallGumpClass()):
                    return True

            
            
                
            
    def CallProcBar(self):
        self.gauge.SetValue(1)
        print("set pulse")
        
        
    def CallGumpClass(self):
        print("##### START #####")
        time.sleep(1)
        username = self.text_user.GetValue()
        password = self.text_password.GetValue()
        render_path = self.BtnPressHere.GetPath()
        renderFormat = "mov" 
        renderCodec = "H264" 
        
        
        resolve = GetResolve()        
        t = gumpclass()     
        t.DeleteAllRenderJobs(resolve)     
        t.renderClip(resolve, password, username, render_path, renderFormat, renderCodec)      
        t.WaitForRenderingCompletion(resolve)
        t.DeleteAllRenderJobs(resolve)    
        print("##### Complete #####")
        wx.CallAfter(self.label_proc.SetLabel, " 100% ")
        self.gauge.SetValue(100)
        return True

    def makeMenuBar(self):
        """
        A menu bar is composed of menus, which are composed of menu items.
        This method builds a set of menus and binds handlers to be called
        when the menu item is selected.
        """

        # Make a file menu with Hello and Exit items
        fileMenu = wx.Menu()
        # The "\t..." syntax defines an accelerator key that also triggers
        # the same event
        helloItem = fileMenu.Append(-1, "&Hello...\tCtrl-H",
                "Help string shown in status bar for this menu item")
        fileMenu.AppendSeparator()
        # When using a stock ID we don't need to specify the menu item's
        # label
        exitItem = fileMenu.Append(wx.ID_EXIT)

        # Now a help menu for the about item
        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        # Make the menu bar and add the two menus to it. The '&' defines
        # that the next letter is the "mnemonic" for the menu item. On the
        # platforms that support it those letters are underlined and can be
        # triggered from the keyboard.
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")

        # Give the menu bar to the frame
        self.SetMenuBar(menuBar)

        # Finally, associate a handler function with the EVT_MENU event for
        # each of the menu items. That means that when that menu item is
        # activated then the associated handler function will be called.
        self.Bind(wx.EVT_MENU, self.OnHello, helloItem)
        self.Bind(wx.EVT_MENU, self.OnExit,  exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)


    def OnExit(self, event):
        """Close the frame, terminating the application."""
        self.Close(True)
        print("Quit APP")
        return 0


    def OnHello(self, event):
        """Say hello to the user."""
        wx.MessageBox("Hello again from HuHu")


    def OnAbout(self, event):
        """Display an About Dialog"""
        wx.MessageBox("This is a function communicate with Davinci Resolve",
                      "About HuHu Davinci Resolve API",
                      wx.OK|wx.ICON_INFORMATION)
class chooseFolder(wx.DirPickerCtrl):
    def __init__(self, *args, **kwargs):
        wx.DirPickerCtrl.__init__(self, *args, **kwargs)
            
            
if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()

