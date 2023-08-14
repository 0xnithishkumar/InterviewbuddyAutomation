# # # Note:- 
# generate auth.json = playwright codegen --save-storage=auth.json -b firefox acme.interviewbuddy.org/b2b/interviewer/login
# run the tests = pytest .\interview_test.py --html=report.html

# # Libraries
import pytest
from playwright.sync_api import sync_playwright



# # Authenticated browser
@pytest.fixture(scope="module")
def browser_context():
    with sync_playwright() as playwright:
        browser = playwright.firefox.launch(headless=False)
        context = browser.new_context(storage_state='auth.json')
        yield browser, context
        context.close()
        browser.close()




# # Fixtures edit 
@pytest.fixture
def user_inputs():
# Edit the inputs below
    return  {"username" : 'username@gmail.com',
            "password" :'password',
            "details" :  ' '.join(details.split()),
            "join" : ' '.join(join.split()),
            "feedback" : ' '.join(feedback.split()),
            "delay" : ' '.join(delay.split()),
            }


details = '''
Mon, 24 Jul 2023
21:05 - 21:15	Testing@	Surya Sac	One on One	Expired
'''
join = '''
	Fri, 4 Aug 2023
18:28 - 18:38	test123	Nithish Kumar	One on One	Ongoing
'''
feedback = '''
Sat, 5 Aug 2023
Sun, 6 Aug 2023	QA	test notifications	One Way	Feedback Pending
'''
delay = '''
Fri, 4 Aug 2023
19:26 - 19:36	test123	Nithish Kumar	One on One	
'''