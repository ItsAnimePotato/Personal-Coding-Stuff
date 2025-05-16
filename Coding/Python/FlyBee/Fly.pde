
class Fly {
  PVector position;
  String string;
  
  
  Fly(int p, String s) {
    position = new PVector(p, p);
    string = s;
  }
  
  void display() {
    circle(position.x, position.y, 10);
    text(string, position.x, position.y + 25); 
  }
}
