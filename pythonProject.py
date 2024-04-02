def registration():                                 #해야할 일을 등록하는 함수
    global mainList                                 #전역번수로써 메인 리스트를 사용

    regList = []                                    #등록하는 할일의 리스트를 새로 선언
    
    regList.append(len(mainList) + 1)                        #리스트에서 각 할일 목록의 구분을 위해 인덱스 번호 생성          
    regList.append(input("해야할 일의 이름 : "))        #해야할 일의 이름을 입력받아 배열에 저장
    regList.append("미완료")                         #기본적으로 미완료 상태로 저장
    mainList.append(regList)                        #메인 리스트에 저장된 배열을 추가하여 2차원 배열로 관리
    print("해야할 일", regList[1], "가",regList[0], "번으로 등록되었습니다!")   #저장된 할일을 사용자가 보기좋게 출력

def search():                                       #할일을 검색하는 함수
    global mainList

    searchstr = input("검색할 해야할 일을 입력하시오 : ")     #문자열 상태로 검색어 입력받기
    for i in range(len(mainList)):                     #메인 리스트에서 검색어와 일치하는 문자열이 있는지 찾고 있다면 해당 배열의 위치와 검색어를 반환
        if mainList[i][1] == searchstr:
            return i, searchstr

def changeComp():                                   #할일을 완료상태로 변경하는 함수
    for i in range(len(mainList)):
        print(mainList[i][0], '번 - ', mainList[i][1] , ', 현재 진행상태 : ', mainList[i][2])
    n = int(input("다음 중 완료로 변경할 할일을 번호로 선택하시오."))   #완료로 변경할 할일의 번호를 입력받고 '완료' 상태로 변경
    mainList[n - 1][2] = "완료"
    for i in range(len(mainList)):
        print(mainList[i][0], '번 - ', mainList[i][1] , ', 현재 진행상태 : ', mainList[i][2])

def delete():
    for i in range(len(mainList)):
        print(mainList[i][0], '번 - ', mainList[i][1] , ', 현재 진행상태 : ', mainList[i][2])
    n = int(input("삭제할 할일의 번호를 입력해주세요."))    #삭제할 할일의 번호를 입력받아 삭제
    del(mainList[n - 1])
    for i in range(len(mainList) - n + 1):              #삭제 후 삭제한 할일보다 인덱스 번호가 높은 것들의 인덱스 값 수정
        mainList[n + i - 1][0] -= 1

if __name__ == "__main__":
    mainList = []

    while True:
        menu = int(input('1. 할일등록 2. 할일검색 3. 완료로바꾸기 4. 삭제 5. 전체출력 6. 미완료 항목 출력 7.종료 \n'))
        if menu == 1:
           registration()
        elif menu == 2:
            n = -1
            n, strPrint = search()
            if n == -1:
                print(strPrint,"은 해야할 일 목록에 없습니다.")
            else:
                print(mainList[n])
        elif menu == 3:
            changeComp()
        elif menu == 4:
            delete()
        elif menu == 5:
            for i in range(len(mainList)):
                print(mainList[i][0], '번 - ', mainList[i][1] , ', 현재 진행상태 : ', mainList[i][2])
        elif menu == 6:
            for i in range(len(mainList)):
                if mainList[i][2] == '미완료':
                    print(mainList[i])
        elif menu == 7:
            break
        else:
            print("1-6 까지의 숫자 중 하나를 입력해주세요.")