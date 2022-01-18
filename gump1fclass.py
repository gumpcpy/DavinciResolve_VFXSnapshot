from python_get_resolve import GetResolve
import time


class gumpclass():
    
    def renderClip(self, resolve, timeline, presetName, targetDirectory, renderFormat, renderCodec ):
        
        print("Timeline: " + timeline)        
        print("Render Preset: " + presetName)        
        print("Render To Where: " + targetDirectory)        
     #    print("Render Format: " + renderFormat)
#         print("Render Codec: " + renderCodec)
        print("------------------")
    
        projectManager = resolve.GetProjectManager()    
        project = projectManager.GetCurrentProject()
    
        if not project:
            return False
    
        resolve.OpenPage("Deliver")
    
        project.SetCurrentTimeline(timeline)
        project.LoadRenderPreset(presetName)
        timeline = project.GetCurrentTimeline()
        print("Get Timeline:")
        print(timeline)
            
            
        #get title track name    
        
        clips = timeline.GetItemsInTrack("subtitle",  1) 
        for clipIdx in clips:
            
            print(clips[clipIdx].GetName() + " In:" + str(clips[clipIdx].GetStart()) + " Out:" + str(clips[clipIdx].GetEnd()) )                        
            project.SetRenderSettings({"MarkIn" : int(clips[clipIdx].GetStart()), "MarkOut" : int(clips[clipIdx].GetStart()), "TargetDir" : targetDirectory, "CustomName" : clips[clipIdx].GetName()+"_"})
            project.AddRenderJob()   
             
        print("Render Queue Added, Start Rendering...")
        if not project.SetCurrentRenderFormatAndCodec(renderFormat, renderCodec):
            return False
        
        return project.StartRendering()      
      
     
    def IsRenderingInProgress( self, resolve ):
    
        projectManager = resolve.GetProjectManager()
        project = projectManager.GetCurrentProject()
        if not project:
            return False
        
        return project.IsRenderingInProgress()

    
    def WaitForRenderingCompletion( self, resolve ):
    
        while self.IsRenderingInProgress(resolve):
            time.sleep(1)
    
        return

    def DeleteAllRenderJobs( self, resolve ):
        projectManager = resolve.GetProjectManager()
        project = projectManager.GetCurrentProject()
        project.DeleteAllRenderJobs()
        return



