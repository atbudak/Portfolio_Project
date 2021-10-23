#!/bash/bin

file_check(){
	until [[ -e "myfile.txt" ]]
	do
		echo "myfile yok"
		sleep 3
	done
	echo "myfile var"
}
file_check
