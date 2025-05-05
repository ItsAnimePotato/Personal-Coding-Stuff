Continent[] place;
int NUM_CONTINENTS = 7;

void setup() {
  size(750, 500);

  place = new Continent[NUM_CONTINENTS];
  for (int i = 0; i < NUM_CONTINENTS; i++) {
    int randSize = int(random(1,NUM_CONTINENTS+1));
    place[i] = new Continent(randSize, randX, randY);
    place[i].display();
  }
}

void draw() {
}
