import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

DRIVER = webdriver.Chrome()  # makes that the default browser of selenium is Chrome


def open_page() -> (
    None
):  # opens the page and makes sure that the files are ready to be installed

    DRIVER.get(
        "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    )

    Wait = WebDriverWait(
        DRIVER, 5
    )  # defines the max time to wait(secs). otherwise quit

    Wait.until(
        EC.presence_of_element_located, (By.LINK_TEXT, "Anexo II.")
    )  # wait until the second file is ready to be downloaded


def get_links() -> dict:  # returnes links and names

    AnexoI = DRIVER.find_element(
        By.LINK_TEXT, "Anexo I."
    )  # gets the element with this name
    AnexoII = DRIVER.find_element(
        By.LINK_TEXT, "Anexo II."
    )  # gets the element with this name

    links = [AnexoI, AnexoII]  # makes a simple list with the elements

    return {
        link.get_attribute("innerText").replace(" ", ""): link.get_attribute("href")
        for link in links
    }  # returns a dict that has the name of the file as key and link as value (dict comprecomprehension)


def download_links(
    links: dict,
) -> (
    None
):  # get the dict with name and links and creates a file with the name of the element from the link that was attached with it

    for (
        name,
        link,
    ) in links.items():  # loops the dict gettings his items(keys and values)

        download = requests.get(f"{link}")  # download the data from the file

        with open(f"projeto/files/{name}pdf", "wb") as file:  # creates a file

            file.write(download.content)  # write in binary code the file as a pdf


def main() -> None:  # runs the entire program

    open_page()
    download_links(get_links())


if (
    __name__ == "__main__"
):  # makes that the program only runs if the file is called, not imported
    main()
