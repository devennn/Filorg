<<COMMENT1
# Test Case
- Check_Filename
    - test_check_rename_newname_1
    - test_check_rename_newname_2

# example of "$arg"
Check_Filename.test_check_rename_newname_1
COMMENT1

# if no arguments, run all, else run only arguments
if [ "$#" -eq  "0" ]
    then
        python -B -m unittest test.test_dp -v ||  python3 -B -m unittest test.test_dp -v
else
    for arg in "$@"
    do
        python -B -m unittest test.test_dp."$arg" -v
    done
fi
