# 1961을 풀며

- 행렬을 회전 했다는 말은 이해했는데, 출력이 왜 저렇게 나오는지 이해하는 데 시간이 좀 걸렸다. 3칸으로 나누어져 있는게 90, 180, 270의 경우라는 것을 인식 한 후... '돌렸다'의 개념보다는 '숫자를 읽는 순서를 바꾼다'라는 개념으로 접근하여보니 반복문의 순회 방식을 적절히 조절하면 비교적 금방 풀겠다고 생각했다.

## 핵심 코드

  ```python
      for i in range(N):  ##
        new_shape = ''
        for j in range(N - 1, -1, -1):  ##
            new_shape += shape[j][i]  ##
        shape_90.append(new_shape)
    trans_shape.append(shape_90)

    for i in range(N - 1, -1, -1):  ##
        new_shape = ''
        for j in range(N - 1, -1, -1):  ##
            new_shape += shape[j][i]  ##
        shape_180.append(new_shape)
    trans_shape.append(shape_180)

    for i in range(N - 1, -1, -1):  ##
        new_shape = ''
        for j in range(N):  ##
            new_shape += shape[j][i]  ##
        shape_270.append(new_shape)
    trans_shape.append(shape_270)

    new_trans_shape = list(map(list, zip(*trans_shape))) ###

  ```

- '##' 순회의 핵심이 되는 부분이라고 생각한다. 1번 입력을 예로 들어보면

  - 90도 회전 행렬은 인덱스를 `[2][0], [1][0], [0],[0] / [2][1], [1][1]...` 순으로 읽으면 되므로 행은 N에서 감소, 열은 0에서 증가하도록 설정한다.

  - 180도 회전 행렬은 인덱스를 `[2][2], [2][1], [2],[0] / [1][2], [1][1]...` 순으로 읽으면 되므로 행은 N에서 감소, 열은 N에서 감소하도록 설정한다.

  - 270도 회전 행렬은 인덱스를 `[0][2], [1][2], [2],[2] / [0][1], [1][1]...` 순으로 읽으면 되므로 행은 0에서 증가, 열은 N에서 감소하도록 설정한다.
  
- '###' 처음에는 아예 순회를 마쳤을 때 결과가 이미 전치행렬처리가 된 결과로 나오게 할까 생각했지만, ~~반복문 중첩시키면서 뒤집을 생각까지 하니 머리가 아파서~~ 그냥 마지막에 전치를 시키는게 깔끔할 것 같아서 zip함수를 사용하기로 했다. zip을 배우긴 했는데 asterisk랑 같이 썼는지 잘 기억이 나지 않았다... 찾아보니 zip함수는 동일한 개수로 이루허진 자료형을 `묶어주기` 때문에 리스트로 다시 나열하려면 `언패킹`하는 과정이 필요하므로 Asterisk를 사용한다고 한다. 


