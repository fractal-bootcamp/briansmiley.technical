from bs4 import BeautifulSoup
import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Scrape the web", formatter_class=argparse.MetavarTypeHelpFormatter)
    parser.add_argument("--url", "-u", dest="url", type = str, help="root URL to scrape", required=True)
    parser.add_argument("--depth", "-d", dest="depth", type = int, help="recursive depth down to which to scrape", required=True)
    
