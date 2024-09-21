#include <stdio.h>

int play_game(int turn)
{
  int choice;
  int res = CONTINUEPLAY;
  
  while(res == CONTINUEPLAY)
  {
    if (turn==USER)
      {
	choice = get_int_from_user();
	state[choice] = 'X';
      }
    else
      {
	choice = get_computer_decision();
	state[choice] = 'O'
      }
    printf_game_state();
    res = compute_result();

  }
}
   

