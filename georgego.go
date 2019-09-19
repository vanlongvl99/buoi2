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
	nm := strings.Split(scanner.Text()," ")
	scanner.Scan()
	a := strings.Split(scanner.Text()," ")
	scanner.Scan()
	b := strings.Split(scanner.Text()," ")
	demA := 0
	// demB := 0
	n,_ := strconv.Atoi(nm[0])
	m,_ := strconv.Atoi(nm[1])
	for i := 0; i < m; i++{
		if demA == n{
			break
		}
		intB,_ := strconv.Atoi(b[i])
		intA,_ := strconv.Atoi(a[demA])
		if intB >= intA{
			demA += 1
		}
		// demB += 1
	}
	fmt.Println(n - demA)
}