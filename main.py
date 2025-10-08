def run_processor():
    file_name= input(" Enter File Name: ")
    category_totals = {}
    print(" Starting transaction analysis ")
    
    try:
        with open(file_name,'r') as file:
            for line in file:
                clean_line=line.strip()
                if(clean_line):
                    parts = clean_line.split(',')
                    if (len(parts) == 3):
                        date = parts[0].strip()
                        category = parts[1].strip()
                        amount_str = parts[2].strip()
                        
                        category = str(category)
                        amount = int(amount_str)
    
                    if category in category_totals:
                        category_totals[category] += amount
                      
                    
                    else: 
                        category_totals[category] = amount
                        
                        
                        
            print("\n    --- Summary Report ---")
            net_total = 0
            for category, total in category_totals.items():
                if(type(category) == str):
                    print(f"{category.ljust(25)}:{total:,.2f} ")
                    net_total += total
            
            print("------------------------------------")
            
            print(f"NET BALANCE/ SPEND{''.ljust(7)}:{net_total:,.2f}")
            
            print("------------------------------------")
                        
    except ValueError:
        print(f"ERROR: {amount} is an invalid value")
    except FileNotFoundError:
        print(f"ERROR: The file, {file_name} could not be found")
    
            
if __name__ == "__main__":
    run_processor()