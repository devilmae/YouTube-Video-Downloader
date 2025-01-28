import os
from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Constants
BANNER = f"""
{Fore.RED}****************************************************
{Fore.CYAN}             YOUTUBE VIDEO DOWNLOADER              
{Fore.YELLOW}   Developer: @devil_mae                          
{Fore.BLUE}   Channel: https://www.youtube.com/@PythonPassiveIncomenew
{Fore.RED}****************************************************
"""

DEFAULT_DIR = os.getcwd()
BASE_YDLOpts = {
    'format': 'best',
    'noplaylist': True,
    'noprogress': True,
}

def print_color(text, color=Fore.WHITE):
    """Print text in specified color."""
    print(f"{color}{text}{Style.RESET_ALL}")

def get_user_input(prompt, color=Fore.CYAN):
    """Get input from user with colored prompt."""
    return input(f"{color}{prompt}{Style.RESET_ALL}").strip()

def validate_directory(path):
    """Validate and create directory if needed."""
    if not os.path.exists(path):
        create = get_user_input(f"Directory '{path}' doesn't exist. Create it? (y/n): ", Fore.YELLOW).lower()
        if create in ('y', 'yes'):
            os.makedirs(path, exist_ok=True)
            return True
        return False
    return True

def download_video():
    """Download a YouTube video with progress handling."""
    try:
        url = get_user_input("\nEnter YouTube video URL: ", Fore.GREEN)
        if not url:
            print_color("URL cannot be empty!", Fore.RED)
            return

        download_dir = get_user_input(
            f"Download directory ({DEFAULT_DIR}): ",
            Fore.GREEN
        ) or DEFAULT_DIR

        if not validate_directory(download_dir):
            print_color("Download aborted due to invalid directory.", Fore.RED)
            return

        ydl_opts = {**BASE_YDLOpts, 'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s')}

        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)  # Get info first
            print_color(f"\nDownloading: {info['title']}", Fore.CYAN)
            ydl.download([url])
            
            file_path = os.path.join(download_dir, f"{info['title']}.{info['ext']}")
            print_color(f"Successfully downloaded to: {file_path}", Fore.GREEN)

    except DownloadError as e:
        print_color(f"Download error: {str(e)}", Fore.RED)
    except Exception as e:
        print_color(f"Unexpected error: {str(e)}", Fore.RED)

def main():
    print(BANNER)
    while True:
        download_video()
        if get_user_input("\nDownload another video? (y/n): ", Fore.YELLOW).lower() not in ('y', 'yes'):
            print_color("\nThank you for using the YouTube Video Downloader. Goodbye!", Fore.CYAN)
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print_color("\nOperation cancelled by user. Exiting...", Fore.RED)
