

len_shop = int(input())
shop_str = input()
shop_str = shop_str.strip().split(' ')

len_request = int(input())
request_str = input()
request_str = request_str.strip().split(' ')

def process(shops, requests):
    count_avaliable = {}
    for size in shops:
        count_avaliable[size] = 0


    for size in shops:
        for i in range(1000):
            t_size = 'X' * i + size
            if t_size in count_avaliable:
                count_avaliable[t_size] += 1
                
    for req in requests:
        Yes = False
        for i in range(1000):
            if req[-1] == 'L':
              t_size = 'X' * i + req
              if t_size in count_avaliable :
                  Yes = True
                  break
            elif req[-1] == 'S':
              if i < len(req)-1:
                t_size = req[i:]
              else:break
              if t_size in count_avaliable :
                  Yes = True
                  break
            else:
              if 'M' in count_avaliable :
                  Yes = True
                  break
              else:
                  t_size = 'X' * i + req
                  if t_size in count_avaliable :
                      Yes = True
                      break
        if not Yes:
            return False

    return True

if process(shop_str, request_str):
    print("Yes")
else:
    print("No")
