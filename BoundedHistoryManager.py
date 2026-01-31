from collections import deque

class BoundedHistoryManager:
    def __init__(self):
        self.limit = 0
        self.history = deque()

    def set_limit(self, n):
        self.limit = n
        self.history.clear()
        print(f"History limit set to {n}")

    def action(self, name):
        if self.limit == 0:
            print("Set history limit first.")
            return

        if len(self.history) == self.limit:
            dropped = self.history.popleft()
            print(f"Full. Dropped {dropped}.")

        self.history.append(name)

    def undo(self):
        if not self.history:
            print("Nothing to undo.")
            return

        removed = self.history.pop()
        print(f"Reverted {removed}.")

    def show_history(self):
        print(f"Hist: {list(self.history)}")


def main():
    manager = BoundedHistoryManager()

    while True:
        try:
            command = input("> ").strip().split()

            if not command:
                continue

            if command[0] == "SET_LIMIT":
                manager.set_limit(int(command[1]))

            elif command[0] == "ACTION":
                manager.action(command[1])

            elif command[0] == "UNDO":
                manager.undo()

            elif command[0] == "SHOW_HISTORY":
                manager.show_history()

            elif command[0] == "EXIT":
                break

            else:
                print("Unknown command.")

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
