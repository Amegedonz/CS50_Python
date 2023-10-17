def main(): 
    plate = input("Plate: ") 
    print(is_valid(plate))


def is_valid(plate): 
    num = "" 
    while True: 
        if not (len(plate) >= 2 and len(plate) <= 6): 
            return 1
        
        if not plate.isalnum(): 
            return 2
        
        if not plate[:1].isalpha(): 
            return 3 
        
        for i in range(len(plate)): 
            if plate[i].isdigit(): 
                num = plate[i:]

                if num.startswith("0"): 
                    return 4
            
                if not num.isdigit(): 
                    return 5
            
                break

        return 10
 
main()