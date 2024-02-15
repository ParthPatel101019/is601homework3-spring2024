from operation import Operation

class History:

    def __init__(self):
        self.data = list()

    def add_history(self, a, b, op):
        op_obj = Operation.create(a, b, op)
        self.data.append(op_obj)

    def get_history(self):
        return self.data
    
    def clear_history(self):
        self.data = list()
