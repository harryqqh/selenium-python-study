import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from utils.config_reader import ConfigReader # Import function form library for optional interaction


class BaseTest:
    @pytest.fixture(scope="class", autouse=True)
    #Initialize webdriver
    def setup(self, request):
        # chrome_options = webdriver.ChromeOptions() # definition option 
        # chrome_options.add_argument("--headless") # add option to Run headless
        # chrome_options.add_argument("--no-sandbox")         # Required for GitHub Actions
        # chrome_options.add_argument("--disable-dev-shm-usage")
        # driver = webdriver.Chrome(options=chrome_options) # implement option 
        
        # driver.get("https://opensource-demo.orangehrmlive.com/")
        
        driver = webdriver.Chrome() # Initialize Chrome driver
        
        # Navigate to base URL with file Config
        base_url = ConfigReader.get_base_url()
        if base_url:
            driver.get(base_url)
        driver.maximize_window()
        request.cls.driver = driver
        self.wait = WebDriverWait(driver,10)
        yield
        driver.quit()
        
  
     