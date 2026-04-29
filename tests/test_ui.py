from playwright.sync_api import Page
from playwright.sync_api import expect as plexcept

def test_successful_login(page: Page):
    page.goto("https://saucedemo.com/")

    page.locator("#user-name").fill("standard_user")

    page.locator("#password").fill("secret_sauce")

    page.locator("#login-button").click()

    header = page.locator(".title")

    plexcept(header).to_have_text("Products")

    print("\nУспешный вход выполнен!")

    inventory_list = page.locator(".inventory_list")

    first_item = inventory_list.locator("div.inventory_item").first

    f_item_name = first_item.locator("div.inventory_item_name").text_content()

    button_add_cart = first_item.locator("button")

    button_add_cart.click()

    plexcept(button_add_cart).to_have_text("Remove")

    page.goto("https://www.saucedemo.com/cart.html")

    if page.locator("#password").is_visible():
        page.locator("#user-name").fill("standard_user")

        page.locator("#password").fill("secret_sauce")

        page.locator("#login-button").click()
    
    cart_list = page.locator(".cart_list")

    first_item_cart = cart_list.locator("div.cart_item").first

    f_item_name_cart = first_item_cart.locator("div.inventory_item_name").text_content()

    assert f_item_name == f_item_name_cart


