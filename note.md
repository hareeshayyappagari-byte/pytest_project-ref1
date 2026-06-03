# note -

### to run specific test cases on folder level -  
* pytest pytest-features-demo/test_running_steps.py

### To run specific test file - 
* pytest pytest-features-demo/test_running_steps.py::test_login

### run the test using keyword - 
* pytest -k "even"

### run in verbose mode (Detailed)- ![img.png](snaps/img.png)
* pytest -v pytest-features-demo/test_sample.py


### To run the last failed testcases
* pytest --lf![img_1.png](snaps/img_1.png)

# markers - used to group the test cases (very useful to group as features)
* pytest -m "sanity or smoke or regression"
![img.png](img.png)

skip marker - used to skip unconditionally - should be used on incomplete tests
* @pytest.mark.skip
![img_1.png](img_1.png)

* @pytest.mark.skip(reason='what ever')
![img_2.png](img_2.png)

* skip if - used for to run with some condition cases
* @pytest.mark.skipif(True, reason='under process test')
* ![img_3.png](img_3.png)


# perametarization - used to test multiple inputs into single test
@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 54)])
![img_4.png](img_4.png)


# Xfail - 