if __name__ == '__main__':
    import sys
    from controller import run_sim
    print("Detected arg: " + sys.argv[1])
    run_sim(int(sys.argv[1]))
