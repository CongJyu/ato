# encoding utf-8

# help information
def command_help():
    print("[------ ato Help ------]")
    print("Basic Commands:")
    print("    'quit' ---- Quit this CLI.")
    print("    'help' ---- Show this message.")
    print("Plotting Commands:")
    print("    'line-chart' ---- Plot a line chart.")
    print("    'fitting' ---- Fitting tool.")
    print("    'pie-chart' ---- Plot a pie chart.")
    print("    'average' ---- Calculate average.")
    print("    'standard-deviation' ---- Calculate standard deviation.")


# show version information
def version():
    print("[------ ato Version ------]")
    print("Version: 1.1.0")


# quit this cli
def quit_cli():
    print("Thank you for using ato! Bye!")
    quit(0)


# unknown command
def unknown_command():
    print("ERR! Unknown command. Type 'help' to get details.")
