# Function flow / DRAFT 
Function flow for the number guesser program
```mermaid
flowchart TD
    %% Functions
    main_loop

    print_intro
    calculate_midpoint
    print_guess
    get_yes_no_input
    is_yes
    print_win_message
    is_higher
    update_low
    update_high

    %% Calls
    main_loop --> print_intro
    main_loop --> calculate_midpoint
    main_loop -->|"each iteration"| print_guess
    main_loop --> get_yes_no_input
    main_loop --> is_yes

    is_yes -->|"True"| print_win_message
    is_yes -->|"False"| get_yes_no_input

    get_yes_no_input --> is_higher

    is_higher -->|"True"| update_low
    is_higher -->|"False"| update_high

    update_low --> calculate_midpoint
    update_high --> calculate_midpoint

    calculate_midpoint -->|"loop back"| main_loop
```