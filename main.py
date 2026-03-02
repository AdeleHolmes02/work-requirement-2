import random
import tasks
import calculator


# Exercise 2: Task List Manager (with separate module)
def run_task_manager() -> None:
    task_list: list[str] = []
    print("\n--- Task List Manager ---")
    print("Skriv kommandoer:")
    print("  add <oppgave>")
    print("  remove <oppgave>")
    print("  list")
    print("  done\n")

    while True:
        user_input = input("> ").strip()

        if user_input.lower() == "done":
            print("Avslutter Task List Manager.\n")
            return

        if user_input.lower() == "list":
            if not task_list:
                print("Liste: (tom)")
            else:
                print("Liste:")
                for i, t in enumerate(task_list, start=1):
                    print(f"  {i}. {t}")
            continue

        if user_input.lower().startswith("add "):
            task = user_input[4:]
            if tasks.add_task(task_list, task):
                print("La til:", task.strip())
            else:
                print("Du må skrive en oppgave etter 'add'.")
            continue

        if user_input.lower().startswith("remove "):
            task = user_input[7:]
            if tasks.remove_task(task_list, task):
                print("Fjernet:", task.strip())
            else:
                print("Fant ikke oppgaven i lista.")
            continue

        print("Ukjent kommando. Bruk: add/remove/list/done.")


# Exercise 4: Math Quiz with Exception Handling
def run_math_quiz() -> None:
    print("\n--- Math Quiz ---")
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    print(f"Hva er {a} + {b}?")

    answer_raw = input("Svar: ").strip()

    try:
        answer = int(answer_raw)
    except ValueError:
        print("Invalid input! Du må skrive et heltall.\n")
        return

    if answer == a + b:
        print("Riktig! 🎉\n")
    else:
        print(f"Ikke helt. Riktig svar er {a + b}.\n")


# Exercise 8: Simple Calculator Module
def run_calculator() -> None:
    print("\n--- Calculator ---")
    print("Velg operasjon: +  -  *  /")

    op = input("Operasjon: ").strip()

    try:
        a = float(input("Tall 1: ").strip())
        b = float(input("Tall 2: ").strip())
    except ValueError:
        print("Ugyldig input! Du må skrive tall.\n")
        return

    try:
        if op == "+":
            result = calculator.add(a, b)
        elif op == "-":
            result = calculator.subtract(a, b)
        elif op == "*":
            result = calculator.multiply(a, b)
        elif op == "/":
            result = calculator.divide(a, b)
        else:
            print("Ugyldig operasjon.\n")
            return

        print("Resultat:", result, "\n")

    except ZeroDivisionError:
        print("Feil: Du kan ikke dele på 0.\n")


def main() -> None:
    while True:
        print("=== Work Requirement 2 ===")
        print("1) Task List Manager (Exercise 2)")
        print("2) Math Quiz (Exercise 4)")
        print("3) Calculator (Exercise 8)")
        print("4) Exit")

        choice = input("Velg (1-4): ").strip()

        if choice == "1":
            run_task_manager()
        elif choice == "2":
            run_math_quiz()
        elif choice == "3":
            run_calculator()
        elif choice == "4":
            print("Ha det!")
            return
        else:
            print("Ugyldig valg. Velg 1-4.\n")


if __name__ == "__main__":
    main()