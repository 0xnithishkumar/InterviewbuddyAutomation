import re
import time
import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as playwright:
        browser = playwright.firefox.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://ib.interviewbuddy.org/b2c/interviewer/login")
        yield page
        browser.close()


@pytest.mark.required
def test_test1_Google_login(browser):
    page = browser
    page.get_by_role("button", name="Google logo Sign in with Google").click()
    page.wait_for_timeout(1000)
    page.get_by_role("textbox", name="Email or phone").click()
    page.wait_for_timeout(1000)
    page.get_by_role("textbox", name="Email or phone").fill("username@gmail.com")
    page.get_by_role("textbox", name="Email or phone").press("Enter")
    page.wait_for_timeout(1000)
    page.get_by_role("textbox", name="Enter your password").click()
    page.wait_for_timeout(1000)
    page.get_by_role("textbox", name="Enter your password").fill("password")
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Next").click()
    page.wait_for_url("https://ib.interviewbuddy.org/b2c/interviewer/dashboard")
    page.wait_for_timeout(1000)


# # Edit first name
def test_edit_first_name(browser_context):
# Set authenticated broswer
    browser, context= browser_context
    page= context.new_page()
    page.goto("https://ib.interviewbuddy.org/b2c/interviewer/dashboard")
    page.get_by_text("View Profile").click()
# edit first name
    page.locator("app-organization-profile-details").get_by_role("img").click()
    page.get_by_role("textbox").first.click()
    value= page.get_by_role("textbox").first.input_value()
# check the first name and modifiy accordingly
    if value!= 'test123': page.get_by_role("textbox").first.fill("test123")
    else: page.get_by_role("textbox").first.fill("test321")
# submit
    page.get_by_role("button", name= "Save Changes").click()
    page.get_by_role("dialog", name= "Confirmation").get_by_role("button", name= "Save Changes").click()
    page.get_by_role("button", name= "Close").click()
# check if the first name is changed
    page.locator("app-navbar").get_by_role("button").click()
    new_value= page.wait_for_selector("h6").text_content()
    assert value in new_value
    page.close()


# # Edit last name
def test_edit_last_name(browser_context):
# Set authenticated broswer
    browser, context= browser_context
    page= context.new_page()
    page.goto("https://ib.interviewbuddy.org/b2c/interviewer/dashboard")
    page.get_by_text("View Profile").click()
# edit last name
    page.locator("app-organization-profile-details").get_by_role("img").click()
    page.get_by_role("textbox").nth(1).first.click()
    value= page.get_by_role("textbox").nth(1).input_value()
# check the last name and modifiy accordingly
    if value!= 'last123': page.get_by_role("textbox").nth(1).fill("last123")
    else: page.get_by_role("textbox").nth(1).fill("last321")
# submit
    page.get_by_role("button", name= "Save Changes").click()
    page.get_by_role("dialog", name= "Confirmation").get_by_role("button", name= "Save Changes").click()
    page.get_by_role("button", name= "Close").click()
# check if the last name is changed
    page.locator("app-navbar").get_by_role("button").click()
    new_value= page.wait_for_selector("h6").text_content()
#check if last name is changed
    assert value in new_value
    page.close()


# # # Edit phone number
def test_edit_phone_number(browser_context):
# Set authenticated broswer
    browser, context= browser_context
    page= context.new_page()
    page.goto("https://ib.interviewbuddy.org/b2c/interviewer/dashboard")
    page.get_by_text("View Profile").click()
# edit phone number
    page.locator("app-organization-profile-details").get_by_role("img").click()
    page.get_by_role("spinbutton").first.click()
    value= page.get_by_role("spinbutton").first.input_value()
# check the phone and modifiy accordingly
    if value!= '1234567':
        page.get_by_role("spinbutton").first.fill("1234567")
        new_value= '1234567'
    else:
        page.get_by_role("spinbutton").first.fill("7654321")
        new_value= '7654321'
# submit
    page.get_by_role("button", name= "Save Changes").click()
    page.get_by_role("dialog", name= "Confirmation").get_by_role("button", name= "Save Changes").click()
    page.get_by_role("button", name= "Close").click()
    assert value!= new_value
# check if phone number is changed
    page.close()


# # Open view details
def test_view_details(browser_context,user_inputs):
# Set authenticated broswer
    browser, context= browser_context
    page= context.new_page()
# Click on interview details
    page.goto("https://ib.interviewbuddy.org/b2c/interviewer/dashboard")
    page.get_by_text("View all Interviews").click()
    page.get_by_role("row", name= user_inputs['details']).get_by_role("button", name= "View details").click()
#check if interview details is opened.
    assert "ib.interviewbuddy.org/b2c/interviewer/interviews/interview-details/" in page.url
    page.close()


# # # Join interview
def test_join_interview(browser_context, user_inputs):
# Set authenticated broswer
    browser, context= browser_context
    page= context.new_page()
# Click on interview details
    page.goto("https://ib.interviewbuddy.org/b2c/interviewer/dashboard")
    page.get_by_text("View all Interviews").click()
    page.get_by_role("row", name= user_inputs['join']).get_by_role("button", name= "View details").click()
# Click on join interview
    page.get_by_role("link", name= "Join Interview").click()
    new_page= context().new_page()
    link= "https://ib.interviewbuddy.org/meeting-session/waiting-room?meeting_id= " + page.url.split("/")[-1]
    new_page.goto(link)
    assert "meeting-session/waiting-room?meeting_id" in new_page.url
    page.close()
    new_page.close()


# # Give feedback
def test_feedback(browser_context, user_inputs):
    # Set authenticated broswer
    browser, context = browser_context
    page = context.new_page()
    # Click on interview details
    page.goto("https://ib.interviewbuddy.org/b2c/interviewer/dashboard")
    page.get_by_text("View all Interviews").click()
    page.get_by_role("row", name=user_inputs['feedback']).get_by_role("button", name="View details").click()
    # To give interview feeback
    page.get_by_role("tab", name=" Interview Feedback Report").click()
    page.get_by_role("region", name=" Interview Feedback Report").locator("img").click()
    page.get_by_role("textbox").first.click()
    page.get_by_role("textbox").first.fill("good, testing automation")
    # page.get_by_role("textbox").nth(1).click()
    # page.get_by_role("textbox").nth(1).fill("testing automation testing, feedback")
    page.get_by_role("button", name="Save Changes").click()
    page.get_by_role("dialog", name="Confirmation").get_by_role("button", name="Save Changes").click()
    page.get_by_role("button", name="Close").click()
    # Check the changes
    assert "Interview Completed" in page.get_by_text("Interview Completed").text_content()
    page.close()


# To be implemented
# # Delay interview by 5 minutes
def test_delay(browser_context, user_inputs):
# Set authenticated broswer
    browser, context= browser_context
    page= context.new_page()
# Click on interview details
    page.goto("https://ib.interviewbuddy.org/b2c/interviewer/dashboard")
    page.get_by_text("View all Interviews").click()
    page.get_by_role("row", name= user_inputs["delay"]).get_by_role("button", name= "View details").click()
# Delay interview
    page.get_by_role("button", name="Delay interview by 5 mins").click()
    page.get_by_role("button", name="Save Changes").click()
    page.get_by_role("button", name="Close").click()
    url= page.url
# Check if it is delayed
    page.locator("[id= \"\\31 \"]").click()
# assert
    assert not page.get_by_role("row", name= user_inputs["delay"]).get_by_role("button", name= "View details").is_enabled()


def test_test100_logout(browser) :
    page = browser
    page.goto("https://ib.interviewbuddy.org/b2c/interviewer/dashboard")
    page.locator("div:nth-child(3)").get_by_role("button").click()
    page.get_by_role("button", name="Logout").click()