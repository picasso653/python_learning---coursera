class Payslips:
    def __init__(self, name, payment, amount) -> None:
        self.name = name
        self.payment = payment
        self.amount = amount
    def pay(self):
        self.payment = "yes"
    def status(self):
        if self.payment == "yes":
            return self.name + " has been paid: " + str(self.amount)
        else:
            return self.name + " has not been paid yet"


nathan =  Payslips("Nathan", "no", 1000)
Roger = Payslips("Roger", "no", 3000)

print(nathan.status(), "\n", Roger.status())
nathan.pay()
print("After Payment")
print(nathan.status(), "\n", Roger.status())