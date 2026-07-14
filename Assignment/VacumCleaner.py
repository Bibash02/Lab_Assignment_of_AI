class VaccumCleaner:
    def __init__(self):
        self.environment = {"A": "Dirty", "B": "Dirty"}
        self.location = "A"

    def suck(self):
        if self.environment[self.location] == "Dirty":
            print(f"Room {self.location} is Dirty cleaning...")
            self.environment[self.location] = "Clean"
        else:
            print(f"Room {self.location} is already clean.")
            
        
    def move(self):
        if self.location == "A":
            self.location = "B"
        else:
            self.location = "A"
        print(f"Vaccum moved to room {self.location}")
        
    def run(self):
        print("Initial state: ", self.environment)
        for _ in range(2):
            self.suck()
            self.move()
        self.suck()
        print("Final State:", self.environment)

vacuum = VaccumCleaner()
vacuum.run()
            
            