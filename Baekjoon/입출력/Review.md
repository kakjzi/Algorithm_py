## Review 입출력

* input() 

> 사용자가 어떤 값을 입력하게 하고, 그 값을 변수에 저장할 수 있습니다.
>
> 입력 받은 값은 문자열로 저장된다.



* map(f, iterable) ***

> 함수( f ) 와 반복 가능한 (iterable) 자료형을 입력받아 iterable요소를 지정된 함수로 처리한다.
>
> 보통 여러개 Data를 한 번에 다른 형태로 바꾸기 위해 사용한다.			
>
> map 의 return 값은 iterator를 반환한다.

<img src="https://user-images.githubusercontent.com/82758364/134859239-a9acd6c2-58c6-46e4-aa0f-874e4c87b9db.png" style="zoom: 67%">

참고 (https://coding-groot.tistory.com/22)



* 파이썬(Python) 3 포맷팅 방식 : "출력형식".format(데이터...)

  *  아래는 예시.

    ```
    print('내 이름은 {0}'.format('신지우'))
    print('내 나이는 {age}'.format(age=100))
    print('만세삼창 :  {0}!!! {0}!!! {0}!!! '.format('만세'))
    print('삼삼칠 박수 :  {0}!!! {0}!!! {1}!!! '.format('짝' * 3, '짝' * 7))
    ```

    

  * 고급 format 형식

    ```
    for i in range(9,0,-2):
    	// 앞뒤로 공백.
    	print('{:^10}'.format('*' * i))
    ```

<img src="https://user-images.githubusercontent.com/82758364/134859306-26321c10-356d-4838-adb7-6286a81a0df6.png" style="zoom: 67%">



* 여러줄을 받아야할 때 input 을 사용한다면 시간초과가 발생할 수 있다.

  ==>> sys.stdin.readline() 을 사용한다. 이때 \n 를 포함한다는 것도 기억! 
  
  

* (Start, Stop, Step)

  * |                        | Range | a[  ] |
    | :--------------------- | :---: | :---: |
    | 범위 내 Stop  포함여부 |   X   |   O   |

  

