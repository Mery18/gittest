// import random

// def main(args):
//     ileKw = int(input("Podaj ilość losowanych punktów: "))
//     ileKo = 0
//     r = 1

//     for i in range(ileKw):
//         x = random.random()
//         y = random.random()
//         if x**2 + y**2 <= r**2:
//             ileKo += 1
//     pi = 4 * ileKo / ileKw
//     print("Przyblizona wartość pi: ", pi)
szerokosc = 640;
wysokosc = 480;

ileKw = prompt("Podaj ilość punktów: ", 100);
ileKw = parseInt (ileKw);
ileKo = 0;
r = prompt("Podaj promień:  ", 100);

function getRnd(min, max){
	return Math.random() * (max - min) + min;
}

for (i = 0; i < ileKw; i++){
		x = Math.floor(getRnd(-r, r));
		y = Math.floor(getRnd(-r, r));
		//onsole.log(x);
		lx[i] = x;
		ly[i] = y;
		if (x*x + y*y <= r * r) {
			ileKo++;

	}
}
console.log(lx);
pi= 4*ileKo/ileKw;
alert("Przyblizona  wartosc: " + pi);

function setup() {
	createCanvas(szerokosv, wysokosc);
	stroke('#666')
	backgroung('#00ff00');
	ellipse(szerokosc / 2, wysokosc / 2, 2*r, 2*r);
	line(szeroksc / 2,0, szerokosc /2, wysokosc );
	lihne(0, wysokosc  / 2,szerokosc, wysokosc / 2 );
}


 function draw() {
 		for(i=0; i <ileKw; i ++){
 			if (lx[i]*lx[i] + ly[i]*ly[i] <= r*r){
 				stroke('#f00');
 			} else {
 				stroke('#000');
 			}
 			point(lx[i] + szerokosc / 2, ly[i]);
 		}

 }


console.log("Liczba Pi: " + (4 * ileKw/ileKo))
function setup() {
  // put setup code here
}

function draw() {
  // put drawing code here
}