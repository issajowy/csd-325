
def main():
    intro()
    
    try:
        miles_driven=float(input("How far did you travel today? In Miles."))          #writing the interactive promt, and used a float value to include decimal values
        miles_to_kilometers(miles_driven)
        
        
    except:
        print("Error has occurred, try once more")                                    #incase they entered the information wrong
        print()
        main()
        
def intro():
    print('At this LLC we care about your mile conversion so that you can get every dollar back!')               #Interactive display saying the conversion units from gallons to liters
    print('This conversion such that;')
    print('1 miles is equal to about 1.609 kilometers.')
    print()
    
def miles_to_kilometers(miles):
    kilometers= miles * 1.609
    print((f'Today you drove {miles:.2f} miles ') + (f'or {kilometers:.2f} kilometers'))
main()
