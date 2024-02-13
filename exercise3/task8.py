class Recording:
    def __init__(self, length) -> None:
        self.length = length

    def get_length(self):
        return self.length
    
    def set_length(self, length):
        self.length = length

reco = Recording(43)
print(reco.get_length())
reco.set_length(44)
print(reco.get_length())