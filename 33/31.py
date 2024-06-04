class Basic:
    def handle_message(self):
        return "Basic"

class AI(Basic):
    def handle_message(self):
        return "Air"

class GR(Basic):
    def handle_message(self):
        return "Ground"

class FI(Basic):
    def handle_message(self):
        return "Fire"

class WA(Basic):
    def handle_message(self):
        return "Water"

class TH(AI, GR):
    pass

class SW(GR, WA):
    pass

class BF(FI, AI):
    pass

class NO(FI, WA):
    pass

class SG(SW, BF):
    pass

sg_instance = SG()
no_instance = NO()

print("SG message:", sg_instance.handle_message())
print("NO message:", no_instance.handle_message())
