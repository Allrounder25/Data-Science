import pandas as pd
import random
import time

BASE_PRICE_PER_KWH = 11.5

def main():
    print("\n*********** MENU ************\n")
    choice = input("DO you want to plugin the car : ").lower()
    if choice not in ["y","yes"]:
        print("\nPlugin Not Detected\n")
        return
        
    df = pd.read_csv('Ev Sales.csv')


    index_value = random.randint(1,73)


    if index_value < 0 or index_value >= len(df):
        print("Invalid index value. Please enter a value between 0 and", len(df) - 1)
        return


    charging_time = df.loc[index_value, 'CHARGING POWER']
    charging_capacity = df.loc[index_value, 'CHARGING CAPACITY']


    charging_time_seconds = charging_time * 0.25

    initial_percentage = random.randint(5, 40)
    
    if charging_time<0.5:
        a= "Normal"
    elif charging_time<0.9:
        a="Super Charge"
    final_percentage = 100
    total_price = (final_percentage-initial_percentage) * BASE_PRICE_PER_KWH
    print(f"The Car Number Detected As : {index_value}")
    print(f"Charging Capacity : {charging_capacity}\nCharging Power : {a}")
    print(f"\ninitial_percentage : {initial_percentage}\n")

    print(f"Total price till {final_percentage}% : ₹{total_price:.2f}")
    payment_received = input("Enter 'yes' if payment is received: ")
    if payment_received.lower() != 'yes':
        print("Payment not received. Charging canceled.")
        return
    
    print(f"Charging started. Initial percentage: {initial_percentage}%")
    
 
    current_percentage = initial_percentage
 
    i = charging_time * 10
    initial = initial_percentage
    while (current_percentage < final_percentage):
        # Calculate the current percentage based on the charging capacity
        current_percentage = initial_percentage +  (i*charging_capacity / 10)
        
        # Ensure we do not exceed 100%
        if current_percentage > 100:
            current_percentage = 100
        
        print(f"Charging progress: {current_percentage:.2f}%")
        
        # Check if charging is completed
        if current_percentage >= final_percentage:
            print("Charging completed!")
            print(f"Charging complete! Battery charged from {initial:.2f}% to {current_percentage:.2f}%.")
            break
        initial_percentage = current_percentage
        time.sleep(charging_time_seconds) 

    # If the loop completes without reaching final percentage
    if current_percentage < final_percentage:
        print("Charging stopped. Final percentage:", current_percentage)

main()