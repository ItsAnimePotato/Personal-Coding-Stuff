
boolean colorPts;
boolean backgroundPts;

void setup() {
  size(500, 500);
  background(255);

  colorPts = false;
  backgroundPts = false;
}

void draw() {
  if (colorPts) {
    colorPts();
  }
  if (backgroundPts) {
    backgroundPts();
  }
}

void colorPts() {
  color c = color(mouseX, 0, mouseY);
  fill(c);
  point(mouseX, mouseY);
}

void backgroundPts() {
  for (int x = 0; x < width; x++) {
    for (int y = 0; y < height; y++) {
      
      color c = color(mouseX, 0, mouseY);
      stroke(c);
      point(mouseX, mouseY);
      point(random(-x/mouseX,x/mouseX) + mouseX, random(-y/mouseY,y/mouseY) + mouseY);
    }
  }
}

void keyPressed() {
  if (key == 'c') {
    colorPts = !colorPts;
  }
  if (key == 'b') {
    backgroundPts = !backgroundPts;
  }
}
