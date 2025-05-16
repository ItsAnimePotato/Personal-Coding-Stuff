class Continent {
  
  int size;
  int airports;
  int seaports;
  PVector position;
  
  Continent() {
    size = 5; 
    airports = int(random(size*1.5));
    seaports = int(random(size));
  }
  
  Continent(int s, int x, int y) {
    size = s;
    airports = int(random(size*1.5));
    seaports = int(random(size));
    
    position = new PVector(x,y);
  }
  
  void display() {
    square(position.x, position.y, size * random(NUM_CONTINENTS * size));
  }
}
