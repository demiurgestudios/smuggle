# smuggle

Useful if you want to import something without messing with sys.path yourself. Usage:

    from smuggle import smuggle


    utils = smuggle("utils", "../shovel")
