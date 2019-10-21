## Google Account creation automation testing with Page Object model


### Install dependencies
```
pip install -r requirements.txt
```
### Create page objects:
+ Sign In page
+ Create Account page

### Test cases:
+ Test navigation to Sign In page
+ Test create account button
+ Test account - username validation
+ Test account - password validation

### Reports:
+ Test runner generates HTML report and saves it to the ./tests/reports folder
+ By default, after tests execution it opens report in default system browser

### Repository tree
```
.
├── README.md
├── pages
│   ├── base_page.py
│   ├── create_account.py
│   └── sign_in.py
├── repo_tree.txt
├── requirements.txt
├── resources
│   ├── data.py
│   └── locators.py
└── tests
    ├── base_test.py
    ├── reports
    │   ├── TestResults___main__.TestAccountCreation_2019-10-20_21-58-48.html
    │   ├── TestResults___main__.TestAccountCreation_2019-10-21_12-11-54.html
    │   └── report_example.png
    └── test.py
```

#### Example of the test runner report:
![alt text](tests/reports/report_example.png)
