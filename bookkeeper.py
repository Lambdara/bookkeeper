# Data is kept as a dict of `name:credit`
data = dict()

# The log is kept as a list of tuples of the following things:
# - Who payed
# - For whom was payed
# - The thing payed for
# - The amount payed
log = list()

# Define a function for mutating the records
def mutate(name,amount):
    if name in data:
        data[name] += amount
    else:
        data[name] = amount

# Define a function to register payments
def pay(payer,payees,subject,amount):
    per_person = amount / len(payees)

    for payee in payees:
        mutate(payee,-per_person)

    mutate(payer,amount)

    record = (payer,payees,subject,amount)
    log.append(record)
