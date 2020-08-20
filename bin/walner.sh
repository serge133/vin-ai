# !/bin/zsh
cd ~/Desktop/Python/walner

helpmenu() {
  echo '''
    -h | --help = is the help menu
    -t | --train = activate training mode
		AI = blue
		You = pink
		action = bold
		error = red
		warning = yellow
  '''
}

while [ ! $# -eq 0 ]
do
	case "$1" in
		--help | -h)
			helpmenu
			exit
			;;
		--train | -t)
			python3 training.py
			exit
			;;
	esac
	shift
done

python3 executable.py


# python3 executable.py