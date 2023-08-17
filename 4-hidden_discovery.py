#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4

    ref = dir(hidden_4)
    for x in range(len(ref)):
        if ref[x][:2] != "__":
            print(ref[x])
