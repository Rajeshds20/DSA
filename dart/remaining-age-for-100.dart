import 'dart:io';

void main() {
  print('Enter your Name :');
  String? name = stdin.readLineSync();
  int n = int.parse(stdin.readLineSync());
  n = 100 - n;
  print('$name, have to go $n years for turning 100');
}
