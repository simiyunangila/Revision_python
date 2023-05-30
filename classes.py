class Ankara:
    def __init__(self,mood,temperature):
        self.mood=mood
        self.temperature=temperature
    def fabric_pattern(self):
        mood_range_to=10
        temperature_range_to=20
        if self.mood  >= mood_range_to and self.temperature >= temperature_range_to:
            print("wear bright and less pattern clothes")  
        elif self.mood <= mood_range_to and self.temperature <=temperature_range_to
            print("wear dull and and more pattern clothes") 
        else:
            print("wear average pattern fabric")    
pattern = Ankara(15,21) 
print(pattern.fabric_pattern())              