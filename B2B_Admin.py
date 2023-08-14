import re
import time
import pytest
from playwright.sync_api import sync_playwright

# Change the following test3, test7, test8, test10, test15 inputs as needed

@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as playwright:
        browser = playwright.firefox.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://acme.interviewbuddy.org/b2b/admin/login")
        yield page
        browser.close()

def test1_login(browser):
    page = browser
    page.get_by_role("button", name="Sign in with Google").click()
    page.get_by_role("textbox", name="Email or phone").click()
    page.get_by_role("textbox", name="Email or phone").fill("username@gmail.com")
    page.get_by_role("button", name="Next").click()
    page.get_by_role("textbox", name="Enter your Password").click()
    page.get_by_role("textbox", name="Enter your Password").fill("password")
    page.get_by_role("button", name="Next").click()
    page.wait_for_url("https://acme.interviewbuddy.org/b2b/admin/dashboard")


########################################################### Organisation Details     ########################################################################################
#Edit Organisation

def test2_edit_organisation(browser):
    # page.wait_for_timeout(1000)
    page = browser
    page.wait_for_timeout(1000)
    page.goto("https://acme.interviewbuddy.org/b2b/admin/dashboard")
    oname = "abc"
    oslug = "acme"
    email = "kasturisivakumari93@gmail.com"
    phone = "3656695"
    website = "www.google.com"
    page.locator("div").filter(has_text=re.compile(r"^Organization Details$")).nth(2).click()
    page.locator("app-org-details div").filter(has_text="Profile Details Organization Details Organization NameOrganization SLUG Contact ").locator("img").click()
    page.get_by_label("Organization Name").click()
    page.get_by_label("Organization Name").fill(oname)
    page.get_by_label("Organization SLUG").click()
    page.get_by_label("Organization SLUG").fill(oslug)
    page.get_by_label("Email ID").click()
    page.get_by_label("Email ID").fill(email)
    page.get_by_role("spinbutton").first.click()
    page.get_by_role("spinbutton").first.fill(phone)
    page.get_by_label("URL").click()
    page.get_by_label("URL").fill(website)
    page.get_by_role("button", name="Update").click()
    page.get_by_role("button", name="Save Changes").click()


def test3_downloadInvoices(browser) :
    page = browser

    # input
    invoice = '''1.	Sat, 8 Apr 2023
  19:43
	Coursera.pdf	Unpaid'''
    invoice = ' '.join(invoice.split())

    page.goto("https://acme.interviewbuddy.org/b2b/admin/dashboard")
    page.get_by_text("Organization Details").click()
    page.get_by_role("row", name=invoice).get_by_role("button",name="View Details").click()
    with page.expect_download() as download_info:
        page.get_by_role("button", name="Download").click()
    download = download_info.value



############################################################Domains################################################################

def test4_addOwnDomain(browser):
    page = browser
    page.goto("https://acme.interviewbuddy.org/b2b/admin/dashboard")
    page.wait_for_timeout(1000)

    # input
    domainname = "Automated Test"

    page.get_by_text("Domains").click()
    page.get_by_role("link", name="Organization Logo Use Own Domains/Subdomains").click()
    page.click("//img[@src='../../../../assets/plus.svg']")
    page.get_by_label("Domain Name 1").click()
    page.get_by_label("Domain Name 1").fill(domainname)
    page.get_by_role("button", name="Add Domains").click()
    page.get_by_role("button", name="Save Changes").click()
    page.get_by_role("button", name="Close").click()


def test5_addSubDomain(browser):
    page = browser
    page.goto("https://acme.interviewbuddy.org/b2b/admin/dashboard")
    page.wait_for_timeout(1000)
    d = "Automated Testing7"
    sub = "Automatted Sub Domain155"
    page.get_by_text("Domains").click()
    page.get_by_role("link", name="Organization Logo Use Own Domains/Subdomains").click()
    page.locator("app-header img").first.click()
    page.get_by_role("textbox").click()
    page.get_by_role("textbox").fill(d)
    page.get_by_role("button", name="Search").click()
    time.sleep(3)
    page.get_by_role("button", name="View Details").click()
    page.locator("app-header img").nth(1).click()
    page.get_by_label("Subdomain 1").click()
    page.get_by_label("Subdomain 1").fill(sub)
    page.get_by_role("button", name="Add Subdomains").click()
    page.get_by_role("button", name="Save Changes").click()
    page.get_by_role("button", name="Close").click()


def test6_deleteSubDomain(browser) :
    page = browser
    page.goto("https://acme.interviewbuddy.org/b2b/admin/dashboard")
    page.wait_for_timeout(1000)
    d = "Automated Testing7"
    sub = "Automatted Sub Domain155"
    page.get_by_text("Domains").click()
    page.get_by_role("link", name="Use Own Domains/Subdomains").click()
    page.locator("app-header img").first.click()
    page.get_by_role("textbox").click()
    page.get_by_role("textbox").fill(d)
    page.get_by_role("button", name="Search").click()
    page.wait_for_timeout(1000)
    # page.get_by_role("row", name=d).get_by_role("button",name = "View Details").click()
    page.get_by_role("button", name="View Details").click()
    page.wait_for_timeout(1000)
    page.get_by_role("row", name=sub).get_by_role("button").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Save Changes").click()


###############################################################Templates###############################################################

def test7_createTemplate(browser):
    page = browser
    page.goto("https://acme.interviewbuddy.org/b2b/admin/dashboard")
    name= "AutomateTest1"
    objective = "Screening" # "Screening" or "Mock Interview" or "Interview"
    description = "no description in the automated testing"
    type = "One Way Interview"    #"One Way Interview" or "One on One Interview"
    dom = "Web dev"
    subdom = "A13"
    years = "0-2 Years" # "0-2 Years" or "2-4 Years" or "4+ Years"
    page.get_by_text("Template Dashboard").click()
    page.get_by_role("link", name="Organization Logo Use Own Templates").click()
    page.locator("app-header img").nth(1).click()
    page.get_by_label("Template Name").click()
    page.get_by_label("Template Name").fill(name)
    page.get_by_text("Select Objective").click()
    page.get_by_role("option", name=objective, exact=True).click()
    page.get_by_label("Template Description").click()
    page.get_by_label("Template Description").fill(description)
    page.locator("p-dropdown").filter(has_text="Select Type").get_by_role("button", name="dropdown trigger").click()
    page.get_by_role("option", name=type).click()
    page.get_by_text("Select Domain", exact=True).click()
    page.get_by_role("option", name=dom).click()
    page.locator("p-dropdown").filter(has_text="Select Sub Domain").get_by_role("button", name="dropdown trigger").click()
    page.get_by_role("option", name=subdom).click()
    page.locator("p-dropdown").filter(has_text="Select Years of Experience").get_by_role("button", name="dropdown trigger").click()
    page.get_by_role("option", name=years).click()
    page.get_by_role("button", name="Add Template").click()
    page.get_by_role("button", name="Save Changes").click()

################################################################# Manage Admins ###############################################
###################To Add new Admin###############################################

def test8_add_admin(browser) :
    page = browser
    page.goto("https://acme.interviewbuddy.org/b2b/admin/dashboard")

    # input
    fname = "automat1"
    lname = "test1"
    email = "testing99@automatioon.com"
    phno = "9977788999"

    page.click("//img[@src='../../../../assets/undraw_meet_the_team_re_4h08 1.svg']")
    page.click("//img[@src='../../../../assets/plus.svg']")
    page.get_by_role("textbox",name = "First Name").fill(fname)
    page.get_by_role("textbox",name = "Last Name").fill(lname)
    page.get_by_role("textbox",name = "Email ID").fill(email)
    page.get_by_role("button", name="Add Admin").click()
    page.get_by_role("button", name="Save Changes").click()
    page.get_by_role("dialog", name="Confirmation").get_by_role("button", name="Close").click()
    page.locator("app-header img").first.click()
    page.get_by_role("textbox").click()
    page.get_by_role("textbox").fill(fname)
    page.get_by_role("button", name="Search").click()
    page.locator("div").filter(has_text=fname).nth(2).click()

####################To Block Admins###############################################

def test9_block_admin(browser) :
    page = browser
    page.goto("https://acme.interviewbuddy.org/b2b/admin/dashboard")

    # Input
    adminname = "Akhil"
    reason = "automation Testing block"

    page.locator("div").filter(has_text=re.compile(r"^Manage Admins$")).nth(2).click()
    page.locator("app-header img").first.click()
    page.get_by_role("textbox").click()
    page.get_by_role("textbox").fill(adminname)
    page.get_by_role("button", name="Search").click()
    page.get_by_role("button", name="View").click()
    page.get_by_role("button", name="Block").click()
    page.locator("textarea").click()
    page.locator("textarea").fill(reason)
    page.get_by_role("dialog", name="Confirmation").get_by_role("button", name="Block").click()
    page.get_by_role("button", name="Close").click()

def test9_unblock_admin(browser) :
    page = browser
    page.goto("https://acme.interviewbuddy.org/b2b/admin/dashboard")

    # Input
    adminname = "Akhil"
    reason = "automation Testing block"

    page.locator("div").filter(has_text=re.compile(r"^Manage Admins$")).nth(2).click()
    page.locator("app-header img").first.click()
    page.get_by_role("textbox").click()
    page.get_by_role("textbox").fill(adminname)
    page.get_by_role("button", name="Search").click()
    page.get_by_role("button", name="View").click()
    page.get_by_role("button", name="Unblock").click()
    page.get_by_role("textbox").nth(1).click()
    page.get_by_role("textbox").nth(1).fill("unblock reason")
    page.get_by_role("dialog", name="Confirmation").get_by_role("button", name="Unblock").click()
    page.get_by_role("button", name="Close").click()



####################################### Manage Interviewer #######################################

def test10_add_interviewers(browser) :
    page = browser
    page.goto("https://acme.interviewbuddy.org/b2b/admin/dashboard")

    # input
    fname = "Automata5"
    lname = "Tezt5"
    email = "automat5@automation.com"
    phno = "9555577155"

    page.get_by_text("Manage Interviewers").click()
    page.locator("app-header img").nth(1).click()
    page.get_by_label("First Name").click()
    page.get_by_label("First Name").fill(fname)
    page.get_by_label("Last Name").click()
    page.get_by_label("Last Name").fill(lname)
    page.get_by_label("Email ID").click()
    page.get_by_label("Email ID").fill(email)
    page.locator("input[type=\"tel\"]").click()
    page.locator("input[type=\"tel\"]").fill(phno)
    page.get_by_role("button", name="Add Interviewer").click()
    page.get_by_role("button", name="Save Changes").click()
    page.get_by_role("button", name="Close").click()
    page.locator("app-header img").first.click()
    page.get_by_role("textbox").click()
    page.get_by_role("textbox").fill(fname)
    page.get_by_role("button", name="Search").click()
    page.locator("div").filter(has_text=f"{fname} {lname}").nth(2).click()

def test11_block_interviewers(browser) :
    page = browser
    page.goto("https://acme.interviewbuddy.org/b2b/admin/dashboard")

    # input
    name = "Automata3"
    reason = 'block testing'

    page.locator("div").filter(has_text=re.compile(r"^Manage Interviewers$")).nth(2).click()
    page.locator("app-header img").first.click()
    page.get_by_role("textbox").click()
    page.get_by_role("textbox").fill(name)
    page.get_by_role("button", name="Search").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="View").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Block").click()
    page.locator("div").filter(has_text=re.compile(r"^Reason$")).nth(2).click()
    page.locator("textarea").fill(reason)
    page.get_by_role("dialog", name="Confirmation").get_by_role("button", name="Block").click()
    page.get_by_role("button", name="Close").click()


def test12_unblock_interviewers(browser) :
    page = browser
    page.goto("https://acme.interviewbuddy.org/b2b/admin/dashboard")

    # input
    name = "Automata3"
    reason = 'unblock testing'

    page.locator("div").filter(has_text=re.compile(r"^Manage Interviewers$")).nth(2).click()
    page.locator("app-header img").first.click()
    page.get_by_role("textbox").click()
    page.get_by_role("textbox").fill(name)
    page.get_by_role("button", name="Search").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="View").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Unblock").click()
    page.locator("textarea").nth(1).fill(reason)
    page.get_by_role("dialog", name="Confirmation").get_by_role("button", name="Unblock").click()
    page.get_by_role("button", name="Close").click()
    

###############################################Manage Candidates ######################################################
def test13_blockCandidate(browser) :
    page = browser
    page.goto("https://acme.interviewbuddy.org/b2b/admin/dashboard")

    # input
    fname = "Donald"
    reason = "Block testing"

    page.get_by_text("Manage Candidates").click()
    page.locator("app-header img").click()
    page.get_by_role("textbox").click()
    page.get_by_role("textbox").fill(fname)
    page.get_by_role("button", name="Search").click()
    page.get_by_role("button", name="View").click()
    page.get_by_role("button", name="Block").click()
    page.get_by_role("dialog", name="Confirmation").get_by_role("textbox").click()
    page.get_by_role("dialog", name="Confirmation").get_by_role("textbox").fill(reason)
    page.get_by_role("dialog", name="Confirmation").get_by_role("button", name="Block").click()
    page.get_by_role("button", name="Close").click()
    


def test14_UnblockCandidate(browser) :
    page = browser
    page.goto("https://acme.interviewbuddy.org/b2b/admin/dashboard")

    # input
    fname = "Donald"
    reason = "Unblock testing"

    page.get_by_text("Manage Candidates").click()
    page.locator("app-header img").click()
    page.get_by_role("textbox").click()
    page.get_by_role("textbox").fill(fname)
    page.get_by_role("button", name="Search").click()
    page.get_by_role("button", name="View").click()
    page.get_by_role("button", name="Unblock").click()
    page.locator("textarea").nth(1).click()
    page.locator("textarea").nth(1).fill(reason)
    page.get_by_role("dialog", name="Confirmation").get_by_role("button", name="Unblock").click()
    page.get_by_role("button", name="Close").click()


################################################################Interview Groups ###################################################
def test15_AddInterviewGroups(browser) :
    page = browser
    page.goto("https://acme.interviewbuddy.org/b2b/admin/dashboard")

    # input, be sure to change the numbers everytime
    groupname = "Automate Testin1"
    interviewType = "One Way Interview"    #"One Way Interview" or "One on One Interview"
    intdur = "4 Min"                # ("{1-5} Min" for One way ) or ("{10,15,20,25,30,45,60} Mins" for One on One)
    bufforattempts = "5"            #("{1-5}" for One way ) or ("{0,2,10,15,20,25,30,45,60} Mins" for One on One)
    temptype = "Use IB Templates (Recommended)" #"Use IB Templates (Recommended)" or "Use Own Template"
    tempname = "notification testing"
    version = "Version 1 Version Description 123 test"

    page.locator("div").filter(has_text=re.compile(r"^Interview Groups$")).nth(2).click()
    page.locator("app-header img").nth(1).click()
    if interviewType == "One Way Interview":
        page.get_by_label("Name of the Interview Group").click()
        page.get_by_label("Name of the Interview Group").fill(groupname)
        page.locator("p-dropdown").filter(has_text="Select the type of interview(s)").get_by_role("button",
                                                                                                  name="dropdown trigger").click()
        page.get_by_role("option", name=interviewType).click()
        page.locator("p-dropdown").filter(has_text="Select Duration").get_by_role("button",
                                                                                  name="dropdown trigger").click()
        page.get_by_role("option", name=intdur).click()
        page.wait_for_timeout(1000)
        page.locator("p-dropdown").filter(has_text="Select no of attempts").get_by_role("button",
                                                                                        name="dropdown trigger").click()
        page.wait_for_timeout(1000)
        page.get_by_role("option", name=bufforattempts).click()

    else:
        page.get_by_label("Name of the Interview Group").click()
        page.get_by_label("Name of the Interview Group").fill(groupname)
        page.locator("p-dropdown").filter(has_text="Select the type of interview(s)").get_by_role("button",
                                                                                                  name="dropdown trigger").click()
        page.get_by_role("option", name=interviewType).click()
        page.locator("p-dropdown").filter(has_text="Select Duration").get_by_role("button",
                                                                                  name="dropdown trigger").click()
        page.wait_for_timeout(1000)
        page.get_by_role("option", name=intdur).click()
        page.locator("p-dropdown").filter(has_text="Select Buffer").get_by_role("button",
                                                                                name="dropdown trigger").click()
        page.wait_for_timeout(1000)
        page.get_by_role("option", name=bufforattempts).click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Next").click()
    page.wait_for_timeout(1000)
    page.locator("span").filter(has_text="Use IB Templates (Recommended)").locator("div").nth(1).click()
    page.get_by_role("button", name="Next").click()
    page.get_by_text(tempname).click()
    page.get_by_role("button", name="Next").click()
    page.get_by_text(version).click()
    page.wait_for_timeout(1000)
    page.locator("app-template-version-card").filter(has_text=version).get_by_role("button", name="Select").click()
    page.get_by_role("button", name="Next").click()
    page.wait_for_timeout(1000)
    time.sleep(3)
    page.get_by_role("button", name="Confirm & Create").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Save Changes").click()


def test16_modifyInterviewInstructions(browser) :
    page = browser
    page.goto("https://acme.interviewbuddy.org/b2b/admin/dashboard")
    grpname = "Automation Testing7" 
    page.locator("div").filter(has_text=re.compile(r"^Interview Groups$")).nth(2).click()
    page.locator("app-header img").first.click()
    page.locator("p-dropdown").filter(has_text="Select group name").get_by_role("button",name="dropdown trigger").click()
    page.wait_for_timeout(1000)
    page.get_by_role("option", name=grpname).click()
    page.get_by_role("button", name="Search").click()
    page.get_by_role("button", name="View Details").click()
    page.wait_for_timeout(1000)
    page.locator(".col-auto > img").click()
    page.locator("textarea").click()
    value = page.locator("textarea").input_value()
    if value == 'Automated modified':ins = 'Automated modified again'
    else:ins = 'Automated modified'
    page.locator("textarea").fill(ins)
    page.get_by_role("button", name="Save changes").click()
    page.pause()
    page.get_by_role("button", name="Save Changes", exact=True).click()
    page.get_by_role("button", name="Close").click()
    page.locator(".col-auto > img").click()
    assert page.locator("textarea").input_value() == ins

# retest
def test17_addingInterviews(browser) :
    page = browser
    page.goto("https://acme.interviewbuddy.org/b2b/admin/dashboard")
    group_name = "Automation Testing7"
    numOfInterviews = "Single" # or "Multiple"
    Reviewers_type = "Own" # or "IB"
    Reviewers_assign = "Auto" # or "Manual"

    #Be sure to change this 
    date = "July 20, 2023" # in the format of {month day, year}
    deadline = "1 day" # "1 day" or "2 days" or "3 days"
    review_deadline = "July 25, 2023"

    page.locator("div").filter(has_text=re.compile(r"^Interview Groups$")).nth(2).click()
    page.locator("app-header img").first.click()
    page.locator("p-dropdown").filter(has_text="Select group name").get_by_role("button",name="dropdown trigger").click()
    page.get_by_role("option", name=group_name).click()
    page.get_by_role("button", name="Search").click()
    page.get_by_role("button", name="View Details").click()
    page.get_by_role("button", name="Add Interview").click()
    if numOfInterviews == "Single" :
        page.locator(".p-radiobutton-box").first.click()
    else :
        page.locator(".col-7 > .p-field-radiobutton > .p-element > .p-radiobutton > .p-radiobutton-box").first.click()
    if Reviewers_type == "Own" :
        page.locator("div:nth-child(4) > .col-5 > .p-field-radiobutton > .p-element > .p-radiobutton > .p-radiobutton-box").click()
        if Reviewers_assign == "Auto" :
            page.locator("div:nth-child(6) > .col-5 > .p-field-radiobutton > .p-element > .p-radiobutton > .p-radiobutton-box").click()
        else :
            page.locator("div:nth-child(6) > .col-7 > .p-field-radiobutton > .p-element > .p-radiobutton > .p-radiobutton-box").click()
    else :
        page.locator("div:nth-child(4) > .col-7 > .p-field-radiobutton > .p-element > .p-radiobutton > .p-radiobutton-box").click()

    page.get_by_role("button", name="Next").click()
    page.get_by_label("Date").fill(date)
    page.get_by_label("Date").press("Enter")
    page.locator("p-dropdown").filter(has_text="Please select Deadline").get_by_role("button",name="dropdown trigger").click()
    page.get_by_role("option", name=deadline).click()
    page.get_by_text("Please select timezone").click()
    page.get_by_role("option", name="IST(GMT +5:30)").click()
    page.get_by_label("Deadline for review").fill(review_deadline)
    page.get_by_label("Date").press("Enter")
    page.get_by_role("button", name="Next").click()
    page.get_by_text("Choose").click()
    page.locator("span").filter(has_text="Choose").first.set_input_files("Single_Candidate_details_sheet.xlsx")
    page.get_by_role("button", name="Upload").click()
    page.get_by_role("button", name="Next").click()
    if Reviewers_type != "Own" :
        page.get_by_role("textbox").click()
        page.get_by_role("textbox").fill("Automated Testing")
        page.get_by_role("checkbox").check()
    else :
        page.locator("#interviewer_name_search").click()
        page.locator("#interviewer_name_search").fill("Akhil")
        page.get_by_role("dialog", name="Add Interview").locator("i").click()
        page.get_by_role("button", name="Select").click()
    page.get_by_role("button", name="Next").click()
    page.get_by_role("button", name="Confirm & Create").click()
    page.get_by_role("button", name="Save Changes").click()
    page.get_by_role("button", name="Close").click()
    page.get_by_role("link", name="").click()



################################################################Logout###########################################################
def test18_logout(browser):
    page = browser
    page.goto("https://acme.interviewbuddy.org/b2b/admin/dashboard")
    page.get_by_role("button").click()
    page.get_by_role("button", name="Logout").click()