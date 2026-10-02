class Service:
    def __init__(self): self.calls=0
    def run(self,value):
        self.calls += 1
        return {"tool":"echo","result":value,"authorized":True,"audit":{"call_count":self.calls}}