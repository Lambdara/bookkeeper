# Bookkeeper

## Why Bookkeeper?
Now and then I have LAN-parties with my friends. One guy gets the vodka, another guy gets the beers, and another guy still gets some networking hardware. Over the course of multiple days a multitude of stuff gets bought, sometimes for everyone, sometimes just for two or three people.
How to keep track? That's why I made Bookkeeper. Bookkeeper is a rather simple Python script which logs the payments, and keeps a HTML page updated with the details. Whenever someone returns from a store, you enter the relevant payment info and you're done. Everyone can view the current balances at any time by simply viewing the HTML file.

## Usage
When you run Bookkeeper it will automatically create the files it uses to keep track of the current state. These are `.bookkeeper.config`, `.bookkeeper.log`, `.bookkeeper.data`.
In addition to that, it keeps an HTML file, `my_bookkeeping.html` by default.

The available commands are:

`init name path` sets name of the bookkeeping, and the path of the HTML file. For example: `init 'My Bookkeeping' bookkeeping.html`. This is a good choice to start a bookkeeping.

`pay payer payee0,payee1,.. subject amount` registers a payment. The first argument is the payer. The second argument consists of comma-seperated names. (quote the argument if you want spaces, like so `'hans hansen,bart bartens'`) The third argument is the thing pay for (again, quote if you want spaces, like so `'nice bacon'`). The fourth argument is the amount payed; use a decimal point, not a comma (`10.24`; not `10,24`). For example: `pay hans bart,hans 'good beers', 10.24`

`html` updates the HTML file. If auto-update is on (by default: yes), this will happen automatically.

`set path my_path` sets the path of the HTML file to the argument.

`set name my_name` sets the name of the bookkeeping.

`set update {yes|no}` sets auto-updating to on or off. On by default. Example: `set update no`

`display {config|data|log|all}` prints either the config, the data (balances), the log, or everything to STDOUT.
