# Test
- Using unittest package

## How to run
Test should be run from File-Organizer directory

### Executable script
> run in main dir : File-Organizer/
> sh run_test.sh

### Command Line
### Run all test
> python -B -m unittest test.test_dp -v

### Specific test
> python -B -m unittest test.test_dp.CLASSNAME.TESTCASE -v
> eg: python -B -m unittest test.test_dp.Check_Filename.test_check_rename_newname_1 -v
> Remove -b if not used

#### Test Case
- Check_Filename
    - test_check_rename_newname_1
    - test_check_rename_newname_2
