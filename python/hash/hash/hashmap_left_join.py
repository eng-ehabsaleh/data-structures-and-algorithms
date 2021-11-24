# 

def left_join(ht1, ht2):
    result = []
    for i in ht1.bucket:
        if i:
            lj = []
            current_value = i.head
            while current_value:
                lj.append(current_value.data[0])
                lj.append(current_value.data[1])
                if ht2.contains(current_value.data[0]):
                    lj.append(ht2.get(current_value.data[0]))
                else:
                    lj.append(None)
                current_value = current_value.nxt

            result.append(lj)
    return result