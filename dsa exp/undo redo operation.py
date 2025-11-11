class texteditor:
    def __init__(self):
        self.document = ""
        self.undostack = []
        self.redostack = []
        
    def makechange(self , change):
        self.undostack.append(self.document)
        self.document += change
        self.redostack.clear()
        print("change made.")
        self.displaystate()
        
    def undoaction(self):
        if self.undostack:
            self.redostack.append(self.document)
            self.document = self.undostack.pop()
            print("undo performed")
        else:
            print("no more action to undo")
        self.displaystate()
        
    def redoaction(self):
        if self.redostack:
            self.undostack.append(self.document)
            self.document = self.redostack.pop()
            
            print("redo performed")
        else:
            print("no more action to redo")
        self.displaystate()
        
    def displaystate(self):
        print("current document state:" + self.document + "'")
        
    def runeditor(self):
        while True :
            print("\n---MENU---")
            print("1. Make a change")
            print("2. Undo")
            print("3. Redo")
            print("4. Display document state")
            print("5. Exit")
            
            choice = input("enter your choice:")
            
            if choice == '1':
                change = input("enter text to add:")
                self.makechange(change)
            elif choice == '2':
                self.undoaction()
            elif choice == '3':
                self.redoaction()
            elif choice == '4' :
                self.displaystate()
            elif choice == '5' :
                print("exiting...")
                break
            else :
                print("invalid choice try again")
                
editor = texteditor()
editor.runeditor()