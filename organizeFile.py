import directory_process as dp

# Get input and check validity
# Input must be correctly format int and in range od choice
def get_input():
    print("(1) Desktop (2) Documents (3) Downloads")
    chosen = input(r"Choose Folder to organize: 1 or 2 or 3 -> ")
    while(1):
        if(isinstance(chosen, float)):
            continue
        else:
            c = int(chosen)
            if(c not in range(1, 4)):
                continue
            else:
                # Index start at 0
                c = c - 1
                return c


# Main
if __name__ == '__main__':
    chosen = get_input()
    print("\nEnter Username")
    userName = input("eg: Directory: c/Users/jack | Username: jack -> ")
    dp.access_dir(chosen, userName)
