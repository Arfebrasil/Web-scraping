import compress
import web_scrap as web


def main() -> None:  # runs both compress and web scrap in order

    web.open_page()
    web.download_links(web.get_links())
    compress.to_zip()


main()
