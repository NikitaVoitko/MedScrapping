import argparse
from scrapper.scrap_urls import write_files


def main():
    parser = argparse.ArgumentParser(description='Scrape Files from URL')
    parser.add_argument('first_page', metavar='first_page',
                        type=int, help='Start page to scrap')
    parser.add_argument('last_page', metavar='last_page',
                        type=int, help='End page to scrap')
    parser.add_argument('-u', '--url',
                        default='https://pro.uptodatefree.ir/Show/',
                        help='Base Url To loop at')
    args = parser.parse_args()

    result = write_files(args.first_page, args.last_page, args.url)
    print(result)


if __name__ == '__main__':
    main()
