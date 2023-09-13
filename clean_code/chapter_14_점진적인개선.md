프로그램을 짜다 보면 종종 명령행 인수의 구문을 분석할 필요가 생긴다.
main 함수로 넘어오는 문자열 배열을 직접 분석하는 유틸리티가 없다면 직접 짜야된다.
새로 짤 유틸리티를 Args라 부른다.
Args는 사용법이 간단하낟.

```java
public static void main(String[] args){
    try{
        Args arg = new Args("l,p#,d*", args);
        boolean logging = arg.getBoolen('l');
        int port =arg.getInt('p');
        String directory = arg.getString('d');
    }
}
```