import compress
import web_scrap as web


def main() -> None:

    web.open_page()
    web.download_links(web.get_links())
    compress.to_zip()


main()
