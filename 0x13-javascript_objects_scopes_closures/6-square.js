#!/usr/bin/node

const Square = require('./5-square');
const Rsquare = new Square ();
class Square extends Rsquare {
  constructor (size){
    super(size, size);
  }

  charPrint(c) {
    if (c === undefined) {
      c = 'X';
    }
    let row = c.repeat(this.width);
    for (let i = 0; i < this.height; i++) {
      console.log(row);
    }
  }
}

