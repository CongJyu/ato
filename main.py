import src.basic
import src.function


# main process
if __name__ == "__main__":
    print("Welcome use ato!")
    print("Alternative To OriginLab! (?Maybe)")
    # waiting for commands
    while True:
        command = input("ato >>> ")
        if command == "quit":
            # this command is used to quit this CLI
            src.basic.quit_cli()
        elif command == "help":
            # help and information
            src.basic.command_help()
        elif command == "line-chart":
            # draw/plot a line chart
            src.function.line_chart()
        elif command == "fitting":
            # optimize data
            src.function.fitting()
        elif command == "pie-chart":
            # draw/plot a pie chart
            src.function.pie_chart()
        elif command == "average":
            # find/calculate average
            src.function.average()
        else:
            # unknown command
            src.basic.unknown_command()
