# 0. 타입스크립트는 변수 매개변수 리턴값에 타입을 붙이는것

    자바스크립트의 변수, 매개변수 리턴값 이 3개만 type을 다 붙히면 타입스크립트가 된다

    const a: string = '5';

    대문자 쓰지말고 소문자만 쓴다.

    string number boolean undefined null any(얘 쓰면 의미가 없다 자바스크립트가 되번린다.)

    함수에도 타입을 붙혀야 된다.
    function add (x: number, y:number)=> number = (x,y) => x+y;
    타입을 지워도 말이되는 코드가 되면 된다. 타입이 들어가는 위치.

    이름 다음에 변수명 나온다 생각하기 C++ 류와는 반대

    function 일때는 : 이 => 일때는 뒤에 타잎이 나온다

    객체(구조체)를 만들고 변수이름 : 타입 을 지정해 객체로도 사용할수가 있다.

    ** interface??? 이건 뭐지 타입스크립트의 핵심이다 이걸 이용해서 함수를 만든다 이건 심화과정 나중에 배운다

    function 을 쓰거나 type을 쓴다ㅣ

    배열 arr

    const arr :stringp[] = ['123', '123']
    
    튜플 : 길이가 고정된 배열

    const arr3: [number, number, string] = [123, 456, 'hell']

    숫자를 고정하거나  true를 고정하는등 값을 고정하는 타잎을 넣을수 있다.


# 1. 타잎 추론을 적극 활용하자

    타잎을 지우면 적절한 타잎을 추천한다 타잎을 쓰지 않아도 적절하게 타잎을 할당해준다(근데 그러면 자바스크립트랑 다를게 없지 않나)
    정확하게 추론을 햿으면 건들지 마락..?
    다른 사람이 볼때 이게 한눈에 읽히는 건가...?
    추론이 틀렸으면 그때 타입을 확정한다
    

    function add (x:number, y:number){return x+y}; 이래도 타잎을 추론해서 작동한다

    그렇지 타잎이 안적혀있으면 읽기가 어렵지
    앤간하면 추론에 맞겨라(좀더 알아보자)

# 2. js 변환 시 사라지는 부분을 파악하자

    타잎 자리 외워두기
    타잎 없어도 올바른 jsp 이여야 된다.
    interface ? 제너릭? 은 jsp로 변환시 사라진다.

    함수 바디를 나중에 선언해도 괜찮다 선언 윗부분 구현 나중도 가능하다는것.

    as 도 사라진다 as는 강제 형변환 시켜주는것
    
    c++에서의 형식이 여기서는 뭔가 당연하지 않나보다 

# 3. never 타입과 느낌표(non-null assertion)

    never 타입
    빈 배열 선언시 const array = []; 이렇게 하면 never 가되는데 어떤 형식도 들어가지 못한다.
    
    
