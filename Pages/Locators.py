class Locators:
    # Locators of Login Page. The name would end with the identifier used.
    hp_txt_username_id = "txtUsername"
    hp_txt_password_id = "txtPassword"
    hp_btn_Login_id = "btnLogin"
    hp_lbl_ErrorMessage_id = "spanMessage"
    hp_lbl_Credentials_xpath = "//span[contains(text(),'Username') and contains(text(),'Password')]"

    # Locators of Dashboard Page. The name would end with the identifier used

    db_lbl_Welcome_id = "welcome"
    db_lbl_Logout_xpath = "//a[text()='Logout']"


    # Locators of My infy page. The name would end with the identifier used

    mi_lbl_MyInfo_id = "menu_pim_viewMyDetails"
    mi_lbl_FirstName_id = "personal_txtEmpFirstName"