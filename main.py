import src.basic
import src.function


#  main process
if __name__ == "__main__":
    print("Welcome use ato!")
    print("Alternative To OriginLab!")
    while True:
        command = input("ato >>> ")
        if command == "quit":
            #  this command is used to quit this CLI
            print("Thank you for using ato! Bye!")
            quit(0)
        elif command == "help":
            #  help and information
            src.basic.command_help()
        elif command == "line-chart":
            #  draw/plot a line chart
            src.function.line_chart()
        else:
            #  unknown command
            print("ERR! Unknown command. Type 'help' to get details.")
