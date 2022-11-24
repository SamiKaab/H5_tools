import h5py
from tkinter import filedialog 

# Recursive function that goes through a H5 file and creates a text file representing the structure of the H5 file
def showall(file,outFilename, layer = 0):
    text = layer * " "+"|\n"+layer * " "+"|-->"
    if(str(type(file)) != "<class 'h5py._hl.dataset.Dataset'>"): # we have not reached the bottom of the dictionary
    
        newD = file.keys()
        # print(text,list(newD))
        for k in newD: #iterate through keys in H5 structure
            if layer  == 0: # on first level of the Dictionary
                with open(outFilename,"w") as f:
                    f.write("{}{}\n".format(text,k))
            else: # on a sublevel of the dictionary so the file should already have been created
                with open(outFilename,"a") as f:
                    f.write("{}{}\n".format(text,k))
                        
            # print(text,k)
            layer +=1 # increment becuse we are going to a deeper layer
            showall(file[k],outFilename,layer)
    else: # We have reached the bottom of the dictionary
       
        #write the first 10 element in the data 
        with open(outFilename,"a") as f:
            f.write("\n".join(["{}{}".format(text,d) for d in file[0:10]]))
        # print(text,["{}{}".format(text,d) for d in file])

if __name__ == "__main__":
    filename = filedialog.askopenfilename(initialdir = ".",
                                          title = "Select a File",
                                          filetypes = (("H5",
                                                        "*.h5*"),
                                                       ("all files",
                                                        "*.*")))
    file= h5py.File(filename, 'r')
    showall(file,"{}.txt".format(filename.split(".")[0]))