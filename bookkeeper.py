# Set a name
name = "Bookkeeping"

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

# Print current state to HTML file
def make_html(path):
    html = str()

    html += "<!doctype html>\n"
    html += "<html>\n"
    html += "<h1>" + name + "</h1>\n"
    html += "<h2>Balance</h2>\n"
    html += "<table>\n"
    html += "<tr><th>Name</th><th>Status</th><th>Amount</th></tr>\n"
    for person in data.keys():
        html += "<tr><td>" + person + "</td><td>"
        if data[person] > 0:
            html += "credit"
        else:
            html += "debt"
        html += "</td><td>" + str(abs(data[person])) + "</td></tr>\n"
    html += "</table>\n"
    html += "<h2>Log</h2>\n"
    html += "<table>\n"
    html += "<tr><th>Payer</th><th>Payees</th><th>Subject</th><th>amount</th></tr>\n"
    for (payer,payees,subject,amount) in log:
        html += "<tr><td>" + payer + "</td>"
        html += "<td>" + " ".join(payees) + "</td>"
        html += "<td>" + subject + "</td>"
        html += "<td>" + str(amount) + "</td></tr>\n"
    html += "</table>\n"
    html += "</html>\n"

    with open(path,'w') as file:
        file.write(html)
