package main
import(
	"fmt"
	"bufio"
	"os"
	"strings"
	"strconv"
)

func main(){
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	nt := strings.Split(scanner.Text()," ")
	scanner.Scan()
	a := strings.Split(scanner.Text()," ")
	n,_ := strconv.Atoi(nt[0])
	t,_ := strconv.Atoi(nt[1])
	sum := 0
	right := 0
	for i := 0; i < n; i++{
		intA,_ := strconv.Atoi(a[i])
		if sum + intA <= t{
			sum = sum + intA
			right += 1
		} else{
			break
		}
	}
	max := right
	for i := 1; i < n; i++{
		if right == n{
			break
		}
		aLeft,_ := strconv.Atoi(a[i -1])
		sum = sum - aLeft
		aRight,_ := strconv.Atoi(a[right])
		for (sum + aRight) <= t{
			sum = sum + aRight
			right += 1
			if right == n{
				break
			}	
			aRight,_ = strconv.Atoi(a[right])
		}
		if max < right - i{
			max = right - i
		}
	} 
	fmt.Println(max)
}