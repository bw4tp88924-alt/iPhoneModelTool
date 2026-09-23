import sqlite3

def ask_menu(prompt, options):
    """
    Presents a numbered menu with a default 'I don't know' option.
    options: list of tuples -> (Display Name, SQL Column Name, Database Value)
    """
    while True:
        print(f"\n[?] {prompt}")
        for i, option in enumerate(options, 1):
            print(f"  ({i}) {option[0]}")
        print("  (0) I don't know / Skip")
        
        choice = input("\nSelect an option number: ").strip()
        
        if choice == "0":
            print("  ↳ Skipping question...")
            return None, None
            
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(options):
                display_name, column, val = options[idx]
                sql_clause = f"{column} = ?"
                return sql_clause, val
                
        print("❌ Invalid selection. Please enter a valid number from the list.")

def run_identifier():
    conn = sqlite3.connect("iphones.db")
    cursor = conn.cursor()
    
    query = "SELECT model_name FROM iphones WHERE 1=1"
    params = []
    
    def get_matches():
        cursor.execute(query, params)
        return [row[0] for row in cursor.fetchall()]

    # Define characteristics and their menu options: (Display Label, DB Column, DB Value)
    
    # 1. Port Type
    port_options = [
        ("lightning", "port_type", "lightning"),
        ("USB-C", "port_type", "USB-C")
    ]
    
    clause, val = ask_menu("What type of charging port does it have?", port_options)
    if clause is not None:
        if val != 0:
            query += " AND (',' || REPLACE(port_type, ' ', '') || ',') LIKE ?"
            params.append(f"%{val},%")
        else:
            query += (
                " AND (port_type IS NULL OR port_options = '' OR"
                " port_type = '0')"
            )
            
    matches = get_matches()
    if len(matches) <=1:
        finalize(matches)
        conn.close()
        return
		
	# 2. Home Button
    print(f"\n--- Potential matches remaining: {len(matches)} ---")
    home_button_options = [
        ("Yes (Has Physical Home Button)", "home_button", 1),
        ("No (Does not have a Physical Home Button)", "home_button", 0)
    ]
    clause, val = ask_menu("Does it have a Physical Home Button?", home_button_options)
    if clause:
        query +=f" AND {clause}"
        params.append(val)
		
    matches = get_matches()
    if len(matches) <=1:
        finalize(matches)
        conn.close()
        return

    # 3. Rear Cameras Count
    print(f"\n--- Potential matches remaining: {len(matches)} ---")
    camera_options = [
        ("1 Rear Camera", "rear_cameras", 1),
        ("2 Rear Cameras", "rear_cameras", 2),
        ("3 Rear Cameras", "rear_cameras", 3)
    ]
    clause, val = ask_menu("How many rear cameras does it have?", camera_options)
    if clause:
        query += f" AND {clause}"
        params.append(val)
        
    matches = get_matches()
    if len(matches) <= 1:
        finalize(matches)
        conn.close()
        return

    # 4. Action Button
    print(f"\n--- Potential matches remaining: {len(matches)} ---")
    action_options = [
        ("Has Action Button", "action_button", 1),
        ("Has Ringer/Silent Switch", "action_button", 0),
        ("Does not have Action Button or Ringer/Silent Switch", "action_button", 2)
    ]
    clause, val = ask_menu("Does it have an Action Button or a Ringer/Silent Switch?", action_options)
    if clause:
        query += f" AND {clause}"
        params.append(val)
        
    matches = get_matches()
    if len(matches) <= 1:
        finalize(matches)
        conn.close()
        return

    # 5. Camera Control Button
    print(f"\n--- Potential matches remaining: {len(matches)} ---")
    camera_control_options = [
        ("Yes (Has Camera Control Button)", "camera_control", 1),
        ("No (Does not have Camera Control Button)", "camera_control", 0)
    ]
    clause, val = ask_menu("Does it have a Camera Control Button?", camera_control_options)
    if clause:
        query += f" AND {clause}"
        params.append(val)
		
    matches = get_matches()
    if len(matches) <=1:
        finalize(matches)
        conn.close()
        return
	        
    #6. Special Colour
    print(f"\n--- Potential matches remaining: {len(matches)} ---")
    colour_options = [
        ("Blue", "special_colour", 1),
        ("Green", "special_colour", 2),
        ("Yellow", "special_colour", 3),
        ("Pink", "special_colour", 4),
        ("Gold", "special_colour", 5),
        ("Rose Gold", "special_colour", 6),
        ("Red", "special_colour", 7), 
        ("Purple", "special_colour", 8), 
        ("Orange", "special_colour", 9), 
        ("Burgundy", "special_colour", 10),
        ("None of the above", "special_colour", 0)
    ] 
    clause, val = ask_menu("Is it one of the following colours?", colour_options)
    if clause is not None:
        if val != 0:
            query += " AND (',' || REPLACE(special_colour, ' ', '') || ',') LIKE ?"
            params.append(f"%{val},%")
        else:
            query += (
                " AND (special_colour IS NULL OR special_colour = '' OR"
                " special_colour = '0')"
            )
            
    matches = get_matches()
    if len(matches) <=1:
        finalize(matches)
        conn.close()
        return
    
    finalize(matches)
    conn.close()

def finalize(matches):
    print("\n" + "="*40)
    if len(matches) == 1:
        print(f"🎯 Identified Model: {matches[0]}")
    elif len(matches) == 0:
        print("❌ No models match this exact combination of traits.")
    else:
        print(f"📋 Possible matching models ({len(matches)} found):")
        for m in matches:
            print(f"  • {m}")
    print("="*40)

if __name__ == "__main__":
    run_identifier()