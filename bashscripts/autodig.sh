#! /bin/bash

echo "This will output all available DNS Records for a given domain";
read -p 'domain name: ' domain

# check if user string contains a "." (very simple input validation)
if (( $domain != *"."* ))
then
        echo 'Not a valid domain name!'
        return 1
fi

echo

# Types of records to check
recordTypes=("A" "AAAA" "CNAME" "NS" "MX" "SOA" "TXT" "PTR" "SRV" "AXFR")

# Check the domain for each record and display them
for t in ${recordTypes[@]}; do
        echo "$t Records:"
        dig $t $domain +noall +answer
        echo
done

echo 'All records have been checked. Consider re-checking with any subdomains found.'
