class TV:
    def __init__(self, cost):
        self.cost = cost
        
    cost_per_month = 0

    def credit(self, month):
        cost_per_month = self.cost/month
        self.cost_per_month = cost_per_month


    def cost_for_user(self):
        return self.cost_per_month + 100

tv_sunsung_jkjkf = TV(10000)
tv_sunsung_jkjkf.credit(3)
print(tv_sunsung_jkjkf.cost_for_user())