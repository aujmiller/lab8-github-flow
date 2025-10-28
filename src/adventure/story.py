from adventure.utils import read_events_from_file
import random
from rich import print
from rich.console import Console

def step(choice: str, events):
    random_event = random.choice(events)

    if choice == "left":
        return left_path(random_event)
    elif choice == "right":
        return right_path(random_event)
    else:
        return "[bright_green]You stand still, unsure what to do. The forest swallows you.[/bright_green]"

def left_path(event):
    return "[bright_yellow]You walk [bright_blue]left[/bright_blue]. " + event + "[/bright_yellow]"

def right_path(event):
    return "[bright_yellow]You walk [bright_red]right[/bright_red]. " + event + "[/bright_yellow]"

if __name__ == "__main__":
    events = read_events_from_file('events.txt')
    console = Console()

    print("[bright_green]You wake up in a dark forest. You can go [bright_blue]left[/bright_blue] or [bright_red]right[/bright_red].[/bright_green]")
    while True:
        choice = console.input("[bright_green]Which direction do you choose? ([bright_blue]left[/bright_blue]/[bright_red]right[/bright_red]/[bright_magenta]exit[/bright_magenta]): [/bright_green]")
        choice = choice.strip().lower()
        if choice == 'exit':
            break
        
        print(step(choice, events))
