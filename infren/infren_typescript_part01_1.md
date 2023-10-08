# 0. 타입스크립트는 변수 매개변수 리턴값에 타입을 붙이는것

    자바스크립트의 변수, 매개변수 리턴값 이 3개만 type을 다 붙히면 타입스크립트가 된다

    const a: string = '5';

    대문자 쓰지말고 소문자만 쓴다.

    string number boolean undefined null any(얘 쓰면 의미가 없다 자바스크립트가 되번린다.)

    함수에도 타입을 붙혀야 된다.
    function add (x: number, y:number)=> number = (x,y) => x+y;
    타입을 지워도 말이되는 코드가 되면 된다. 타입이 들어가는 위치.
    