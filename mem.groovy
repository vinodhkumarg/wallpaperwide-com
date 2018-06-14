def mem = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
def mem1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
def memMap = [:]
def memCopy = mem1

for(int itr = 1;itr <1000; itr++) {
//    println(itr+"---")
    Collections.shuffle(memCopy)
//    println(memCopy)
    for (int i = 0; i <= 9; i++) {
        memMap.put(mem[i], memCopy[i])
    }
//    println(mem)
//    println(memMap)
    def per = 0
    for (String s : mem) {
        def t = s

        for (int i = 1; i < 6; i++) {
            def m = memMap.get(t)
//            print(t + "=" + m + " , ")
            if (t == m) {
//                println("true")
                per ++
                break
            }
            t = m
        }

    }
    if(per>0)println((per/10)*100)
}
