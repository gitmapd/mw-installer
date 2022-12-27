#!/usr/bin/env bash
unset choice
die() { echo "$*" >&2; exit 2; }  # complain to STDERR and exit with error
needs_arg() { if [ -z "$OPTARG" ]; then die "No arg for --$OPT option"; fi; }

github_api="https://api.github.com"

repo="repos/CanastaWiki/Canasta-CLI/git/refs/tags"

data=$(curl ${github_api}/${repo} 2>/dev/null)

refs=$(jq -r '.. | select(.ref?) | .ref' <<< "${data}")
versions=( $(cut -d '/' -f 3 <<< "${refs}" | sort -h | tac | head -n 5) )

get_versions() {
	for index in "${!versions[@]}"; do
	  echo "  $((index))) ${versions[$index]}"
	done
}

query_version() {
	read -r -p "Pick a version (index): " choice # Read stdin and save the value on the $choice var
	echo ${choice}
}

download_package() {
	version=${versions[${1}]}
	if [[ -n ${version} ]]; then # Verify if the version with that index exists
		wget -q --show-progress "https://github.com/CanastaWiki/Canasta-CLI/releases/download/${version}/canasta"
		echo "Installing ${version} Canasta CLI"
		chmod u=rwx,g=xr,o=x canasta
		sudo mv canasta /usr/local/bin/canasta
	else
		echo "Invalid version"
	fi
}

while true; do
	case "${1}" in
		-l|--list-versions)
			get_versions
			break
			;;
		-i|--install)
			if [[ -n ${2} ]]; then
				download_package ${2}
				shift
			else
				get_versions
				download_package $(query_version)
			fi
			shift
			;;
		-*)
			die "Illegal option ${1}"
			;;
		*) 	
			wget -q  --show-progress "https://github.com/CanastaWiki/Canasta-CLI/releases/latest/download/canasta"
			echo "Installing latest Canasta CLI"
	                chmod u=rwx,g=xr,o=x canasta
        	        mv canasta /usr/local/bin/canasta
			break
			;;
  esac
done
