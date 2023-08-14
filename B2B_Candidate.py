import re
import time
import pytest
from playwright.sync_api import sync_playwright

# Change inputs for the following tests 3, 4 and 5


@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as playwright:
        browser = playwright.firefox.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://acme.interviewbuddy.org/b2b/candidate/login")
        yield page
        browser.close()


def test1_login(browser):
    page = browser
    page.get_by_role("button", name="Sign in with Google").click()
    page.wait_for_timeout(1000)
    page.get_by_role("textbox", name="Email or phone").click()
    page.wait_for_timeout(1000)
    page.get_by_role("textbox", name="Email or phone").fill("username@gmail.com")
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Next").click()
    page.wait_for_timeout(1000)
    page.get_by_role("textbox", name="Enter your Password").click()
    page.wait_for_timeout(1000)
    page.get_by_role("textbox", name="Enter your Password").fill("password")
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Next").click()
    page.wait_for_url("https://acme.interviewbuddy.org/b2b/candidate/dashboard")
    page.wait_for_timeout(1000)

######################################## Profile #######################################

def test2_editProfileDetails(browser):
    page = browser
    page.get_by_text("View Profile").click()
    if 'test123' == page.get_by_label("First Name").input_value(): flag = True
    else: flag =  False
    if flag:
        firstname = 'test321'
        lastname = 'last321'
        nickname = 'testacc'
        yob = '1981'
        gender = 'Female'
        country = "United States"
        state = 'ker'
        pin = '487454'
        add = 'xyz, abc'
        col = 'GITAM'
        deg = "Bachelor of Science (BSc)"
        course = 'xyz'
        yoc = '2002'
        skills = "xyz abc"
        project = 'projecty'
        link = 'https://acme.interviewbuddy.org'
        hear = 'Friends'

        prev_yob = "1980"
        prev_gender = 'Male'
        prev_country = "India"
        prev_degree = "Bachelor of Arts (BA)"
        prev_hear = 'LinkedIn'
    else:
        firstname = 'test123'
        lastname = 'last123'
        nickname = 'testaccount'
        yob = '1980'
        gender = 'Male'
        country = "India"
        state = 'kar'
        pin = "223520"
        add = 'abc, xyz'
        col = 'gitam'
        deg = "Bachelor of Arts (BA)"
        course = 'abc'
        yoc = '2000'
        skills = 'abc xyz'
        project = 'projectx'
        link = 'https://www.google.com'
        hear = 'LinkedIn'

        prev_yob = '1981'
        prev_gender = 'Female'
        prev_country = "United States"
        prev_degree = "Bachelor of Science (BSc)"
        prev_hear = 'Friends'
        
    page.locator("app-organization-candidate-profile-details div").filter(has_text="Basic Details First NameLast NameNick NameYear of Birth").locator("img").click()
    page.wait_for_timeout(500)
    page.get_by_label("First Name").fill(firstname)
    page.get_by_label("Last Name").fill(lastname)
    page.get_by_label("Nick Name").fill(nickname)
    page.get_by_text(prev_yob).click()
    page.get_by_role("option", name=yob).click()
    page.get_by_text(prev_gender).click()
    page.get_by_role("option", name=gender, exact=True).click()
    page.get_by_role("button", name="Save Changes").click()
    page.get_by_role("dialog", name="Confirmation").get_by_role("button", name="Save Changes").click()
    page.get_by_role("button", name="Close").click()

    page.locator("app-organization-candidate-profile-details div").filter(has_text="Contact Details Email IDPhone Number").locator("img").click()
    page.wait_for_timeout(500)
    page.get_by_label("Address").fill(add)
    page.locator("div").filter(has_text=re.compile(r"^Domicile State$")).first.click()
    page.get_by_label("Domicile State").fill(state)
    page.get_by_text(prev_country).click()
    page.get_by_role("option", name=country, exact=True).click()
    page.get_by_role("button", name="Save Changes").click()
    page.get_by_role("dialog", name="Confirmation").get_by_role("button", name="Save Changes").click()
    page.get_by_role("button", name="Close").click()

    page.locator("app-organization-candidate-profile-details div").filter(has_text="Education Details College Degree (Select 'Others' if degree is not found)Bachelo").locator("img").click()
    page.wait_for_timeout(500)
    page.get_by_label("College").click()
    page.get_by_label("College").fill(col)
    page.get_by_placeholder("Select Courses").fill(course)
    page.get_by_placeholder("Select Year Of Completion").fill(yoc)
    page.get_by_text(prev_degree).click()
    page.get_by_role("option", name=deg).click()
    page.get_by_role("button", name="Save Changes").click()
    page.get_by_role("dialog", name="Confirmation").get_by_role("button", name="Save Changes").click()
    page.get_by_role("button", name="Close").click()

    page.locator("app-organization-candidate-profile-details div").filter(has_text="Skills & Projects Mention your skillsMention your projects").locator("img").click()
    page.wait_for_timeout(500)
    page.get_by_label("Mention your skills").fill(skills)
    page.get_by_label("Mention your projects").fill(project)
    page.get_by_role("button", name="Save Changes").click()
    page.get_by_role("dialog", name="Confirmation").get_by_role("button", name="Save Changes").click()
    page.get_by_role("button", name="Close").click()

    page.locator("app-organization-candidate-profile-details div").filter(has_text="Linkedin Profile URL").locator("img").click()
    page.wait_for_timeout(500)
    page.locator("form").filter(has_text="Profile URL").locator("#college").fill(link)
    page.get_by_role("button", name="Save Changes").click()
    page.get_by_role("dialog", name="Confirmation").get_by_role("button", name="Save Changes").click()
    page.get_by_role("button", name="Close").click()
    
    page.locator("app-organization-candidate-profile-details div").filter(has_text="Additional Information How did ").locator("img").click()
    page.wait_for_timeout(500)
    page.get_by_text(prev_hear, exact=True).click()
    page.get_by_role("option", name=hear).click()
    page.get_by_role("button", name="Save Changes").click()
    page.get_by_role("dialog", name="Confirmation").get_by_role("button", name="Save Changes").click()
    page.get_by_role("button", name="Close").click()
    
######################################## Interviews #######################################

# retest
# CREATE INTERVIEW FIRST
def test3_joinInterview(browser):
    page = browser

    # input
    intjoin = """Sat, 5 Aug 2023
17:57 - 18:07	Testing@	One on One  Ongoing"""
    intjoin = ' '.join(intjoin.split())

    # Click on interview details
    page.goto("https://acme.interviewbuddy.org/b2b/candidate/dashboard")
    page.get_by_text("View all Interviews").click()
    page.get_by_role("row", name = intjoin).get_by_role("button", name= "View details").click()
# Click on join interview
    page.get_by_role("link", name= "Join Interview").click()
    link= "https://acme.interviewbuddy.org/meeting-session/waiting-room?meeting_id= " + page.url.split("/")[-1]
    page.goto(link)
    assert "meeting-session/waiting-room?meeting_id" in page.url
    page.close()


def test4_viewInterviewDetails(browser):
    page = browser
    page.goto("https://acme.interviewbuddy.org/b2b/candidate/dashboard")

    # input
    interviewName = """	Sat, 5 Aug 2023
Mon, 7 Aug 2023	QA	One Way	Feedback"""
    feed = ' '.join(interviewName.split())

    page.get_by_text("View all Interviews").click()
    page.get_by_role("row", name=interviewName).get_by_role("button", name="View details").click()
    page.get_by_role("link", name="").click()

######################################## Feedback #######################################

#Use only the following template for feedback: af13f9fe-e317-48c3-8d28-bd91ffb5064d
def test5_giveFeedback(browser):
    page = browser

    # input
    feed = """	Sat, 5 Aug 2023
Mon, 7 Aug 2023	QA	One Way	Feedback"""
    feed = ' '.join(feed.split())

    page.get_by_text("View all Interviews").click()
    page.get_by_role("link", name="").click()
    page.get_by_text("View all Interviews").click()
    page.get_by_role("row", name=feed).get_by_role("button", name="View details").click()
    page.get_by_role("tab", name=" Your Feedback").click()
    page.get_by_role("region", name=" Your Feedback").locator("img").click()
    page.locator("div:nth-child(5) > .p-element > .p-radiobutton > .p-radiobutton-box").first.click()
    page.locator("div:nth-child(6) > .row > div:nth-child(5) > .p-element > .p-radiobutton > .p-radiobutton-box").click()
    page.locator("div:nth-child(8) > .row > div:nth-child(5) > .p-element > .p-radiobutton > .p-radiobutton-box").click()
    page.locator("div:nth-child(10) > .row > div:nth-child(5) > .p-element > .p-radiobutton > .p-radiobutton-box").click()
    page.get_by_role("button", name="Save Changes").click()
    page.get_by_role("dialog", name="Confirmation").get_by_role("button", name="Save Changes").click()
    page.get_by_role("button", name="Close").click()
    page.get_by_role("link", name="").click()

######################################## Logout #######################################


def test6_logout(browser):
    # page.goto("https://acme.interviewbuddy.org/b2b/candidate/dashboard")
    page = browser
    page.locator("app-navbar").get_by_role("button").click()
    page.get_by_role("button", name="Logout").click()