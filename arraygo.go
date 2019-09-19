package main
import (
	"fmt"
	"os"
	"bufio"
	"strings"
	"strconv"
)

func main(){
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	nk := strings.Split(scanner.Text()," ")
	scanner.Scan()
	arrA := strings.Split(scanner.Text()," ")
	var cnt [100001]int
	count := 0
	n,_ := strconv.Atoi(nk[0])
	k,_ := strconv.Atoi(nk[1])
	right := 0
	for i := 0; i < n; i++{
		a,_ := strconv.Atoi(arrA[i])
		cnt[a] = cnt[a] + 1
		if cnt[a] == 1 {
			count += 1
		} 
		if count == k{
			right = i
			break
		}
	}
	if count != k{
		fmt.Println("-1 -1")
	}else{
		for i := 0; i < right + 1; i++{
			b,_ := strconv.Atoi(arrA[i])
			if cnt[b] > 1{
				cnt[b] = cnt[b] - 1
			}else{																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																											
				x := strconv.Itoa(i + 1)
				y := strconv.Itoa(right + 1)
				fmt.Println(x + " " + y)
				break
			}
		}
	}
}