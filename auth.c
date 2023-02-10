#include <stdio.h>
#include <string.h>

int main() {
  char username[10];
  char password[10];

  printf("Enter username: ");
  scanf("%s", username);

  printf("Enter password: ");
  scanf("%s", password);

  if (strcmp(username, "admin") == 0 && strcmp(password, "password") == 0) {
    printf("Access granted\n");
  } else {
    printf("Access denied\n");
  }

  return 0;
}
