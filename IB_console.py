import re
import time
import pytest
from playwright.sync_api import sync_playwright, expect


@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as playwright:
        browser = playwright.firefox.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://ib.interviewbuddy.org/ib/console/login")
        yield page
        browser.close()

def test1_login(browser):
    page = browser
    page.get_by_role("button", name="Sign in with Google").click()
    page.wait_for_timeout(500)
    page.get_by_role("textbox", name="Email or phone").click()
    page.wait_for_timeout(500)
    page.get_by_role("textbox", name="Email or phone").fill("username@gmail.com")
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Next").click()
    page.wait_for_timeout(500)
    page.get_by_role("textbox", name="Enter your Password").click()
    page.wait_for_timeout(500)
    page.get_by_role("textbox", name="Enter your Password").fill("password")
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Next").click()
    page.wait_for_url("https://ib.interviewbuddy.org/ib/console/dashboard")


######################################## Manage Interviewer #######################################

#####################Block Interviewer###########################################################
# Make sure the inyerbiewer is unblocked
def test2_block_interviewer(browser):
    page = browser
    page.goto("https://ib.interviewbuddy.org/ib/console/dashboard")
    interviewer = "notification"
    reason = "automation Testing"
    page.get_by_text("Interviewers", exact=True).click()
    page.locator("app-header img").click()
    page.get_by_role("textbox").click()
    page.get_by_role("textbox").fill(interviewer)
    page.get_by_role("button", name="Search").click()
    page.get_by_role("link", name="View").click()
    page.get_by_role("button", name="Block").click()
    page.locator("textarea").click()
    page.locator("textarea").fill(reason)
    page.get_by_role("dialog", name="Confirmation").get_by_role("button", name="Block").click()

# Make sure the interviewer is blocked
def test3_unblock_interviewers(browser):
    page = browser
    page.goto("https://ib.interviewbuddy.org/ib/console/dashboard")
    interviewer = "notification"
    reason = "automation Testing"
    page.get_by_text("Interviewers", exact=True).click()
    page.locator("app-header img").click()
    page.get_by_role("textbox").click()
    page.get_by_role("textbox").fill(interviewer)
    page.get_by_role("button", name="Search").click()
    page.wait_for_timeout(1000)
    page.get_by_role("link", name="View").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Unblock").click()
    page.get_by_role("textbox").nth(1).click()
    page.get_by_role("textbox").nth(1).fill(reason)
    page.get_by_role("dialog", name="Confirmation").get_by_role("button", name="Unblock").click()

# Make sure the interviewer is not in the same state
def test4_statuschange(browser):
    page = browser
    page.goto("https://ib.interviewbuddy.org/ib/console/dashboard")
    interviewer = "Abhiram"
    status = "Active" # Active or Pending Approval or Not Approved
    page.get_by_text("Interviewers", exact=True).click()
    page.locator("app-header img").click()
    page.get_by_role("textbox").click()
    page.get_by_role("textbox").fill(interviewer)
    page.get_by_role("button", name="Search").click()
    page.wait_for_timeout(1000)
    page.get_by_role("link", name="View").click()
    page.get_by_role("button", name="Change Status").click()
    page.pause()
    page.get_by_role("dialog", name="Change Status").get_by_text("Active").click()
    page.get_by_role("option", name=status).click()
    page.get_by_role("button", name="Save").click()
    page.get_by_role("button", name="Save changes").click()
    page.get_by_role("button", name="Close").click()


######################################## Domains #######################################

##Add Domains
def test5_addDomains(browser):
    page = browser
    page.goto("https://ib.interviewbuddy.org/ib/console/dashboard")
    n = 3 # 1-4
    D = ["automatedd","testingg","trifii"]
    page.get_by_text("Domains").click()
    page.locator("app-header img").nth(1).click()
    if n == 1:
        page.get_by_label("Domain Name 1").click()
        page.get_by_label("Domain Name 1").fill(D[0])
    elif n == 2:
        page.locator("form").get_by_role("button").click()
        page.get_by_label("Domain Name 1").fill(D[0])
        page.locator("#domain_name").nth(1).fill(D[1])
    elif n == 3:
        page.locator("form").get_by_role("button").click()
        page.get_by_role("dialog", name="Add Domains").get_by_role("button").nth(2).click()
        page.get_by_label("Domain Name 1").fill(D[0])
        page.locator("#domain_name").nth(1).fill(D[1])
        page.locator("#domain_name").nth(2).fill(D[2])
    elif n == 4:
        page.locator("form").get_by_role("button").click()
        page.get_by_role("dialog", name="Add Domains").get_by_role("button").nth(2).click()
        page.locator("form").get_by_role("button").nth(2).click()
        page.get_by_label("Domain Name 1").fill(D[0])
        page.locator("#domain_name").nth(1).fill(D[1])
        page.locator("#domain_name").nth(2).fill(D[2])
        page.locator("#domain_name").nth(3).fill(D[3])
    page.get_by_role("button", name="Add Domains").click()
    page.get_by_role("button", name="Save Changes").click()
    page.get_by_role("button", name="Close").click()
    page.get_by_role("link", name="").click()


###Delete Domains
def test6_deleteDomain(browser):
    page = browser
    page.goto("https://ib.interviewbuddy.org/ib/console/dashboard")
    domname = "trifii"
    page.get_by_text("Domains").click()
    page.locator("app-header img").first.click()
    page.get_by_role("textbox").click()
    page.get_by_role("textbox").fill(domname)
    page.get_by_role("button", name="Search").click()
    page.get_by_role("row", name=domname).get_by_role("button").nth(1).click()
    page.get_by_role("button", name="Save Changes").click()
    page.get_by_role("button", name="Close").click()
    page.get_by_role("link", name="").click()

###Add SubDomains
def test7_addSubdomains(browser):
    page = browser
    page.goto("https://ib.interviewbuddy.org/ib/console/dashboard")
    domain = "automatedd"
    subname = "SUbTesting"
    page.get_by_text("Domains").click()
    page.locator("app-header img").first.click()
    page.get_by_role("textbox").click()
    page.get_by_role("textbox").fill(domain)
    page.get_by_role("button", name="Search").click()
    time.sleep(2)
    page.get_by_role("button", name="View Details").click()
    page.locator("app-header img").nth(1).click()
    page.get_by_label("Sub-Domain Name 1").click()
    page.get_by_label("Sub-Domain Name 1").fill(subname)
    page.get_by_role("button", name="Add Subdomains").click()
    page.get_by_role("button", name="Save Changes").click()
    page.get_by_role("button", name="Close").click()
    page.get_by_role("link", name="").click()

######################################## Templates #######################################

### Create Template
def test8_addTemplate(browser):
    page = browser
    page.goto("https://ib.interviewbuddy.org/ib/console/dashboard")
    name = "Automated Testing2"
    objective = "Screening"  # "Screening" or "Mock Interview" or "Interview"
    description = "no description in the automated testing"
    type = "One Way Interview"  # "One Way Interview" or "One on One Interview"
    dom = "sasa"
    subdom = "subbu"
    years = "0-2 Years"  # "0 - 2 Years" or "2 - 4 Years" or "4+ Years"

    page.get_by_text("Templates").click()
    page.locator("app-header img").nth(1).click()
    page.get_by_label("Template Name").click()
    page.get_by_label("Template Name").fill(name)
    page.locator("p-dropdown").filter(has_text="Select Objective").get_by_role("button",name="dropdown trigger").click()
    page.get_by_role("option", name=objective, exact=True).click()
    page.get_by_label("Template Description").click()
    page.get_by_label("Template Description").fill(description)
    page.locator("p-dropdown").filter(has_text="Select Type").get_by_role("button", name="dropdown trigger").click()
    page.get_by_role("option", name=type).click()
    page.get_by_text("Select Domain", exact=True).click()
    page.get_by_role("option", name=dom).click()
    page.get_by_text("Select Sub Domain").click()
    page.get_by_role("option", name=subdom).click()
    page.get_by_text("Select Years of Experience").click()
    page.get_by_role("option", name=years).click()
    page.get_by_role("button", name="Add Template").click()
    page.get_by_role("button", name="Save Changes").click()
    page.get_by_role("button", name="Close").click()
    page.get_by_role("link", name="").click()

## Add Version
def test9_addVersion(browser):
    page = browser
    page.goto("https://ib.interviewbuddy.org/ib/console/dashboard")
    template = "BCD"
    measurement = "Auto"
    Version_Description = "Auto"
    page.get_by_text("Templates").click()
    page.locator("app-template-card").filter(has_text=template).get_by_role("button",name="View").click()
    page.get_by_role("button", name="Add a New Version").click()
    page.get_by_label("Version description").click()
    page.get_by_label("Version description").fill(Version_Description)
    page.locator("#area_of_measurement").click()
    page.locator("#area_of_measurement").fill(measurement)
    page.get_by_role("button", name="Next").click()
    page.get_by_role("button", name="Confirm & add version").click()
    page.get_by_role("button", name="Save Changes").click()
    page.get_by_role("button", name="Close").click()

######################################## Organizations #######################################

##Add Organization
def test10_addOrganization(browser):
    page = browser
    page.goto("https://ib.interviewbuddy.org/ib/console/dashboard")
    org_name = "Automationtest1"
    slug = "mncasdf"
    email = "hgbr@vrrer.com"
    phone1 = "214525622"
    phone2 = "689855592"
    url = "bvjasdf.in"
    page.get_by_text("Manage B2B").click()
    page.get_by_role("button", name="View Organisations").click()
    page.locator("app-header img").nth(1).click()
    page.locator("div").filter(has_text=re.compile(r"^Name$")).get_by_role("textbox").fill(org_name)
    page.locator("div").filter(has_text=re.compile(r"^Organization Slug$")).get_by_role("textbox").fill(slug)
    page.locator("div").filter(has_text=re.compile(r"^Email ID$")).get_by_role("textbox").fill(email)
    page.locator("div").filter(has_text=re.compile(r"^Phone no\.\+91$")).get_by_role("spinbutton").fill(phone1)
    page.locator("div").filter(has_text=re.compile(r"^Alternate Phone no\.\(Optional\)\+91$")).get_by_role("spinbutton").fill(phone2)
    page.get_by_role("textbox").nth(3).fill(url)
    page.get_by_role("button", name="Add").click()
    page.get_by_role("button", name="Save Changes").click()
    page.get_by_role("button", name="Close").click()
    page.get_by_role("link", name="").click()


######################################## Manage Console Users #######################################

# Make sure the Console User is unblocked 
def test11_blockConsoleUser(browser):
    page = browser
    page.goto("https://ib.interviewbuddy.org/ib/console/dashboard")
    name = "Akhil"
    reason = "Internship over!"
    page.get_by_text("Console Users").click()
    page.locator("app-header img").first.click()
    page.get_by_role("textbox").click()
    page.get_by_role("textbox").fill(name)
    page.get_by_role("button", name="Search").click()
    page.get_by_role("button", name="View").click()
    page.get_by_role("button", name="Block").click()
    page.locator("textarea").click()
    page.locator("textarea").fill(reason)
    page.get_by_role("button", name="Save Changes").click()
    page.get_by_role("link", name="").click()

# Make sure the Console user is blocked
def test12_unblockConsoleUser(browser):
    page = browser
    page.goto("https://ib.interviewbuddy.org/ib/console/dashboard")
    name = "Akhil"
    reason = "Automation"
    page.get_by_text("Console Users").click()
    page.locator("app-header img").first.click()
    page.get_by_role("textbox").click()
    page.get_by_role("textbox").fill(name)
    page.get_by_role("button", name="Search").click()
    page.get_by_role("button", name="View").click()
    page.get_by_role("button", name="Unblock").click()
    page.get_by_role("textbox").nth(1).click()
    page.get_by_role("textbox").nth(1).fill("automation")
    page.get_by_role("button", name="Save Changes").click()
    page.get_by_role("link", name="").click()

# Make sure to create a request from B2B admin
def test13_AcceptRequest(browser) :
    page = browser
    grpname = "sometng" #here Interview Group name
    reveiewer_name = "Nithish Kumar (QA) +91 987654321245832ActiveViewSelect"
    page.goto("https://ib.interviewbuddy.org/ib/console/dashboard")
    page.get_by_role("button", name="View all alerts").click()
    page.get_by_role("button", name="View Details").click()
    page.get_by_role("button", name="Accept and Create Interviews").click()
    page.get_by_role("button", name="Next").click()
    page.locator("app-interviewer-card").filter(has_text=reveiewer_name).get_by_role("button", name="Select").click()
    page.get_by_role("button", name="Next").click()
    page.get_by_role("cell", name="15", exact=True).click()
    page.get_by_role("button", name="Next").click()
    page.get_by_role("button", name="Save and create interviews").click()
    page.get_by_role("button", name="Create", exact=True).click()
    page.get_by_role("button", name="Close").click()
    page.get_by_text("Accepted").click()

################################################################Logout###########################################################

def test14_logout(browser):
    page = browser
    page.goto("https://ib.interviewbuddy.org/ib/console/dashboard")
    page.locator("app-navbar").get_by_role("button").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name= "Logout").click()
    page.wait_for_url("https://ib.interviewbuddy.org/ib/console/login")
# Check the page url
    expect(page).to_have_url("https://ib.interviewbuddy.org/ib/console/login")
    page.close()