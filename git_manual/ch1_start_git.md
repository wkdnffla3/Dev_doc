깃의 역할

1. 버전 관리
    - 문서를 수정할 때마다 언제 수정했는지, 어떤 것을 변경했는지 등을 구체적으로 기록하는 것을 버전 관리 라고 하고 이것을 가능케 하는게 깃이다.

2. 백업하기
    - 당신의 컴퓨터가 언제 죽을지 모른다
    - 확실한건 컴퓨터는 언젠간 죽는다.
    - 원격 저장소인 깃허브를 쓴다.

3. 협업하기
    - 온라인 서비스를 사용하면 여러 사람이 함께 일할수 있다는 장점이 생긴다.
    - 업로드를한 이력이 남아 오류 파악이 쉽다.

위의 3가지 기능들은 순서대로 배워야 한다.

버전관리 -> 백업 -> 협업.

깃 프로그램의 종류

- 깃허브 데스크 톱
    - 깃 사용법을 GUI로 구현한 것.

- 토터스 깃
    - 윈도우 탐색기의 빠른 메뉴에 추가되는 윈도우 전용 프로그램이다.

- 소스 트리
    - 깃의 기본 기능부터 고급 기능까지 사용가능한 프로그램

- 커맨드 라인 인터페이스 (CLI)
    - 터미널 창에 직접 입력해서 사용한다.


깃 설치
    깃 설치시 브랜치 이름을 master 에서 main 으로 한다.
    커맨드 라인에서 깃을 어떤 방법으로 사용할지 선택한다 git from the command line and also from 3rd-party software로 사용한다.
    use bundled OpenSSH로 사용한다
    https 처럼 보안이 추가되었을때 뭐로 연결할 것인지 선택할 차례 use the openSSL library를 선택한다.
    Use MinTTY가 선택된 상태로 Next를 한다..

git config --gloabl user.name "이름"
git config --global user.email "mail address"

pwd 현재 디렉토리

ls -al 숨김파일들과 파일 상세 정보 권한까지 다 보인다.
-r reverse 정렬 순서를 거꾸로 표기
-t 파일 작성 시간순 내림차순으로 표시

clear

git init 을 하면 저장소가 생긴 것이다