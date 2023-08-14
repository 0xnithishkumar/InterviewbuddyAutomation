# # # Note:- 
# generate auth.json = playwright codegen --save-storage=auth.json -b firefox acme.interviewbuddy.org/b2b/interviewer/login
# run the tests = pytest .\interview_test.py --html=report.html

from browser_context import browser_context, user_inputs
from playwright.sync_api import sync_playwright, expect
import re

# Change inputs for the following tests login, join, details, feedback, delay in browser context

# Login
def test_login(user_inputs):
# Set broswer as firefox
    with sync_playwright() as playwright:
        browser= playwright.firefox.launch(headless=False)
        page= browser.new_page()
    # Login
        page.goto("https://acme.interviewbuddy.org/b2b/interviewer/login")
        page.get_by_role("button", name="j3tG-on-clear Sign in with Google").click()
        page.get_by_role("textbox", name= "Email or phone").click()
        page.get_by_role("textbox", name= "Email or phone").fill(user_inputs['username'])
        page.get_by_role("button", name= "Next").click()
        page.get_by_role("textbox", name= "Enter your password").click()
        page.get_by_role("textbox", name= "Enter your password").fill(user_inputs['password'])
        page.get_by_role("button", name= "Next").click()
        page.wait_for_url("https://acme.interviewbuddy.org/b2b/interviewer/dashboard")
    # Check the page url
        expect(page).to_have_url("https://acme.interviewbuddy.org/b2b/interviewer/dashboard")
        page.close()


# Edit first name
def test_edit_first_name(browser_context):
# Set authenticated broswer
    browser, context= browser_context
    page= context.new_page()
    page.goto("https://acme.interviewbuddy.org/b2b/interviewer/dashboard")
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


# Edit last name
def test_edit_last_name(browser_context):
# Set authenticated broswer
    browser, context= browser_context
    page= context.new_page()
    page.goto("https://acme.interviewbuddy.org/b2b/interviewer/dashboard")
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


# Edit phone number
def test_edit_phone_number(browser_context):
# Set authenticated broswer
    browser, context= browser_context
    page= context.new_page()
    page.goto("https://acme.interviewbuddy.org/b2b/interviewer/dashboard")
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


# Open view details
def test_view_details(browser_context,user_inputs):
# Set authenticated broswer
    browser, context= browser_context
    page= context.new_page()
# Click on interview details
    page.goto("https://acme.interviewbuddy.org/b2b/interviewer/dashboard")
    old_url = page.url
    page.get_by_text("View all Interviews").click()
    page.get_by_role("row", name= user_inputs['details']).get_by_role("button", name= "View details").click()
    new_url = page.url
#check if interview details is opened.
    assert len(old_url.split('/')) != len(new_url.split('/'))
    page.close()


# Join interview
def test_join_interview(browser_context, user_inputs):
# Set authenticated broswer
    browser, context= browser_context
    page= context.new_page()
# Click on interview details
    page.goto("https://acme.interviewbuddy.org/b2b/interviewer/dashboard")
    page.get_by_text("View all Interviews").click()
    page.get_by_role("row", name= user_inputs['join']).get_by_role("button", name= "View details").click()
# Click on join interview
    page.get_by_role("link", name= "Join Interview").click()
    new_page= context.new_page()
    link= "https://acme.interviewbuddy.org/meeting-session/waiting-room?meeting_id= " + page.url.split("/")[-1]
    new_page.goto(link)
    assert "meeting-session/waiting-room?meeting_id" in new_page.url
    page.close()
    new_page.close()


# Use only the following template for feedback: af13f9fe-e317-48c3-8d28-bd91ffb5064d
# Give feedback
def test_feedback(browser_context, user_inputs):
    # Set authenticated broswer
    browser, context = browser_context
    page = context.new_page()
    # Click on interview details
    page.goto("https://acme.interviewbuddy.org/b2b/interviewer/dashboard")
    page.get_by_text("View all Interviews").click()
    page.get_by_role("row", name=user_inputs['feedback']).get_by_role("button", name="View details").click()
    # To give interview feeback
    page.get_by_role("tab", name=" Interview Feedback Report").click()
    page.get_by_role("region", name=" Interview Feedback Report").locator("img").click()
    page.get_by_role("textbox").first.click()
    page.get_by_role("textbox").first.fill("good, testing automation")
    page.locator(".p-radiobutton-box").first.click()
    page.locator("div:nth-child(5) > div > div > .row > .col-auto > .p-element > .p-radiobutton > .p-radiobutton-box").first.click()
    page.get_by_role("textbox").nth(1).click()
    page.get_by_role("textbox").nth(1).fill("abc")
    page.locator("div:nth-child(8) > div > div > .row > .col-auto > .p-element > .p-radiobutton > .p-radiobutton-box").first.click()
    page.get_by_role("textbox").nth(2).click()
    page.get_by_role("textbox").nth(2).fill("abc")
    page.locator("div:nth-child(11) > div > div > .row > .col-auto > .p-element > .p-radiobutton > .p-radiobutton-box").first.click()
    page.get_by_role("textbox").nth(3).fill("a")
    page.get_by_role("textbox").nth(3).click()
    page.get_by_role("textbox").nth(3).fill("abc")
    page.get_by_role("textbox").nth(4).click()
    page.get_by_role("textbox").nth(4).fill("abc")
    page.get_by_role("button", name="Save Changes").click()
    page.get_by_role("dialog", name="Confirmation").get_by_role("button", name="Save Changes").click()
    page.get_by_role("button", name="Close").click()
    # Check the changes
    assert "Interview Completed" in page.get_by_text("Interview Completed").text_content()
    page.close()


# Delay interview by 5 minutes
def test_delay(browser_context, user_inputs):
# Set authenticated broswer
    browser, context= browser_context
    page= context.new_page()
# Click on interview details
    page.goto("https://acme.interviewbuddy.org/b2b/interviewer/dashboard")
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


# Logout
def test_logout(browser_context):
# Set authenticated broswer
    browser, context= browser_context
    page= context.new_page()
# Logout
    page.goto("https://acme.interviewbuddy.org/b2b/interviewer/dashboard")
    page.locator("app-navbar").get_by_role("button").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name= "Logout").click()
    page.wait_for_url("https://acme.interviewbuddy.org/b2b/interviewer/login")
# Check the page url
    expect(page).to_have_url("https://acme.interviewbuddy.org/b2b/interviewer/login")
    page.close()